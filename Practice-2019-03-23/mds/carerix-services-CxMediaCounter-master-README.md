CxMediaCounter 
==============

Introduction
------------
CXCounter is a stand-alone application that can be used
to log "clicks". In this context, a click is a visit to
an URI, which usually occurs due to clicking a link, but can also
happen when an image is shown.

The eventual goal of a click is to redirect the user to
an URI, while reporting the redirection to the client through his
Carerix App. Therefore, the user should not notice significant delay
in opening the URI, while the client can still report about the
effectiveness of its links.

Each click is logged as an activity of type Node in the
Carerix application, linked to the relevant records (Candidate,
Vacancy).

A typical use case for this application would be a
recruiter (client) sending an automated list of vacancies to multiple
candidates (users), who click on the vacancies of interest, allowing
the recruiter to immediately see who was interested in which vacancy.

Design goals and their implications
-----------------------------------
### Low footprint
Preferably, the code is virtually stand alone, the only
configuration required would be to set up the clients XML password.
To allow for this, the URI's have been set up to always contain
the app name of the client, such that the redirecting host is
interdependent among clients. Also, the code is to be setup to allow
for simple drag-and-drop into another environment; the use of sqlite
means the hosts DB scheme is unaffected, and all code can be run from
any location in the host's public html folder.

### Fast User interaction
Ideally, the user doesn't even notice the
redirection, so we want the redirection itself to be done as soon as
possible. Therefore, the click is stored in the DB as quickly as
possible, a asynchronous call will made to a queue handling
mechanism, a header is set for redirection and finally the script is
exited. This means the heavy lifting of the application (sending all
relevant information to the Carerix App) is done asynchronously, and
does not slow down the user experience.

### Comprehensive information about the interaction
When a note is inserted into the Carerix App, as much
relevant details about the click should be made available, eg: if the
link is situated within an email to a candidate, showing him a list
of selected vacancies, the candidate, vacancy, company and its
contact should be visible in the Carerix Note that this click
created. The original mail that was sent should also be available for
backreference. This all means that the URI's should contain all
relevant information, but this can be different for each type of
click; if the link is to be put on the clients website, the candidate
information would not be available. All in all, the click system
should be flexible enough to allow for many different types of click,
but should also be strict enough to prevent malicious use. To reach
this goal, each type of click will be it's own verb, detailing
exactly what the rest of the URI should look like. The underlying
code should be extensible enough to easily create new verbs.

### User interaction
When the user visits an URI, Limonade redirection will
take care of applying the correct class. This class implements a
method "redirect", which stores all relevant information
about the click, triggers the queuehandler asynchronously and uses a
302 header redirect to the URI passed in `$_REQUEST["url"]`
The HTTP code 302 was used, because modern browsers will register
each click, instead of redirecting once and remembering it did so.
Therefore, 302 gives more information.

### URL overview
The URL's used in the emails have the following format:

	http://{host}/{directory}/{verb}/{param1}/{...}/{paramN}/?url=target_url

+ The `host` is assumed the webhost available for each Cx application:
  appname.carerix.com. [CxClickCounter could be made to work located
  in 1 central place, handling all cx customers instead of just one
  each]
+ The `directory` containing the application is now named `cxcntr`,
  but this can be changed to any other name, because the script is
  independent of location
+ The `verb` specifies what needs to be counted. Eg: vacancies2candidates 
  indicate that vacancy's urls will be clicked by candidates.
+ The various `param1...paramN` ;(URI parts / slugs) are described in the 
  sections below, they indicate the `Vacancy`, `Candidate`;and/or `Contact`
+ the query parameter `?url=target_url` contains the URL where the user will be
	redirected to. This is typically a publication of an online vacancy.

### Queue handling
The queue is handled by a separate script, and has the following script flow

1. Retrieve an unhandled click from DB. Unhandled is currently defined as having
	 `NULL` value of its `synchronise_started` attribute. This could later be 
	 changed to allow for retrying failed clicks after a certain period of time.
2. Set the clicks's `synchronise_started` attribute to
   prevent double submitting. Do this as quickly as possible to reduce
   the number of race conditions with other calls of the script. Later
   on, more attention could be given to table locking and preventing
   race conditions altogether. For the current scope however, this was
   decided to be too unlikely to allocate time to.
3. Sends the click as per it's types model. This creates a note in Carerix (see 
   below).
4. Set the clicks finished or error fields.
5. Continue on from step 1 until no more unhandled clicks are found.

### Carerix
In Carerix, a note (`CRToDo` with `todoTypeKey = 4`) is created by
the queue handler through the XML api. This note MUST have
 
