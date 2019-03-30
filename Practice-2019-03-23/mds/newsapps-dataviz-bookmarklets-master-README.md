Tribune DataViz Bookmarklets
============================

Bookmarklets that might be useful to members of the Chicago Tribune DataViz team.

Installation
------------

Create a new bookmark in your Browser.  In Chrome, on Mac OS X, I go to Bookmarks > Bookmark Manager.  Then I right click on "Bookmarks Bar" and choose "Add Page" from the contextual menu.

In the bookmark name field, type a string that will be shown for the "button" that you click to use your bookmarklet. This can be anything, but should describe what the bookmarklet does.  For the link, copy and paste the snippet for one of the bookmarklets shown below. 


Copy a markdown link to an Unfuddle ticket
------------------------------------------

If you have an Unfuddle ticket open in your browser window, click this bookmarklet to copy a Markdown-formatted link to the ticket to your clipboard.  I use this to reference tickets in my personal developer notes.

### Bookmarklet

    javascript:!function(document,window){var issueNumber=document.querySelector(".summary .number").textContent.trim(),title=document.querySelector(".summary .text-field-text").textContent.trim(),linkText=issueNumber+" "+title,url=document.location.href,markdown="["+linkText+"]("+url+")",dummy=document.createElement("div"),textContent=document.createTextNode(markdown),range=document.createRange();dummy.appendChild(textContent),document.body.appendChild(dummy),range.selectNode(textContent),window.getSelection().addRange(range),document.execCommand("copy"),window.getSelection().removeAllRanges(),document.body.removeChild(dummy)}(document,window);

TODO: Automatically load snippet from source files above 

Building the bookmarklets
-------------------------

To get your dev environment set up, clone this repository, then change to its directory, then install dependencies:

    npm install

To generate minified versions of the bookmarklet JavaScript run

    npm run build

Minified versions will be created in the `dist` directory.

Author
------

Geoff Hing <geoffhing@gmail.com>

