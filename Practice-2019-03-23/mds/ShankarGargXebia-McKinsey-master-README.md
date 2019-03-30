## Software required for setting up this project:
	1. Install Java7 on your system and update path variable
	2. Install Eclipse 
	3. if you want to execute from command line: Install Maven on your system and update path variable
	4. if you want to execute from eclipse: Install Eclipse-Maven Plugin an Install Eclipse-TestNG plugin
	6. To get source code: Install Git SCM on your system for Git Command line

## How to execute test cases:
	1. From Command line:
		1. Open Terminal and CD to project root directory
		2. To execute all test cases as per current TestNG.xml file enter following command and click enter:
		mvn clean install
		3. To specify conditions and override existing TestNG.xml file:
		mvn clean install -DtestGroups=Base_Outfit:Base_Outfit_1:chrome
			
			a. Here "testGroups" parameter has 3 values seprated by colon
				i.  __First Attribute__: This is the test group we want to execute. for example: Base_Outfit. This should match the column in TestCase excel. This could be comma seprated list if we want to execute multiple test groups in one go.
				
				ii. __Second Attribute__: This is for parallel execution within TestGroup mentioned in first attribute, This could be comma seprated list and test cases in above mentionbed test group will be divided in number of comma seprated values in this field. If testgroupd has 20 test cases and we have 4 values in this field, than test cases will be divided in group of 5 and all 4 threds will execute in parallel.
				No of command seprated enteries in second attribute = No of Threads started to execute the test cases in parallel
				
				iii. __Thrid Attribute__: This is for browser. This could also be a comma separated list. Values could be mix also like chrome,firefox, ie etc.
				No of command seprated enteries in third attribute = No of command seprated enteries in first attribute
				
				Note: This field is of no significance for API Test cases.
			In this example test cases that match "Base_Outfit" in TestGroup column in Test Case excel will be executed in One Thread on Chrome Browser.
			
			We can multiple values in all the attrbutes also:
			mvn clean install -DtestGroups=Outfits07:O1,O2,O3:chrome,chrome,chrome
			here Outfits07 test cases will be divided in Three groups and each child group will be executed on its own chrome browser.
        	__platform__: You can specify platform like Android or iOS.only applicable for Native App Automation. This is not mandatory. Default value for this field is Android and iOS for Browswer containing Android and iOs Respectively.
	    	__platformVersion__: You can specify platformversion like 5.0 for Android or 9.0 iOS.only applicable for Native App Automation. This is not mandatory. Default value for this field is 5.0 for Android and 9.0 for iOS for Browswer containing Android and iOs Respectively.
	    __deviceName__ : You can specify Device like AndroidPhone for Android or iPhone6/iPad Air iOS.only applicable for Native App Automation. This is not mandatory. Default value for this field is AndroidPhone for Android or iPhone6/iPad Air iOS for Browswer containing Android and iOs Respectively.
	    __orientation__: You can specify orientation like orientation or landscape.only applicable for Native App Automation. This is not mandatory.
	    __AUT__ : We need to specify type of AUT also. This is mandatory field and its value could be any one of the follwoing: Web, REST and CT.

			b.Execute from Eclipse:
			Go/Open to TestNG.xml in eclipse. Right click and execute as TestNG suite. Here you need to focus on this tag:
			 <test name="Outfits">
            	<parameters>
                	<parameter name="browser" value="IOSPhonePortraitNative"/>
                	<parameter name="TestGroup" value=""/>
                	<parameter name="TestCaseID" value="iOS_Navigation_Buying_credits"/>
            	</parameters>
            	<classes>
                	<class name="com.tribune.uiautomation.testscripts.TestEngine"/>
            	</classes>
        	</test>

        	Parameters:
        	__TestGroup__: You can specify TestGroup to be executed in parameter TestGroup, this could be a comma seprated value. When using TestGroup, TestCaseID should be empty
        	__Browser__: You can specify Browser to be executed in parameter TestGroup, this could be a comma seprated value.
        	__TestCaseID__: You can also mention test cases to be executed. This could also be a comma seprated value for multiple test cases to executed in one go. When using TestCaseID, TestGroup should be empty.
        	__AUT__: You can also mention application under test to be executed. 
        	Eg: web for executing desktop browser test cases
        	rest for executing rest web services test cases
        	CT for executing chicago tribune native app test cases in Android/ iOS
