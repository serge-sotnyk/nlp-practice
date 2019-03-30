DISCONTINUATION OF PROJECT.  This project will no longer be maintained by Intel.  Intel will not provide or guarantee development of or support for this project, including but not limited to, maintenance, bug fixes, new releases or updates.  Patches to this project are no longer accepted by Intel.  In an effort to support the developer community, Intel has made this project available under the terms of the Apache License, Version 2. If you have an ongoing need to use this project, are interested in independently developing it, or would like to maintain patches for the community, please create your own fork of the project.

intel.xdk.device
================

Configure the device and/or retrieve information pertinent to the device.

Description
-----------

The device object provides access to information about the device itself through
a series of properties and functions. See the events section of this document
below for more information on events thrown by the device object.

### Methods

-   [addRemoteScript](#addremotescript) — This method allows for remote loading 
    of a JavaScript file for Microsoft Windows 8
-   [addVirtualPage](#addvirtualpage) — This function will intercept a single 
    press of the device's hardware "back" button and fire the 
    [intel.xdk.device.hardware.back](#hardwareback) event instead.
-   [blockRemotePages](#blockremotepages) — Use this method to block remote 
    pages, and also set up a white list of allowable remote pages.
-   [closeRemoteSite](#closeremotesite) — Call this command to force a remote 
    site opened with [showRemoteSite](#showremotesite) or 
    [showRemoteSiteExt](#showremotesiteext) to close.
-   [copyToClipboard](#copytoclipboard) — Copies text to the device clipboard 
    for allowing pasting into another application after the Intel app is closed.
-   [getRemoteData](#getremotedata) — This function is used for making 
    background POST/GET requests for remote data
-   [getRemoteDataExt](#getremotedataext) — This function is used for making 
    background POST/GET requests for remote data
-   [getRemoteDataWithID](#getremotedatawithid) — This function is used for 
    making background POST/GET requests for remote data
-   [hideSplashScreen](#hidesplashscreen) — This method will hide the 
    application splash screen earlier than it automatically does
-   [hideStatusBar](#hidestatusbar) — This method hides the device status bar
-   [launchExternal](#launchexternal) — This function will open a url in the 
    device's native browser application.
-   [managePower](#managepower) — This method controls how the device behaves in 
    certain power states.
-   [removeVirtualPage](#removevirtualpage) — This method will help control a 
    device's hardware "back" button.
-   [runInstallNativeApp](#runinstallnativeapp) — Run or install a native app on 
    the device
-   [sendEmail](#sendemail) — This method will open an email view to send an 
    email without exiting the application
-   [sendSMS](#sendsms) — This method will send an SMS message
-   [setAutoRotate](#setautorotate) — This function will control whether the 
    device should automatically handle rotation or not based on a boolean value.
-   [setBasicAuthentication](#setbasicauthentication) — This function will set 
    header data required for basic authentication over the Internet.
-   [setRotateOrientation](#setrotateorientation) — This function will lock the 
    orientation of the device to either "landscape" or "portrait" orientation.
-   [showRemoteSite](#showremotesite) — This function is used to show a remote 
    web site in a different web view.
-   [showRemoteSiteExt](#showremotesiteext) — This function is used to show a 
    remote web site in a different web view.
-   [updateConnection](#updateconnection) — This function will query the device 
    to determine its current connection to the internet.

### Properties

-   [connection](#connection) — This property senses the best type of internet 
    connection available
-   [hasCaching](#hascaching) — This property says whether caching has been 
    enabled for this application
-   [hasStreaming](#hasstreaming) — This property indicates whether streaming 
    has been enabled for this application
-   [initialOrientation](#initialorientation) — This property returns the 
    initial orientation of the device
-   [lastStation](#laststation) — This property will hold information about the 
    audio stream currently playing
-   [model](#model) — This property returns the model of the device that the 
    application is running on.
-   [orientation](#orientation) — This property returns the current orientation 
    of the device
-   [osversion](#osversion) — This property returns the device’s current 
    operating system version information.
-   [phonegapversion](#phonegapversion) — This property returns the version of 
    phonegap running below the intel.xdk layer
-   [platform](#platform) — The platform property returns a text string 
    identifying the platform that the application is running on.
-   [queryString](#querystring) — This property returns any query string 
    parameters passed along with a protocol handler call to start an application

### Events

-   [intel.xdk.device.connection.update](#connection.update) — This event is 
    fired in response to the 
    [intel.xdk.device.updateConnection](#updateconnection) command to indicate
    that the device's Internet connection has changed
-   [intel.xdk.device.continue](#continue) — This event is fired when the screen 
    is unlocked
-   [intel.xdk.device.hardware.back](#hardware.back) — This event is fired when 
    the Android hardware back button is pressed following a call to 
    [intel.xdk.device.addVirtualPage](#addvirtualpage)
-   [intel.xdk.device.orientation.change](#orientation.change) — This event will 
    fire whenever the current orientation of the device changes
-   [intel.xdk.device.pause](#pause) — This event is fired when the screen locks
-   [intel.xdk.device.ready](#ready) — This event will fire once the Intel XDK 
    JavaScript bridge library is completely loaded
-   [intel.xdk.device.remote.block](#remote.block) — This event is fired once 
    navigation to a web page from the main browser window is blocked by the 
    [device.blockRemotePages](#deviceblockremotepages) command
-   [intel.xdk.device.remote.close](#remote.close) — This event will fire once a 
    new webview opened by the [intel.xdk.device.showRemoteSite](#showremotesite)
    command is closed
-   [intel.xdk.device.remote.data](#remote.data) — This event is fired when a 
    response is received from the remote server in response to the 
    [getRemoteDataExt](#getremotedataext) command
-   [intel.xdk.device.resume](#resume) — This event indicates that the user has 
    switched back to using the application
-   [intel.xdk.device.suspend](#suspend) — This event indicates that the user 
    has task-switched away from the application

### addRemoteScript

This method allows for remote loading of a JavaScript file for Microsoft
Windows 8

```javascript
intel.xdk.device.addRemoteScript(url, onLoad, onError);
```

#### Description

This method allows for remote loading of a JavaScript file for Microsoft Windows
8 because you can not include script tags loading remote files for this
platform. Additional information can be found
[here](http://www.jasonfollas.com/blog/post/2012/07/09/Metro-Introducing-the-Local-and-Web-Contexts.aspx).

#### Available Platforms

-   Microsoft Windows 8 - BETA

#### Parameters

-   **url:** The URL of the JavaScript file to load.
-   **onLoad:** A function to handle the successful load of the JavaScript file.
-   **onError:** A function to handle the failed load response.

#### Returns

-   **data:** The data returned to the user for the onLoad and onError 
    parameters will be an xmlHttpResponse object. For more information, 
    [click here](http://www.w3.org/TR/XMLHttpRequest/#response).

#### Example

```javascript
var url= "http://www.somesite.com/script.js"; 

intel.xdk.device.addRemoteScript(url, onLoad_handler, onError_handler);

//Example Event Handlers
function onLoad_handler(data) {  alert("sript file load successful"); }
function onError_handler(data) {  alert(data.status + ": " + data.statusText); }
```

### addVirtualPage

This function will intercept a single press of the device's hardware "back"
button and fire the intel.xdk.device.hardware.back event instead.

```javascript
intel.xdk.device.addVirtualPage();
```

#### Description

This function will intercept a single press of the device’s hardware "back"
button and fire the intel.xdk.device.hardware.back event instead. Call this
function several times to intercept multiple device hardware button presses.
This is used in applications that want to simulate flow through their app and
have the device’s hardware back button be able to be used to navigate backwards
through the flow.

This method is not available on all platforms.

#### Platforms

-   Google Android

#### Example

```javascript
document.addEventListener("intel.xdk.device.ready",function() {

    //start grabbing the Android hardware back button
    intel.xdk.device.addVirtualPage(); 
    
},false);

        
document.addEventListener("intel.xdk.device.hardware.back", function() {
    
    //continue to grab the back button
    intel.xdk.device.addVirtualPage(); 
    
    document.getElementsByTagName("body")[0].innerHTML += 
        "Hardware back button pressed";
    
}, false);    
```

### blockRemotePages

Use this method to block remote pages, and also set up a white list of allowable 
remote pages.

```javascript
intel.xdk.device.blockRemotePages(shouldblock,whitelist);
```

#### Description

Use this method to block remote pages from this application, while turning on
the ability to intercept a remote page redirect.

This method requires two parameters, a boolean value that indicates whether to
block remote pages or not, and a pipe ("|") delimited list of domains or
domain:port pairs that are not to be blocked if the boolean value is "true".

Following a call to this method, it will fire the intel.xdk.device.remote.block
event which includes a "success" property that is set to true or false and a
"blocked" property which contains the URL which was blocked. The application can
ignore this URL or use the device.showRemoteSite method to view it instead.

#### Platforms

-   Apple iOS
-   Google Android

#### Parameters

-   **shouldblock:** This boolean value controls whether the application should 
    block remote pages or not.
-   **whitelist:** This parameter is a "|" delimited list of of domains and or 
    domain:port combos that are NOT to be blocked if shouldblock=true.

#### Events

-   **[intel.xdk.device.remote.block](#remoteblock):** This event will fire once
    the command has made a round trip to the server. Its event object includes a     "success" property that is set to true or false and an "blocked" property     which contains the URL which was blocked.

#### Example

```javascript
//Set up a list of domains for which you allow remote pages
var whitelist = "www.cnn.com|www.intel.xdk.com:44|www.aol.com";

//Set up a list of domains for which you allow remote pages
intel.xdk.device.blockRemotePages(true,whitelist);

document.addEventListener("intel.xdk.device.remote.block",blockRemotePagesEvent,false);
var blockRemotePagesEvent=function(event)
{
    if(event.success==false)
       {
          alert("error: " + event.message);
       }
    else
       {
          alert(event.blocked + "ignored");
       }
}
```

### closeRemoteSite

Call this command to force a remote site opened with 
[showRemoteSite](#showremotesite) or [showRemoteSiteExt](#showremotesiteext) to
close.

```javascript
intel.xdk.device.closeRemoteSite();
```

#### Available Platforms

-   Apple iOS
-   Google Android
-   Microsoft Windows 8 - BETA
-   Microsoft Windows Phone 8 - BETA

#### Example

```javascript
function onDeviceReady(){
    try
    {
        intel.xdk.device.mainViewExecute(
        'intel.xdk.cache.setCookie("remoteSiteCookie","'+iCookieValue+'",-1);')
        intel.xdk.device.closeRemoteSite();
    } catch(e) {
        console.log("oops "+e);
    }
}
```

### getRemoteData

This function is used for making background POST/GET requests for remote data

```javascript
intel.xdk.device.getRemoteData(url, requestMethod, requestBody, 
    successCallback, errorCallback)
```

#### Description

This function is used for making background POST/GET requests. It is an
alternative to the HTML XMLHttpRequest function.

The url parameter should hold the URL to request the XML data from. The
requestMethod must be either "GET" or "POST". The requestBody is unused for a
request with the "GET" method (just pass an empty string) and should hold the
post data for a "POST" method request in a name=value format separated by
ampersands. The successCallback should hold the name of a function with a single
parameter holding the data returned from the success. The errorCallback should
hold the name of a similar function with a single parameter holding the data
returned from the error.

Any line breaks returned from a getRemoteData will be replaced with a string of
"\\n".

Please note that the callback properties are both strings with the names of the
callback functions, not the functions themselves.

#### Available Platforms

-   Apple iOS
-   Google Android
-   Microsoft Windows 8 - BETA
-   Microsoft Windows Phone 8 - BETA

#### Parameters

-   **url:** The URL of the page to access.
-   **requestMethod:** The method to use for the page access. This parameter 
    should be either "get" or "post".
-   **requestBody:** The requestBody is unused for a request with the "GET" 
    method (just pass an empty string) and should hold the post data for a 
    "POST" method request in a name=value format separated by ampersands.
-   **successCallback:** The successCallback should hold the name of a function 
    with a single parameter holding the data returned from the success.
-   **errorCallback:** The errorCallback should hold the name of a similar 
    function with a single parameter holding the data returned from the error.

#### Example

```javascript
//GET method example
intel.xdk.device.getRemoteData(
    "http://twitter.com/statuses/public_timeline.xml", "GET","","success_handler","error_handler");

//POST method example
intel.xdk.device.getRemoteData(
    "http://twitter.com/statuses/public_timeline.xml", "POST", 
    "E-MAIL=html5tools@intel.com&TEST=1&MAX=0",
    "success_handler", "error_handler");

//Example Event Handlers
function success_handler (data) {  alert("success: " + data); }
function error_handler(data) {  alert("error: " + data); }
```

### getRemoteDataExt

This function is used for making background POST/GET requests for remote data

```javascript
intel.xdk.device.getRemoteDataExt(paramsObj);
```

#### Description

This function is used for making background POST/GET requests of XML data. It is
an alternative to the HTML XMLHttpRequest function.

The url parameter should hold the URL to request the XML data from. The
requestMethod must be either "GET" or "POST". The id parameter should hold a
unique ID that may be used to correlate the request to an event. The requestBody
is unused for a request with the "GET" method (just pass an empty string) and
should hold the post data for a "POST" method request in a name=value format
separated by ampersands.

Any line breaks returned from a getRemoteDataExt call will be replaced with a
string of "\\n".

Following a call to this method, it will fire the intel.xdk.device.remote.data
event that includes a a response element which contains the server response, and
an extras element which contains the name/value pairs for each item in the
headers object.

#### Available Platforms

-   Apple iOS
-   Google Android
-   Microsoft Windows 8 - BETA
-   Microsoft Windows Phone 8 - BETA

#### Parameters

-   **paramsObj:** A parameters object.

The parameters object is created as

    new intel.xdk.Device.RemoteDataParameters();

(Yes, that _is_ "intel.xdk.**D**evice" with an uppercase "D". Really.)

Its contents are:

|Item Name|Description|Default|
|---------|-----------|-------|
|url|The URL of the page to access|`""`|
|id|ID that correlates the request to the event|`""`|
|method|The method to use for the request. This parameter should be either `"GET"` or `"POST"`.|`"GET"`|
|body|post data for a POST method request in a name=value format separated by ampersands|`""`|
|headers|This parameter is not to be accessed directly, use addHeader|`""`|

 Be aware that capitilization for this particular object is "intel.xdk.**D**evice".

#### Events

-   **[intel.xdk.device.remote.data](#remotedata):** The event is fired when a
    response is received. It contains a response element which contains the 
    server response, and an extras element which contains the name/value pairs 
    for each item in the headers object.

#### Example

```javascript
//GET method example
var parameters = new intel.xdk.Device.RemoteDataParameters();
parameters.url = "http://twitter.com/statuses/public_timeline.xml";
parameters.id = '12345';

intel.xdk.device.getRemoteDataExt(parameters);

//POST method example
var status = "status=" + "It is good to be alive";

var parameters = new intel.xdk.Device.RemoteDataParameters();
parameters.url = "http://twitter.com/statuses/public_timeline.xml";
parameters.id = '12345';
parameters.method = 'POST';
parameters.body = status;

//To add headers call addHeader
parameters.addHeader(name,value);

intel.xdk.device.getRemoteDataExt(parameters);

//Example Event Handlers
document.addEventListener("intel.xdk.device.remote.data",getRemoteDataEvent,false);
var getRemoteDataEvent=function(event)
{
    if(event.success==false)
       {
          alert("error obtaining remote data");
       }
    else
       {
          alert("success: " + event.response);
       }
}
```

### getRemoteDataWithID

This function is used for making background POST/GET requests for remote data

```javascript
intel.xdk.device.getRemoteDataWithID(url, requestMethod, requestBody, 
    successCallback, errorCallback, uniqueIdentifier)
```

#### Description

This function is used for making background POST/GET requests. It is an
alternative to the HTML XMLHttpRequest function.

The url parameter should hold the URL to request the XML data from. The
requestMethod must be either "GET" or "POST". The requestBody is unused for a
request with the "GET" method (just pass an empty string) and should hold the
post data for a "POST" method request in a name=value format separated by
ampersands. The successCallback should hold the name of a function with a single
parameter holding the data returned from the success. The errorCallback should
hold the name of a similar function with a single parameter holding the data
returned from the error.

Any line breaks returned from a getRemoteData will be replaced with a string of
"\\n".

Please note that the callback properties are both strings with the names of the
callback functions, not the functions themselves.

#### Available Platforms

-   Apple iOS
-   Google Android
-   Microsoft Windows 8 - BETA
-   Microsoft Windows Phone 8 - BETA

#### Parameters

-   **url:** The URL of the page to access.
-   **requestMethod:** The method to use for the page access. This parameter 
    should be either `"get"` or `"post"`.
-   **requestBody:** The requestBody is unused for a request with the GET method
    (just pass an empty string) and should hold the post data for a POST method
    request in a name=value format separated by ampersands.
-   **successCallback:** The successCallback should hold the name of a 
    separately created function. That function should include two parameters. 
    The first will hold the unique identifier passed in the original call. The 
    second will hold the data returned from the successful call.
-   **errorCallback:** The errorCallback should hold the name of a separately 
    created function. That function should include two parameters. The first 
    will hold the unique identifier passed in the original call. The second will 
    hold the data returned from the error.
-   **uniqueIdentifier:** A unique identifier that will be returned with the 
    success or error callback function.

#### Example

```javascript
//GET method example
var uniqueID=12345;
intel.xdk.device.getRemoteDataWithID(
    "http://twitter.com/statuses/public_timeline.xml", 
    "GET","","success_handler","error_handler",uniqueID);

//POST method example
intel.xdk.device.getRemoteDataWithID(
    "http://twitter.com/statuses/public_timeline.xml",
    "POST","E-MAIL=html5tools@intel.com&TEST=1&MAX=0",
    "success_handler","error_handler",uniqueID);

//Example Event Handlers
function success_handler (uniqueID, data) {  alert("success: " + data); }
function error_handler(uniqueID, data) {  alert("error: " + data); }
```

### copyToClipboard

This method allows apps to write to the device clipboard

```javascript
intel.xdk.device.copyToClipboard("code to copy");
```

#### Description

Copies text to the device clipboard for allowing pasting into another 
application after the Intel app is closed.

#### Available Platforms

-   Apple iOS
-   Google Android
-   Microsoft Windows 8
-   Microsoft Windows Phone 8

#### Example

```javascript
//copy to clipboard
intel.xdk.device.copyToClipboard("this is a test");
```

### hideSplashScreen

This method will hide the application splash screen earlier than it 
automatically does

```javascript
intel.xdk.device.hideSplashScreen();
```

#### Description

This command is intended for use as the last function called in response to the
intel.xdk.device.ready event. Typically, intel.xdk applications will display
their splash screen until either the index.html document is completely loaded,
or a 15-second limit has been reached. Call this method to force the automated
application splash screen to disappear early.

#### Available Platforms

-   Apple iOS
-   Google Android
-   Microsoft Windows 8 - BETA
-   Microsoft Windows Phone 8 - BETA

#### Example

```javascript
document.addEventListener("intel.xdk.device.ready",function(){ 
    intel.xdk.device.hideSplashScreen(); 
},false);  
```

### hideStatusBar

This method hides the device status bar

```javascript
intel.xdk.device.hideStatusBar();
```

#### Description

Triggering this method will hide the native device's status bar allowing the app 
to run in a full-screen window.

#### Platforms

-   Apple iOS
-   Google Android

#### Example

```javascript
document.addEventListener("intel.xdk.device.ready",onDeviceReadyHideStatus,false);
function onDeviceReadyHideStatus(evt)
{
intel.xdk.device.hideStatusBar();
}    
```

### launchExternal

This function will open a url in the device's native browser application.

```javascript
intel.xdk.device.launchExternal(url);
```

#### Description

This function will open an url in the device's native browser application. For
example, on an iOS device, the URL will open in a Safari window.

It can also be used to launch device services (such as SMS, email, or twitter)
using known protocol handlers.

#### Available Platforms

-   Apple iOS
-   Google Android
-   Microsoft Windows 8 - BETA
-   Microsoft Windows Phone 8 - BETA

#### Parameters

-   **url:** The URL for the browser window to open.

#### Example

```javascript
//Open a URL example
intel.xdk.device.launchExternal("http://www.google.com");

// Email example
intel.xdk.device.launchExternal('mailto:my@emailaddress.com?subject=email%20Me&body=test%20test%20test');

// Twitter example
intel.xdk.device.launchExternal('twitter://post?message=Message%20Tex');

// SMS example
intel.xdk.device.launchExternal('sms://7175551212');
```

### mainViewExecute

Call this command from within a new web view created by the 
[showRemoteSite](#showremotesite) or [showRemoteSiteExt](#showremotesiteext) 
command to execute JavaScript commands within the main web view.

```javascript
intel.xdk.device.mainViewExecute(command);
```

#### Platforms

-   Apple iOS
-   Google Android

#### Parameters

-   **command:** Any JavaScript that should be passed to and executed in the
    main web view of the application.

#### Example

```javascript
function onDeviceReady(){
    try
    {
        intel.xdk.device.mainViewExecute('intel.xdk.cache.setCookie("remoteSiteCookie","'+iCookieValue+'",-1);')
        intel.xdk.device.closeRemoteSite();
    } catch(e) {
        console.log("oops "+e);
    }
}
```

### managePower

This method controls how the device behaves in certain power states.

```javascript
intel.xdk.device.managePower(shouldStayOn,onlyWhenPluggedIn);
```

#### Description

This method controls how the device behaves in certain power states. It is
passed two Boolean values. If shouldStayOn is false, normal power management for
the device applies. If shouldStayOn is true and onlywhenPluggedIn is true, then
the device will not go to sleep if the device is plugged in. If shouldStayOn is
true and onlyWhenPluggedIn is false, then the device will never go to sleep.

#### Platforms

-   Apple iOS
-   Google Android

#### Parameters

-   **shouldStayOn:** This boolean value sets whether normal power management 
    for the device applies or not.
-   **onlyWhenPluggedIn:** This boolean value is only used if **shouldStayOn**
    is set to true. If **shouldStayOn** is true and **onlywhenPluggedIn** is
    true, then the device will not go to sleep if the device is plugged in. If 
    **shouldStayOn** is true and **onlyWhenPluggedIn** is false, then the device
    will never go to sleep.

#### Example

```javascript
intel.xdk.device.managePower(true,false);
```

### removeVirtualPage

This method will help control a device's hardware "back" button.

```javascript
intel.xdk.device.removeVirtualPage();
```

#### Description

This method will remove the interception of a single press of the device's hardware "back" button. For example, the back button on the Android device platform. This method is not available on all platforms.

#### Platforms

-   Google Android

#### Example

```javascript
function stopCapturingBackButton() {
    //stop grabbing the Android hardware back button
    intel.xdk.device.removeVirtualPage(); 
}

document.addEventListener("intel.xdk.device.ready",function() {

    //start grabbing the Android hardware back button
    intel.xdk.device.addVirtualPage(); 
    
},false);

        
document.addEventListener("intel.xdk.device.hardware.back", function() {
    
    //continue to grab the back button
    intel.xdk.device.addVirtualPage(); 
    
    document.getElementsByTagName("body")[0].innerHTML += 
        "Hardware back button pressed";
    
}, false);    
```

### runInstallNativeApp

Run or install a native app on the device

```javascript
intel.xdk.device.runInstallNativeApp(appName, protocolHandler, appLocationURL, bundleID);
```

#### Description

Call this method to run a previously installed native app, or install and run
the app if not already installed on the device.

#### Platforms

-   Apple iOS
-   Google Android

#### Parameters

-   **appName:** The name of the application being loaded.
-   **protocolHandler:** The protocol handler required for the application to 
    run/install
-   **appLocation :** The URL specifying the location of the application to run 
    or install. This URL will be specific to the store from where the app is 
    retrieved.
-   **bundleID :** The full Android bundle ID for the desired store (this 
    parameter can be left blank for iOS). Example: "com.companyname.projectname"

#### Example

```javascript
// iOS example
if (intel.xdk.device.platform=="iOS")
   {
      intel.xdk.device.runInstallNativeApp('Old Lady Puzzle',
      'oldemo.puzzle://', 
      'itms-apps://itunes.apple.com/us/app/old-lady-puzzle/id525537202?mt=8');
   }

// Android example 
if (intel.xdk.device.platform=="Android")
   {
      intel.xdk.device.runInstallNativeApp('Boom Town', 'applab.boomtown://', 
      'market://details?id=com.intel.xdk.applab.boomtown', 
      'com.intel.xdk.applab.boomtown');
   }
```

### sendEmail

This method will open an email view to send an email without exiting the 
application

```javascript
intel.xdk.device.sendEmail(bodyText, toString, subjectText, isHTML,
    ccString, bccString);
```

#### Platforms

-   Apple iOS
-   Google Android

#### Parameters

-   **bodyText:** This mandatory parameter includes the body of the email to 
    send
-   **toString:** Comma separated string of email addresses to send email to
-   **subjectText:** Content of the email subject line
-   **isHTML:** A boolean value indicating whether body is to be sent in HTML 
    format or not
-   **ccString:** Comma separated string of email addresses to be CCed
-   **bccString:** Comma separated string of email addresses to be BCCed

#### Example

```javascript
var bodyText = 'I am having trouble with building my app';
intel.xdk.device.sendEmail(bodyText, "html5tools@intel.com.com", 
    "I Need Help", true, "", "" ); 
```

### sendSMS

This method will send an SMS message

```javascript
intel.xdk.device.sendSMS(bodyText, toNumber);
```

#### Platforms

-   Apple iOS
-   Google Android

#### Parameters

-   **bodyText:** Content of the message body.
-   **toNumber:** String containing number to send message.

#### Example

```javascript
var bodyText = 'I am at XYZ if you want to join me';            
intel.xdk.device.sendSMS(bodyText, "7175551234");
```

### setAutoRotate

This function will control whether the device should automatically handle 
rotation or not based on a boolean value.

```javascript
intel.xdk.device.setAutoRotate(shouldAutoRotate);
```

#### Available Platforms

-   Apple iOS
-   Google Android
-   Microsoft Windows 8 - BETA
-   Microsoft Windows Phone 8 - BETA

#### Parameters

-   **shouldAutoRotate:** This boolean value controls whether the device is 
    allowed to automatically handle rotation or not.

#### Example

```javascript
intel.xdk.device.setAutoRotate(false);
```

### setBasicAuthentication

This function will set header data required for basic authentication over the Internet.

```javascript
intel.xdk.device.setBasicAuthentication(domain,username,password)
```

#### Description

This function will set header data required for basic authentication over the
Internet. It requires the domain and realm of the server it will make the
request to as well as the appropriate username and password credentials. This
method is not available on all platforms.

#### Platforms

-   Apple iOS
-   Google Android

#### Parameters

-   **domain:** The domain and realm of the server to make the request to.
-   **username:** The appropriate username for the authentication request.
-   **password:** The appropriate password for the authentication request.

#### Example

```javascript
intel.xdk.device.setBasicAuthentication('api.twitter.com', username, password);

try
{
    xmlhttp = new XMLHttpRequest(); // instantiate XMLHttpRequest
}
catch (err)
{
    alert("Error initializing XMLHttpRequest.\n"+ err); 
    return;
}

xmlhttp.onreadystatechange = function()
{
    alert(xmlhttp.status + "   " + xmlhttp.readyState);
    if (xmlhttp.readyState == 4) 
    {
        if(xmlhttp.status == 200)
        {
            try { RequestResponse(url,true,xmlhttp.responseText); } catch(e) {}
        }

    }
}

try
{
   xmlhttp.open('GET', url);      
}
catch (err)
{
    alert("XMLHttpRequest.open() failed.\n"+err.message + " \n URL : " + url); 
    return;
}

xmlhttp.send(strData);
```

### setRotateOrientation

This function will lock the orientation of the device to either "landscape" or
"portrait" orientation.

```javascript
intel.xdk.device.setRotateOrientation(orientation);
```

#### Description

This function will lock the orientation of the device to either "landscape" or
"portrait" orientation. The orientation will be locked based on which specific
string is passed to the function. Passing “portrait” will lock the application
into portrait orientation and passing “landscape” will lock the application into
landscape orientation. If the current orientation is not the specified
orientation, the device will lock in the specified orientation only once the
device is oriented in that position.

To unlock the orientation, set the orientation to an empty string.

#### Available Platforms

-   Apple iOS
-   Google Android
-   Microsoft Windows 8 - BETA
-   Microsoft Windows Phone 8 - BETA

#### Parameters

-   **orientation:** A specific string. Either `"landscape"` or `"portrait"` to
    specify which orientation to use. Pass a string of `"any"` to allow the
    application to rotate freely again.

#### Example

```javascript
//lock in "portrait" orientation 
intel.xdk.device.setRotateOrientation("portrait");
```

### showRemoteSite

This function is used to show a remote web site in a different web view.

```javascript
intel.xdk.device.showRemoteSite(url, closeImageX, closeImageY, 
    closeImageWidth, closeImageHeight)
```

#### Description

This function is used to show a remote web site in a different web view.
Touching the close image will shut down the web view and return the user to the
normal application view.

The url parameter is for the new view’s target url. The image coordinates define
the position, width, and height of the close image that the user may touch to
close the web view. By default close image is set to 48x48 pixels and positioned
in the upper left hand corner of the screen.

When the close button is touched, it fires an intel.xdk.device.remote.close
event.

#### Available Platforms

-   Apple iOS
-   Google Android
-   Microsoft Windows 8 - BETA
-   Microsoft Windows Phone 8 - BETA

#### Parameters

-   **url:** The URL for the web view to open.
-   **closeImageX:** The position of the button to close the web view from the 
    left edge in pixels.
-   **closeImageY:** The position of the button to close the web view from the 
    top edge in pixels.
-   **closeImageWidth:** The width of the button to close the web view in 
    pixels.
-   **closeImageHeight:** The height of the button to close the web view in 
    pixels.

#### Events

-   **[intel.xdk.device.remote.close](#remoteclose) :** The event is fired once
    a user touches the close image and the new web view is closed down.

#### Example

```javascript
intel.xdk.device.showRemoteSite("http://www.twitter.com/",280,0,50,50);
```

#### Version

This method is available in appMobi Version 3.2.0

### showRemoteSiteExt

This function is used to show a remote web site in a different web view.

```javascript
intel.xdk.device.showRemoteSiteExt(url, closeImagePortraitX, 
    closeImagePortraitY, closeImageLandscapeX, closeImageLandscapeY,
    closeImageWidth, closeImageHeight)
```

#### Description

This function is used to show a remote web site in a different web view.
Touching the close image will shut down the web view and return the user to the
normal application view.

The url parameter is for the new view’s target url. The image coordinates define
the position, width, and height of the close image that the user may touch to
close the web view. By default close image is set to 48x48 pixels and positioned
in the upper left hand corner of the screen.

When the close button is touched, it fires an intel.xdk.device.remote.close
event.

This method replaces the intel.xdk.device.showRemoteSite.

#### Available Platforms

-   Apple iOS
-   Google Android
-   Microsoft Windows 8 - BETA
-   Microsoft Windows Phone 8 - BETA

#### Parameters

-   **url:** The URL for the web view to open.
-   **closeImagePortraitX:** The position of the button to close the web view 
    from the left edge in pixels when the device is in the portrait orientation.
-   **closeImagePortraitY:** The position of the button to close the web view 
    from the top edge in pixels when the device is in the portrait orientation.
-   **closeImageLandscapeX:** The position of the button to close the web view 
    from the left edge in pixels when the device is in the landscape 
    orientation.
-   **closeImageLandscapeY:** The position of the button to close the web view 
    from the top edge in pixels when the device is in the landscape orientation.
-   **closeImageWidth:** The width of the button to close the web view in 
    pixels.
-   **closeImageHeight:** The height of the button to close the web view in 
    pixels.

#### Events

-   **[intel.xdk.device.remote.close](#remoteclose) :** The event is fired once
    a user touches the close image and the new web view is closed down.

#### Example

```javascript
intel.xdk.device.showRemoteSiteExt("http://www.google.com/",280,0,50,50);
```

### updateConnection

This function will query the device to determine its current connection to the internet.

```javascript
intel.xdk.device.updateConnection();
```

#### Description

This function will query the device to determine its current connection to the 
internet. When it is done it will fire an event 
[intel.xdk.device.connection.update](#connectionupdate) and the connection 
property of [intel.xdk.device](#intelxdkdevice) will be updated.

#### Available Platforms

-   Apple iOS
-   Google Android
-   Microsoft Windows 8 - BETA
-   Microsoft Windows Phone 8 - BETA

#### Events

-   **intel.xdk.device.connection.update:** This event will fire after the 
    [updateConnection](#updateconnection) method is called to let the device
    know that the latest network connection state is up to date.

#### Example

```javascript
intel.xdk.device.updateConnection();
```

Properties
----------

### connection

This property senses the best type of internet connection available

```javascript
intel.xdk.device.connection
```

#### Description

This property senses the best network connection type available and returns the
result (either "wifi", "cell", or "none"). If the connection is still being
negotiated by the device and the best network connection type is still being
determined, this property will return the value "unknown". This property is
updated only when the [device.updateConnection](#deviceupdateconnection) command
is called and the [intel.xdk.device.connection.update](#connectionupdate) event
is triggered.

#### Example

```javascript
document.addEventListener("intel.xdk.device.connection.update",function(){
    alert(intel.xdk.device.connection);
},false);

intel.xdk.device.updateConnection();
```

### hasCaching

This property says whether caching has been enabled for this application

```javascript
AppMobi.device.hasCaching
```

#### Description

This property says whether caching has been enabled for this application.
Functions under AppMobi.cache for mediacache will not be available if this is
false.

#### Example

```javascript
alert(AppMobi.device.hasCaching);
```

### hasStreaming

This property indicates whether streaming has been enabled for this application

```javascript
intel.xdk.device.hasStreaming
```

#### Description

This property indicates whether streaming has been enabled for this application.
Functions under intel.xdk.player for station and shoutcast will not be available
if this is false.

#### Example

```javascript
alert(intel.xdk.device.hasStreaming);
```

### initialOrientation

This property returns the initial orientation of the device

```javascript
intel.xdk.device.initialOrientation
```

#### Description

This property returns the current orientation of the device. It will return one
of the following values:

|Orientation	        |Value  |
|-----------------------|-------|
|Portrait	            |0      |
|Upside Down Portrait   |180    |
|Landscape Right	    |90     |
|Landscape Left	        |-90    |

#### Example

```javascript
//detect the initial orientation of the device
if (intel.xdk.device.initialOrientation == "90" ||     
    intel.xdk.device.initialOrientation == "-90")
{
        //landscape
}
else
{
        //portrait
}
```

### lastStation

This property will hold information about the audio stream currently playing

```javascript
intel.xdk.device.lastStation
```

#### Description

This property will hold the NetStationID or ShoutcastURL of the station that is
playing. Otherwise, this property only holds a null. This allows the user to
know if their station is already playing at startup. This can happened if the UI
is destroyed and the audio continues in the background and then the application
is later brought back to the foreground.

#### Example

```javascript
alert(intel.xdk.device.lastStation);
```

### model

This property returns the model of the device that the application is running on.

```javascript
intel.xdk.device.model
```

#### Description

This property is defined by the manufacturer of the device. Consequently, this property varies by maker as well as by model. Some valid values include:

-   iPad
-   Motorola Droid
-   iPhone 3G
-   iPhone 4
-   HTC Incredible
-   Galaxy Tab
-   Galaxy S
-   Wave

#### Example

```javascript
alert(intel.xdk.device.model);
```

### orientation

This property returns the current orientation of the device

```javascript
intel.xdk.device.orientation
```

#### Description

This property returns the current orientation of the device. It will return one
of the following values:

|Orientation	        |Value  |
|-----------------------|-------|
|Portrait	            |0      |
|Upside Down Portrait   |180    |
|Landscape Right	    |90     |
|Landscape Left	        |-90    |

#### Example

```javascript
//detect the current orientation of the device
if (intel.xdk.device.orientation == "90" || 
    intel.xdk.device.orientation == "-90")
{
        //landscape
}
else
{
        //portrait
}
```

### osversion

This property returns the device’s current operating system version information.

```javascript
intel.xdk.device.osversion
```

#### Example

```javascript
alert(intel.xdk.device.osversion);
```

### phonegapversion

This property returns the version of phonegap running below the intel.xdk layer

```javascript
intel.xdk.device.phonegapversion
```

#### Example

```javascript
alert(intel.xdk.device.phonegapversion);
```

### platform

The platform property returns a text string identifying the platform that the application is running on.

```javascript
intel.xdk.device.platform
```

#### Description

The platform property returns a text string identifying the platform that application is running on. Valid values include "iOS"and "Android".

#### Example

```javascript
alert(intel.xdk.device.platform);
```

### queryString

This property returns any query string parameters passed along with a protocol handler call to start an application

```javascript
intel.xdk.device.queryString
```

#### Description

This property returns any query string parameters passed along with a protocol handler call to start an application.

#### Example

```javascript
alert(intel.xdk.device.queryString);
```

Events
------

### connection.update

This event is fired in response to the 
[intel.xdk.device.updateConnection](#updateconnection) command to indicate that
the device's Internet connection has changed

#### Description

This event is fired in response to the 
[intel.xdk.device.updateConnection](#updateconnection) command. The connection
parameter on the event object will contain one of the following values:

|Values |Connection|
|-------|----------|
|"wifi"	|The device has an active wifi connection|
|"cell"	|The device has an active cellular data connection|
|"none"	|The device does not currently have a data connection|

#### Example

```javascript
var previousConnectionState = "";
document.addEventListener("intel.xdk.device.connection.update",function(e){
    if (previousConnectionState != intel.xdk.device.connection)
    {
        previousConnectionState = intel.xdk.device.connection;
        debug(intel.xdk.device.connection);
    }
    setTimeout("intel.xdk.device.updateConnection();",2000);  //after we get an update on the connection, check again 2 seconds later
},false);
```

### continue

This event is fired when the screen is unlocked

#### Description

This event is triggered when the device is restarted following the screen being
locked. The screen is locked when turns off due to power saving timeout or the
user presses the power button.

#### Example

```javascript
document.addEventListener("intel.xdk.device.continue",function(evt){
        intel.xdk.player.play();
},false); 
```

### hardware.back

This event is fired when the Android hardware back button is pressed following a
call to intel.xdk.device.addVirtualPage

#### Description

If the [intel.xdk.device.addVirtualPage](#addvirtualpage) command has been
called, and a virtual page is available to be trapped, pressing the hardware
back button will fire this event rather than the default functionality of the
back button. The hardware back button refers to the physical button on the
device, and so it is obviously not available on all platforms (for example, the
iPhone does not have a back button).

#### Example

```javascript
document.addEventListener("intel.xdk.device.ready",function() {

    //start grabbing the Android hardware back button
    intel.xdk.device.addVirtualPage(); 
    
},false);

        
document.addEventListener("intel.xdk.device.hardware.back", function() {
    
    //continue to grab the back button
    intel.xdk.device.addVirtualPage(); 
    
    document.getElementsByTagName("body")[0].innerHTML += 
        "Hardware back button pressed
";
    
}, false);    
```

### orientation.change

This event will fire whenever the current orientation of the device changes

#### Description

This event will fire whenever the current orientation of the device changes. The
value is sent with the event and updated in intel.xdk.device.orientation. The
orientation parameter on the event object will contain one of the following
values:

|Orientation	        |Value  |
|-----------------------|-------|
|Portrait	            |0      |
|Upside Down Portrait   |180    |
|Landscape Right	    |90     |
|Landscape Left	        |-90    |

### pause

This event is fired when the screen locks

#### Description

This event is triggered when the screen turns off due to power saving timeout or
the user presses the power button.

#### Example

```javascript
document.addEventListener("intel.xdk.device.pause",function(evt){
        intel.xdk.player.pause();
},false); 
```

### ready

This event will fire once the Intel XDK JavaScript bridge library is completely
loaded

#### Description

This event will fire once the Intel XDK JavaScript bridge library is completey
loaded. Be sure to allow this event to fire before attempting any Intel XDK
JavaScript Bridge API commands. In order to load the Intel XDK JavaScript
library, be sure to include the following JavaScript library in your HTML file.

#### Example

```javascript
document.addEventListener("intel.xdk.device.ready",function(){
    //lock the application in portrait orientation
    intel.xdk.device.setRotateOrientation("portrait");
    intel.xdk.device.setAutoRotate(false);

    //hide splash screen
    intel.xdk.device.hideSplashScreen();        
},false);   
```

### remote.block

This event is fired once navigation to a web page from the main browser window 
is blocked by the 
[blockRemotePages](#blockremotepages) command

#### Description

This event is fired upon completion of the [blockRemotePages](#blockremotepages) method. It includes a boolean `success` property that indicates whether the request was blocked or not as well as a `blocked` property which will contain the URL in the case that it is blocked. The application can ignore this URL or use the [showRemoteSite](#showremotesite) method to view it instead.

#### Example

```javascript
document.addEventListener("intel.xdk.device.remote.block",function(evt){

    if (evt.success == true)
    {
        intel.xdk.device.showRemoteSite(evt.blocked,50,50,50,50);
    }
    else
    {
        alert(evt.message);
    }

},false); 
intel.xdk.device.blockRemotePages(true,"");
```

### remote.close

This event will fire once a new webview opened by the 
[intel.xdk.device.showRemoteSite](#showremotesite) command is closed

#### Description

The [intel.xdk.device.showRemoteSite](#showremotesite) command is used to create
a brand new web view in an application. This event will fire this event once a
user closes the new webview.

#### Example

```javascript
document.addEventListener("intel.xdk.device.remote.close", function(){
        alert("Twitter Window Closed");
}, false);
AppMobi.device.showRemoteSite("http://www.twitter.com/",280,0,50,50);
```

### remote.data

This event is fired when a response is received from the remote server in response to the [getRemoteDataExt](#getremotedataext) command

#### Description

This event is fired when a response is received from the remote server in
response to the [getRemoteDataExt](#getremotedataext) command. It contains a
`response` element which contains the server response, and an `extras` element 
which contains the name/value pairs for each item in the headers object.

#### Example

```javascript
//GET method example
var parameters = new intel.xdk.Device.RemoteDataParameters();
parameters.url = "http://twitter.com/statuses/public_timeline.xml";
parameters.id = '12345';

intel.xdk.device.getRemoteDataExt(parameters);

//POST method example
var status = "status=" + "It is good to be alive";

var parameters = new intel.xdk.Device.RemoteDataParameters();
parameters.url = "http://twitter.com/statuses/public_timeline.xml";
parameters.id = '12345';
parameters.method = 'POST';
parameters.body = status;

//To add headers call addHeader
parameters.addHeader(name,value);

intel.xdk.device.getRemoteDataExt(parameters);

//Example Event Handlers
document.addEventListener("intel.xdk.device.remote.data",
    getRemoteDataEvent,false);
var getRemoteDataEvent=function(event)
{
        if(event.success==false)
           {
              alert("error obtaining remote data");
           }
        else
           {
              alert("success: " + event.response);
           }
}
```

### resume

This event indicates that the user has switched back to using the application

#### Description

If an application was minimized, but it never left memory, this event will fire in lieu of the intel.xdk.device.ready command.

#### Example

```javascript
document.addEventListener("intel.xdk.device.resume",function(e){
        //restart application sound
},false);
```

### suspend

This event indicates that the user has task-switched away from the application

#### Description

When an application is minimized, this event will be fired as soon as possible
to alert the application that it is losing the user’s focus. When the
application reloads, be aware that you might see an intel.xdk.device.resume
rather than the typical intel.xdk.device.ready event.

#### Example

```javascript
document.addEventListener("intel.xdk.device.suspend",function(e){
        //pause application sound
},false);
```