+ `ActivityTypeNode` with `exportcode=COUNTCLICK`
+ The email that was sent (if any) as its `PreviousToDo`
+ Valid `owner`, `notes` and `subject` fields. 

The values of the last three, as well as any other entities the note should be 
linked to, are dependent on the type of the click, and will be explained in the 
next chapter.

Available types
---------------
For all types (think of them as 'types of actions'), the scheme MUST contain the 
`ClickType` as the first URI part and the `AppName` as second. It SHOULD contain 
a `CampaignName`, which is basically a string the client can choose, which will 
be shown as part of the created note's subject.

The subject will be set to the `$_REQUEST['subject']` (with html_entities called 
upon it) if not empty, or will be generated as per the schemes below otherwise.

Usually the value of `notes` will be set to `print_r($_SERVER)`, to allow for 
debugging if required.

### visit
This is a generic type for creating a CRToDo and linking it to any of the following:

+ email
+ vacancy
+ employee
+ contact

This verb is the new generic version, and the other verbs
with the same goal have therefore been deprecated.

#### Default fields
+ `owner` is set to the owner of the supplied employee, contact, vacancy or
	email, in that order, whichever is supplied first.
+ `notes` is set to `print_r($_SERVER).PHP_EOL.PHP_EOL.print_r($click)`
+ `subject` is set to "`{Campaign}, Employee: {EmployeeID}, Contact: {ContactID}, Vacancy: {VacancyID}, Email:
  {EmailID}`", filtering out the ones not supplied.
+ `checksum` is set to the concat of the `stableHash.hexadecimalDescription` of
	the available fields.

#### Links made
Any of the supplied fields will be linked.

#### Additional information
None.

#### URI scheme
	/visit/{AppName}/{Campaign}/{ExportCode}/{EmailID}/{VacancyID?}/{EmployeeID?}/{ContactID?}/{checksum}?url={RedirectURL}

Any field that is "empty" (see php's `empty` language construct) will be
considered to not have been supplied. Since apache webserver
will change `//` to `/` in the path, this means only fields that
have the value 0 will be used. If a certain object can't be
found, it will also be considered not-supplied. If no fields have
been supplied at all, this click will be considered as non-existent.

An additional field in this type is the `ExportCode`. This is the required 
exportcode of the typeID for the CRToDo. If that type does not exist, the note 
will not be created. If exportcode is `empty`, `COUNTCLICK` will be used.

#### Example
Only link an email, but give it the status with the default exportcode

	http://www.recruitersalesevent.nl/cxcntr/visit/services/TEST/0/9324/3171121711/?url=http://google.nl

Link to everything, with the status `JOBS2CANDS`, and a generated subject

	http://www.recruitersalesevent.nl/cxcntr/visit/services/TEST/JOBS2CANDS/9324/442/5508/5864/608625648.452543454.3171121711.167069773/?url=http://google.nl&amp;subject=My%20test%20subject%3C

#### CxScript
	<cx:let name="url" value="http://www.carerix.net/UNIQUE_JOB_URL" keep=""/>
	<cx:let name="base" value="http://${utilities.userDefaults.Customer}" expand="" keep=""/>
	<cx:let name="base" value="${base}.carerix.net/cxcntr/visit/" expand="" keep=""/>
	<cx:let name="base" value="${base}/${utilities.userDefaults.Customer}" expand="" keep=""/>
	<cx:let name="base" value="${base}/jobmailing" expand="" keep=""/>
	<cx:let name="base" value="${base}/JOBS2CANDS" expand="" keep=""/>
	<cx:let name="base" value="${base}/${activity.id}" expand="" keep=""/>
	<cx:foreach item="vac" list="$selectedItems.@sortAscending.jobTitle" index="i">
		<cx:let name="href" value="${base}/${vac.vacancyID}" expand="" keep=""/>
		<cx:let name="href" value="${href}/${activity.toEmployee.employeeID}" expand="" keep=""/>
		<cx:let name="href" value="${href}/${activity.toContact.contactID}" expand="" keep=""/>
		<cx:let name="href" value="${href}/${activity.stableHash.hexadecimaldescription}" expand="" keep=""/>
		<cx:let name="href" value="${href}.${vac.stableHash.hexadecimaldescription}" expand="" keep=""/>
		<cx:let name="href" value="${href}.${activity.toEmployee.stableHash.hexadecimaldescription}" expand="" keep=""/>
		<cx:let name="href" value="${href}.${activity.toContact.stableHash.hexadecimaldescription}" expand="" keep=""/>
		<cx:let name="href" value="${href}?url=${url}" expand="" keep=""/>
		<cx:let name="href" value="${href}&subject=To ${activity.toEmployee.informalName}" expand="" keep=""/>
		<cx:element tag="a">
			<cx:parameter name="href" value="$href"/>
			Click here (<cx:write value="$href"/>) to see <cx:write value="$activity.toVacancy.jobTitle"/>
		</cx:element>
	</cx:foreach>