## Test group for test cases:
	
	Outfits:
        	__OutfitsFirefox__: Test group specified for Outfits test cases to execute in firefox browser.
        	__OutfitsChrome__: Test group specified for Outfits test cases to execute in chrome browser.
        	__OutfitsIE__: Test group specified for Outfits test cases to execute in ie browser.
        	__OutfitsSafari__: Test group specified for Outfits test cases to execute in safari browser.
        	__OutfitsIOSPhonePortrait__: Test group specified for Outfits test cases to execute in iphone portrait browser.
        	__OutfitsIOSPhoneLandscape__: Test group specified for Outfits test cases to execute in iphone landscape browser.
        	__OutfitsIOSTabletPortrait__: Test group specified for Outfits test cases to execute in ipad portrait browser.
        	__OutfitsIOSTabletLandscape__: Test group specified for Outfits test cases to execute in ipad landscape browser.
	
	Barkers:
        	__BarkersFirefox__: Test group specified for Barkers test cases to execute in firefox browser.
        	__BarkersChrome__: Test group specified for Barkers test cases to execute in chrome browser.
        	__BarkersIE__: Test group specified for Barkers test cases to execute in ie browser.
        	__BarkersSafari__: Test group specified for Barkers test cases to execute in safari browser.
        	__BarkersIOSPhonePortrait__: Test group specified for Barkers test cases to execute in iphone portrait browser.
        	__BarkersIOSPhoneLandscape__: Test group specified for Barkers test cases to execute in iphone landscape browser.
        	__BarkersIOSTabletPortrait__: Test group specified for Barkers test cases to execute in ipad portrait browser.
        	__BarkersIOSTabletLandscape__: Test group specified for Barkers test cases to execute in ipad landscape browser.

## Browser names:	        	

		Mobile Web Automation:
        __IOSPhonePortraitWeb : iOS Phone 6 Portrait
		__IOSPhoneLandscapeWeb : iOS Phone 6 Landscape
		__IOSTabletPortraitWeb : iPad Air Portrait
		__IOSTabletLandscapeWeb : iPad Air Landscape

		__AndroidPhonePortraitWeb : Google Nexus 5 Portrait
		__AndroidPhoneLandscapeWeb : Google Nexus 5 Landscape
		__AndroidTabletPortraitWeb : Google Nexus 10 Portrait
		__AndroidTabletLandscapeWeb : Google Nexus 10 Landscape
		
        Native App Automation:
        __IOSPhonePortraitNative : iOS Phone 6 Portrait
		__IOSPhoneLandscapeNative : iOS Phone 6 Landscape
		__IOSTabletPortraitNative : iPad Air Portrait
		__IOSTabletLandscapeNative : iPad Air Landscape

		__AndroidPhonePortraitNative : Google Nexus 5 Portrait
		__AndroidPhoneLandscapeNative : Google Nexus 5 Landscape
		__AndroidTabletPortraitNative : Google Nexus 10 Portrait
		__AndroidTabletLandscapeNative : Google Nexus 10 Landscape

