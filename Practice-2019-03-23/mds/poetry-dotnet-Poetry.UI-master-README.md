Consistent, modular, cross-platform, responsive management dialog UI.

![Animation showcasing the Poetry UI portal, with two sample apps and blades](Docs/introduction.gif)

With Poetry UI, you can navigate to `/Admin` and put reusable functionality there. It is a web *portal* with *apps*, consisting of *blades*.

**Highlights:**

* Runtimes for both .NET Framework and .NET Core
* Written directly in ES6, using JS modules (no 💔 IE)

Overview
--------

On the backend, resources are grouped by .NET assemblies. To make an assembly accessible to Poetry UI, create a component: Add a `[Component("MyComponent")]` public POCO.

Then you can start adding Scripts, Styles, and make Apps.

Some components are built-in to provide a consistent experience across apps from different vendors. Data tables, scaffolded forms, context menus ...

An App is a javascript object of type App, containing one or more Blades. That script file needs to be embedded, and reside in a Component assembly (the POCO mentioned above).

Your components and apps will then run on both .NET Core and .NET Framework.

Workflow
--------

To create a new “LoremIpsum” App, start with a normal web project. To make Poetry UI utilize your code, first create a Component class to map your assembly to an id string.

It should look something like this:

    [Component("Dolor")]
    public class DolorComponent
    {
    }

Now, Poetry UI can access your assembly.

Then make sure you do the following at startup:

	.AddPoetryUI(configurator =>
        configurator.AddComponent<DolorComponent>()
    );

If you're on .NET Core, that goes into your `ConfigureServices` method. Otherwise `Global.asax.cs` will do. You also need to do this in your `Configure` method:

	app.UsePoetryUI();

Then we make an LoremIpsumApp class.

Something like this will do:

    [App("LoremIpsum")]
    [Script("Scripts/lorem-ipsum.js")]
    public class LoremIpsumApp
    {
    }

Create `/Scripts/lorem-ipsum.js` and insert something like this:

    import App from '../../Poetry.UI.PortalSupport/Scripts/app.js';
    import Blade from '../../Poetry.UI.PortalSupport/Scripts/blade.js';

    portal.addApp(new class extends App {
        constructor() {
            super('LoremIpsum');
        }

        open() {
            if (this.blades.length) {
                return;
            }

            this.openBlade(new class extends Blade {
				constructor(app) {
					super();

					this.setTitle('My app');

					this.setContent('Lorem ipsum dolor sit amet');
				}
			});
        }
    });

**This one's important:** Right-click the `lorem-ipsum.js` and select Properties. Then, in the Properties pane, click "Build Action" and choose "Embedded resource". Every time you update this file, you need to rebuild your project.

![Screenshot of the Visual Studio dialog when choosing Embedded resource as Build Action on lorem-ipsum.js](Docs/embedded-resource.png)

And 🎻 viola:

![Screenshot of the resulting LoremIpsum app](Docs/lorem-ipsum.png)

Installation
------------

NuGet packages are published under Poetry.UI.AspNet and Poetry.UI.AspNetCore, respectively. Dev packages are also available at each commit.

Target                 | Release                                                                                                                                                                                  | Development
-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------
AspNet                 | [![Build status .NET Framework (release)](https://ci.appveyor.com/api/projects/status/5n1n1krh2kt0p850?svg=true)](https://ci.appveyor.com/project/bjorn-ali-goransson/poetry-ui-3g357)   | [![Build status .NET Framework (development)](https://ci.appveyor.com/api/projects/status/5n1n1krh2kt0p850?svg=true)](https://ci.appveyor.com/project/bjorn-ali-goransson/poetry-ui-3g357) ([nuget](https://ci.appveyor.com/nuget/poetry-ui-aspnet-dev))
AspNetCore             | [![Build status .NET Core (release)](https://ci.appveyor.com/api/projects/status/ibhby2rdi3p28nw2?svg=true)](https://ci.appveyor.com/project/bjorn-ali-goransson/poetry-ui-oylk0)        | [![Build status .NET Core (development)](https://ci.appveyor.com/api/projects/status/ibhby2rdi3p28nw2?svg=true)](https://ci.appveyor.com/project/bjorn-ali-goransson/poetry-ui-oylk0) ([nuget](https://ci.appveyor.com/nuget/poetry-ui-aspnetcore-dev))

Status
------

This software is very much in an unfinished alpha state. No LTS, etc.

What’s more
-----------

Stay tuned. If you want to be emailed about updates specifically, contact me on bjorn.a.goransson@gmail.com