?subject... is optional, see above.

### mailopened
This type is used to create a image end URI which allows
the client to determine whether a mail recipients has opened its
mail. _This is not reliable though!_ It
is merely an indication: most modern email clients prevent automatic
downloading of external images, which results in the possibility
(indeed: the likelihood) that the recipient might have read the
email, but without loading the image, and therefore without it
registering in your Carerix App.

#### Default fields
+ `owner` is set to the owner of the visitor
+ `notes` is set to `print_r($_SERVER)`
+ `subject` is set to "`MAILOPENED {visitorType} {CampaigName} visitor={VisitorName}`"
+ `checksum` is set to the visitor's `toUser.stableHash.hexadecimalDescription`

#### Links made
Aside from the default links, the note is linked to the visitor, which can be a candidate or a contactperson.

#### Additional information
The `CustomerName` does nothing at the moment.

#### URI scheme

	/mailopened/{AppName}/{CustomerName}/{CampaignName}/{VisitorType}/{VisitorID}/{EmailID}/{Checksum}/{slug}?url={RedirectURL}

Where `VisitorType` is
either `employee` or `contact`. Supplying the url query is
optional; if not supplied, a transparent image of 1x1 px will be
returned. The slug is used to allow you to name the image of the
resulting pixel anyway you like, as long as it has the extension `.gif`. This requirement is set to allow
older browsers to show the image even if they don't recognize
the mimetype.

#### Example
+ Basic use

	http://www.recruitersalesevent.nl/pagevisit/services/166/??/px.gif

+ To a contact, shows up as an external image: 

	http://www.recruitersalesevent.nl/cxcntr/mailopened/services/ABBC-Holding/Test%20Campagne/employee/5514/9324/167149111/px.gif?url=https://www.google.nl/logos/2012/Teachers_Day_Alt-2012-hp.jpg

### pagevisit
This type is used to create a image end URI which allows
the client to determine whether a webpage has been viewed.