## Functions available for API Testing:
	1. __GETRequest__: This function is to send a getRequest. Parameters used are:
	First Parameter: URL for get request. example: http://image.p2p.tribstage.com/photos/turbine/bal-monochrometest-1-20150709.json
	Second Parameter: Bearer. example: Bearer
	Thrid Paramter: Authentication token. example: gvg_aq7asjhg75g912ifyrc0ljo4s_czrjjvz3q2dx9x46vrvw8x7nu
	Output: This method will update httpResponse, statusCode, mimeType varibale which can be used for verification in next Steps.

	2. __GETRequestAfterAction__ : This function is to send a getRequest immediatley after a POSTRequest, DeleteRequest or updateRequest. Difference between getRequestAfterAction and getRequest is, getRequestAfterAction can only be used to verify results of POSTRequest, DeleteRequest or UPDATEReques while getRequest is can be used independently.

	First Parameter: URL for get request. example: http://image.p2p.tribstage.com/photos/turbine/
	Here the photoID and ".json" is added by the function it self. Program stores the photoID of the the photo used in previuos function which could be either of POSTRequest, DeleteRequest or updateRequest.
	Second Parameter: Bearer. example: Bearer
	Thrid Paramter: Authentication token. example: gvg_aq7asjhg75g912ifyrc0ljo4s_czrjjvz3q2dx9x46vrvw8x7nu
	Output: This method will update httpResponse, statusCode, mimeType varibale which can be used for verification in next Steps.

	3. __POSTrequest__: This function is for sending a POST Request to PhotoService API.
	First Parameter: URL for POST request. example: http://image.p2p.tribstage.com/photos.json
	Second Parameter: Slug. example: Turbine
	Third Parameter: Bearer. example: Bearer
	Fourth Paramter: Authentication token. example: gvg_aq7asjhg75g912ifyrc0ljo4s_czrjjvz3q2dx9x46vrvw8x7nu
	Output: This method will update httpResponse, statusCode, mimeType and PhotoID varibale which can be used for verification in next Steps.
	Steps for POST Request TEst Should be:
	postRequest
	verifyResponseStatusREST
	getRequestAfterAction
	verifyResponseStatusREST

	4. __UPDATERequest__ : This function is for sending an update request to PhotoService API.
	First Parameter: URL for update request. example: http://image.p2p.tribstage.com/photos/turbine/
	Second Parameter: Bearer. example: Bearer
	Third Paramter: Authentication token. example: gvg_aq7asjhg75g912ifyrc0ljo4s_czrjjvz3q2dx9x46vrvw8x7nu
	Fourth Paramter: New photo to be updated. This photo will be stored in src/test/resources/images folder. example: REST_Testing.png
	Output: This method will update httpResponse, statusCode, mimeType and PhotoID varibale which can be used for verification in next Steps.
	Steps for a Update Request test should be:
	postRequest
	verifyResponseStatusREST
	updateRequest
	verifyResponseStatusREST
	getRequestAfterAction
	verifyResponseStatusREST

	5. __DeleteRequest__: This function is for sending delete request to the PhotoService API. This method will take PhotoID of newly created Photo using POSTRequest method.
	First Parameter: URL for Delete request. example: http://image.p2p.tribstage.com/photos/turbine/
	Second Parameter: Bearer. example: Bearer
	Third Paramter: Authentication token. example: gvg_aq7asjhg75g912ifyrc0ljo4s_czrjjvz3q2dx9x46vrvw8x7nu
	Output: This method will update httpResponse, statusCode, mimeType and PhotoID varibale which can be used for verification in next Steps.
	Steps for a Update Request test should be:
	postRequest
	verifyResponseStatusREST
	deleteRequest
	verifyResponseStatusREST
	getRequestAfterAction
	verifyResponseStatusREST

	6. __verifyResponseStatusrRest__: This function is to verify the Status code for any API Request. 
	Parameter : String: Example: 200, 201, 400 etc.

	7. __verifyrResponseTypeRest__: This function will verify the Status type for any API Request.
	Parameter : String: Example: application/json, xml, html etc.

	8. __verifyResponseContent__: This function will verify if given String is present in response of API Request.
	Parameter : String: 

## Android Setup on Mac and run AVD from command line:
	1. Download Android SDK from: https://developer.android.com/sdk/index.html
	2. Unzip the file.
	3. Open Terminal and go to the path of unzipped folder.
	4. Type android and ENTER.
	5. Wait for SDK manager to open.
	6. check all necessary Packages and click Install Package.
	7. Once all packages are installed, Do as per following link: http://smallbusiness.chron.com/getting-android-emulator-running-os-x-38684.html