#### Default fields
+ `owner` is set to the owner of the publication
+ `notes` is set to `print_r($_SERVER)
+ `subject` is set to "`{PublicationID}-{PublicationMedium}:
	{Publication.toVacancy.jobTitle.firstChars(20)}
	[{Publication.toVacancy.vacancyID}]`"
+ `checksum` is set to the publications `stableHash.hexadecimalDescription`

#### Links made
Since the publication can not be linked to a CRToDo, the
vacancy is linked instead. The publications medium can be determined
from the subject.

#### Additional information
No additional notes.

#### URI scheme

	/pagevisit/{AppName}/{Publication}/{slug}?url={RedirectURL}

Supplying the url query is optional; if not supplied, a
transparent image of 1x1 px will be returned. The slug is used to
allow you to name the image of the resulting pixel anyway you like,
as long as it has the extension `.gif`.
This requirement is set to allow older browsers to show the image
even if they don't recognize the mimetype.

#### Example

	http://www.recruitersalesevent.nl/cxcntr/pagevisit/services/166/158857880/img.gif

### vacancies2candidates [deprecated]
This type is used to send available vacancies to
candidates and registering their interest

#### Default fields
+ `owner` is	set to the owner of the candidate
+ `notes` is set to `print_r($_SERVER)`
+ `subject` is set to "`CLICK vancancy2cand {CampaignName} vacancy={VacancyID} {VacancyName}`"
+ `checksum` is set to the candidate's `toUser.stableHash.hexadecimalDescription`

#### Links made
Aside from the default links, the note is linked to the
candidate, the vacancy and to the company of the vacancy.

#### Additional information
The `CustomerName` does nothing at the moment. *@deprecated*: Use verb `visit` instead

#### URI scheme

	/vacancies2candidates/{AppName}/{CustomerName}/{CampaignName}/{VacancyID}/{CandidateID}/{EmailID}/{Checksum}/?url={RedirectURL}

#### Example

	http://www.recruitersalesevent.nl/cxcntr/vacancies2candidates/services/ABBC-Holding/Test%20Campagne/441/5514/9324/3328387747/?url=http://www.google.nl

### vacancies2contacts [deprecated]
This type is used to send available vacancies to contacts and registering their interest

#### Default fields
+ `owner` is set to the owner of the contact
+ `notes` is set to `print_r($_SERVER)`
+ `subject` is set to "`CLICK vacancy2cp {CampaignName} vacancy={VacancyID} {VacancyName}`"
+ `checksum` is set to the contact's `stableHash.hexadecimalDescription`

#### Links made
Aside from the default links, the note is linked to the contact, the vacancy and to the company of the vacancy.

#### Additional information
The `CustomerName` does nothing at the moment. *@deprecated*: Use verb `visit` instead

#### URI scheme

	/vacancies2contacts/{AppName}/{CustomerName}/{CampaignName}/{VacancyID}/{ContactID}/{EmailID}/{Checksum}/?url={RedirectURL}

#### Example

	http://www.recruitersalesevent.nl/cxcntr/vacancies2contacts/services/ABBC-Holding/Test%20Campagne/441/5863/9324/167149111/?url=http://www.google.nl

### candidates2contacts [deprecated]
This type is used to send available candidates to contacts and registering their interest

#### Default fields
+ `owner` is set to the owner of the candidate
+ `notes` is set to `print_r($_SERVER)`
+ `subject` is set to "`CLICK cand2cp {CampaignName} cand={CandidateName}`"
+ `checksum` is set to the candidate's `toUser.stableHash.hexadecimalDescription`

#### Links made
Aside from the default links, the note is linked to the contact, the vacancy and to the company of the vacancy.

#### Additional information
The `CustomerName` does nothing at the moment. *@deprecated*: Use verb `visit` instead

#### URI scheme

	/candidates2contacts/{AppName}/{CustomerName}/{CampaignName}/{VacancyID}/{ContactID}/{EmailID}/{Checksum}/?url={RedirectURL}

#### Example

	http://www.recruitersalesevent.nl/cxcntr/candidates2contacts/services/ABBC-Holding/Test%20Campagne/5514/5863/9324/3328387747/?url=http://www.google.nl


Notes linked overview
---------------------
For each click, a note is created in the target Carerix
application. This note is linked to a candidate, and/or a vacancy
and/or a contact person.  Here is an overview:

<table cellpadding="0" cellspacing="0" style="width: 100%" class="table table-condensed table-striped table-hover">
	<thead>
		<tr>
			<th></th>
			<th>export code (suggested)</th>
			<th>Candidate</th>
			<th>Vacancy / Job Order</th>
			<th>Contact Person</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th>A</th>
			<td>(not used)</td>
			<td>0</td>
			<td>0</td>
			<td>0</td>
		</tr>
		<tr>
			<th>B</th>
			<td>mailopened</td>
			<td>0</td>
			<td>0</td>
			<td>1</td>
		</tr>
		<tr>
			<th>C</th>
			<td>visit</td>
			<td>0</td>
			<td>1</td>
			<td>0</td>
		</tr>
		<tr>
			<th>D</th>
			<td>vacs2contacts</td>
			<td>0</td>
			<td>1</td>
			<td>1</td>
		</tr>
		<tr>
			<th>E</th>
			<td>mailopened</td>
			<td>1</td>
			<td>0</td>
			<td>0</td>
		</tr>
		<tr>
			<th>F</th>
			<td>cands2contacts</td>
			<td>1</td>
			<td>0</td>
			<td>1</td>
		</tr>
		<tr>
			<th>G</th>
			<td>(not possible)<sup>*</sup></td>
			<td>1</td>
			<td>1</td>
			<td>0</td>
		</tr>
		<tr>
			<th>H</th>
			<td>vacs2contacts</td>
			<td>1</td>
			<td>1</td>
			<td>1</td>
		</tr>
	</tbody>
</table>

+ 1 = note is linked to object of category in column heading
+ 0 = note is not linked
+ <sup>*</sup> = Carerix automatically links a contact when a vacancy is linked, therefore situations G leads to situation H

Installation
------------
To install the application, all that is required is to
put the sourcecode in a separate folder on the desired host. Then,
find the `passLookup` function
in the file `configure.php` and
add a case to the switch such that the method will return the XML
password for your app. This password can be found through 
`settings > XML Interface > xmlPassword`.

Other than that, you only need to make sure the folder `db` is globally read- and writeable (`chmod 777`).

### Requirements
To make this all work, the following software components are used

+ PHP 5.2 (but it should work from PHP5.1 and onwards): http://php.net
+ Limonade library for routing: http://limonade-php.github.com/
+ Sqlite for the stand alone DB file: http://www.sqlite.org/
+ PDO for the DB interaction: http://php.net/manual/en/book.pdo.php (available by default since PHP5.0)

The Limonade library makes it much easier to process the various URL structures 
needed for different countings.