## Run iOS simulator from command line:
	1. Follow Steps as per : http://stackoverflow.com/questions/10379622/how-to-run-iphone-emulator-without-starting-xcode
        
## Image comparison Test
	1. Go to .\src\test\resources\images folder and put the Expected image there. ( note the name of the expected image)
	2. Go to the test case in excel make following chnages:
		1. For StepAction "cutRequiredImage", enter the name of actual image in "data" column ( This name would be used by system to save the actual image)
		2. For StepAction "compareImages", enter the name of the expected image saved in step 1.
	3. Execute the test case.

## Safari browser Selenium Extension:
	1. Download latest jar of selenium-safari-driver from maven central
	2. Extract the JAR
	3. Install SafariDriver.safariextz
	4. Verify installed extension in Safari browser
	
## Safari Browser Phishing Error
	1. Please follow Steps mentioned on this link: https://support.apple.com/en-in/HT201265

## Following steps are to launch selenium grid for Tribune Project
	1. Make sure that you've a stable build of project which is up and running.
	
	2. Make sure that selenium-server-standalone-2.45.0.jar, IEDriverServer.exe, chromedriver.exe are all in same folder before you start execution.
	3. In Our Project, all these are inside folder: .\src\main\resources\drivers
	
	4. Open command prompt with Administrator rights
	
	5. Run following command in that
			java -jar selenium-server-standalone-2.45.0.jar -role hub  (It will launch server on the default port 4444)
			
	6. Go to node machine\s and open command prompt window with administrator rights
	
	7. Run following command in that
			For Firefox
				java -jar selenium-server-standalone-2.45.0.jar -role node -hub http://<HUB_Machine_IP>:Hub_Port/grid/register (It'll launch the node on default port 5555 )
			
			For Chrome
				java -jar selenium-server-standalone-2.45.0.jar -role node -hub http://<HUB_Machine_IP>:Hub_Port/grid/register -browser browserName=chrome,maxInstances=5 -Dwebdriver.chrome.driver=chromedriver.exe

			For Internet Explorer
				java -jar selenium-server-standalone-2.45.0.jar -role node -hub http://<HUB_Machine_IP>:Hub_Port/grid/register -browser browserName="internet explorer",maxInstances=5 -Dwebdriver.iexplore.driver=IEDriverServer.exe

            For Safari Web Browser (MAC)
                java -jar selenium-server-standalone-2.47.1.jar -role node -browser browserName=safari -hub http://forgehub.tribpub.com:4444/grid/register
				
	8. Go to server machine and open browser then type the following url
			http://localhost:4444/grid/console
			It'll show all the connected nodes with configuration details

	9. In Project, open uiautomation.properties and make following changes:
		IsRemoteExecution=true
			
	10.  Now on the server machine open the project folder and type following command of Maven
			mvn clean install
	
	11. It should clean the project and build it, you can check the test cases execution on the nodes.

## Important notes for iOS Native Node Setup and Test case execution:
	1. __Please start Appium Server always first for iOS Native and then after for others.
	   Node sequence should be like below on hub console "http://forgehub.tribpub.com:4444/grid/console":
	   a) http://forge-ios-slave.usa.tribune.com:4723 (iOS Native Node)
	   b) http://EditorUX.usa.tribune.com:4723 (iOS Safari Node)
	2. Execute only one job at a time from Jenkins for each iOS instance like iOS Web (Safari) or iOS Native (Mobile).

## Important notes for Android Native Node Setup and Test case execution:
	1. Execute only one job at a time from Jenkins for each Android Native instance( this is not applicable now)

## Important notes for MAC Safari Node Setup and Test case execution:
	1. Execute only one job at a time from Jenkins for each MAC Safari instance
	2. Gap should be atleast for 5 minutees between 2 MAC Safari Jenkins execution.

