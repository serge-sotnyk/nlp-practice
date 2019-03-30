Welcome to Adventure Game Studio! This new Windows Help version of the
manual should help you get even more out of AGS. Enjoy!

Copyright and terms of use 
==========================

Copyright (c) 1999-2011 Chris Jones and 2011-2017 various contributors.

The software is provided under Artistic License 2.0
(http://www.opensource.org/licenses/artistic-license-2.0.php). Adventure
Game Studio is an open source software, its source code is available at
https://github.com/adventuregamestudio/ags.

THE SOFTWARE IS PROVIDED 'AS-IS' AND WITHOUT WARRANTY OF ANY KIND,
EXPRESS, IMPLIED OR OTHERWISE, INCLUDING WITHOUT LIMITATION, ANY
WARRANTY OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.

IN NO EVENT SHALL CHRIS JONES OR ANY OF THE CONTRIBUTORS BE LIABLE FOR
ANY SPECIAL, INCIDENTAL, INDIRECT OR CONSEQUENTIAL DAMAGES OF ANY KIND,
OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS,
WHETHER OR NOT ADVISED OF THE POSSIBILITY OF DAMAGE, AND ON ANY THEORY
OF LIABILITY, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.

NO MONEY WHATSOEVER MAY BE CHARGED FOR ADVENTURE GAME STUDIO UNLESS
EXPRESS WRITTEN PERMISSION IS GIVEN BY THE AUTHORS. IF YOU PAID FOR
THIS, THE SELLER IS BREACHING THE TERMS OF DISTRIBUTION OF THIS
APPLICATION.

AGS is an adventure game creation system. As such, it is provided to you
in good faith by its authors. Neither Chris Jones nor any of the
contributors can be held responsible for the contents of any works
created with AGS, including but not limited to any which infringe on
copyright, are libellous or contain offensive material. Please use AGS
responsibly.

AGS allows user-made “Plugins” to be incorporated into games created by
the system. These Plugins can access all standard Windows functionality
and are therefore not protected from system functions as the scripting
language is. Neither Chris Jones nor any of the contributors can be held
responsible for any Plugins for AGS which you use in your game. Any
problems with the Plugin should be addressed to its author.

TrueType font display uses ALFont by Javier Gonzalez and the Freetype
project. Distributed under the terms of the Freetype Project license.

OGG Vorbis player is alogg by Javier Gonzalez, using the Ogg Vorbis
decoder, which is available from http://www.xiph.org/ . Copyright (c)
2002, Xiph.org Foundation

OGG Theora player is APEG by Chris Robinson, using the Ogg Theora
decoder, which is Copyright (C) 2002-2008 Xiph.Org Foundation and
contributors.

MP3 player is almp3 v2.0.4, by Javier Gonzalez and the MPG123 team. It
uses the mpg123 MP3 decoder, and again is distributed under the terms of
the GNU Lesser General Public License version 2.1.

Copyright information on the various other modules AGS uses can be found
in the section.

Pentium is a trademark of Intel corporation. Windows is a trademark or
registered trademark of Microsoft corp.

Introduction
============

------------------------------------------------------------------------

Welcome to AGS!

Adventure Game Studio allows you to create your own point-and-click
adventure games like the old Sierra and Lucasarts classics, but with
modern features such as digital music and alpha blending.

AGS is based around an easy-to-use IDE, where you can set up all the
parts of your game, and then add some script to process game events.
Making a game has never been so productive!

To get started, .

System Requirements
-------------------

To work with the Editor, you need following:

-   Windows XP or higher

-   At least 128 Mb RAM

-   .NET 2.0 Framework

-   Microsoft Visual C++ 2008 Service Pack 1 Redistributable

Note that games you create do **NOT require .NET nor Visual
C++ redistributable.**

Any games you create have at least these system requirements:

-   Pentium or higher processor

-   64 Mb RAM

-   Windows 98, ME, 2000, XP, Vista, Seven with DirectX 5 or above

-   Supports all DirectX-compatible sound and video cards

Depending on your game's resolution and colour depth, you may have
higher requirements. The processor required is as follows:

-   320x200, 256-colour: Any Pentium-class system

-   640x400, 256-colour: 266 Mhz or above

-   800x600, 256-colour: 500 Mhz or above recommended

-   320x200, 16-bit colour: 233 Mhz or above

-   640x400, 16-bit colour: 500 Mhz system minimum, may need faster if
    you use large objects

-   800x600, 16-bit colour: 600 Mhz system minimum, may need faster if
    you use large objects

-   320x200, 32-bit colour: 300 Mhz or above

-   640x400, 32-bit colour: 700 Mhz system minimum, may need faster if
    you use large objects

-   800x600, 32-bit colour: 900 Mhz system minimum, may need faster if
    you use large objects

These requirements are not an exact science though - game speed is
affected by many factors, including how many objects/characters are on
the screen, whether background music is playing, the complexity of your
scripts, and more. The best way to determine the requirements of your
game are to test it on different computer configurations.

The run-time engine
===================

The engine (also called the “interpreter”) is what runs your game and is
what the end player will use.

If you are using the default interface, then you use the right mouse
button to cycle between the available 'modes', and the left button to
use the current mode on the mouse position. You can also move the mouse
to the top of the screen to bring up the icon bar where you can directly
select a mode. To exit the engine, press Ctrl-Q. You can save your game
position using F5 and restore with F7.

The controls described above work with the default setup; however, you
can customize your game to use a different interface and shortcut keys.

The demo game
-------------

The first thing you'll probably want to do is to run the demo game. This
game will try to show you some of what AGS can do.

To run the demo, choose the “Open the Demo Game” option from the AGS
folder in your start menu. If you're looking for the files, they're
located in the All Users Application Data folder (this is for
compatibility with the security filters in Windows Vista and later
versions).

**NOTE: The demo game is currently under development. It
has various unfinished or unimplemented areas.**

Graphics driver selection 
-------------------------

AGS has two different graphics drivers when run on Windows – DirectDraw
and Direct3D.

DirectDraw is the 'classic' software graphics driver, that AGS has used
ever since the initial Windows version was released. It's perfectly fine
for simple games that don't use many large sprites, tinting or alpha
blending. It's also quite fast at doing RawDrawing to the screen.

Direct3D is a new, hardware accelerated graphics driver. It uses the
Direct3D 9.0 to render the game in a fully hardware-accelerated
environment. This means that the game will run a lot faster if you use
features such as alpha blending and tinting, which are quite slow to
perform in software mode. However, with Direct3D doing RawDraw
operations can be quite slow, and the driver won't work on all graphics
cards.

No matter which you choose as your default graphics driver, the player
can always run the Setup program and switch to using the other driver if
they are having problems on their PC.

**System Requirements**

**DirectDraw: any Windows-based PC with DirectX 5 or later
installed ILBRK **Direct3D: any Windows-based PC with
DirectX 9.0 installed and a graphics card designed for DirectX 8.1 or
later (most cards manufactured from 2003 onwards).****

If you get the error message “Graphics card does not support Pixel
Shader 1.4” on startup, this indicates that your graphics card is too
old to run with the Direct3D driver. You should choose the DirectDraw
driver instead.

See Also:

Run-time engine setup
---------------------

The engine Setup program allows the player to customize certain game
settings.

**NOTE: currently setup program is featured only for
Windows.**

The options in setup are divided into two parts: common and advanced.
Advanced options could be accessed by pressing “Advanced” button.

**Graphics settings**

Lets player choose a graphics driver. Currently supported are DirectX 5
(old driver) and Direct3D 9 (newer and faster driver with hardware
acceleration).

If checked, the game will be run in windowed mode, as opposed to
fullscreen.

Lets choose a fullscreen display mode (otherwise shows the approximate
size of window the game will be running in). The list of modes depends
on graphic card and system capabilities.

Determines the method game will be scaled (when required):

**None. The game will be shown in its native resolution.
Note that low-resolution games will be running in a tiniest window on
modern monitors, so this choice is more suitable for high-resolution
games.**

**Max round multiplier. The game will be scaled up using a
maximal round integer (2, 3, 4, etc) multiplier with which it still fits
inside the screen.**

**Stretch to fit screen. The game will be stretched to fill
whole screen. Note that if the game's native aspect ratio is different
from screen one's, the game image will appear deformed.**

**Stretch to fit screen (preserve aspect ratio). The game
will be stretched to screen borders while respecting game's native
aspect ratio (width/height proportions). This ensures that game image
will always look correct, but may cause black borders appear at the left
& right or top & bottom sides of the screen.**

Here player may choose a graphics scaling filter. Filter type defines
the method of scaling (nearest-neighbour is most simple one). Some of
the filters (notably Hqx filter) are restricted to which scaling
multiplier they may use; if the filter own scaling is not enough to
resize the game, the most basic image scaling method will be applied
additionally. The list of available filters depend on graphics driver
selection.

**Gameplay settings**

Game language

:   Here player may choose one of the available game translations.

**Advanced graphics options**

Vertical sync

:   This option enables vertical synchronisation mode, which reduces
    “tearing” effect on game image, but may decrease the game
    running speed.

Use 85 Hz display

:   This option sets the monitor refresh rate to 85 Hz to run the game,
    which eliminates flicker. However, this does not work on all
    monitors, and not at all on flat panel displays, which is why it is
    disabled by default.

Smooth scaled sprites

:   This option will apply anti-aliasing to scaled characters, in order
    to give a smoother look to the resizing. This can slow down the game
    though, so it is off by default.

Downgrade 32-bit graphics to 16-bit

:   This option is only available for 32-bit games. It allows people
    with slower PCs to choose to play the game at 16-bit instead, in
    order to boost performance. If they use this, the graphical quality
    will reduce, but it should at least allow them to play the game at a
    decent speed.

**Sound options**

Digital sound

:   Here player may choose the digital audio driver, or disable digital
    sound completely.

MIDI music

:   Here player may choose the MIDI music playback method, or disable
    MIDI music completely.

Use voice pack is available

:   When checked, this option enables voice speech in game
    (where available).

**Mouse options**

Auto lock to window

:   If this option is enabled, the mouse will be locked inside game
    window whenever player clicks on it or switches into game. The
    locked mouse cannot leave game window, making it impossible to
    switch out from the game by mistake (by clicking on desktop,
    for example). Naturally, this option only has importance if game is
    run in windowed mode; when in fullscreen the mouse is always locked.

Mouse speed

:   This slider allows player to set up mouse cursor speed in game. It
    should be noted that this parameter is only applied if the game is
    run in fullscreen mode.

**Other advanced settings**

Sprite cache max size

:   This option limits the maximum amount of memory that the game will
    use for its sprite cache. Sprite cache is used to keep a partition
    of all the game sprites loaded to the memory, thus reducing loading
    times between rooms and preventing slowdowns during game play. Of
    course, higher values make the game use more memory. Usually only
    high-resolution games with long animations need to have this
    value increased.

Custom game saves path

:   When unchecked, the game will store its files - saved games, and
    custom runtime data - in the default Windows folders:
    “C:/Users/&lt;Username&gt;/Saved Games/&lt;Game Title&gt;” and
    “C:/Program Data/Adventure Game Studio/&lt;Game Title&gt;”
    respectively. Players may enable this option and define their own
    location to store game files.

Tutorial
========

This section will introduce you to the AGS by leading you through how to
create a simple game.

Starting off 
------------

The tutorial has now been updated for AGS 3.0. Follow the links below to
run through it.

For the latest version of the tutorials, always check the AGS website.

Setting up the game 
-------------------

Now that you know how to create a room, it's time to set up the
game-wide settings. These include inventory items, sprite graphics,
palette setup and other things which do not depend on individual rooms.

### Palette setup 

The first thing you need to do when you create a new game is to decide
whether you want to use 8-bit (palette-based) colour or 16-bit
(hi-colour). If you want to use 16-bit colour, you can still use
256-colour backgrounds and sprites if you want to, but the engine will
only run in a 16-bit colour resolution, thus slowing it down.

If you want to use 8-bit (because it runs faster), you need to set up
the palette. This is because all sprite and background scene imports
rely on the palette setup to be the same. You **CANNOT use
hi-colour sprites or backgrounds in a 256-colour game.**

You set your chosen colour depth by opening the General Settings pane
and adjusting the Colour Depth setting near the top of the list.

Now, choose the “Colours” pane. Here you will see the 256-colour palette
displayed in a grid. Most of the slots are marked “X” - these are the
slots reserved for the background pictures, and will be different in
each room. The other colours will be as they look here for the entire
game. These fixed colours allow things like the main character graphics,
which must be displayed on more than one screen, to work.

If you want, you can assign more or less colours to the backgrounds. To
toggle the background assignment on/off, click on the slot, then check
the “This colour is room-dependant” box to swap the slot's status.

**IMPORTANT NOTE: *You must set up the palette as you
want it before you start making your game - if you change it later, you
will have to re-import all the sprites and background scenes.***

You can select multiple colour slots by clicking on the first slot, then
shift-clicking on the last slot in the range you want to select. You can
then toggle the background status of all the selected slots at once.

You can right-click in the palette grid to export the entire palette to
a .PAL or PCX file which you can then use to read back into the Editor
in a different game. If you choose to export to a pcx file, then a
screen shot of the Palette Editor will be saved as the picture. This way
you can see all the game-wide colours in the file.

The “Replace palette” option replaces the palette entries with those
entries from the PAL or PCX file you choose. It can read standard
768-byte PAL files, SCI palette resources (renamed to extension .pal)
and JASC PSP palette files.

### Inventory

Most adventure games allow the player to carry a set of objects, which
he can then use to solve puzzles. Adventure Game Studio makes this
inventory easy for you to manage.

Every inventory item which the player may carry during the game at one
time or another is listed under the “Inventory items” node. Here, each
item has a number and a script name which you use in scripts to identify
the object. To create a new item, right-click on the “Inventory items”
node.

Double-click on an inventory item to open it up. On the left you'll see
the graphic used for the object in the inventory window. To change this,
select the “Image” entry in the property grid on the right, and click
the “...” button.

The last thing to do with the inventory items is to define their events:
what happens when the player manipulates them in the inventory window.
Click the “Events” button (the lightning bolt button at the top of the
property grid), which brings up a list which works identically to the
hotspot events. The available events are described in the reference
section.

*NOTE: Each character in the game carries their own set of
inventory items. This means, if you want to create a game like Day of
the Tentacle, where the player can control three different characters,
each character will have a separate inventory.*

You have two choices about how the inventory is displayed to the player
– a built-in inventory window to get you started, and support for custom
inventory windows when you're ready to make your own.

The default option is the Sierra-style pop-up inventory window, which is
popped up by clicking on the Inventory icon on the icon bar. You can
also have the current inventory item displayed in its own button on the
icon bar by creating a button on the GUI and setting its text to (INV)
which stretches the item picture to the button size, or (INVNS) which
draws the inventory item picture straight onto the button with no
resizing. Finally, (INVSHR) , probably the best option, will draw it at
actual size if it will fit, or shrink it if not.

The other option is a custom inventory window. To use this, you will
need to edit the GUI to add it, so I will explain this later on. While
you are starting off with AGS, it is recommended to use the supplied
standard Sierra-style inventory window.

Finally, you may have noticed a “Hotspot Marker Settings” frame at the
top of the Inventory pane. This allows you to switch on an option so
that when the selects an inventory item, the mouse cursor for it will
have a dot and mini-crosshair drawn on it, to show the player where the
hotspot is. You can enter the colour for the centre dot and also for the
surrounding 4 pixels.

### Importing your own sprite graphics

When you were choosing the graphics for the object earlier in this
tutorial, you probably noticed that most of the graphics available
didn't look up to much. This is no problem, because you can import your
own graphics using the Sprite Manager.

Go to the **Sprites pane in the editor. Here, you will see
the complete sprite set for the game. There are two ways to import your
graphics - either overwrite an existing slot with your graphic, or
create a new slot for it.**

To overwrite an existing sprite, right-click the sprite and select
“Replace sprite from file”. To import a new slot, right-click on the
background to the window and choose “Import new sprite”.

The graphic you choose to import must be at the same colour depth as
your game (ie. if you are using hi-colour backgrounds, your sprites must
be hi-colour, and vice versa). AGS will attempt to convert the image if
possible, but if your game is 256-colour then the results of downgrading
a hi-colour image can be poor.

Then, the Import Sprite window will appear. Here, you need to decide
which portion of the image will be imported. You do this by
right-clicking and dragging in the image, which will produce a yellow
rectangle showing the selection. Once you are happy with it, left-click
to import. Alternatively, you can import the entire image with the
“Import whole image” button.

**

NOTE (256-colour only): You may well find that the colours on your
graphic look slightly strange in the AGS Editor. This is because the
sprites are only allocated, by default, the first 41 of the palette
colours (see the ), so your graphic will be remapped to this much
smaller palette. If you find that many of your imported sprites look
strange, you can increase the number of colours assigned to sprites, at
the expense of background colours (again see the section above for
information on how to do this).

If your sprite will only be used in one room then alternatively you can
use the “use background palette” option, which will remap your graphic
to the palette of the room currently loaded, giving much better results.
Note, however, that if you do this, and then try and use the sprite on
another screen, its colours will most likely be screwed up. To use the
room palette, check the “use bkgrnd pal” check-box. Make sure to
un-check this box before you import any other sprites.

NOTE: The transparent colour used by AGS is palette index 0 (for
256-colour sprites) and RGB (255,0,255) for hi-color. Any pixels you
draw on imported sprites in these colours will be transparent.

You can group imported sprites into folders. This prevents the main
sprite list from becoming too long. By default, the Sprite Manager
displays the Main folder, which contains some graphics and a sub-folder
called “Defaults”. Folders work the same way as Windows folders.
Right-click on a folder in the tree to rename it or make a sub-folder.

You can delete a folder by right-clicking on it and selecting the
“Delete” option; beware though that **this will also delete all
the sprites in the folder.**

\* *NOTE: A few people have experienced problems when importing
from clipboard, in that the image colours get reversed (red becomes
blue, blue becomes red, and so on) when they are running Windows at
24-bit or 32-bit colour. If this happens to you, there are two
solutions: (a) turn down your desktop colour depth to 16-bit to run the
AGS Editor, or (b) import your sprites from files rather than the
clipboard.*

**Tiled sprite import**

You may have noticed a checkbox called “Tiled sprite import”. Some
people find this a useful way of importing many frames of a character's
animation at once.

In order for this to work, you need to have all your sprites lined up on
your source bitmap at even intervals. Then, use the “Import from file”
option and import it as usual. Check the “Tiled sprite import” box, and
select the upper-left frame.

When you click the left mouse button, the selection rectangle will
become un-filled and now you can drag the mouse to define how many
frames to import - they'll all be enclosed by selection rectangles. Once
you have the correct number, click the left button again and they will
all be imported.

**Alpha blended sprites**

AGS supports alpha blended sprites if your game is 32-bit colour. In
this case, you need to import a PNG image with an alpha channel (you
cannot paste alpha-blended images from the clipboard).

When you do so, AGS will prompt you asking whether you want to use the
image's alpha channel or not. If you select Yes, then the sprite will be
drawn alpha blended in the game if it is used for a character, object,
mouse cursor or GUI.

Note that if you use alpha blending, any overall transparency that you
set (such as Character.Transparency, Object.Transparency,
GUI.Transparency) will be ignored.

**NOTE: Currently, alpha blended sprites cannot be
antialiased, so if you have the Anti Alias Sprites option turned on in
Setup, it will not be applied to alpha-blended characters.**

### Introduction sequences

You can easily add intro, outro and cutscene sequences to your game.
There is no specific function to do these, but using the provided
animation and script commands you can create almost anything you might
need.

Normally, the game will start in room 1. This is defined by the starting
room number of the player character. To change it, open up the player
character's Character pane, and change the StartingRoom number in the
property grid.

*TIP: The starting room facility is also useful when testing your
game - you can make the game start in any room, at the point where you
are testing it, rather than having to keep playing the game through to
get there.*

Cutscenes are created using the normal animation script commands, such
as Character.Walk, Object.SetView, and so forth. I would suggest you
leave this until you are more comfortable with AGS, and have some
experience of how to use these functions.

### Animations 

In most games you will use some sort of animation during the game,
whether it be a flag waving in the breeze or the player bending over to
pick something up. The term “animation” refers to the ability to change
the look of, and move, objects.

Animations in AGS are managed using Views. A “view” is a set of one or
more “loops”. A loop is a set of frames which, when put together, give
the effect of movement. Each frame in the view can be set a graphic and
a speed.

Go to the editor's “Views” node, right-click it and select the “New
view” option to create us a new, empty view. Double-click the new view
to open it. Each loop is displayed horizontally with its number at the
left hand side, frames going out to the right. To add a frame, click the
grey “New frame” button. To delete a frame, right-click it.

To change a frame's graphic, double-left-click it. The sprite list
screen will be displayed (you may remember this from the Object graphic
selection) where you can choose the graphic you want to use for this
frame.

Note that for walking animations, the first frame in each loop is
reserved for the standing frame, and when walking it will only cycle
through from the second frame onwards.

You select a frame by left-clicking it – when you do so, the property
grid will update with information about the frame. One of these settings
is called “Delay”, which is the frame's **relative speed.
The larger the number, the longer the frame stays (ie. the slower it
is). When the animation is run, an overall animation speed will be set,
so the actual speed of the frame will be: overall\_speed + frame\_speed
. Note that you can use negative numbers for the frame delay to make it
particularly fast, for example setting it to -3 means that the frame
will stay for hardly any time at all. ILBRK Animation speed is specified
in Game Loops (ie. animation speed 4 will show the frame for 4 game
loops - at 40fps, that would be 0.1 seconds).**

The “Sound” propery allows you to enter a sound number that will be
played when this frame becomes visible on the screen. This is especially
useful for footstep sounds.

You run an animation by using the script animation commands, which will
be explained in detail later. Briefly, to animate an object, you first
of all need to set the object's view to the correct view number (use the
Object.SetView script command), and then use the Object.Animate script
command to actually start the animation.

### Characters

A character is similar to an object, except that it can change rooms,
maintain its own inventory, and take part in conversations (more on
these later). It can also have its own custom animation speed and
movement speed.

Go to the “Characters” node in the main tree. You will see under it a
list of all the characters in the game. To create a new character,
right-click the “Characters” node and choose the “New character” option.

You will see that there are a lot of options which you can set for each
character. The most immediately obvious one is the “Make this the player
character” button, which allows you to change which character the player
will control at the start of the game. When the game starts, the first
room loaded will be this character's starting room.

The rest of the options are hidden away in the property grid on the
right. Some of them are described below:

The “UseRoomAreaScaling” option allows you to specify whether this
character will be stretched or shrunk in scaling areas of the screen.
You might want to disable this if you have a character who always stands
still in the same place, and you want the graphics on-screen to be the
same size as you drew them, even though he is standing on a scaled area.

The “Clickable” option tells AGS whether you want the player to be able
to click on the character. If Clickable is enabled, then the character
will be interactable, like the way things worked in Sierra games. If it
is not enabled then the character works like the main character did in
Lucasarts games - if you move the cursor over him or click to look,
speak, etc, then the game will ignore the character and respond to
whatever is behind him.

To set which room this character starts in, change the “StartingRoom”
property. You can set the character's location within this room by using
the “StartX” and “StartY” properties to type in the X,Y co-ordinates you
want him to start at. These co-ordinates define where the middle of his
feet will be placed.

The “NormalView” is where you set what the character looks like. You
must create a view in the , and this view must have either 4 or 8 loops.
If you use 4 loops, then when walking diagonally the closest straight
direction is used for the graphics. Each loop is used for the character
walking in one direction, as follows:

     Loop 0 - walking down (towards screen)
     Loop 1 - walking left
     Loop 2 - walking right
     Loop 3 - walking up (away from screen)
     Loop 4 - walking diagonally down-right
     Loop 5 - walking diagonally up-right
     Loop 6 - walking diagonally down-left
     Loop 7 - walking diagonally up-left

To change the rate at which the character animates, change the Animation
Speed box. Here, a smaller number means faster animation. Note that this
does NOT effect the speed at which the character actually moves when
walking.

**NOTE: The first frame in each loop is the standing still
frame. When walking, the game will cycle through the rest of the frames
in the loop.**

The “MovementSpeed” option allows you to control how fast the character
moves when walking. Here, a larger number means he walks faster. If you
find that a movement speed of 1 is still too fast, you can use negative
numbers (eg. -3) which will move even more slowly. The lower you go, the
slower the movement speed.

The “SpeechColor” option specifies which colour is used for the text
when this character is talking. It effects all messages that are said by
this character. You can find out the colour for each number by going to
the “Colours” pane.

The “IdleView” option allows you to set an idle animation for the
character. To do this, create a new view, with one or more loops of the
character idle (eg. smoking, reading a book, etc). Then, set the “Idle
view” to this view number. If the player stands still for 20 seconds
(you can change the timeout with the Character.SetIdleView script
function), then the current loop from the idle view will be played.

The “ScriptName” property sets the name by which the character will be
referred to in scripts and in conversation scripting. The difference
from the RealName of the character is that the script name may only
contain letters A-Z and numbers 0-9 (the first character must be a
letter, however). The convention in AGS is that character script names
start with a lower case “c”.

To set what happens when the player interacts with the character, click
the “Events” button (this is the lightning bolt button at the top of the
property grid). You will be presented with the events list; select an
event and press the “...” button to allow you to enter some script to
handle the event.

You can also set a talking view for the character. To set one, use the
“SpeechView” property. If you set a talking view, then that view will be
used to animate the character while they are speaking. You should
generally have about 2-3 frames in each loop (the loops are used for the
same directions as in the main view).

There is also an available “Blinking view”. This is used to play
intermittent extra animations while the character is talking. You may
want to use this for effects such as blinking (hence the name). If you
set a view here, it will play intermittently while the character talks
(it is drawn on top of the normal talking view). The default time
between it playing is 3-4 seconds, but you can change this with the
Character.BlinkInterval script property.ILBRK **NOTE: the
blinking view is currently only supported with sierra-style speech.**

“UseRoomAreaLighting” allows you to tell AGS whether this character will
be affected by light and tint levels set on room regions.

If you disable “TurnBeforeWalking”, it will override the General Setting
for turning and tell AGS not to turn this particular character around on
the spot before they move.

“Diagonal loops” specifies that loops 4-8 of the character's view will
be used for the four diagonal directions. If this option is not enabled,
the character will only face 4 ways, and you can use loops 4-8 for other
purposes.

“Adjust speed with scaling” modifies the character's walking speed in
line with their zoom level, as set on the walkable areas.

“Adjust volume with scaling” modifies the volume of any frame-linked
sounds on the character's view (eg. footstep sounds) with their zoom
level, as set on the walkable areas.

“Solid” specifies that this character is solid and will block other
characters from walking through it. Note that **both
characters must be solid in order for them to block one another.**

AGS allows you to export your characters to a file, and then import the
file into a different game - so you can share the same main character
between games, or create one for distribution on the internet.
Right-click on the character and choose “Export character”. The entire
character setup and graphics will be exported to the file, including the
character's walking and talking animations. To import the character into
a different game, load it up, right-click the “Characters” node and
choose “Import Character”. The file selector appears, where you find the
CHA file which you exported earlier. A new character slot will be
created and all the settings imported.

*NOTE: Because importing always creates a new slot, you cannot use
it to overwrite an existing character.*

### Conversations

While the old Sierra games were mainly based on action and not talking,
the Lucasarts games took the opposite approach.

If you want to create a game with conversations where the player can
choose from a list of optional topics to talk about, you can now with
the new Dialog Editor. Go to the “Dialogs” node.

Conversations are made up of Topics. A “topic” is a list of choices from
which the player can choose. You may have up to 30 choices in a topic.
However, not all of them need to be available to the player at the start
of the game - you can enable various options for conversation once the
player has said or done other things. For example, when you talk to the
man in the demo game, the first option is just “Hi”. Once he has said
this, however, a new option becomes available.

The Dialog Editor is quite self-explanatory. Double-click a dialog topic
to open up its window. You'll see the list of options for the topic on
the left, and the dialog script on the right. Each option has a couple
of checkboxes to its right:

-   The “Show” column specifies whether that option is available to the
    player at the start of the game.

-   The “Say” column defines whether the character says the option when
    the player clicks it. The default is on, but if you want options
    describing the player's actions rather than the actual words, you
    may want to turn this column off for that dialog.

**Dialog scripts**

You control what happens when the player chooses an option by editing
the script on the right. This is called the **dialog
script, and is a simplified version of scripting streamlined for
conversations.**

With a newly created dialog topic, all you will see in the script is a
number of lines starting with an '@' symbol. In the dialog script, these
signify the starting points of the script for each option. For example,
when the player clicks on option 3, the script will begin on the line
following “@3”. There is also a special starting point, called “@S”.
This is run when the conversation starts, before any choices are given
to the player. This could be used to display a “Hello” message or
something similar.

To display some speech, you begin the line with the character's SCRIPT
NAME (not full name), followed by a colon, then a space, and then what
you want them to say. For example, if my main character's script name is
EGO, I would write

    ego: "I am very happy today because it's my birthday."

The character name is used by the system to choose the correct colour
for the text.

**IMPORTANT: Do **NOT include the “c” at the
start of the character's script name here.****

You can also use the special character name “narrator”, which displays
the text in the pop-up message box instead of as speech text; and the
alias “player”, which will say it as the current player character -
useful if you don't know which character the player will be controlling
when they speak the conversation.

If you just use `...` as the text for a character to say, the game will
pause briefly as if they are stopping to think, and nothing will be
displayed.

To signal the end of the script for this option, place a “return”
command on the last line of it. For example,

    @1
    ego: "Hello. How are you?"
    narrator: The man looks you in the eye.
    otherman: ...
    otherman: "I'm fine."
    return

“return” tells AGS to go back and display the choices again to the
player. If you use “stop” instead of return, then the conversation is
ended. Alternatively, you can use “goto-dialog” or “goto-previous”,
which abort the current dialog script and transfer control to the new
dialog.

**NOTE: Do **NOT indent these lines with
spaces or tabs. Indented lines signify that AGS should interpret the
line as a normal scripting command rather than a dialog scripting
command.****

The dialog commands available are:

-   **goto-dialog X ILBRK Switches the current topic to
    Topic X, and displays the current list of choices for that topic.**

-   **goto-previous ILBRK Returns to the previous topic
    that this one was called from. If the dialog started on this topic,
    then the dialog will be stopped.**

-   **option-off X ILBRK Turns option X for the current
    topic off, meaning it won't be displayed in the list of choices
    next time.**

-   **option-off-forever X ILBRK Turns option X
    off permanently. It will never again be displayed, not even if an
    “option-on” command is used.**

-   **option-on X ILBRK Turns option X for the current
    topic on, including it in the list of choices to the player next
    time they are displayed.**

-   **returnILBRK Stops the script and returns to the list
    of choices.**

-   **stop ILBRK Stops the conversation and returns the
    player to the game.**

For an example of a dialog script, load the demo game into the editor
and look at the script for its topic 0.

**Using scripting commands in dialogs**

Often the provided dialog scripting commands won't be enough for what
you want to do in the dialog. You might want to give the player an
inventory item or add some points to their score, for example.

AGS now lets you put normal scripting commands in your dialog script, by
indenting the line with spaces or tabs. For example:

    @1
    ego: "Hello. How are you?"
    narrator: The man looks you in the eye.
      player.AddInventory(iKey);
      Display("This line is displayed from a normal script command");
    otherman: "I'm fine."
    return

Here, you can see dialog script commands being used, but also then a
couple of normal scripting commands have been inserted, on indented
lines.

When working with dialog scripts, the **this keyword allows
you to access the currently running dialog.**

If you want to conditionally break out of the dialog script, the special
tokens `RUN_DIALOG_GOTO_PREVIOUS`, `RUN_DIALOG_RETURN` and
`RUN_DIALOG_STOP_DIALOG` are available which you can `return` from
inside a script block. For example:

    @1
    ego: "Hello. How are you?"
    narrator: The man looks you in the eye.
      if (player.HasInventory(iKey)) {
        player.Say("Actually, I'd better go.");
        return RUN_DIALOG_STOP_DIALOG;
      }
    otherman: "Here's a key for you."
    return

**Parser input**

You'll notice in the dialog editor, the property grid has an option
called “ShowTextParser”. If you enable this, a text box will be
displayed below the predefined options in the game, which allows the
player to type in their own input.

If they type in something themselves, then the dialog\_request global
script function will be run, with its parameter being the dialog topic
number that the player was in.

AGS automatically calls ParseText with the text they typed in before it
calls dialog\_request, so you can use Said() calls to respond. See the
section for more info.

### Game options

The Game Settings pane contains a list of all the various overall
options that you can set for your game.

Note that some things listed here are explained later in the
documentation, so if you don't understand one of the items in this list,
come back to it later.

Most of these options can be changed at runtime with the script command
SetGameOption.

-   **Debug Mode - whether the debug keys are active. When
    debug mode is on, you can press Ctrl-X to teleport to any room,
    Ctrl-S to give all inventory items, Ctrl-A to display walkable areas
    on the screen, and Ctrl-D to display statistics about the
    current room. When debug mode is off, these do nothing. See the
    section for more.**

-   **Play sound on score - controls whether a sound effect
    is played when the player scores points. If so, you can set the
    sound number, which will play SOUNDx.WAV (or SOUNDx.MP3), where X is
    the number you set.**

-   **Walk to hotspot in Look mode - controls whether the
    player will walk to “walk-to” spots when the player looks at
    the hotspot. Normally he only walks on use, speak and use-inv.**

-   **Dialog options on GUI - controls where the player's
    options for dialog are displayed. If this option is not checked,
    then in a conversation, the options will be displayed at the bottom
    of the screen. If you check this box, then instead the options will
    be displayed on the GUI you specify.**

-   **Use “anti-glide” mode - you may notice that, as the
    character walks, it can seem as if he is gliding, especially if you
    have a slow animation speed setting. When anti-glide mode is on, the
    man's position is only updated when the frame of animation changes.
    You will need to increase each character's walking speed if you use
    this option.**

-   **Text windows use GUI - allows you to customize the
    standard text window appearance in the game, using the specified
    interface element. See for more information.**

-   **Pixel gap between options - defines the gap between
    the options displayed to the player in a conversation. Normally this
    is 0, which means the options are right below each other. Changing
    it to 1 or 2 can make the option display look less cluttered; it's a
    matter of personal preference.**

-   **Skip Speech - determines how and whether the player
    can skip speech in-game. This can be set to allow the mouse and/or
    keyboard, or neither, to skip speech in the game.**

-   **When interface disabled - determines what happens to
    buttons on your GUIs while the game interface is disabled (eg.
    during a cutscene).**

-   **GUI alpha rendering style - determines which
    rendering method to use in 32-bit games when a GUI Control is drawn
    over GUI. The “Proper alpha belnding” choice is meant for full alpha
    blending support, other options exist for compatibility with older
    versions of AGS only.**

-   **Sprite alpha rendering style - determines which
    rendering method to use in 32-bit games when an image is drawn
    over . The “Proper alpha belnding” choice is meant for full alpha
    blending support, “Classic” style exists for compatibility with
    older versions of AGS only.**

-   **Always display text as speech - if you select this
    option, then all normal text in the game will be displayed above the
    main character's head as speech text, much like the way the
    Lucasarts games worked. If this option is not checked, then normal
    text appears in a pop-up message box, like the way that the Sierra
    games worked.**

-   **Speech style - in the default Lucasarts-style speech,
    when a character talks, the speech text is displayed above their
    head in the game, and the character's talking view is used to
    animate the actual character. ILBRK However, if you set this option
    to Sierra-style then the talking view is used to display an
    animating portrait separately in the top-left of the screen, with
    the text to the right of it. This is similar to the way that Space
    Quest 5, King's Quest 6 and other later Sierra games worked. You can
    also cycle to another option, “Sierra- style with background”, which
    is the same except a text window is drawn behind the speech text to
    make it easier to read. ILBRK “Whole Screen” uses a full-screen
    character portrait, like the way that QFG4 worked.**

-   **Speech portrait side - if you're using Sierra-style
    speech, then this determines whether the portrait appears on the
    left or the right of the screen. The “alternate” setting means it
    swaps sides whenever a different person talks, and the “Based on X
    position” setting means that the side of the screen is chosen
    depending on where the characters are standing.**

-   **Room transition style - defines what type of screen
    transition is used when moving from one room to another. Various
    options are available.**

-   **Save screenshots in save games - Saves a
    mini-screenshot of the player's current position into the save
    game file. This will create larger save game files, but it will mean
    that you can use a save game thumbnails GUI to make the save/load
    interface more professional.**

-   **Enforce object-based scripting - Puts the script
    compiler into strict mode, where it will not accept the old-style
    (pre-AGS 2.7) script commands. This should preferably be ticked,
    since you should no longer be using the old commands.**

-   **Left-to-right operator precedence - if this is
    ticked, then operators of equal precedence in the script will be
    evaluated left to right. For example, 5 - 4 - 3 could be interpreted
    as (5 - 4) - 3 or as 5 - (4 - 3), thus giving different results. You
    should always use parenthesis to clarify expressions like this, so
    that the operator precedence doesn't affect the result.**

-   **Pixel-perfect click detection - normally, when the
    player clicks the mouse, AGS just checks to see if the cursor is
    within the rectangular area of each character and object on
    the screen. However, if this option is checked, then it will further
    check whether the player clicked on an actual pixel of the object
    graphic, or whether it was a transparent part of the graphic. If
    this option is enabled and they click on a transparent pixel, then
    the hotspot behind the object will be activated instead.**

-   **Don't automatically move character in Walk mode -
    normally, when you click the mouse in the Walk mode, the main
    character will move to where you clicked. However, if you want to
    create a game all viewed from a 1st-person perspective, and so don't
    have a main character, then selecting this option allows you to use
    the Walk mode for other things. If selected, then “Character stands
    on hotspot” events are instead triggered by clicking the Walk cursor
    on the hotspot.**

-   **Don't use inventory graphics as cursors - normally,
    when you select an inventory item the mouse cursor is changed into
    that item. However, if you want to create a Lucasarts-style game
    (where the inventory cursor is always a cross-hair), check this
    option and it won't be changed.**

-   **Don't scale up fonts at 640x400 - normally, if the
    player chooses 640x400, then the fonts will be scaled up to match.
    However, if you have drawn your fonts for the 640x400 resolution,
    use this option to stop them being stretched.**

-   **Resources split every Mb - see for information.**

-   **Characters turn before walking - specifies that when
    a character starts to walk somewhere, it will first turn round to
    face the correct direction using available animation frames, rather
    than just suddenly switching to face the right way.**

-   **Override built-in inventory window click handling -
    AGS has some built-in processing of Inventory Window GUI controls,
    whereby a right-click will Look at the item, and a left click will
    select it if the cursor mode is Interact. However, if you enable
    this option, then clicking on an inventory item in an Inventory
    Window will call your `on_mouse_click` function with eMouseLeftInv,
    eMouseMiddleInv or eMouseRightInv, and you then need to process
    it yourself. You can use the `game.inv_activated` variable to find
    out what they clicked on.**

-   **Enable mouse wheel support - if enabled,
    on\_mouse\_click can be called with the values eMouseWheelNorth and
    eMouseWheelSouth, which signify the user scrolling their mouse wheel
    north or south, respectively.**

    **NOTE: Not all mice have mouse wheels, and the DOS
    engine does not support the mouse wheel at all. Therefore, your game
    should never require the mouse wheel in order to be playable - it
    should only be used as a handy extra.**

-   **Number dialog options - enables keyboard shortcuts to
    choose dialog options (keys 1-9) and adds an index number before
    each dialog option when they are displayed to the player. For
    example,**

        1. Hello there!
        2. Goodbye

    This allows you to visually show the player which option the
    shortcut keys will choose, as well as seperating the options if you
    don't use a bullet point.

-   **Dialog options go upwards on GUI - Normally, if you
    select a non-textwindow GUI for the dialog options, they will be
    printed from the top down. However, if you select this option they
    will go from the bottom of the GUI upwards.**

-   **Crossfade music tracks - This allows you to tell AGS
    to crossfade between your background music tracks. Crossfading means
    fading out the old track while fading in the new one when the
    music changes. You can select a crossfade speed from the drop-down
    list. There are some disadvantages to using this option - firstly,
    it's fairly slow, since AGS has to decode two music files at once.
    Secondly, it only works with OGG, MP3 and WAV music. You cannot
    crossfade MIDI, XM, MOD, S3M or IT music.**

-   **Anti-alias TTF fonts - If enabled, any TTF fonts you
    have in your game will be rendered to the screen anti-aliased. This
    can make them look a lot better, but it has two drawbacks - firstly,
    anti-aliasing is significantly slower than normal rendering, so you
    might want an option to allow the player to turn it off. Second,
    anti-aliasing only works in hi-color games (in 256-colour games, the
    output will look blurred and unreadable). **NOTE that
    anti-aliasing is not currently done on lucasarts-style speech due to
    technical reasons.****

-   **Thought uses bubble GUI - Determines which text
    window GUI is used for displaying thoughts with .**

-   **Characters turn to face direction - if set, then when
    a character turns round with the or script commands, they will
    visibly turn around using their available loops. If this option is
    not set, they will immediately appear facing their new direction.**

-   **Write game text backwards - in-game text will be
    written right-to-left, ie. line breaks are worked out from the end
    of the sentence going backwards, and the last words are
    displayed first. This is used by languages such as Arabic
    and Hebrew.**

-   **Display multiple inventory items multiple times -
    normally, if the player has two of an inventory item, the item will
    still only be shown once in the Inventory window. If you check this
    option, however, then all the copies of the item that the player has
    will be displayed. Useful for RPG-style inventories.**

-   **Save games folder name - if this is blank, then the
    player's saved games will be saved to the folder where the game
    is installed. This is not a good idea, because it forces different
    users on the same machine to share save games, and Windows Vista and
    later versions discourage games from writing to the Program
    Files folder. Instead, if you supply a folder name here, then AGS
    will automatically create it within the user's Saved Games (Vista
    and later) or My Documents (XP and earlier) folder, and their save
    games will be saved there.**

See Also: ILBRK See Also:

### Cursors

The Cursors node of the editor shows you the current mouse cursor modes
available in the game. Each cursor mode performs a different action
within the game. Double-click one to open it up.

The “StandardMode” option in the property grid tells AGS that this is a
'normal' cursor mode - ie. using this cursor will fire an event on
whatever is clicked on as usual. This mode applies to the standard Walk,
Look, Interact and Talk modes, but you can create others too. Do not
tick it for the Use Inventory mode, since this is a special mode.

The “Animate” option allows you to specify that the mouse cursor will
animate while it is on the screen. Choose a view number, and the cursor
will animate using the first loop of that view. You can make it animate
only when over something (hotspot, object or character) by enabling the
“AnimateOnlyOnHotspots” option.

The “AnimateOnlyWhenMoving” box allows you to do a QFG4-style cursor,
where it only animates while the player is moving it around.

Three of the cursor modes are hard-coded special meanings into AGS:

-   **Mode 4 (Use Inventory). This is special because the
    game decides whether to allow its use or not, depending on whether
    the player has an active inventory item selected.**

-   **Mode 6 (Pointer). This cursor is used whenever a
    modal dialog is displayed (ie. a GUI that pauses the game). Normally
    this is a standard arrow pointer.**

-   **Mode 7 (Wait). This cursor is used whenever the
    player cannot control the action, for example during a
    scripted cutscene. For a lucasarts-style game where the cursor
    disappears completely in this state, simply import a blank graphic
    over the wait cursor.**

For the standard modes,

-   Mode 0 will cause the player to walk to the mouse pointer location
    when clicked.

-   Modes 1, 2, 3, 5, 8 and 9 will run the event with the same name as
    the cursor mode.

### Fonts

AGS comes with a couple of default fonts, but you can replace the and
add your own. You can use both TrueType (TTF) and SCI fonts (Sierra's
font format).

SCI fonts can be created in two ways:

-   Extract the font from a Sierra game, using the SCI Decoder program
    available on the internet.

-   Create your own font and save it in SCI Font format, using the .

There are also some fonts available on the .

Note that SCI fonts are faster to render than TTF fonts, and so may give
your game a speed advantage. It's preferable to use a SCI font if you
can.

Go to the “Fonts” node in the main tree. Here you can see all the
current fonts listed underneath. You can create a new font by
right-clicking the “Fonts” node and choosing “New font”. To overwrite an
existing font, open it up and press the “Import over this font” button.

Fonts can have outlines. For lucasarts-style speech, outlines are really
a necessity since they stop the text blending into the background and
becoming un-readable. To outline a font, either set the OutlineStyle to
“Automatic” to have AGS do it for you, or you can use a specific font
slot as the outline font (it will be drawn in black behind the main font
when the main font is used).

**NOTE: If you go to your Windows Fonts folder, you will
not be able to select any fonts to import, since double-clicking them
will open them up in the Windows Font Viewer. Unfortunately there is
nothing I can do about this, you must either type the filename in
manually, or copy the font to another folder and import it from there.**

**NOTE: Font 0 is used as the normal text font, and font 1
is used as the speech font. To use any additional fonts, you can set the
Game.NormalFont and Game.SpeechFont properties in your script.**

Advanced room features
----------------------

This section describes slightly more advanced things you can do with the
rooms.

### Character scaling

AGS supports scaling of characters, where the character can appear to
get smaller as he walks away from the screen. Character scaling is
supported as part of the walkable areas in a room.

The reason why you have multiple colours available for the walkable
areas is because you can set a zoom level for each colour, which defines
how large the character will be while he is in that area. The default
for all walkable areas is `100%`, ie. full size. However, you can adjust
it using the “Walkable Areas” mode to anywhere from `10%` (one-tenth
size) to `200%` (double size).

The scaling settings can effect all characters and objects in the game.
For characters, it is on by default but you can disable the scaling for
an individual character by setting the “UseRoomAreaScaling” option in
that character's properties.

For objects, it is off by default but you can make a specific object
obey scaling levels by setting its “UseRoomAreaScaling” option.

If you set the “UseContinuousScaling” option, then rather than just
specifying a zoom level for the whole walkable area, you specify a min
and max zoom level. These specify the scaling at the top and bottom of
the walkable area. When the game is run, AGS will interpolate these
values to make the character smoothly scale down from one value to
another as he walks towards the back or front of the screen.

### Scrolling

It's easy to create scrolling rooms like the ones used in Lucasarts
games like Monkey Island (tm) and Day of the Tentacle.

To do this, just import a background scene that is larger than your game
resolution. For example, in a 320x200 game, 500x200 is a good size for
Lucasarts-type rooms.

That's all you have to do. Draw on the walkable areas, hotspots and so
on, as normal, and then save the room. The screen will scroll to follow
the main character around.

The script command allows you to manually scroll the room around if you
don't want it to follow the character.

### Importing a file as the walkable area mask

AGS has the ability to import an external BMP or PNG file to use as the
walkable-area, hotspot or walk-behind area mask. If you don't like the
way you have to draw these in the editor itself, you can draw them in
another program and then import them. This is also useful if you are
converting a game you were making with another game-creation system into
AGS.

To use the feature, click the “Import Mask” button (in the toolbar) in
the relevant mode of the Areas editor. There are some restrictions to
how this file must be drawn: it must be the exact same size as the
background scene, and it must be in 16-colour (4-bit) or 256-colour
(8-bit). Then, colour 0 on the bitmap signifies transparency and colours
1-15 are used as the respective hotspot/walk-behind/walkable area
numbers.

**IMPORTANT: Do NOT use any colour numbers above 15 on the
mask bitmap. Use only palette indexes 0 to 15.**

### Animating background scenes

If you want to have a lot of animation on the screen, you will come
across two problems if you try to do it using objects:

-   There is a limit on the number of objects per screen, so you may not
    be able to animate everything that you want to that way.

-   Objects slow down the game - the more objects on the screen, the
    slower the game runs.

The solution to these problems is to use an animating background scene.

How it works is this: Each room can have from 1 to 5 backgrounds.
Normally, each room just has one background. However, you can import up
to four extra backgrounds in each room, and if you do so then the game
will cycle through them, giving the effect of animation.

This gives two main advantages - you can animate the entire screen, and
due to the way the engine works, it doesn't slow down the game at all.

To import a second background for a room, load the room into the editor,
pull down the “Main background” list box, and choose the “Import new
background” option. Choose the file that's storing the background and
you're done.

To delete a background, select it then click the “Delete” button.

You define the speed at which the backgrounds will animate by setting
the “BackgroundAnimationDelay” option in the property grid for the room.
The default is 5, which cycles background every 5 frames.

**

NOTE: All the background scenes must be the same size.

NOTE: (256-colour only) The backgrounds frames each have their own
palette (unless you select “Share palette with main background” before
importing). This means that when the current frame switches in-game, the
palette will get reset - therefore you can't use special palette effects
such as CyclePalette or SetPalRGB on screens with animating backgrounds.

### Lighting effects

You can control the brightness of your characters, courtesy of the
“LightLevel” setting for room Regions.

By default this is `100%`, but you can change it from `0% to 200%`. This
number is the light level in the current walkable area. Smaller numbers
are darker, so that `0%` is pitch black and `200%` is very bright.

This feature could be useful if, for example, you have a street lamp on
your scene so when the character walks under it they get brighter, or if
a wall is shading the character from the light they can get darker.

You can alternatively use a colour tint for the region. If you select
this, then you can enter Red, Green and Blue values as numbers from
0-255, which reflect the colour you want the area to be tinted to. The
Amount setting determines to what extent characters will be tinted, and
is from 0-100.

**NOTE: Light levels only work when the character's graphic
is at the same colour depth as the background (ie. a 256-colour
character in a hi-colour game won't get lightened).**

**NOTE: In a 256-colour game, only darkening areas (light
level &lt; `100%`) will work. Also, depending on the room palette the
quality of the darkening will vary in 256-colour games.**

**NOTE: Light levels affect characters and objects,
depending on the “UseRoomAreaLighting” setting for each one. They do not
affect overlays or the background scene.**

Other Features
==============

This section describes AGS features that were not covered in the
tutorial.

Music and sound 
---------------

Sound and music are an essential part of any gameplay experience, and
AGS 3.2 and higher provides a re-written audio system giving you full
control over your game audio.

**File formats**

AGS is able to play the following types of audio file: OGG, MP3, MIDI,
WAV (uncompressed), MOD, XM, IT, S3M and VOC.

The only limitation to this is that AGS is only able to play one MIDI
file at a time. If you attempt to play two simulataneous MIDI music
files, the first one will be cut off when the second one starts playing.

If you haven't heard of OGG before, it's a digital music format, similar
to MP3, but achieving better compression and higher quality. More
importantly, it is a totally free format so no royalty payments or
licenses are required to use it. For more information and programs to
encode your music to OGG, see http://www.vorbis.org/

**Audio in the Editor**

Look under the “Audio” branch in the project tree. Here you'll find
sub-nodes called “Speech”, “Types” and two default folders called
“Music” and “Sounds”.

**Speech**

At the moment, voice speech files are not setup within the editor. See
the help page to find out more about adding speech to your game.

**Audio Types**

Audio Types allow you to group together similar types of audio files.
The standard distinction here is between Sound and Music, whereby you
usually only want one Music file to be playing at any one time; whereas
you might have several simultaneous sound effects.

Double-click on an Audio Type and it will open up; you can see its
properties in the Property Grid. Here, the “MaxChannels” setting allows
you to specify how many audio clips of this type are allowed to play at
the same time. The “VolumeReductionWhenSpeechPlaying” setting allows you
to have AGS automatically reduce the volume of these audio clips while
speech is playing, to make it easier for the player to hear the speech
over the background music.

You'll probably find that the default settings here are fine, and in
many games you won't need to change them.

**Importing audio files**

Now let's get on to the important question – how do you add sound and
music to your game? Well, if you right-click on the “Sound” or “Music”
folders (or any other folders that you create yourself), you'll see an
option called “Add Audio Files”.

Select this option, and you'll be given a dialog box to find the audio
files that you want to import. Once imported, they'll be assigned script
names automatically.

Double-click an audio file in the project tree to open a window where
you can preview it, as well as change its properties in the Property
Grid.

**Playing audio in the game**

The script to play an audio clip in the game is very simple. For
example:

    aExplosion.Play();

plays the audio clip called *aExplosion.*

**Priorities and channels**

AGS currently has an 8-channel audio system, which means that up to 8
sounds can be playing at the same time. With the default Audio Types
settings, one channel is reserved for speech, one for music and one for
ambient sounds; thus leaving 5 available for sound effects.

If you try to play an audio clip and there are no channels available,
then an existing one will be stopped and the new one will take its
place. However, this will only happen if the new audio clip has an
**equal or higher priority than one of the currently
playing sounds.**

Thus, the priority allows you to decide which audio clips are more
important than others. For example, you might set a footstep sound as
low priority, and a door opening as high priority. This can be
configured at the folder level in the editor, and also by changing the
properties of an individual audio clip (by default they will inherit
from their containing folder).

Sometimes you might not want the priority of the sound to be fixed in
the editor – you might want to decide it at run-time in the script. For
this reason the *Play command has an optional parameter
which allows you to explicity specify the priority when you play it, for
example:*

    aExplosion.Play(eAudioPriorityLow);

**Seeking and changing volume**

So, how do you change a sound once it is playing? Well, there are no
methods on the Audio Clip to do this, because you might be playing two
copies of the same sound at once, and then AGS wouldn't know which one
you wanted to access. That's where **Audio Channels come to
the rescue.**

When you use the Play() command, AGS returns to you an AudioChannel\*
instance representing the channel on which the sound is playing. You can
store this to a global variable and access it later on. For example:

    AudioChannel* chan = aExplosion.Play();
    chan.Volume = 20;

This will start the *aExplosion audio clip playing, and
then change its volume to `20%`.*

**Using Audio Channels**

Supposing you want to start playing a sound now, and then change its
volume or panning later on. How would you do that? Well, you'd need to
keep the AudioChannel around, so that you can access it later. The
easiest way to do that is to make it a Global Variable; if you open the
Global Variables editor, you can create a new AudioChannel\* variable
(let's call it *longWindedSound). Then when you play the
sound you set it like this:*

`longWindedSound = aExplosion.Play();`

later on, elsewhere in the script, you can change the volume by doing:

    if (longWindedSound != null)
    {
      longWindedSound.Volume = 20;
    }

Note the check for null here – this makes sure that your game won't
crash if the sound isn't playing (it might have finished, or not have
been started yet).

**Overall system volume**

There is a property called that controls the overall game volume, which
you can use with some sort of volume control slider for the player. All
individual sound volumes work within the overall system volume.

**Conclusion**

The new audio system in AGS gives you much more control over your game
audio. Please see the following sections for a complete list of the
supported commands:

,

### Voice speech 

With AGS you can link a line of dialog to a speech file, to enable
“talkie”- style games. Suppose you have a dialog script with the
following:

    ego: "Hi! How are you?"
    michael: "I'm fine."

Normally this would display the words in the speech text above the
characters heads. However, you can add the special character '&' to
symbolise that a voice file should also be played.

The file name has format XXXXY.EXT, where XXXX is made of up to
**first four letters of the character's script name (except
the leading 'c'), the Y is the speech file number (with no leading or
trailing zeroes or padding of any kind), and EXT is the file
extension.**

For example, if you have dialog script:

    ego: &10 "Hi! How are you?"
    michael: &7 "I'm fine."

or common script using Say script function:

    cEgo.Say("&10 Hi! How are you?");
    cMichael.Say("&7 I'm fine.");

Both of those examples would play EGO10.WAV with the first line, and
MICH7.WAV with the second. When a line of text has a voice linked to it,
the text on the screen will not be removed until the voice file has
finished playing. If the player interrupts it by clicking the mouse or
pressing a key, the text and voice will be stopped. Voice files must be
placed in the “Speech” sub-directory of the game folder.

**NOTE: WAV, OGG and MP3 format files can be used for
speech.**

**NOTE: You cannot use speech file numbers above 9999. That
is, you can have EGO1.OGG all the way up to EGO9999.OGG, but not
EGO10000.OGG or higher.**

Speech is compiled into a file called SPEECH.VOX and is separate from
the rest of your game data so that you can offer it as an optional extra
download to the player. The game will function correctly if the file is
not present.

*SeeAlso:*

### The AudioCache folder 

When you import audio files into AGS, you'll probably notice that a
folder inside your game folder, called AudioCache, starts to fill up
with files. What is it and why is it there?

Well, when you import audio into AGS, you might be importing it from
anywhere – it could be off your hard drive, but it might also be off a
USB stick or a CD. AGS can't rely on the audio files always being there
because you might remove the USB stick or delete the files on it.

Therefore, when you import audio into AGS it makes a copy of the file in
the AudioCache folder. AGS also remembers where the file came from, and
when you compile your game it will check if the file has been updated in
its original location – if so it will copy the latest version to the
AudioCache.

But if the source file no longer exists, your game will continue to
build just fine because AGS has its own copy of the file.

This allows AGS to stick to one of its core principles, that all the
files you need to build your game are within the game's folder. That
way, you have complete security in knowing that by backing up your game
folder, your game will be safe if the worst happens.

Editing the GUIs
----------------

The game interface is split up into GUIs. Each GUI is a rectangular
region on the screen which is drawn on top of the background scene. Each
can be set to either:

-   be always displayed (for example the Sierra status-line)

-   pop-up when the mouse moves to a certain position (eg.
    Sierra icon-bar)

-   pop-up on script command only

The default interface is made up of two GUIs - the status line, and the
icon bar.

Go to the “GUIs” node in the main tree. Under this all the GUIs in the
game are listed – double-click one to edit it. To create a new one,
right-click on the main “GUIs” node and choose “New GUI”.

Once you've opened up a GUI, you'll notice the GUI itself in the main
window, and its settings can be edited in the Properties grid. This
allows you to change the background colour of the GUI, set a background
picture, and set the location and width/height amongst other things.

The “Visibility” property allows you to set when the GUI is displayed.
The default is “Normal”, which means that the GUI will initially be
visible, though you can turn it off with a GUI.Visible=false command in
game\_start if you need to.

The “Popup modal” option means that the GUI will be initially off and
must be turned on by a script command. With this option, the game will
be paused while the GUI is displayed, during which time the
on\_mouse\_click and on\_key\_press functions will not get run.

The “Mouse YPos” option means that the GUI only appears when the mouse
vertical position moves above the y-coordinate set with the “Popup-YP”
option.

“Persistent” is like “Normal”, except that this GUI will not be removed
during a cutscene when the setting “GUIs turn off when disabled” is set
in the general settings. Useful if you want most of your GUIs to turn
off, except a status line or whatever.

The “Z-Order” setting allows you to set which order the GUIs are drawn
in - ie. when there are two GUIs that overlap, which is drawn in front.
The Z-order setting is an arbitrary number between 0 and 1000. AGS draws
the GUIs in order, from the lowest numbered at the back to the highest
numbered at the front.

The “Clickable” setting allows you to set whether the GUI and buttons on
it respond to mouse clicks. This is on by default, but if you turn it
off and the player clicks on the GUI, the game will actually process the
click as if they clicked behind the GUI onto the actual screen. Useful
for transparent GUIs which are only used to display information.

You'll notice that the GUIs have names. These can be used in the script
in the same way as character names. For example, if a GUI is called
“gIconBar”, you can use scripts such as:

`gIconBar.Visible = true;`

### GUI buttons

To provide interactivity with the interface, you use buttons.

To add a button, click the “Add button” button in the toolbar, and then
drag a rectangle with the mouse onto the GUI. You will see it displayed
as a text button, with the text “New button” on. Notice that the
Properties window is now displaying properties for your new button
rather than the GUI.

Using the Properties window, you can set a picture for the button
instead, and you can also set various other self-explanitory attributes.
You set what happens when the player clicks on the button by using the
“Click Action” attribute. This can be set to “Run Script” (the default),
and also “Set mode”, which changes the cursor mode to the mode specified
in the “New mode number” property.

To delete a GUI button, right-click it and choose Delete.

### Interface text

You can easily display static text on interfaces. For example, the
Sierra-style interface displays the score in the status bar.

To show text to a GUI, you need a label. Click the “Add label” button in
the toolbar, then drag out a rectangle like you did when adding a
button. You can change the text displayed in the label by editing the
“Text” property. Notice that the text automatically wraps round to fit
inside the rectangle you drew.

As well as typing normal text into the label, you can add some special
markers which allow the text to change during the game. The following
tokens will be replaced with the relevant values in the game:

     @GAMENAME@    The game's name, specified on the Game Settings pane
     @OVERHOTSPOT@ Name of the hotspot which the cursor is over
     @SCORE@       The player's current score
     @SCORETEXT@   The text "Score: X of XX" with the relevant numbers filled in.
     @TOTALSCORE@  The maximum possible score, specified on the Game Settings pane

Example: You have @SCORE@ out of @TOTALSCORE@ points.

The Properties window also allows you to align the text to left, right
or centre, as well as change its font and colour.

### Customized Text Windows 

If you want to add a personal touch to the standard white text-boxes
which display all the messages during the game, you can create a border
using the GUI Editor. Right-click the “GUIs” node, and choose “New Text
Window GUI”.

The element will be resized to about 1/4 of the screen, and you will see
8 pictures - one in each corner and one on each side. These are the
border graphics. You change the graphic for a corner in the normal way.

In the game, the corner graphics will be placed in the respective
corners of the text window, and the side graphics will be repeated along
the edge of the window. To tell the game to use your custom text window
style, go to the General Settings pane, and check the “Text windows use
GUI” box. Then, enter the number of the GUI which you used.

You can also set a background picture for the text window. In the GUI
editor, simply set a background picture for the GUI element. The graphic
you specify will not be tiled or stretched in the game; however, it will
be clipped to fit the window. You should use a graphic of at least about
250x80 pixels to make sure that it fills up the whole window.

To set the text colour in the window, simply set the Foreground Colour
of the GUI and that will be used to print the message text in.

Additionally, you may configure padding - the distance kept between text
window's border and text inside of it.

### Custom inventory

Another option you may have noticed in the GUI editor is the Add
Inventory button. This allows you to drag out a rectangle which will
display the player's current inventory, in the same way as the Lucasarts
games did. To make the inventory window scrollable, you will need to add
Up and Down arrow buttons, and attach script code to those buttons to
use the available functions such as and .

To see a full list of commands available for inventory windows, see the
section.

### Sliders

You can now add sliders to your GUIs. This allows you to have a nice
interface for the player to change settings such as volume and game
speed. To add a slider, click the “Add slider” button and drag out its
rectangle just like you would for a button. You can also resize it by
dragging the bottom- right hand corner out in the same way as a button.

Sliders can be either vertical or horizontal. The direction that it is
drawn in is automatic depending on the size that you stretch the slider
box to - if it is wider than it is tall you will get a horizontal
slider, otherwise you'll get a vertical slider.

For the properties of a slider you can set the minimum, maximum and
current values that the slider can have. In the game, the user will be
able to drag the handle from MIN to MAX, and the slider will start off
set to VALUE. For horizontal sliders, MIN is on the left and MAX on the
right, for vertical sliders MAX is at the top and MIN is at the bottom.

Whenever the user moves the handle's position on the slider, the
OnChange event is called. This means that if they continually drag the
handle up and down, the event will get called repeatedly.

Your script can find out the value of the slider using the Slider.Value
script property.

### Text Boxes

A text box is a simple device that allows the player to type information
into your game. Adding a text box works like adding the other types of
control.

If a text box is on a currently displayed GUI, all standard keypresses
(ie. letter keys, return and backspace) are diverted to the textbox
instead of being passed to the on\_key\_press function. When the player
presses Return in the text box, the OnActivate event is called. You can
then use the TextBox.Text property to retrieve what they typed in.

### List Boxes

List box controls allow you to add a list of items to your GUI. This
could be useful for doing a custom save/load dialog box, allowing the
user to choose between various options, and so forth.

You use the ListBox script functions to manipulate the list box - for
example, ListBox.AddItem to add an item, or ListBox.SelectedIndex to get
the current selection.

The ListBox.Translated property defines whether the translation will be
applied to list items or not. It is recommended to disable translation
for lists containing saved games.

The OnSelectionChanged event is fired when the player clicks on an item
in the list. You may wish to ignore this or to do something useful with
it.

Distributing your game 
----------------------

When you choose the “Build EXE” option in the Editor, a “Compiled”
sub-directory is created in your game's folder, where more
subdirectories are created in turn for every target platform you are
building the game for. For example, “Compiled/Windows” subfolder will be
created if you have Windows build checked in General Settings, and
“Compiled/Linux” subfolder if you have Linux build enabled. The
“Compiled” folder itself will contain all the “raw” game files that
cannot be run on their own, but distinct subfolders will contain a
runnable variant of the compiled game for corresponding operating
system. For example, if you want to distribute Windows version of your
game, you need to take the contents of “Windows” subfolder. At its
simplest this will just be your game executable and the setup program,
but you may also have audio and speech libraries (AUDIO.VOX and
SPEECH.VOX); and if you have selected to split resources files, you will
also have several files named “game.001”, “game.002”, and so forth.

So, when you want to upload your game to the internet, just zip up the
files in the “Windows” folder, and there you go!

*NOTE: It is not possible to load the exe file back into the AGS
Editor. This means two things when only the EXE file is available: (1)
other people can't edit your game's data, and (2) you can't either.
Always keep a backup of the other files produced (\*.CRM, GAME.AGF, etc)
as they are what the Editor needs to be able to load your game for
editing.*

*TIP: You can make a “Loading...” style splash screen to be
displayed while your game starts up. To do so, simply save the image as
PRELOAD.PCX (must be the same resolution and colour depth as the game)
in the game folder, and build the game. It should then display while the
game is loading.*

*NOTE: Due to the licenses of code used by AGS, your documentation
should acknowledge the following:*

TrueType font display uses ALFont by Javier Gonzalez and the Freetype
project. Distributed under the terms of the FreeType project license.

OGG player is alogg by Javier Gonzalez, using the Ogg Vorbis decoder,
which is available from http://www.xiph.org/ Copyright (c) 2002-2008,
Xiph.org Foundation

MP3 player is almp3, by Javier Gonzalez and the FreeAmp team. It uses
the mpg123 MP3 decoder, and is distributed under the terms of the GNU
Lesser General Public License version 2.1.

You should also include all the license\_\* files from the DOCS
directory with your game.

**IMPORTANT: If you intend to make money for your game, be
it shareware or commercial, it is imperative that you read the Legal
Information page on the AGS website, currently at
http://www.bigbluecup.com/aclegal.htm**

**NOTE: The AUDIO.VOX file contains audio clips that you
have marked as “InSeperateVOX” in the editor. This allows you to have an
optional audio download, if your game uses lots of sound files but you
don't want the player to have to download them.**

### Custom icon

If you wish, you can use your own custom icon when you build a Windows
EXE file. To do this, simply place your icon in your game's folder, and
name it USER.ICO. Then, load the editor and save the game.

AGS is only able to build your custom icon if you are running the editor
on Windows 2000 and later. If you're using Windows 98 then your game
will be built with the standard AGS icon.

*NOTE: The icon **must be a proper Windows .ICO file,
**not just a renamed BMP file. Icon editors, such as
AX-Icons from http://www.axialis.com, will convert it for
you.*****

You can also have a custom icon for the Setup program generated. To do
so, create your icon as above but name it **setup.ico in
the game folder.**

### Splitting resource files 

Some people found that once their game became large, the single EXE file
was slow to load due to anti-virus checkers scanning the whole file. AGS
includes an option to split up the resource files into smaller chunks to
avoid this happening. On the General Settings pane you'll notice a
setting “Split resource files into X Mb sized chunks”.

If you tick this, then type in a number such as 1 or 2, then save the
game, the game data will be split up into chunks that size, named
GAME.001, GAME.002 and so on.

Some resources are still combined into the EXE file but all the rooms
will be placed into the other files. If you use this option, you need to
distribute your game's EXE file plus all the GAME.00? files.

Backing up your game
--------------------

You will no doubt want to back up your game files, and should do so
regularly during your game development. But which files should you back
up?

When taking a backup, make sure you copy **ALL the files
listed below:**

-   **GAME.AGF - this is the main data file for your game
    and contains almost all of the game settings. Without it, your game
    is lost.**

-   **ACSPRSET.SPR - this is your game's sprite file,
    containing all the sprites from the sprite manager.**

-   **ROOM\*.CRM - all the ROOM\*.CRM files are your room
    files, and obviously without one of them you wouldn't be able to go
    into that room any longer.**

-   **\*.ASC, \*.ASH - these are your script files, and
    contain all of your scripting handywork.**

-   **\*.TRS - translation source files. They contain any
    translations that you've had done.**

-   **AGSFNT\*.TTF, AGSFNT\*.WFN - these files contain any
    fonts you have imported.**

Also remember to back up any sound, music and video files you are using.

The text parser 
---------------

You can now use a text parser in your games if you wish to, much as the
older Sierra games did. Go to the “Text parser” pane in the editor.
There, you will see a short list of words which are provided for you.
Each word has a number beside it.

Basically, you add words you want to use by right-clicking the list, and
selecting “Add word”. However, the real beauty of the parser is its
ability to recognise synonyms - that is, two words that mean the same
thing. So, for example, if you wanted the player to type “look at
fence”, they might well type “look at wall” instead, if that's how they
see the drawing. Or, a British person might type “colour” whereas an
American might type “color”, both of which should have the same effect.

To add a synonym for an existing word, highlight the current word,
right-click it and choose “Add synonym”. You'll notice that the new word
is given the same number as the old one. All words with the same number
are considered identical by the parser.

You will notice that the provided list has a lot of words with number 0.
This is a special number, that indicates that the parser should ignore
the word completely. In our previous example, the player might type
“look at the fence”, “look at fence”, or just “look fence”. By adding
words like “at” and “the” to the ignore list, they get stripped out of
the user's input automatically. To add new ignore words, just select an
existing one and add a synonym.

So, how do you use the text parser? Well, you'll need a text box GUI
control somewhere in order for the user to type in their input, or you
could just use the InputBox command (but it has quite a short line
length).

When the user has typed in their text (you'll probably know this by the
text box's event being activated), you call the Parser.ParseText script
function which tells AGS what input string to use in subsequent
commands. You then simply use the Said command to test what the player
typed in.

You type the whole sentence (but NOT including any ignore words), and
AGS will compare it to the user's string, considering all synonyms
identical. For example (assuming our text box is called “txtUserInput”):

      String input = txtUserInput.Text;
      Parser.ParseText(input);
      if (Parser.Said("look fence")) {
        Display("It's an old wooden fence.");
      }
      if (Parser.Said("eat apple")) {
        Display("You'd love to, but you don't have one.");
      }

There are a couple of special words you can use with the Said command.
“anyword” will match any word that the user types in. For example,
Said(“throw anyword away”) will match if they type “throw dagger away”,
or “throw trash away”. “rol” (short for Rest-of-Line) will match the
rest of the user's input. So, you might want to do:

    if (Parser.Said("kill rol")) {
      Display("You're not a violent person.");
    }

This way if they try to kill anything they will get the generic
response.

Sometimes, you want to accept two different words that are not synonyms
as the same thing. For example, the words “take” and “eat” normally have
totally different meanings, so you wouldn't make them synonyms of each
other. However, if the player has a headache tablet, for instance, then
“take tablet” and “eat tablet” would both be valid. This is where the
comma “,” comes in - if you include a comma in your input, all synonyms
of all words separated by the comma will match. So:

    if (Parser.Said("eat,take tablet"))

will match eat or take and all their synonyms, then tablet and its
synonyms.

Another fairly common task with a parser is to check for optional words
- for example, if there is a brick wall on the screen, you want the
player to be able to type “look wall” and “look brick wall”. Although
this can be done with two OR'ed Said commands, AGS makes it easier. You
can use \[brackets\] to signify an optional word. So:

    if (Parser.Said("look [brick] wall"))

will match “look wall” and “look brick wall”.

Now this is all very well, but in different rooms you have different
items to interact with - for example, in one room there might be a tree
that the player should be able to type “look at tree” to look at, and so
on. Putting all this in your global script would make a big mess. So,
enter the function. Using this, you can do:

      Parser.ParseText(input);
      String badWord = Parser.SaidUnknownWord();
      if (badWord != null)
        Display("You can't use '%s' in this game.", badWord);
      else if (Parser.Said("eat apple")) {
        Display("You'd love to, but you don't have one.");
      }
      ... // other game-wide commands
      else
        CallRoomScript (1);

Then, the room script can check for things that the player can do in the
current room. See the description for more information.

Translations
------------

AGS now makes it easy for you to create translations of your games.
Right-click the “Translations” node in the tree, and choose “New
translation”. Once you've named it, AGS will ask if you want to populate
the file now. Say yes.

Creating the translation writes all lines of game text to the file - no
script sources, just all the displayable text from the game. The file is
generated with each line of text separated by a blank line.

You can now give this file to your translators. They should **fill
in each blank line with the corresponding translation of the English
line above it (DO NOT REPLACE THE ORIGINAL ENGLISH LINES WITH THE
TRANSLATION). If a line is left blank, it will simply not be
translated.**

Once the translation is done, right-click the translation and choose
“Compile”. It will be converted into a compiled translation (`.TRA`)
file in the Compiled folder, which can be used with the game engine.

Run the game Setup program, and select the translation from the
drop-down box. Then, run the game, and all the text should be
translated.

*NOTE: With SCI fonts, only 128 characters are available, so many
of the extended characters needed for non-english translations are not
available. You may need to use substitute characters, or consider using
TTF fonts for international applications. However, bear in mind that TTF
rendering slows down the engine.*

While most in-game text is translated automatically, there are a few
instances when this is not possible. These are when a script uses
functions like Append to build up a string, or CompareTo to check some
user input. In these cases, you can use the function to make it work.

You'll also have noticed a “Update” option when right-clicking a
translation. This is useful if you've got a translated version of your
game, but you want to update the game and add a few bits in. Once you've
updated your game, run the Update Translation option and the translation
file you select will get any new bits of text added to it at the bottom
– then you can just ask your translator to additionally translate these
lines.

Global variables 
----------------

The Global Variables pane allows you to easily add variables to your
game which can then be accessed from all your scripts.

In previous versions of AGS, declaring a global variable in the script
involved defining it in three different places, with import and export
clauses in the appropriate locations. Now, this whole process is vastly
simplified with the new Global Variables Editor.

**When should I use a global variable?**

Use a global variable when you need to store some information that you
need to access from different scripts. For example, if you want to store
the player's health and you want all your different scripts to be able
to access this value, then use a global variable.

If you just need to store some information locally (for example, a “door
opened” flag that only applies to one particular room) then you should
declare the variable manually at the top of the room's script file
instead.

**What about GlobalInts and Graphical Variables?**

GlobalInts and Graphical Variables were ways in which previous versions
of AGS provided global variable capabilities. They are now considered
obsolete, and are replaced with this new Global Variables system
instead.

**How do I use global variables?**

The Global Variables Editor is pretty self-explanitory. To add a
variable, right-click and choose “Add”. You can name the variable, and
choose its type and initial value. Most of the time you'll probably be
using the *int and *String types. Optionally,
you can also set a default value for the variable.**

Then, in your scripts it's a simple matter of just using the variable
with the name that you gave it. Simple! So, for example if you add an
int global variable called “myVariable”, then in your script you can
just do things like this:

    if (myVariable == 3)
    {
      myVariable = 4;
    }

or

`Display("myVariable: %d", myVariable);`

That's it! Just use it as you'd use any other variable declared in the
script.

Note that some of the types available are managed instance pointers,
like “GUI”, “DynamicSprite” and “Character”. These are for more advanced
users only. If you create one of these you cannot set a default value,
and it will initially be set to *null. You will need to
initialize the pointer in your script to point to something before you
use it.*

Custom Properties
-----------------

**What are custom properties?**

Suppose you're making a Lucasarts-style game, and you want all your
hotspots to have a default event (so if the player right-clicks a
window, for example, “Open” will be the default, but if they click on a
pen, “Pick up” will be the default).

To do that, surely you would have to script in lots of code to change
the default mode over each different object?

This is where Custom Properties come to the rescue. You can create a
custom property for “Default event”, for example, and then have some
simple code in the global script to use the setting accordingly.

**How do I use them?**

You'll notice that characters, objects, hotspots, rooms and inventory
items all have a “Properties” option in their property grids. Select it
and click the “...” button.

Since you don't yet have any custom properties, you'll get a blank
window, so click the “Edit Schema” button. This takes you to the Schema
Editor, where you can create the various properties you want in your
game. To begin with you are presented with an empty list box, so
right-click in it and choose “Add property”.

In the “Add Property” window you can set various options about the new
property:

-   **Name - this is the name by which you will access the
    property from the script. This cannot be changed after the property
    has been created.**

-   **Description - this is the user-friendly description
    which will be displayed in the custom property editor when you are
    setting the property.**

-   **Type - this specifies what type of property you want.
    “Boolean” gives you a checkbox (which will return 0 or 1 to the
    script), “Number” gives you a text box which you can type numbers
    into, and “Text” gives you a larger text box which can store
    a string.**

-   **Default value - this specifies what the default value
    of the property will be for objects where you have not set
    it specifically.**

For example, add a new “Boolean” property. Close the schema editor, and
then click the “Properties” button again. You'll now have a window with
a checkbox with the description text you typed in. You can click the
“Edit schema” button there to return to the schema editor if you like.

All types of game item share the same schema. That is, if you create a
“Jibble” property in the schema editor for a hotspot, it will also
appear in the properties window for characters, objects, and so on.

**Getting and setting values in the script**

To access the properties from the script, there are various script
functions. See their descriptions for how they work:

, ILBRK , ILBRK , ILBRK , ILBRK , ILBRK , ILBRK , ILBRK , ILBRK , ILBRK
,

**NOTE: Calling will reset that room's properties to
default values, as well as that room's hotspot and object properties.**

Plugins
-------

AGS supports user-written plugins in order to provide functionality to
your game that AGS itself does not support.

The plugin developer's guide is available from the Resources section of
the AGS website.

Plugins come as DLL files with the names AGS\*.DLL, for example
agscircle.dll might be a plugin providing a DrawCircle script function.

**How to use a plugin**

So, you've downloaded a plugin for AGS. What do you do with it? Well,
firstly read any readme file that the plugin author has included. But to
get any plugin to work you must do the following:

1\. Place a copy of the plugin files in the AGSEDIT directory (not your
game folder).

2\. Start the AGS Editor up, and load your game. Go to the Plugins node
in the main tree. Open it up, and you should see all available plugins
listed. To use one in your game, right-click it and choose “Use plugin”.
The plugin developer should provide instructions on what to do next.
Save your game to make sure that AGS remembers that you want to use the
plugin.

Lip sync
--------

Lip sync is a way to animate character talking in connection with
particular letters and their combinations (phonemes).

Normally when a character is talking, AGS simply cycles through the
speech animation from start to finish, and then loops back round.
However, lip syncing allows you to be cleverer by specifying a
particular frame to go with various letters and sounds. Then, as the
character talks, AGS plays appropriate frames to simulate the character
actually saying those words.

Lip sync is being configured on corresponding 'Lip Sync' pane in the
editor.

### Text-based lip syncing

In the Lip Sync Editor, you have 20 text boxes, one for each possible
frame of the talking loop. In each box, you can enter all the letters
which will cause that frame of the loop to be played. Letter
combinations such as 'th' and 'ch' can be used too - AGS will match each
part of the spoken text to the longest possible phrase in the lip sync
editor.

separate the letters by forward slashes. For example,

    3  R/S/Th/G

will mean that frame 3 of the character's talking animation is shown
whenever the letter R, S, Th or G is spoken.

The “Default frame for unlisted characters” box allows you to set which
frame is used when a character not listed in any of the text boxes is
encountered.

### Voice-based lip sync

AGS supports lip syncing voice speech to the talking animation. If you
enable this feature, you cannot use the standard lip-sync for non-voice
lines.

**NOTE: This is an unofficial feature and is not currently
supported. Use at your own risk**

**NOTE: The voice sync feature only supports Sierra-style
speech.**

In order to do this, you need to download one of the third-party
applications that produce lip sync data based on voice clips. AGS
supports two such data formats: **PAMELA and
**Papagayo.****

### PAMELA

Download PAMELA application by the following link:
`http://www-personal.monash.edu.au/~myless/catnap/pamela/`

Set up the phenomes in Pamela so that there are only 10 (or as many
talking frames as you have) available choices. Then, in the Lip Sync
pane of AGS, change the Type property to “Voice”. Enter the Pamela
phenomes into the text boxes to create the association between the
pamela phenome code and the AGS frame number.

For example, enter “AY0” into frame 0's box, “E” into frame 1, and so
forth - corresponding to how it is set up in Pamela. For multiple
phenomes to share the same frame, seperate them with forward slashes –
for example, “AY0/AY1” allows both of those phenomes to correspond to
the specified frame.

Use the Pamela application on each of your speech lines, and save a
Pamela project file (.pam file) for each speech file, naming it the same
as the speech.

For example, the pamela project for EGO46.OGG would be called EGO46.PAM,
placed in your game's Speech folder.

When you build the game, this pam file is compiled into the speech.vox
and will be used to sync the animation of the talking frames during the
game.

**NOTE: Voice lip sync does not work well with MP3 files.
It is strongly recommended that you use OGG or WAV for speech.**

### Papagayo

Download Papagayo application by the following link:
`http://www.lostmarble.com/papagayo/`

First you would need to set up your 10 or so phonemes associations (as
described above for PAMELA).

Then start up the Papagayo program and open a speech file in .WAV
format. The waveform will appear on-screen, represented by a blue,
horizontal bar. You can press the triangular 'Play' button at the top of
the screen to listen to the speech audio.

In the “Spoken Text” field at the bottom of the screen, type in the
exact text words heard in the speech file. As you type, you will notice
that each word appears as a horizontal orange bar above the blue
waveform. At the same time, individual pink phonemes start appearing
below the blue waveform bar. (These pink phonemes at the bottom should
correspond to the fields in AGS editor's “Lip Sync” tab).

If you play the speech audio at this point, you'll see that the mouth
image at the upper right corner of the screen changes as each pink
phoneme is reached during playback. However, the result will not be
perfect. To remedy this, you need to drag the orange words at the top of
the screen so that their length matches up with the timing of each
spoken word in the audio. Double-clicking an orange word will make that
portion of the audio play, so you can test if it's accurate.

Sometimes an orange word will contain too many, too few, or inaccurate
phonemes. You can edit these by right-clicking an orange word and
adding, editing, or deleting the desired phonemes. Each one should be
separated by a space.

For even further accuracy, individual pink phonemes can be dragged left
or right to position them more precisely.

When you're happy with the results, you can save the project as a .pgo
file, which will allow you to open and re-edit this line later. But to
use it in AGS, click the “Export” button at the bottom right side of the
screen, and save it as a .dat file.

Use the Papagayo application on each of your speech lines, and export a
Papagayo file (.dat file) for each speech file, naming it the same as
the speech.

For example, the Papagayo project for EGO46.OGG would be called
EGO46.DAT, placed in your game's Speech folder.

When you build the game, this dat file is compiled into the speech.vox
and will be used to sync the animation of the talking frames during the
game.

New Game templates
------------------

When you choose “Start a new game” in the initial “Welcome to AGS”
dialog box, a window appears with various templates that you can base
your game off.

AGS comes with a few standard templates, but you can create your own
too.

**Using downloaded templates**

If you've downloaded a game template from the internet, you should find
a file with a .AGT extension. This is the AGS Template File, and you
just need to copy it into the “Templates” folder within the AGS Editor
directory.

**Creating your own template**

A game template is basically just an archive containing all of the game
source files, which are then extracted into the new folder when the user
creates a new game. It is similar to you just zipping up your game
folder and sending it to a friend - except that this way looks far more
professional.

To create a template, first of all you create a game as normal in the
editor. Once you have everything set up how you want it, select “Make
template from this game” on the File menu. This will prompt you for a
name for the template (this is what will appear under its icon in the
“Start New Game” dialog box), and then it will go away and compile the
template for you.

The template game takes the following files from your game folder: Core
game files (GAME.AGF, ACSPRSET.SPR), all script and room files, all
sound and music files, all fonts, game icons, and \*.TXT (to allow you
to include a README.TXT or whatever).

If you include a **template.ico file in your game folder
when you make the template, then it will be used as the icon in the
Start New Game dialog box. Otherwise, the icon will be taken from
user.ico (if present), or if not it will get the default AGS icon.**

You can also include a “template.txt” file in your game folder. If you
do, then its contents will be displayed to the user in a messagebox
after they create a new game based on the template. You could use this
to explain briefly about any key aspects of the template, or it could
tell them to read your README.TXT file. This file should be quite small
- its entire contents need to fit into a standard message box.

**NOTE: Do not simply make a template out of a
half-finished game. If you want to make a template, you should start a
game from scratch and make your changes - the user probably doesn't want
to already have a semi-completed game when they use your template.**

Debugging features 
------------------

It happens to the best of us - you're merrily ploughing along making
your game, when suddenly something just isn't working right. It's not
always obvious where the problem is.

AGS now has some advanced debugging features that can help you out. If
all else fails, you can of course ask for help on the AGS forums.

There are two different types of debugging, that are enabled in
different ways. The script debugger is only enabled when you use F5 to
run your game; but the Debug() commands are only available when “Enable
debug mode” is set in your Game Settings. So, just before you release
your game, set that option to False and compile the game again to make
sure the player can't cheat using these features.

**1. The script debugger**

When you run the game using the Run (F5) option, the game will be
started with the debugger. This allows you to pause your game and follow
it through one line at a time.

There are two main ways to use this feature:

\* Press SCROLL LOCK while playing the game. This will break out when
the next line of script is run.

\* Place a breakpoint in your script. You do this by clicking on a line
of code in the script editor, then pressing F9. Then, when the game
arrives at this line of code, it will stop running.

**NOTE: The editor will allow you to place a breakpoint on
any line of script. However, in order for it to work, it must be placed
on a line that has some code on it.**

Once the script has stopped, you can use the “Step Into” button (F11) to
step through the lines of code, one by one. To allow the game to
continue running normally, use the Run (F5) button.

**NOTE: The Script Debugger is not supported on Windows 98
or Windows ME systems. If you're still using Windows 98, please upgrade
to Windows XP or higher to take advantage of this feature.**

**2. The Debug() command**

There is a scripting command, , which you can use in your script to help
you find problems. The default setup enables some hotkeys for the
various features - in particular, Ctrl+X allows you to teleport to
another room, Ctrl+A shows the walkable areas on the screen and Ctrl+S
gives you all the inventory items.

You can also use the Debug command to assign a hotkey to toggle FPS
display on and off. (FPS is Frames Per Second, which allows you to see
the game speed and spot any slow-running rooms).

This command only works if Debug Mode is enabled in your Game Settings.

**3. Current room information**

Pressing Ctrl+D displays some information about the current room. It
tells you what room number you are in, followed by the current status of
all objects in the room. After that, another messagebox tells you all
the characters that are in the current room and various information
about them.

This command only works if Debug Mode is enabled in your Game Settings.

Auto-number speech files
------------------------

If you've already made your game, and then you decide you want a voice
pack to go with it, the thought of manually adding speech numbers to
every line of speech in the game is rather daunting. But never fear,
this is where the Auto-number Speech Files feature comes in.

If you select this option, then it will go through all the speech lines
in the game and add a &NUM to the start of them. A summary of the
results is written to a file called SPEECHREF.TXT in the game folder, so
that you can easily see what file is what when recording the speech.

The following types of message are auto-numbered. If one of the messages
already has a speech number, it will be overwritten:

-   room messages set to be displayed as speech

-   dialog script messages

-   dialog options (if “Say” is selected for the option)

-   Say commands in scripts

Integration with Windows
------------------------

AGS has the ability to integrate with Windows in two ways. Firstly, it
can be set up to launch save games directly from explorer when the
player double-clicks them; and secondly, in Windows Vista and later, AGS
can integrate with the Game Explorer feature.

### Enhanced Save Games 

Optionally, AGS can set up Windows Explorer so that you can double-click
on a save game file to directly launch the game and continue from where
you left off.

**Setting it up**

In order to enable this, open the General Settings pane, and look for
the “Saved Games” section. Here, there is an option called “Enhanced
Save Games”. If you switch this on, then AGS will enable the integration
with Windows Explorer.

To make this work, you need to set the Save Game File Extension setting
to a file extension. This is how Windows will identify the save game
files, and you must supply an extension of between 5 and 20 characters
in length (“DemoQuestSave” would be an appropriate extension for Demo
Quest, for example).

By changing these settings, your game's saved game filenames will
change, and therefore you will lose access to any existing saved games.

**Extra features for Windows Vista and later**

If the player is running Windows Vista or later versions, then this
feature will also allow them to see the save game description and
screenshot (if enabled) in the Explorer preview window:

LTSSimg src=“images/GameExplorer3.jpg” GTSS ILBRK *Save games with
embedded screenshots on Vista and later versions*

**Enabling the integration**

Once you've built the game, the integration won't be enabled
immediately. If you want to use this feature, you'll need to distribute
your game in an installer rather than a zip file, because there's an
extra step you need to run after installation to set up the association.

In your installer, you need to run the game executable with the special
parameter `-registergame` When you do this, AGS will create the
necessary associations in Explorer to get the feature working. If it is
successful, it will not display any messages.

You can manually test this by creating a shortcut to your game EXE file,
and modifying it to add `-registergame` to the end of the command line.
Then, run the shorcut and the associations should be created for you.

For un-installing, run the game EXE again but with a `-unregistergame`
parameter. This will cause AGS to remove the associations from the
player's system.

**Cross-Platform Support**

Windows: ** Yes ILBRK MS-DOS: ** No ILBRK
Linux: ** No ILBRK MacOS: ** No ********

### Windows Game Explorer 

Windows Vista and later versions have a feature called the Game
Explorer, which is a special folder on the Start Menu that lists all the
games installed on the user's system and provides easy shortcuts to play
them.

AGS is now able to add your games to this list. However, in order to do
so you would need to distribute your game using an installer rather than
just in a plain zip file, since you need to tell AGS to add the game to
the list at install-time.

LTSSimg src=“images/GameExplorer1.jpg” GTSS ILBRK *The “Games”
option launches the Game Explorer*

**Enabling Game Explorer support**

Open the General Settings pane in the editor. If you scroll down to the
bottom of the list, you'll find a section titled “Windows Game
Explorer”. The main setting is called “Enable Game Explorer
integration”, and is disabled by default. Set this to True if you want
to be able to add your game to the Game Explorer (it will have no effect
on Windows XP and earlier versions).

**Game Explorer settings**

The rest of the settings here allow you to set up various fields that
the Game Explorer can display. **Developer Website must be
a URL starting with “http://” if you fill it in, and
**Version must be a four-point version number (eg.
1.0.0.0).****

The **Windows Experience Index is a score that Windows
gives each computer depending on its game-playing prowess. 1 is the
lowest score, and 5 is the highest at present. This field allows you to
specify the minimum score required to play your game (this will usually
be 1 for AGS games, unless you have high resolution and lots of
animation).**

**Save games**

If you set the *Save games folder name property in the
Saved Games section, then the Game Explorer will provide a right-click
option to go straight to the save game folder. This is only useful if
you also enable Enhanced Save Games.*

**Parental controls**

AGS is not currently able to support the Windows Parental Controls, due
to Windows requiring the game to be digitally signed for this to work.
Digital signatures require you to buy a certificate from an authority
such as Verisign, so at present they are not supported. Your game will
be classed as “Unrated” by Windows.

**Boxart image**

The Game Explorer can display a high-resolution alpha-blended image for
your game, rather than the standard game icon. To utilise this, place a
file called `GameExplorer.png` in your game folder, and rebuild the game
EXE. This must be a PNG image, no larger than 256 x 256 pixels:

LTSSimg src=“images/GameExplorer2.jpg” GTSS ILBRK *My game (“Chris
Kwest”) in the Game Explorer*

**Adding the game to the Game Explorer**

In order to actually add the game to the Game Explorer's list, you need
to run the game executable with the special parameter `-registergame`
When you do this, AGS will add the game to the Game Explorer and exit.
If it is successful, it will not display any messages.

Therefore, as part of your installer, once the game files are all
installed you should add a step at the end to run the game EXE file with
this parameter. It will do nothing on Windows XP and earlier versions.

For un-installing, run the game EXE again but with a `-unregistergame`
parameter. This will cause AGS to remove the game from the Game
Explorer's list.

**NOTE: If you have both Enhanced Save Games and Game
Explorer Integration enabled, then the `-registergame` and
`-unregistergame` commands will register/unregister both.**

**Cross-Platform Support**

Windows: ** Vista and later ILBRK MS-DOS: ** No
ILBRK Linux: ** No ILBRK MacOS: ** No
********

Source Control integration 
--------------------------

The AGS Editor supports integration with source control systems like
SourceSafe and Perforce.

**What is source control?**

Source Control allows you to easily keep copies of old versions of your
files, so that if you break something you can easily look back and see
what your script was like in previous versions.

AGS does not provide this functionality itself, but it is able to
integrate with Source Control applications such as SourceSafe and
Perforce in order to allow you to easily check things in and out.

**Which providers are supported?**

AGS supports any source control system that can integrate with Visual
Studio (this is called the MSCCI interface). Most source control systems
are quite heavyweight and designed for use by large teams, but there are
smaller systems like SourceSafe available which work well on a
standalone PC.

**How do I use it?**

If AGS detects an installed source control system, an extra option “Add
to source control” will appear on the File menu. Use this to add your
game to source control, and from then on whenever AGS attempts to edit a
file it will prompt you to check it out if necessary.

You can check in files by using the “Show Pending Checkins” option that
appears on the File menu once you've added your game to source control.

**Which files does AGS put under source control?**

AGS currently puts the main game file and your scripts, rooms, fonts and
translations under source control. Optionally, you can also add sound,
music and sprites by changing the setting in the General Settings pane.

Scripting
=========

The AGS scripting system allows you to write a mini-program, giving you
great control over your game.

Scripting tutorial part 1
-------------------------

The Scripting Tutorial is online here:

Scripting tutorial part 2
-------------------------

The Scripting Tutorial Part 2 is online here:

Pointers in AGS 
---------------

Various commands in the new scripting language will require you to use
pointers. This section has been split into three separate topics to
introduce you to pointers depending on your previous programming
experience – select one of the links below:

### Pointers for programming newbies 

Pointers can be quite a daunting prospect, and in languages like C and
C++ they certainly are; but AGS tries to make things as simple as
possible.

Basically, a pointer is a variable that *points to
something of a particular type. For example, a *Character
pointer would point to characters. What's the point of all this, I hear
you ask?**

Well, let's look back at AGS 2.62. If you wanted to reference a
particular hotspot, you'd need to remember its number. If you wanted to
switch on an object, you'd need to remember what number it was too. And
because you could accidentally use an object number where you wanted a
hotspot number, mistakes could easily happen and it all got rather
messy.

That's where pointers step in – basically, they allow you to do away
with identifying things by number, and in the process provide
*type checking, so you can't accidentally use a hotspot
where you meant to use an object.*

Let's look at an example. If you wanted to write a string to a file in
2.62, you'd do this:

    int handle = FileOpen("temp.txt", FILE_WRITE);
    FileWrite(handle, "Test!");
    FileClose(handle);

That's simple enough; but what if you wanted to open the file in one
place, and write to it somewhere else? You'd have to make
*handle a global variable, and then make sure you
remembered that it was a file handle and not a hotspot number or
anything else. Now, with 2.7 the same code would be:*

    File *file = File.Open("temp.txt", eFileWrite);
    file.WriteString("Test!");
    file.Close();

Looks fairly simple, doesn't it. The only slightly confusing part is
getting used to declaring the variable as `File*` rather than `int`; but
that's something you'll get used to quite quickly, and all the examples
in the manual should point you in the right direction.

Let's look at another example. Suppose you want a variable that contains
the current hotspot that the mouse is over. In 2.62, you might have
something like this:

    // top of global script
    int mouseOverHotspot;

    // repeatedly_execute
    mouseOverHotspot = GetHotspotAt(mouse.x, mouse.y);

How would you do this in 2.7? Well, quite simply:

    // top of global script
    Hotspot *mouseOverHotspot;

    // repeatedly_execute
    mouseOverHotspot = Hotspot.GetAtScreenXY(mouse.x, mouse.y);

But hold on, what if you want to know whether the mouse is over your
Door hotspot (say it's hotspot 2). In 2.62, you'd have done:

    if (mouseOverHotspot == 2) {
      Display("Mouse over the door");
    }

but that's rather messy, because what if you change the door's hotspot
number? You'd have to remember to go back and change all the 2's to 3,
or whatever. In 2.7, you now just do this (assuming you gave the hotspot
a script name of hDoor):

    if (mouseOverHotspot == hDoor) {
      Display("Mouse over the door");
    }

If you're a fan of numbers for some strange reason, you can still use
them like this:

    if (mouseOverHotspot == hotspot[2]) {
      Display("Mouse over the door");
    }

So, that concludes our introduction to pointers. Hopefully you've got an
understanding of what they are and what they do; if there's anything you
can't work out, feel free to ask on the Technical forums.

### Pointers for people who know Java or C`#` 

AGS pointers work in a very similar way to object variables in Java and
C`#`. The main difference is that AGS pointers are declared in the
C-style manner with an asterisk t represent the pointer. So:

    Hotspot *hs;

would declare a variable *hs which points to a Hotspot.
This would be equivalent to the following in Java or C`#`:*

    Hotspot hs;

In AGS, pointers are used to point to various built-in types, such as
Hotspots, Inventory Items, Characters and so on. Because AGS does not
have a *new keyword, you cannot create pointers to custom
struct types.*

You use pointers in the same way as you would in Java and C`#`. Various
built-in AGS static methods return a pointer to an instance (for
example, , , and so on). You can save this pointer into a pointer
variable, and then call its methods as you would in Java or C`#`. The
following examples are all valid:

    File *theFile = File.Open("test.dat", eFileWrite);
    if (theFile == null) Display("It's null!");
    File *file2 = theFile;
    if (theFile == file2) Display("They're the same file!");
    theFile = null;
    file2.WriteInt(10);
    file2.Close();

If you attempt to call a method on a null pointer, an error will occur
(just like you'd get an exception in Java or C`#`).

Pointer memory management in AGS is all automatic – the memory is freed
when there are no longer any variables pointing to the instance. Thus,
if you have global pointer variables in your global script, it's a good
idea to set them to *null when you're no longer using them,
to allow the memory to be freed.*

### Pointers for people who know C or C++ 

Pointers in AGS are based on the C/C++ syntax, so they are declared with
an asterisk. However, in AGS you can only create pointers to built-in
AGS types, and not to any custom structs declared in your script.

Pointer members are accessed with the dot operator, and not the `->`
C-style operator. Because AGS doesn't support features such as
pointers-to-pointers and so forth, there is no need for a separate
operator.

In AGS, pointer memory management is done automatically based on
reference counting (similar to the way COM works), so there is no
*new or *delete keyword. When an object is no
longer referenced by any pointer variables, it will be freed. For this
reason, if you have any global pointer variables it's advisable to set
them to *null if you are done with them.***

AGS pointers are strongly typed, and you cannot cast between types at
will like you can in C and C++. AGS will only allow you to compare and
assign pointers of the same type, or of the same base type. There is a
special keyword *null which all pointers can be set to and
compared with, which indicates that they are unassigned.*

Because there is no *new keyword, you cannot create object
instances; rather, they are returned by static member functions in AGS,
such as and . See the examples for the functions to get an idea of how
to use them.*

Calling global functions from local scripts
-------------------------------------------

You can now call your global script functions directly from your rooms.
This means that if you have a common script that you want to use in
response to various different events during the game, you can call it
from your room scripts rather than duplicating code.

To use a global function, open up the main script header
(GlobalScript.ash), and add a line similar to the following:

    import function my_function_name (parameters);

Where *my\_function\_name is the name of the global script
function, and *parameters is a list of the TYPES ONLY of
the parameters it takes. For example, if you had in your global
script:**

    function do_animation (int anim_number) {

then you would write:

    import function do_animation (int);

To use the function, you just call it normally in your script, eg:

    do_animation (3);

You can also return a value to the caller by using the “return”
statement, and the local script picks this up the same way it does with
built-in functions. For example, the end of your global script function
could be:

    return 51;

then the local script just does:

    int value = do_animation(3);

The script header
-----------------

This allows you to include the same information into all your scripts.
For example, if you have a global function you want all the room scripts
to use, you can add its import definition to the header file.

Do NOT place any actual functions or variables in this header, because
if you do you will need to re-compile ALL the scripts whenever you
modify the function. Instead, place your functions in your global script
and just place an import line in the header file to allow the other
scripts to access it.

String formatting 
-----------------

You will find many times in your game when you need to create a string
based on the values of variables, and functions like and allow you to do
so.

AGS uses printf-style argument formatting (used by the C language). This
means that you intersperse your text with special codes to insert a
variable's value. These special codes begin with a percent sign, and
then specify the variable type. The actual variables that you want to
display are then listed afterwards.

The special codes you can use are as follows:

|l|l|

Some examples:

    int life = 42;
    float twoPi = Maths.Pi * 2.0;
    String message = "A string variable";

    Display("A normal string with no variables.");
    Display("The meaning of life is %d.", life);
    Display("The meaning of life in 3 digits is %03d.", life);
    Display("2 times Pi is %f.", twoPi);
    Display("The message says: %s.", message);

would display:

    A normal string with no variables.
    The meaning of life is 42.
    The meaning of life in 3 digits is 042.
    2 times Pi is 6.283186.
    The message says: A string variable.

You can display as many variables as you like in one line:

    int life = 42;
    float twoPi = Maths.Pi * 2.0;

    Display("Life is %d, 2 x Pi = %f, and my dinner is %s.", life, twoPi, "awful");

but, **be very careful that you supply the right number of
variables to correspond with the tags you use in the text. If you don't
supply enough variables, your game could crash.**

Multiple Scripts 
----------------

If you're working on a fairly large game, you'll find that your global
script can quickly become rather large and unwieldy. AGS allows you to
create extra scripts (formerly known as Script Modules) in order to
split up your code and easily import scripts written by other people.

The main global script still has to contain all the event functions
(Look At Character scripts, Interact With Inventory scripts and so
forth) and all the GUI handlers (btnSave\_Click, etc).

But if you have any custom functions then you can put them in a separate
script in order to divide up your code. Scripts have the added advantage
that they can be easily exported and imported, if you want to share some
of your code with other people, or even just move it from one game to
another.

The scripts for the game can be seen under the “Scripts” node in the
project tree. Each script has its own header, which is where you place
the definitions for that script to allow the rest of your game to access
its functionality.

The order of the scripts is important. A script can only use
functionality from other scripts that come before it in the list, so the
Move Up and Move Down options allow you to adjust the order. The global
script is always at the bottom so that it can access all other scripts,
and room scripts are automatically provided with access to all the
scripts.

As an example, suppose you want to have a special
*AddNumbers function in a module. You'd create a new
script, then put this in its header file (.ASH):*

    import function AddNumbers(int a, int b);

Then, in the script file (.ASC) you could put:

    function AddNumbers(int a, int b) {
      return a + b;
    }

That's the basic principle behind using multiple scripts!

**Special functions**

Can extra scripts use special functions like `game_start` and
`repeatedly_execute`? Well, yes and no. They can contain the following
functions, and they will be called at the appropriate times just before
the global script's function is:

-   function game\_start()

-   function on\_event(EventType event, int data)

-   function on\_key\_press(eKeyCode keycode)

-   function on\_mouse\_click(MouseButton button)

-   function repeatedly\_execute()

-   function repeatedly\_execute\_always()

-   function late\_repeatedly\_execute\_always()

All other special functions, such as `dialog_request`, will only be
called in the Global Script, even if they exist in another script. If
you need other scripts to handle any of this functionality, you can
simply create a custom function in the script and then call it from the
global script.

The command is supported for on\_key\_press, on\_mouse\_click and
on\_event. Calling it prevents the rest of the scripts (including the
global script) from being called.

Understanding blocking scripts 
------------------------------

You will see some commands listed as “blocking”, where control does not
return to the script until the command finishes. But what does this
mean, exactly?

In order to better understand this, we need to explore a little about
the way that the AGS script engine works. In an AGS game, there are
three script **threads that can be running at once. Think
of a thread as a mini-CPU that executes your scripts.**

At the start of the game, the threads are all idle (not running any
scripts):

LTSSimg src=“images/threads1.gif” GTSS

Now, as and when your scripts need to be run, AGS will try to run them
on the appropriate thread (the Room thread for local scripts, and the
Global thread for global scripts).

So, on the first game loop, your global scripts' repeatedly\_execute
will be run:

LTSSimg src=“images/threads2.gif” GTSS

That's fine, and when it finishes running the thread becomes idle again.

But, suppose that within repeatedly\_execute, you make a call to the
Character.Say command. Say (or *DisplaySpeech in old-style
scripting) is a blocking command and does not return until the character
finishes talking:*

LTSSimg src=“images/threads3.gif” GTSS

The global thread is now **blocked, waiting for the
character to finish talking. This means that none of your global script
functions such as repeatedly\_execute, on\_event and on\_key\_press will
be run while the character is talking, since the thread is busy.**

Now, AGS does queue up to 5 script functions to be run on the thread as
soon as it is free; but if you have a lot of things happening within
your script, it's possible that you will lose some events such as
on\_events and keypresses if you script is blocked for a long time.

Let's explore the most common situation in which this causes confusion.
Suppose you have a *Player looks at inventory event on a
Key inventory item, which runs a script to display a message.*

Let's also suppose that you have some code at the end of your
on\_mouse\_click function to make the character stand still after
running mouse click events.

What you'll find is that the code at the end of on\_mouse\_click
actually gets called *before the inventory item's event.
Let's look at why:*

LTSSimg src=“images/threads4.gif” GTSS

Remember that AGS does not run events automatically; rather, the
on\_mouse\_click script function handles the mouse click and calls
ProcessClick to run the appropriate event. When it does so, it finds
that the key's Look At Item event has a script function associated with
it.

But oh no! Inventory item scripts are in the global script, and the
global thread is already blocked because of the mouse click. Therefore,
the inventory event script gets added to the thread's queue, and
on\_mouse\_click then finishes running. The inventory event script will
follow on afterwards.

Now you might think that this means that object and hotspot events can
run within on\_mouse\_click, since they use the room thread, like this:

LTSSimg src=“images/threads5.gif” GTSS

However, this is not the case. It is still the global thread that is
calling ProcessClick, so the room script will actually be run on the
global thread once it is free.

Finally, we come onto the No-Block thread. This thread is only used to
run the *repeatedly\_execute\_always and
*late\_repeatedly\_execute\_always functions. Because these
two are not allowed to run any blocking functions, this ensures that the
thread never gets blocked and so it will always run, even when the other
threads are busy:**

LTSSimg src=“images/threads6.gif” GTSS

I hope that helps explain blocking in terms of AGS scripting. If there's
anything that you don't think is clear, please suggest amendments on the
Technical forum.

Dynamic Arrays 
--------------

Suppose that you're writing a script that you want people to be able to
use in their games. You need to store the Health for every character in
the game, but you don't know how many characters there will be. What do
you do?

Dynamic Arrays are designed for just this purpose. You can declare an
array like this:

`int characterHealth[];`

in your script file. This special notation tells AGS that you don't yet
know how large you want the array to be. Now, before you use the array
(so probably in game\_start), you can do this:

`characterHealth = new int[Game.CharacterCount];`

If you forget to do this `new` command, you'll get a Null Pointer Error
if you try to access the array. You can change the size of an array by
simply using another `new` command with a different size; but this will
erase the contents of the array in the process.

Currently dynamic arrays are supported as global and local variables, or
members of normal (not managed) structs. Also, at present you can create
arrays of basic types (int, char, etc) and of built-in types (String,
Character, etc) but not of custom structs.

Extender functions 
------------------

Suppose that you wanted to add a new function, “Scream”, to characters
which would make them cry out “AARRRGGGHHH”. Because the Character type
is defined within AGS, it's not possible for you to just add a method to
it.

That's where Extender Functions come in. Here's an example:

    function Scream(this Character*)
    {
      this.Say("AAAAARRRRGGGGHHHHHH!!!!");
    }

This adds a new “Scream” function to the Character type, so that in your
script code elsewhere you can do things like:

    player.Scream();
    character[EGO].Scream();
    cJohn.Scream();

and so on.

**Where do I put this code?**

In the script header, you'd put:

`import function Scream(this Character*);`

and then put the main function in the script file. This will then allow
it to be used by other scripts.

**Static extenders**

Since AGS 3.4.0 you may also create static extender functions, that is
functions that are called from type, rather than an actual object.
Static extender declaration is a bit different, for example:

    int AbsInt(static Maths, int value)
    {
      if (value < 0)
        return -value;
      return value;
    }

You declare the function's import in the script header:

`import int AbsInt(static Maths, int value);`

and you use such function as:

    int x = Maths.AbsInt(-10);

Game variables 
--------------

The following variables are available to your script. They allow you to
do various tweaks to the engine at run-time.

Names in **bold are **read-only variables and
should NOT be modified by the script.****

All the following variables are `int` variables.

|l|l|

Predefined global script functions 
----------------------------------

In your main global script file, there are some functions which are
automatically added when you create the game. These are global events,
and the function is called when a particular event happens. There are
also some other events which you can add if you want to.

The available event functions are:

dialog\_request (int parameter)

:   Called when a dialog script line “run-script” is processed.
    PARAMETER is the value of the number following the “run-script” on
    that line of the dialog script.

game\_start ()

:   Called at the start of the game, before the first room is loaded.
    You can use this to set up the initial positions of characters, and
    to turn GUIs on and off. **You cannot run animations or do
    anything else which relies on a room being loaded.**

interface\_click (int interface, int button)

:   **(Now Obsolete) Called when the player clicks on a
    button on a GUI which has its action set as “Run script”. INTERFACE
    is the number of the GUI which they clicked on. BUTTON is the object
    number of the button within this GUI.**

on\_event (EventType event, int data)

:   Called whenever certain game events happen. The value of DATA
    depends on which event has occurred. This allows you to perform
    checks or update things every time the player does something,
    regardless of which room it is in. The possible values of event are:

        eEventEnterRoomBeforeFadein
              called just before room Player Enters Room event is run.
              DATA = new room number
        eEventLeaveRoom
              called just after room Player Leaves Room event is run.
              DATA = room number they are leaving
        eEventGotScore
              called whenever the player's score changes
              DATA = number of points they got
        eEventGUIMouseDown
              called when a mouse button is pressed down over a GUI
              DATA = GUI number
        eEventGUIMouseUp
              called when a mouse button is released over a GUI
              DATA = GUI number
        eEventAddInventory
              the player just got a new inventory item
              DATA = inventory item number that was added
        eEventLoseInventory
              the player just lost an inventory item
              DATA = inventory item number that was lost
        eEventRestoreGame
              tells your game that it has just been restored from a save game
              DATA = save slot number

on\_key\_press (eKeyCode keycode)

:   Called whenever a key is pressed on the keyboard. KEYCODE holds the
    ASCII value of the key. A list of these values is in .

on\_mouse\_click (MouseButton button)

:   Called when the player clicks a mouse button. BUTTON is either LEFT,
    RIGHT or MIDDLE, depending on which button was clicked. The
    “mouse.x” and “mouse.y” global variables contain the
    mouse's position. ILBRK If 'Handle inventory clicks in script' is
    enabled in the game options, this function can also be called with
    eMouseLeftInv, eMouseMiddleInv or eMouseRightInv, which indicate a
    left, middle or right click on an inventory item, respectively.
    ILBRK If 'Enable mouse wheel support' is enabled, this function can
    also be called with eMouseWheelNorth or eMouseWheelSouth, which
    indicate the user moving the mouse wheel north or
    south, respectively.

repeatedly\_execute()

:   Called every game cycle (normally 40 times per second). See for
    more information.

repeatedly\_execute\_always()

:   Called every game cycle, even when a blocking routine (eg.
    speech/cutscene) is in progress. You **cannot call any
    blocking functions from this event handler.
    **repeatedly\_execute\_always is called
    **BEFORE the game objects (characters, rooms, etc) get
    updated. See for more information.******

late\_repeatedly\_execute\_always()

:   Called every game cycle, even when a blocking routine (eg.
    speech/cutscene) is in progress. You **cannot call any
    blocking functions from this event handler.
    **late\_repeatedly\_execute\_always is called
    **AFTER the game objects (characters, rooms, etc) got
    updated, but before game is redrawn on screen.******

unhandled\_event (int what, int type)

:   Called when an event occurs, but no handler is set up in the Events
    list. This could be used to display a default “I can't do that” type
    of message. The values of WHAT and TYPE tell you what the
    player did. ILBRK The possible values are listed below:

            WHAT TYPE Description
             1    1   Look at hotspot
             1    2   Interact with hotspot
             1    3   Use inventory on hotspot
             1    4   Talk to hotspot
             1    7   Pick up hotspot
             1    8   Cursor Mode 8 on hotspot
             1    9   Cursor Mode 9 on hotspot
             2    0   Look at object
             2    1   Interact with object
             2    2   Talk to object
             2    3   Use inventory on object
             2    5   Pick up object
             2    6   Cursor Mode 8 on object
             2    7   Cursor Mode 9 on object
             3    0   Look at character
             3    1   Interact with character
             3    2   Speak to character
             3    3   Use inventory on character
             3    5   Pick up character
             3    6   Cursor Mode 8 on character
             3    7   Cursor Mode 9 on character
             4    1   Look at nothing (ie. no hotspot)
             4    2   Interact with nothing
             4    3   Use inventory with nothing
             4    4   Talk to nothing
             5    0   Look at inventory
             5    1   Interact with inventory (currently not possible)
             5    2   Speak to inventory
             5    3   Use an inventory item on another
             5    4   Other click on inventory

    Note that the “Character stands on hotspot” event does not trigger
    this function, and it will not be triggered if there is an “Any
    click” event defined.

    This function is **not triggered if the player clicks
    on nothing (hotspot 0).**

The *on\_key\_press and *on\_mouse\_click
events can also be handled by individual room scripts. If you add their
function definitions to your room script in a similar way to how they
are in the global script, the room script can intercept the
keypress/mouseclick first, and then decide whether to pass it on to the
global script or not. See the function for more.**

repeatedly\_execute (\_always) 
------------------------------

One of the most common things you'll need to do when scripting is to
check if something has happened in the game – and if so, then make the
game do something in response.

For example, suppose that you want a bird to fly backwards and forwards
across the screen in the background. You need a way of telling the bird
to move in one direction, recognise when it has finished, and tell it to
move back again.

This is where *repeatedly\_execute,
*repeatedly\_execute\_always and
*late\_repeatedly\_execute\_always come in.***

**What's the difference between them?**

The *repeatedly\_execute event is run on every game loop
(by default this is 40 times per second), but only when the game is not
blocked. That means that it will run as long as there are no current
blocking animations or moves going on (ie. a Walk or Animate command
where *eBlock has been specified as a parameter).**

On the other hand, *repeatedly\_execute\_always and
*late\_repeatedly\_execute\_always are always run on every
game loop, no matter whether the game is blocked or not. This comes at a
price though, which is that you cannot run any blocking code within it.
So if you try to script a *player.Walk() command that
passes the *eBlock parameter – or even just try to use a
`Wait(1);` command, these will fail within
*(late\_)repeatedly\_execute\_always.*****

The difference between *repeatedly\_execute\_always and
*late\_repeatedly\_execute\_always is that first is run
**before game updates itself, changing animation frames,
moving objects into new position etc, while the second, “late” version,
is run **after the game was updated, but before it redrew
its new state on screen.******

**What would I use each one for?**

You would usually use *repeatedly\_execute for doing things
that affect the player character, and
*repeatedly\_execute\_always for doing background tasks
that don't directly affect the player.**

For example, if your game kept track of the player's hunger, you might
want to check in *repeatedly\_execute how long it has been
since he last ate – and if it has been more than 20 minutes, make the
player character stop walking and rub his stomach. Because you want to
perform a blocking animation, and you wouldn't want this to interrupt
any specific cutscenes that were going on, repeatedly\_execute would be
the ideal place for it.*

On the other hand, in the case of our bird flying across the screen,
because we don't want to block the game while the bird flies, and we
just want it to happen in the background,
*repeatedly\_execute\_always would be the place to put it.*

The *late\_repeatedly\_execute\_always is used in similar
way to its “earlier” counterpart, but it may be essential if you need to
precisely keep track of a game object movement. When
*late\_repeatedly\_execute\_always is called all the
objects are already updated to their new states, therefore you will have
accurate information about them. On contrary, the
*repeatedly\_execute\_always will always be “one step
behind” of the game state.***

In a nutshell, if you need to do something right before game state
changes, use *repeatedly\_execute\_always, if you need to
do something right after game state has changed, use
*late\_repeatedly\_execute\_always.**

**How do I create them?**

In main game scripts, you create your *repeatedly\_execute
script function by just pasting it into the script as follows. In the
GlobalScript.asc it is already created for you:*

    function repeatedly_execute()
    {
      // Put your script code here
    }

In rooms, it is slightly different. If you want to run some script that
is specific to a particular room, open that room's Events Pane and
you'll see a “Repeatedly execute” event. Click the “...” button and a
function called something like *Room\_RepExec will be
created for you.*

This is important to remember – in a room script, **you cannot
simply paste in a repeatedly\_execute function; you need to use
the Events Pane to create it instead.**

To create *repeatedly\_execute\_always, you can simply
paste it into the script as above – but you can also paste it into room
scripts. Therefore the following will work in any script, whether it be
a room or a global script.*

    function repeatedly_execute_always()
    {
      // Put your script code here
    }

Remember, of course, that RepExec or
*repeatedly\_execute\_always functions in a room script
will only be run while the player is actually in that room!*

**Can you show me an example?**

Let's implement the two things we just talked about. Here's our hunger
checking code:

    function repeatedly_execute()
    {
      // increment our timer variable (we would have created this
      // in the Global Variables editor)
      hungerTimer++;

      if (hungerTimer == 800)
      {
        Display("You are getting very hungry.");
        player.LockView(RUBSTOMACH);
        player.Animate(0, 5, eOnce, eBlock, eForwards);
        player.UnlockView();
      }
    }

and let's put the bird flying code in the room script, because we only
want it to happen in that one room:

    function repeatedly_execute_always()
    {
      if (!cBird.Moving)
      {
        if (cBird.x < 100)
        {
          // if the bird is on the left hand side of the screen,
          // start it moving towards the right
          cBird.Walk(400, cBird.y, eNoBlock, eAnywhere);
        }
        else
        {
          // otherwise, move it towards the left
          cBird.Walk(0, cBird.y, eNoBlock, eAnywhere);
        }
      }
    }

Custom dialog options rendering 
-------------------------------

By default, AGS comes with two types of dialog options – displaying them
using the size and position of an existing GUI, or creating a text
window to display the options in.

As of AGS 3.1, if neither of these methods suit you (for example,
because you want to use picture-based dialog options, or you want to add
scroll arrows), you can now implement the dialog options display
yourself in the script.

**NOTE: This topic involves some advanced scripting. If
you're just starting out with AGS, please just use one of the built-in
dialog option styles for now, and come back to this later when you're
comfortable with scripting.**

To write your custom dialog options code, you need to do the following:

-   Add a `dialog_options_get_dimensions` function to your script (an
    example follows). This function is called by AGS to find out which
    part of the screen you will be drawing onto. By setting the width
    and height to values greater than 0, the custom dialog system
    is activated.

-   Add a `dialog_options_render` function, which is called by AGS when
    it needs to draw the dialog options. A standard script is supplied,
    which you can use to draw onto.

-   Optionally, add a `dialog_options_mouse_click` function. This is
    called by AGS if the player clicks the mouse anywhere on dialog
    options GUI. You might want to use this to process clicks on dialog
    options, and also on some custom scroll arrows, for example.

-   Optionally, add a `dialog_options_key_press` function. This is
    called by AGS if the player presses any key while custom dialog
    options are shown on screen. You can use this to implement
    key-controlled selection of dialog option, for example.

-   Optionally, add a `dialog_options_repexec` function. This works
    similarily to general `repeatedly_execute` function, but is called
    only if custom dialog options are shown on screen. You may use this
    to handle any other situations, such as determining which option the
    mouse is currently hovering over, or scripting time-related actions.

These functions don't have to go in the global script; you can put them
in any script you like. However, beware that if the functions are
present in more than one script they could interfere with each other and
cause problems.

**COMPATIBILITY NOTE: The older versions of AGS (pre-3.4.0)
supported slightly different set of functions. Thus, there was no
`dialog_options_repexec`, but you had to add `dialog_options_get_active`
function instead, in which you set active option property. Clicks on the
options were processed by AGS automatically, so doing this was
essential. If you have imported older project and want to keep old
dialog option scripts, then you should go to General Settings and enable
“Use old-style dialog options rendering API”.**

**IMPORTANT: When adding the functions to the script, they
all take in a parameter of type . The dialog\_options\_mouse\_click
function has an extra parameter for the mouse button, and
dialog\_options\_key\_press has an extra parameter for the key code. See
the example below.**

**IMPORTANT: All of the Custom Dialog functions run on the
non-blocking thread. That means that you should not make any blocking
calls, such as Character.Say, Wait or Display within them, as they may
not behave correctly.**

**Example A. Classic mouse controls**

    int dlg_opt_color = 14;
    int dlg_opt_acolor = 13;
    int dlg_opt_ncolor = 4;

    function dialog_options_get_dimensions(DialogOptionsRenderingInfo *info)
    {
      // Create a 200x200 dialog options area at (50,100)
      info.X = 50;
      info.Y = 100;
      info.Width = 200;
      info.Height = 200;
      // Enable alpha channel for the drawing surface
      info.HasAlphaChannel = true;
      // Put the text parser at the bottom (if enabled)
      info.ParserTextBoxX = 10;
      info.ParserTextBoxY = 160;
      info.ParserTextBoxWidth = 180;
    }

    function dialog_options_render(DialogOptionsRenderingInfo *info)
    {
      info.Surface.Clear(dlg_opt_color);
      int i = 1,  ypos = 0;
      // Render all the options that are enabled
      while (i <= info.DialogToRender.OptionCount)
      {
        if (info.DialogToRender.GetOptionState(i) == eOptionOn)
        {
          if (info.ActiveOptionID == i)
            info.Surface.DrawingColor = dlg_opt_acolor;
          else
            info.Surface.DrawingColor = dlg_opt_ncolor;
            
          info.Surface.DrawStringWrapped(5, ypos, info.Width - 10, 
                  eFontFont0, eAlignLeft, info.DialogToRender.GetOptionText(i));
          ypos += GetTextHeight(info.DialogToRender.GetOptionText(i), eFontFont0, info.Width - 10);
        }
        i++;
      }
    }

    function dialog_options_repexec(DialogOptionsRenderingInfo *info)
    {
      info.ActiveOptionID = 0;
      if (mouse.y < info.Y || mouse.y >= info.Y + info.Height ||
          mouse.x < info.X || mouse.x >= info.X + info.Width)
      {
        return; // return if the mouse is outside UI bounds
      }

      int i = 1, ypos = 0;
      // Find the option that corresponds to where the mouse cursor is
      while (i <= info.DialogToRender.OptionCount)
      {
        if (info.DialogToRender.GetOptionState(i) == eOptionOn)
        {
          ypos += GetTextHeight(info.DialogToRender.GetOptionText(i), eFontFont0, info.Width - 10);
          if ((mouse.y - info.Y) < ypos)
          {
            info.ActiveOptionID = i;
            return;
          }
        }
        i++;
      }
    }

    function dialog_options_mouse_click(DialogOptionsRenderingInfo *info, MouseButton button)
    {
      if (info.ActiveOptionID > 0)
        info.RunActiveOption();
    }

The examples above are slightly naive; in reality you would probably
want to track the Y position of each option in a variable to save having
to continually scan through all the options.

**Example B. Keyboard controls**

    int dlg_opt_color = 14;
    int dlg_opt_acolor = 13;
    int dlg_opt_ncolor = 4;

    function dialog_options_get_dimensions(DialogOptionsRenderingInfo *info)
    {
      // Create a 200x200 dialog options area at (50,100)
      info.X = 50;
      info.Y = 100;
      info.Width = 200;
      info.Height = 200;
      info.ActiveOptionID = 1; // set to first option
    }

    function dialog_options_render(DialogOptionsRenderingInfo *info)
    {
      info.Surface.Clear(dlg_opt_color);
      int i = 1,  ypos = 0;
      // Render all the options that are enabled
      while (i <= info.DialogToRender.OptionCount)
      {
        if (info.DialogToRender.GetOptionState(i) == eOptionOn)
        {
          if (info.ActiveOptionID == i)
            info.Surface.DrawingColor = dlg_opt_acolor;
          else
            info.Surface.DrawingColor = dlg_opt_ncolor;

          info.Surface.DrawStringWrapped(5, ypos, info.Width - 10, 
              eFontFont0, eAlignLeft, info.DialogToRender.GetOptionText(i));
          ypos += GetTextHeight(info.DialogToRender.GetOptionText(i), eFontFont0, info.Width - 10);
        }
        i++;
      }
    }

    function dialog_options_key_press(DialogOptionsRenderingInfo *info, eKeyCode keycode) 
    {
      if (keycode == eKeyUpArrow && info.ActiveOptionID > 1)
        info.ActiveOptionID = info.ActiveOptionID - 1;
      if (keycode == eKeyDownArrow && info.ActiveOptionID < info.DialogToRender.OptionCount)
        info.ActiveOptionID = info.ActiveOptionID + 1;
      if (keycode == eKeyReturn || keycode == eKeySpace)
        info.RunActiveOption();
    }

For more detail on the commands used here, see the page.

*Compatibility: Supported by **AGS 3.1.0 and
later versions.***

Built-in enumerated types 
-------------------------

AGS has several built in. These are used in calls to various commands,
and will usually pop up automatically in autocomplete. However, for
times where autocomplete doesn't do the job, having a manual reference
is invaluable:

    enum BlockingStyle {
      eBlock,
      eNoBlock
    };

*Used by: , , , , , , , ,*

    enum CharacterDirection {
      eDirectionDown = 0,
      eDirectionLeft,
      eDirectionRight,
      eDirectionUp,
      eDirectionDownRight,
      eDirectionUpRight,
      eDirectionDownLeft,
      eDirectionUpLeft,
      eDirectionNone = SCR_NO_VALUE
    };

*Used by: ,*

    enum Direction {
      eForwards,
      eBackwards
    };

*Used by: ,*

    enum WalkWhere {
      eAnywhere,
      eWalkableAreas
    };

*Used by: , ,*

    enum RepeatStyle {
      eOnce,
      eRepeat
    };

*Used by: , ,*

    enum Alignment {
      eAlignLeft,
      eAlignCentre,
      eAlignRight
    };

*Used by:*

    enum eFlipDirection {
      eFlipLeftToRight,
      eFlipUpsideDown,
      eFlipBoth
    };

*Used by:*

    enum TransitionStyle {
      eTransitionFade,
      eTransitionInstant,
      eTransitionDissolve,
      eTransitionBoxout,
      eTransitionCrossfade
    };

*Used by: ,*

    enum MouseButton {
      eMouseLeft,
      eMouseRight,
      eMouseMiddle,
      eMouseLeftInv,
      eMouseMiddleInv,
      eMouseRightInv,
      eMouseWheelNorth,
      eMouseWheelSouth
    };

*Used by: ILBRK *Passed into:
on\_mouse\_click**

    enum EventType {
      eEventLeaveRoom,
      eEventEnterRoom,
      eEventGotScore,
      eEventGUIMouseDown,
      eEventGUIMouseUp,
      eEventAddInventory,
      eEventLoseInventory,
      eEventRestoreGame
    };

*Passed into: on\_event*

    enum RoundDirection {
      eRoundDown,
      eRoundNearest,
      eRoundUp
    };

*Used by:*

    enum eSpeechStyle {
      eSpeechLucasarts,
      eSpeechSierra,
      eSpeechSierraWithBackground,
      eSpeechFullScreen
    };

*Used by:*

    enum SkipSpeechStyle {
      eSkipKeyMouseTime = 0,
      eSkipKeyTime      = 1,
      eSkipTime         = 2,
      eSkipKeyMouse     = 3,
      eSkipMouseTime    = 4,
      eSkipKey          = 5,
      eSkipMouse        = 6
    };

*Used by:*

    enum eVoiceMode {
      eSpeechTextOnly,
      eSpeechVoiceAndText,
      eSpeechVoiceOnly
    };

*Used by:*

    enum DialogOptionState {
      eOptionOff,
      eOptionOn,
      eOptionOffForever
    };

*Used by: ,*

    enum CutsceneSkipType {
      eSkipESCOnly,
      eSkipAnyKey,
      eSkipMouseClick,
      eSkipAnyKeyOrMouseClick,
      eSkipESCOrRightButton
    };

*Used by:*

    enum eOperatingSystem {
      eOSDOS,
      eOSWindows,
      eOSLinux,
      eOSMacOS,
      eOSAndroid,
      eOSiOS,
      eOSPSP
    };

*Used by:*

    enum eCDAudioFunction {
      eCDIsDriverPresent,
      eCDGetPlayingStatus,
      eCDPlayTrack,
      eCDPausePlayback,
      eCDResumePlayback,
      eCDGetNumTracks,
      eCDEject,
      eCDCloseTray,
      eCDGetCDDriveCount,
      eCDSelectActiveCDDrive
    };

*Used by:*

    enum CursorMode {
      eModeXXXX,
      eModeXXXX,
      ...
    };

The CursorMode enumeration is generated automatically based on your
mouse cursors. The cursor mode name is taken, all its spaces are
removed, and *eMode is added to the front. ILBRK
*Used by: , , , , , , , , , , , , , , ,**

    enum FontType {
      eFontXXXX,
      eFontXXXX,
      ...
    };

The FontType enumeration is generated automatically based on your fonts.
The font name is taken, all its spaces are removed, and
*eFont is added to the front. ILBRK *Used by:
, , , , , , , , , , , ,**

    enum LocationType {
      eLocationNothing,
      eLocationHotspot,
      eLocationCharacter,
      eLocationObject
    };

*Returned by:*

    enum FileMode {
      eFileRead,
      eFileWrite,
      eFileAppend
    };

*Used by:*

    enum FileSeek {
      eSeekBegin = 0,
      eSeekCurrent = 1,
      eSeekEnd = 2
    };

*Used by:*

    enum DialogOptionSayStyle {
      eSayUseOptionSetting,
      eSayAlways,
      eSayNever
    };

*Used by:*

    enum VideoSkipStyle {
      eVideoSkipNotAllowed,
      eVideoSkipEscKey,
      eVideoSkipAnyKey,
      eVideoSkipAnyKeyOrMouse
    };

*Used by:*

    enum AudioFileType {
      eAudioFileOGG,
      eAudioFileMP3,
      eAudioFileWAV,
      eAudioFileVOC,
      eAudioFileMIDI,
      eAudioFileMOD
    };

*Used by:*

    enum AudioPriority {
      eAudioPriorityVeryLow = 1,
      eAudioPriorityLow = 25,
      eAudioPriorityNormal = 50,
      eAudioPriorityHigh = 75,
      eAudioPriorityVeryHigh = 100
    };

*Used by: , ,*

Script language keywords
------------------------

### Arrays 

*data\_type *name `[` *size
`];`***

Arrays allow you to easily create several variables of the same type.
For example, suppose you wanted to store a health variable for all the
different characters in the game. One way would be to declare several
different variables like this:

    int egoHealth;
    int badGuyHealth;
    int swordsmanHealth;

but that quickly gets messy and difficult to keep up to date, since you
need to use different script code to update each one. So instead, you
can do this:

    int health[50];

This example declares 50 int variables, all called *health.
ILBRK You access each seperate variable via its **index
(the number in the brackets). Indexes start from 0, so in this case the
*health array can be accessed by indexes 0 to 49. If you
attempt to access an invalid index, your game will exit with an
error.****

Here's an example of using the array:

      health[3] = 50;
      health[4] = 100;
      health[player.ID] = 10;

this sets Health 3 to 50, Health 4 to 100, and the Health index that
corresponds to the player character's ID number to 10.

See Also:

### Data types 

|l|l|

You will normally only need to use the **int and
**String data types. The smaller types are only useful for
conserving memory if you are creating a very large number of
variables.****

To declare a variable, write the type followed by the variable name,
then a semicolon. For example:

`int my_variable;`

declares a new 32-bit integer called my\_variable

**WARNING: When using the *float data type,
you may find that the == and != operators don't seem to work properly.
For example:***

    float result = 2.0 * 3.0;
    if (result == 6.0) {
      Display("Result is 6!");
    }

may not always work. This is due to the nature of floating point
variables, and the solution is to code like this:

    float result = 2.0 * 3.0;
    if ((result > 5.99) && (result < 6.01)) {
      Display("Result is 6!");
    }

The way floating point numbers are stored means that 6 might actually be
stored as 6.000001 or 5.999999; this is a common gotcha to all
programming languages so just be aware of it if you use any floating
point arithmetic.

### Operators

The AGS scripting engine supports the following operators in
expressions. They are listed in order of precedence, with the most
tightly bound at the top of the list.

**WARNING: When using operators of equal precedence, AGS by
default evaluates them right-to-left. So, the expression
`a = 5 - 4 - 2;` evaluates as `a = 5 - (4 - 2);` which is not what you
might expect. Always use parenthesis to make it clear what you want.
ILBRK The “Left-to-right operator precedence” option on the General
Settings pane allows you to control this behaviour.**

****

    Operator  Description              Example

      !    NOT                        if (!a)
      *    Multiply                   a = b * c;
      /    Divide                     a = b / c;
      %    Remainder                  a = b % c;
      +    Add                        a = b + c;
      -    Subtract                   a = b - c;
      <<   Bitwise Left Shift         a = b << c;
           (advanced users only)
      >>   Bitwise Right Shift        a = b >> c;
           (advanced users only)
      &    Bitwise AND                a = b & c;
           (advanced users only)
      |    Bitwise OR                 a = b | c;
           (advanced users only)
      ^    Bitwise XOR                a = b ^ c;
           (advanced users only)
      ==   Is equal to                if (a == b)
      !=   Is not equal to            if (a != b)
      >    Is greater than            if (a > b)
      <    Is less than               if (a < b)
      >=   Is greater than or equal   if (a >= b)
      <=   Is less than or equal      if (a <= b)
      &&   Logical AND                if (a && b)
      ||   Logical OR                 if (a || b)

This order of precedence allows expressions such as the following to
evaluate as expected:

`if (!a && b < 4)`

which will execute the 'if' block if **a is 0 and
**b is less than 4.****

However, it is always good practice to use parenthesis to group
expressions. It's much more readable to script the above expression like
this:

`if ((!a) && (b < 4))`

### Constants 

The following predefined macros are available in your scripts:

|l|l|

You can check for whether a macro is defined or not by using the
`#ifdef` and `#ifndef` keywords:

    #ifndef STRICT
      // only compile the MoveCharacter command if not using object-based scripting
      MoveCharacter(EGO, 30, 40);
    #endif
    #ifdef DEBUG
      // only display this when the game is compiled in debug mode
      Display("Debugging information");
    #endif

There is also an `#error` directive you can use to stop the script
compiling:

    #ifndef AGS_NEW_STRINGS
    #error This script requires at least AGS 2.71
    #endif

The other constants (AGS\_MAX\_\*) are useful if you are writing some
script code that you want to be portable to different versions of AGS,
and to pick up the limits from the user's AGS version. For example, if
you wanted to store some extra information on all the inventory items,
you could do:

    int invWeights[AGS_MAX_INV_ITEMS];

To get the actual number of things in the game rather than the AGS
limit, use the -style properties.

### Version checking 

If you are writing a script module, you may need to check which version
of AGS the user of your module is using.

For this purpose there are two directives:

    #ifver 2.72
    // do stuff for 2.72 and above
    #endif
    #ifnver 2.72
    // do stuff for 2.71 and below
    #endif

Note that this ability was only added in 2.72, so you cannot use the
`#ifver` checks if you want your module to work with earlier versions
than this.

### if, else statements 

**if ( *expression **) `{` ILBRK
*statements1 ILBRK `}` ILBRK \[ **else `{`
ILBRK *statements2 ILBRK `}` \]*********

If *expression is true, then *statements1 are
run.**

If *expression is not true, and there is an
**else clause present, then *statements2 are
run instead.****

For example:

    if (GetGlobalInt(5) == 10) {
      Display("Globalint 5 is 10.");
    }
    else {
      Display("Globalint 5 is not 10.");
    }

In this example, the first message will be displayed if the return value
from `GetGlobalInt(5)` is 10, and the second message will be displayed
if it is not.

**if statements can be nested inside **else
statements to produce an “else if” effect. For example:****

    if (GetGlobalInt(5) == 1) {
      Display("Globalint 5 is 1.");
    }
    else if (GetGlobalInt(5) == 2) {
      Display("Globalint 5 is 2.");
    }
    else {
      Display("Globalint 5 is not 1 or 2.");
    }

### switch, case statements 

**switch ( *expression **) `{`
ILBRK \[ **case *expression: ILBRK
*statements ILBRK \[ **break; \] \] ILBRK \[
**default: ILBRK *statements ILBRK \[
**break; \] \] ILBRK `}`****************

Calculates first *expression in the **switch
header, then finds a **case statement which *constant
expression matches the *result of the previous
calculation, and begins executing statements under that
**case. When doing so, it ignores any other
**case statements, but runs all the statements under them.
Stops only when reaching the switch's end, or **break
statement. If the result of *expression is not found in any
of the **case lines, then goes to **default
line and runs statements from that point. If no **default
statement found in the switch, then the whole switch is skipped.
**Switch may have any number of **case
statements and only one **default statement, but they may
be arranged in any order.**************************

Unlike many programming languages, AGS allows expression result of any
type (integer, boolean, string, pointers).

**KNOWN ISSUES:**

-   Since the final release of AGS 3.4.0 usage of strings in the switch
    is broken: instead of comparing by value, as intended, they are
    instead compared as pointers.

-   Local function variables do not work when being used in the
    “case” expression.

We expect above to be fixed in the future updates.

Example:

    switch (player)
    {
    case cEgo: Display("Hello, my name is Ego, default player controlled character."); break;
    case cJohn: Display("Greetings, I am John, the male character."); break;
    case cMary: Display("Hi there, I am Mary, the female character."); break;
    default:
      Display("I am not really sure what character the player is controlling, this might be a bug");
      break;
    }

Example with “fall-through” cases:

    switch (player)
    {
    case cJohn:
    case cMary:
      player.Say("I like oranges.")
      break;
    case cEgo:
      player.Say("I like apples.");
    default:
      player.Say("I would like some berries.");
    }

In the above example both cJohn and cMary cases lead to “I like oranges”
line. cEgo sais “I like apples” and then also “I would like some
berries”. If there were any other player controlled character, not
mentioned in this switch, they would go straight to default line.

### while 

**while ( *expression **) `{`
ILBRK *statements ILBRK `}`******

Runs *statements continuously, while
*expression is true.**

For example:

    while (cEgo.Moving) {
      Wait(1);
    }

will run the script `Wait(1);` repeatedly, as long as `cEgo.Moving` is
not zero. Once it is zero, the **while statement will exit
at the end of the loop.**

### do..while 

**do `{` ILBRK *statements ILBRK `}`
**while ( *expression
**);********

Similarily to runs *statements continuously, so long as
*expression is true, but unlike **while it
checks the expression AFTER executing statements, not before. This also
means that the statements will be executed at least once.****

For example:

    do
    {
      cEgo.Move(cEgo.x + 1, cEgo.y);
    }
    while (IsKeyPressed(eKeyRightArrow));

will run the script `cEgo.Move(cEgo.x + 1, cEgo.y);` once, and then
continue run it repeatedly, as long as the right arrow key is pressed by
player.

### for 

**for ( \[*initialization\]**;
\[*expression\]**; \[*iteration\]
**) `{` ILBRK *statements ILBRK
`}`************

This loop command first performs *initialization
statements, then runs *statements inside curved brackets
continuously. Each time before executing these statements it checks
whether *expression is true, and if not - ends the loop.
Each time after statements were executed it additionally runs
*iteration statements.****

*Initialization is commonly used to declare variables or
setting up existing variable values. If a new variable is declared in
*initialization - such variable will exist and may be used
only inside the loop. *Iteration step is usually meant to
“move” to the next step, by changing some variable value. Every part of
the command header - *initialization,
*expression and *iteration - is optional:
there may be **for command without initialization, or
without iteration, or even without conditional expression (in which case
loop should be ended with either or statement).********

For example:

    for (int i = 0; i < Game.CharacterCount; i++)
    {
      Display("My name is %s", character[i].Name);
    }

will look over every character in game and display their names.

Another example (note missing initialization and iteration):

    for (; cEgo.x < 100;)
    {
      Wait(1);
    }

This will repeat `Wait(1);` until cEgo character does not move beyond
coordinate x = 100.

### break 

**break;**

`break` statement ends the execution of most inner loop or immediately.
After this script continues running from the next line after loop or
switch.

For example:

    while (cEgo.Moving) {
      if (IsKeyPressed(eKeyEscape))
        break;

      Wait(1);
    }

will run the script `Wait(1);` repeatedly, as long as `cEgo.Moving` is
not zero. If player presses Escape key, the loop is terminated
immediately.

### continue 

**continue;**

`continue` statement makes the loop skip remaining statements in current
iteration and proceed to the next end-condition check, followed by the
loop restart, if condition is still met, or loop end. If in kind of
loop, the *iteration statement is executed right before
that.*

For example:

    for (int i = 0; i < 100; i++)
    {
      // multiple statements here
      
      if (i > 50)
        continue;
      
      // more statements following
    }

will run first part of the loop statements always, and second part only
when `i <= 50`.

### function

**function *name `(` \[*type1
param1, *type2 param2, ... \] `)`*****

Declares a custom function in your script. A function is a way in which
you can separate out commonly used code into its own place, and thus
avoid duplicating code.

For example, suppose that you quite often want to play a sound and add
an inventory item at the same time. You could write both commands each
time, or you could define a custom function:

    function AddInvAndPlaySound(InventoryItem* item) {
      player.AddInventory(item);
      aInventorySound.Play();
    }

then, elsewhere in your code you can simply call:

    AddInvAndPlaySound(iKey);

to add inventory item *iKey and play the sound.*

Generally, you place your functions in your global script. You then need
to add an line to your script header to allow the function to be called
from room scripts.

**Optional parameters**

You can make *int parameters optional if there is a default
value that the user doesn't need to supply. To do this, change the
script header *import declaration like this:**

    import function TestFunction(int stuff, int things = 5);

that declares a function with a mandatory *stuff parameter,
and an optional *things parameter. If the caller does not
supply the second parameter, it will default to 5.**

**NOTE: To use optional parameters, you need to have an
“import” declaration for the function in the script header. The default
values cannot be specified in the actual function declaration itself.**

### return 

**return;**

Immediately quits currently run function and returns to the previous
script function current one was called from, if there was any, otherwise
passes execution to engine. **return can be put in any
place in the the function, no matter if it is inside the if/else
statement group, loop or switch - it will still work as immediate
function exit.**

If the function is declared with return type other than
**void (or simply like `function`), then the
**return statement **has to specify
**return value.********

    int GetHowManyTradeGoodsShopkeeperHas() {
      return 2;
    }

Alternatively, when function is not supposed to have any return value,
sometimes you may want to break out of current function before it ends
naturally:

    function DoThisAndOptionallyThat(bool do_all) {
      // multiple statements here
      
      if (!do_all)
        return; // quit the function prematurely
        
      // more statements following
    }

### struct

**struct *name `{`***

Declares a custom struct type in your script. ILBRK Structs allow you to
group together related variables in order to make your script more
structured and readable. For example, suppose that wanted to store some
information on weapons that the player could carry. You could declare
the variables like this:

    int swordDamage;
    int swordPrice;
    String swordName;

but that quickly gets out of hand and leaves you with tons of variables
to keep track of. This is where structs come in:

    struct Weapon {
      int damage;
      int price;
      String name;
    };

Now, you can declare a struct in one go, like so:

    Weapon sword;
    sword.damage = 10;
    sword.price = 50;
    sword.name = "Fine sword";

Much neater and better organised. You can also combine structs with :

    // at top of script
    Weapon weapons[10];
    // inside script function
    weapons[0].damage = 10;
    weapons[0].price = 50;
    weapons[0].name = "Fine sword";
    weapons[1].damage = 20;
    weapons[1].price = 80;
    weapons[1].name = "Poison dagger";

structs are essential if you have complex data that you need to store in
your scripts.

### managed (struct) 

**managed struct *name `{`***

**Managed is a modifier that can be applied to
**struct declaration to make them managed structs.****

Managed structs are special in the way that objects of their types are
created in dynamic pool as opposed to global variables, that exist from
the game start to when the game is shut down, and local variables, that
exist only when their function is run. You cannot declare a variable of
managed struct, but only a pointer variable.

The advantage of such managed (or dynamic) objects is that they are
created only when needed and disposed of when no longer needed. Also,
since you work with pointer to object instead of object itself, you may
assign them to another variable without copying object itself, pass them
to function as parameter, or return from the function.

**IMPORTANT: there is a big limitation for user-defined
managed structs now, it is that they themselves cannot have members of
pointer types (or dynamic arrays).**

Example:

    managed struct Apple {
      int color;
      int freshness;
    };

This declares managed struct. To declare a pointer to such struct you
do:

    Apple* my_apple;

This creates a pointer variable `my_apple` of managed type `Apple`.

However, this does **not create an object itself yet, and
`my_apple` is assigned **null value now. If you try to
access struct members using `my_apple` now, you will get errors. To
create an actual object you need to use a keyword:****

    my_apple = new Apple;

The object is now created in the dynamic memory pool, and variable
`my_apple` **points to it. This lets us access object
contents:**

    my_apple.color = Game.GetColorFromRGB(255, 0, 0);
    my_apple.freshness = 100;

You may copy pointer to another variable of same type:

    Apple* apple2 = my_apple;

This does **not copy object itself, only its address in
dynamic pool, meaning both variables - `my_apple` and `appl2` - point to
same object!**

You may write a function that take such pointer as parameter:

    function DisplayAppleDescription(Apple* apple) {
      String s = String.Format("Apple has color %d and freshness %d", apple.color, apple.freshness);
      Display(s);
    }

and then call it like:

    DisplayAppleDescription(my_apple);

You may write a function that returns pointer to apple:

    Apple* CreateYellowApple(int fresh) {
      Apple* apple = new Apple;
      apple.color = Game.GetColorFromRGB(255, 0, 255);
      apple.freshness = fresh;
      return apple;
    }

and then use such function just like:

    Apple *my_apple = CreateYellowApple(50);

**When does the dynamic object gets destroyed? After you
created dynamic object as described above, it will exist in memory as
long as *there is at least one pointer variable pointing to
it. As soon as the last pointer gets destroyed itself (for
example, if it was local function variable, and function ended), or is
assigned another object, or simply assigned `null`, then the dynamic
object is removed from your game forever.***

See Also: ,

### new 

*pointer\_variable = **new
*managed\_type;****

Creates a new dynamic (managed) object of *managed\_type
and assigns it to *pointer\_variable.**

Example:

    // Here we declare a managed struct for Apple
    managed struct Apple {
      int color;
      int freshness;
    };

    // ...and declare a global pointer to Apple
    Apple* SomeApple;

    // At the game start we create a new dynamic object of Apple type
    // and assign its address to the pointer variable
    function game_start()
    {
      SomeApple = new Apple;
    }

See Also: ,

### enum

**Recommended for advanced users only**

**enum *name `{` ILBRK *option1
\[ = *value1 \], ILBRK *option2 \[ =
*value2 \], ILBRK ... ILBRK `};`*******

Declares an enumeration type. An enumeration allows you to group
together a set of related options, where only one will be true at any
one time – a bit like the contents of a list box.

For example, if you have a script function, *doStuff, that
can perform 3 different operations, you could do this:*

    function doStuff(int param) {
      if (param == 1) {
        // do something
      }
      else if (param == 2) {
        // do something else
      }
      // etc
    }

but it's hard to read, and when calling the function from elsewhere in
your script, it's not clear what 1 or 2 means. That's where enums come
in:

    enum DoStuffOption {
      BakeCake,
      DoLaundry
    };

    function doStuff(DoStuffOption param) {
      if (param == BakeCake) {
        // do something
      }
      else if (param == DoLaundry) {
        // do something else
      }
      // etc
    }

and then the calling code looks like: ILBRK `doStuff(BakeCake);` ILBRK
thus making it perfectly clear what the command will do.

Normally, you would put the enum definition into the script header.

In summary, enums are not an essential part of scripting and you can get
away perfectly well without using them, but in some specific situations
they're very handy.

### this

There are two uses for the `this` keyword.

**1. Accessing members of the current struct**

When you are creating custom , you use the “this” keyword inside member
functions to refer to the current struct. For example:

Suppose you had this in your script header:

    struct MyStruct {
      int myValue;

      import function MyMethod();
    };

Then, in your main script, you could put this:

    function MyStruct::MyMethod()
    {
      this.myValue = 5;
    }

The `MyStruct::MyMethod` tells AGS that you are defining the function
*MyMethod which belongs to the struct
*MyStruct (the `::` operator means “belongs to”).**

The code above will mean that when the MyMethod function is called, it
sets the `myValue` variable to 5.

**2. Declaring extender functions**

Please see the page for details.

### import 

**import *declaration ;***

Declares *declaration as a variable or function which is
external to the current script, but that the script needs access to it.
You use this to provide your room scripts with access to parts of your
global script.*

For example:

    import int counter;
    import function add_numbers (int, int);

This imports an integer variable `counter` and the function
`add_numbers` from the global script to enable the current script to
call them. You normally place import statements into the script header
so that all rooms can benefit from them.

In order to import the variable, it must have been exported from the
global script with the .

**NOTE: You **MUST import external variables
with the correct type. If `counter` was declared as a
**short in the global script, you MUST import it as a
short, otherwise your game may crash.******

**NOTE: You cannot import old-style `string` variables
(this does not apply to new-style `String` variables).**

### export 

**export *variable \[, *variable
... \] ;****

Declares that *variable can be exported and accessed by
other scripts. You must place this at the **end of your
global script. You can export many variables with one export line.***

For example:

    export my_variable;
    export counter, strength;

This exports three variables - my\_variable, counter and strength.

### noloopcheck

function **noloopcheck *function\_name (
*parameters ... ) `{`****

The noloopcheck keyword disables the script loop checking for the
current function.

Normally, if a loop runs for more than 150,000 loops, AGS will assume
that the script has hung and abort the game. This is to assist scripting
since otherwise the game would lock up if you scripted a loop wrongly.

However, there are some rare situations in which you need a loop to run
several thousand times (for example, when initialising a very large
array). In this case, the *noloopcheck keyword can be used
to stop AGS aborting your script.*

**NOTE: The *noloopcheck keyword must be
placed between “function” and the function's name. ILBRK If you import
the function into the script header, you **do not include
the “noloopcheck” keyword in the import declaration – it is only
included in the actual function body.*****

**NOTE: If AGS gives you a script iterations error,
**DO NOT just automatically add this keyword as a way to
fix the problem – more often than not, it is a fault in your scripting
and using this keyword will mean that the game will hang rather than
abort.****

For example:

    function noloopcheck initialize_array() {
      char bigarray[200000];
      int a = 0;
      while (a < 200000) {
        bigarray[a] = 1;
        a++;
      }
    }

without the “noloopcheck” keyword here, AGS would abort that script.

AudioChannel functions and properties 
-------------------------------------

The AudioChannel instance represents a currently playing audio file. You
can use this instance to check the status of playing sounds, and adjust
them.

### Seek (audio channel) 

*(Formerly known as SeekMIDIPosition, which is now
obsolete) ILBRK *(Formerly known as SeekMODPattern, which
is now obsolete) ILBRK *(Formerly known as
SeekMP3PosMillis, which is now obsolete)***

    AudioChannel.Seek(int position)

Seeks the audio clip that is currently playing on this channel to
*position.*

What *position represents depends on the FileType of the
audio clip:*

-   **MIDI - the beat number**

-   **MOD/XM/S3M - the pattern number**

-   **WAV/VOC - the sample number (eg. in a 22050 Hz sound,
    22050 = 1 second)**

-   **OGG/MP3 - milliseconds offset**

<!-- -->

    AudioChannel *channel = aExplosion.Play();
    Wait(40);
    channel.Seek(0);

will start playing the *aExplosion audio clip, wait for a
second, then seek it back to the start.*

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also:*

### SetRoomLocation 

*(Formerly part of PlayAmbientSound, which is now
obsolete)*

    AudioChannel.SetRoomLocation(int x, int y)

Sets the currently playing audio to be a directional sound, eminating
from (x,y).

The volume of the channel will be dynamically adjusted depending on how
close the player character is to the co-ordinates. Therefore, as the
player walks closer the volume will increase, and as they walk away the
volume will decrease.

The channel's Volume setting sets the maximum possible volume when the
player is standing on the specified co-ordinates.

Pass the co-ordinates as (0,0) to remove the directional effect and
return this channel to playing at its normal volume.

    AudioChannel *channel = aMachine.Play();
    channel.SetRoomLocation(oMachine.X, oMachine.Y);

will start playing the *aMachine audio clip, and set it at
the location of the *oMachine room object.**

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also:*

### Speed property (audio channel) 

    int AudioChannel.Speed

Gets/sets the playing audio clip's playback speed. The value is defined
in clip's milliseconds per second: 1000 is default, meaning 1000 of
clip's ms in 1 real second (scale 1:1). Set &lt; 1000 for slower play
and &gt; 1000 for faster play. **NOTE: currently works for
MP3 and OGG audio clips only.**

    AudioChannel *channel = aFunnyTalk.Play();
    channel.Speed = 2000;

plays *aFunnyTalk clip at the double speed.*

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

### Stop (audio channel) 

*(Formerly known as StopAmbientSound, which is now
obsolete) ILBRK *(Formerly known as StopChannel, which is
now obsolete)**

    AudioChannel.Stop()

Stops the sound that is currently playing on this audio channel.

    AudioChannel *channel = aExplosion.Play();
    Wait(40);
    channel.Stop();

will start playing the *aExplosion audio clip, wait for a
second, then stop it.*

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also:*

### ID property (audio channel) 

    readonly int AudioChannel.ID

Gets the Channel ID of this audio channel. You will not normally need to
use this, but it can be used for inter-operating with legacy commands
such as StopChannel.

    AudioChannel *channel = aExplosion.Play();
    Display("Explosion playing on channel %d", channel.ID);

will start playing the *aExplosion audio clip, and display
which channel it is playing on.*

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

### IsPlaying property 

*(Formerly known as IsChannelPlaying, which is now
obsolete)*

    readonly bool AudioChannel.IsPlaying

Gets whether this audio channel is currently playing a sound. Returns
*true if it is, or *false if it is not.**

    AudioChannel *channel = aExplosion.Play();
    while (channel.IsPlaying) Wait(1);
    Display("Finished playing the explosion");

will start playing the *aExplosion audio clip, and wait
until it finishes.*

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also:*

### LengthMs property 

    readonly int AudioChannel.LengthMs

Gets the length of the audio playing on this channel, in milliseconds.

This is supported by all file types, but with MIDI music it is only
accurate to the nearest second.

If this channel is not currently playing any audio, returns 0.

    AudioChannel *channel = aExplosion.Play();
    Display("The Explosion sound is %d ms long.", channel.LengthMs);

will start playing the *aExplosion audio clip, then display
its length.*

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also:*

### Panning property 

    int AudioChannel.Panning

Gets/sets the panning of this audio channel.

Panning allows you to adjust the stereo balance of the audio. The
default is 0, which is centred and will play at the same volume on both
speakers. However you can adjust this between -100 (fully left) to 100
(fully right) to adjust the balance between the speakers.

**NOTE: MIDI music files do not support panning.**

    AudioChannel *channel = aExplosion.Play();
    channel.Panning = -100;

will start playing the *aExplosion audio clip on the left
speaker only.*

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also:*

### PlayingClip property 

*(Formerly known as GetCurrentMusic, which is now
obsolete)*

    readonly AudioClip* AudioChannel.PlayingClip

Gets the audio clip that is playing on this channel. This allows you to
find out the type of the clip, and other information.

Returns *null if there is no sound currently playing on
this channel.*

    AudioChannel *channel = System.AudioChannels[2];
    if (channel.PlayingClip == null)
    {
      Display("Nothing is playing on channel 2");
    }
    else
    {
      Display("Channel 2 is playing a clip of type %d", channel.PlayingClip.Type);
    }

will display what is currently playing on audio channel 2.

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also: ,*

### Position property (audio channel) 

*(Formerly known as GetMIDIPosition, which is now obsolete)
ILBRK *(Formerly known as GetMODPattern, which is now
obsolete) ILBRK *(Formerly known as GetMP3PosMillis, which
is now obsolete)***

    readonly int AudioChannel.Position

Gets the current position of the audio playing on this channel.

What *position represents depends on the FileType of the
audio clip:*

-   **MIDI - the beat number**

-   **MOD/XM/S3M - the pattern number**

-   **WAV/VOC - the sample number (eg. in a 22050 Hz sound,
    22050 = 1 second)**

-   **OGG/MP3 - milliseconds offset**

This property is read-only. If you want to change the current playback
position within the audio file, use the function.

    AudioChannel *channel = aExplosion.Play();
    Wait(40);
    channel.Seek(channel.Position + 1000);

will start playing the *aExplosion audio clip, wait for a
second, then seek it ahead one second (if it is OGG/MP3/WAV).*

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also: ,*

### PositionMs property 

    readonly int AudioChannel.PositionMs

Gets the current position of the audio playing on this channel, in
milliseconds.

This is supported by all file types except MIDI, and returns the current
offset into the sound in milliseconds. MIDI files will always return 0.

This property is read-only. If you want to change the current playback
position within the audio file, use the function.

    AudioChannel *channel = aExplosion.Play();
    Wait(40);
    Display("After 1 second, offset is %d ms.", channel.PositionMs);

will start playing the *aExplosion audio clip, wait for a
second, then display its position.*

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also: *See Also: ,**

### Volume property (audio channel) 

*(Formerly known as SetChannelVolume, which is now
obsolete) ILBRK *(Formerly known as SetMusicVolume, which
is now obsolete)**

    int AudioChannel.Volume

Gets/sets the volume of this audio channel, from 0 to 100. This allows
you to dynamically adjust the volume of a playing sound.

This command adjusts the volume of this channel relative to the other
channels. It is still constrained within the overall volume, set by the
System.Volume property.

**NOTE: This command only affects the current sound being
played on the channel. When a new audio clip starts playing on this
channel, the volume will be set to the DefaultVolume of the new audio
clip.**

**NOTE: The volume returned by this property is the
channel's base volume, ie. it does not include the effects of any
directional audio set with SetRoomLocation, or any temporary volume drop
while speech is playing.**

    AudioChannel *channel = aExplosion.Play();
    Wait(40);
    channel.Volume = 20;

will start playing the *aExplosion audio clip, wait for a
second, then reduce its volume.*

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also: , ,*

AudioClip functions and properties 
----------------------------------

AudioClips are created when you import files in the AGS Editor. The
commands in this section allow to play them.

### Play 

*(Formerly known as PlayAmbientSound, which is now
obsolete) ILBRK *(Formerly known as PlayMP3File, which is
now obsolete) ILBRK *(Formerly known as PlayMusic, which is
now obsolete) ILBRK *(Formerly known as PlaySound, which is
now obsolete) ILBRK *(Formerly known as PlaySoundEx, which
is now obsolete) ILBRK *(Formerly known as SetMusicRepeat,
which is now obsolete)******

    AudioChannel* AudioClip.Play(optional AudioPriority, optional RepeatStyle)

Plays the audio clip.

Optionally you can supply a priority and Repeat setting; if you do not
supply these, the defaults set for the audio clip in the editor will be
used.

This command searches through all the available audio channels to find
one that is available for this type of audio. If no spare channels are
found, it will try to find one that is playing a clip with a lower or
equal priority, and interrupt it to replace it with this new sound.

If all audio channels are busy playing higher priority sounds, then this
new audio clip will not be played.

This command returns the AudioChannel instance that the new sound is
playing on, or *null if it did not play for any reason.*

**NOTE: AGS can only play one MIDI file at a time.**

    aExplosion.Play();

plays the *aExplosion audio clip.*

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also: , ,*

### PlayFrom 

    AudioChannel* AudioClip.PlayFrom(int position, optional AudioPriority,
                                     optional RepeatStyle)

Plays the audio clip, starting from *position. For the
meaning of the position, see the help page.*

Otherwise, this command behaves identially to . Please see that help
page for more information.

    aExplosion.PlayFrom(1000);

plays the *aExplosion audio clip, starting from a 1 second
offset (if it is OGG/MP3).*

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also:*

### PlayQueued 

*(Formerly known as PlayMusicQueued, which is now
obsolete)*

    AudioChannel* AudioClip.PlayQueued(optional AudioPriority, optional RepeatStyle)

Plays the audio clip, or queues it to be played later if it cannot be
played now.

This command behaves identially to , except that if there are no
available audio channels, it will queue this audio clip to be played
when a channel becomes available.

Additionally, unlike the Play command, using PlayQueued will not
interrupt an existing audio clip with an equal priority; it will only
interrupt clips with a lower priority.

You can queue up to 10 tracks in the audio queue. Note that if you queue
audio clips to be played after a repeating audio clip, they will never
be played.

    aExplosion.Play();
    aAftermath.PlayQueued();

plays the *aExplosion audio clip, and queues the
*aAftermath sound to be played afterwards.**

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also:*

### Stop (audio clip) 

    AudioClip.Stop()

Stops all currently playing instances of this audio clip.

    aExplosion.Play();
    Wait(40);
    aExplosion.Stop();

plays the *aExplosion audio clip, waits 1 second and then
stops it again.*

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also:*

### FileType property (audio clip) 

    readonly AudioFileType AudioClip.FileType;

Gets the file type of this audio clip. This is useful in conjunction
with the PlayFrom and Seek commands to determine what the position
offset represents.

    if (aExplosion.FileType == eAudioFileMIDI)
    {
      Display("Explosion is a MIDI file!");
    }

displays a message if aExplosion is a MIDI file

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also: , ,*

### IsAvailable property (audio clip) 

*(Formerly known as IsMusicVoxAvailable, which is now
obsolete)*

    readonly bool AudioClip.IsAvailable;

Gets whether this audio clip is available on the player's system.

This will normally be *true, unless the clip was bundled in
the external AUDIO.VOX file and the player does not have the file on
their system.*

You do not normally need to check this property, since the Play command
will silently fail if it cannot find the audio clip to play.

    if (aExplosion.IsAvailable)
    {
      aExplosion.Play();
    }

checks if the aExplosion audio clip is available, and if so plays it.

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also:*

### Type property (audio clip) 

    readonly AudioType AudioClip.Type;

Gets the type of this audio clip, as initially set in the editor.

The AudioType allows you to group audio clips into areas such as Sound
and Music.

    if (aExplosion.Type == eAudioTypeMusic)
    {
      Display("Explosion is music!");
    }

displays a message if the *aExplosion clip is music.*

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also: ,*

Character functions and properties
----------------------------------

### AddInventory 

*(Formerly known as global function AddInventory, which is now
obsolete) ILBRK *(Formerly known as global function
AddInventoryToCharacter, which is now obsolete)**

    Character.AddInventory(InventoryItem *item, optional int addAtIndex)

Adds the specified item to the character's inventory. This ensures that
the item gets added to the character's inventory list, and that any
on-screen inventory display gets updated if appropriate.

The first parameter is the inventory item's Script O-Name from the
editor (for example, *iPoster).*

By default, the new item is added to the end of the character's
inventory list. However, you can insert it in a particular position in
the list by supplying the second parameter. The new item is inserted
*before the current item at *addAtIndex.
Indexes are numbered from 0, so to add the item at the start of the
list, pass 0 as the second parameter.**

    cEgo.AddInventory(iKey);

will give inventory item iKey to character EGO.

*See Also: , ,*

### AddWaypoint 

*(Formerly known as MoveCharacterPath, which is now
obsolete)*

    Character.AddWaypoint(int x, int y)

Tells the character to move to (X,Y) directly, after it has finished its
current move. This function allows you to queue up a series of moves for
the character to make, if you want them to take a preset path around the
screen. Note that any moves made with this command ignore walkable
areas.

This is useful for situations when you might want a townsperson to
wander onto the screen from one side, take a preset route around it and
leave again.

    cSomeguy.Walk(160, 100);
    cSomeguy.AddWaypoint(50, 150);
    cSomeguy.AddWaypoint(50, 50);

tells character SOMEGUY to first of all walk to the centre of the screen
normally (obeying walkable areas), then move to the bottom left corner
and then top left corner afterwards.

*See Also:*

### Animate (character) 

*(Formerly known as AnimateCharacter, which is now
obsolete) ILBRK *(Formerly known as AnimateCharacterEx,
which is now obsolete)**

    Character.Animate(int loop, int delay, optional RepeatStyle,
                      optional BlockingStyle, optional Direction)

Starts the character animating, using loop number LOOP of his current
view. The overall speed of the animation is set with DELAY, where 0 is
the fastest, and increasing numbers mean slower. The delay for each
frame is worked out as DELAY + FRAME SPD, so the individual frame speeds
are relative to this overall speed.

Before using this command, you should use in order to select the view
you want to animate with and prevent any automatic animations (eg.
walking or idle animations) from playing.

The *RepeatStyle parameter sets whether the animation will
continuously repeat the cycling through the frames. This can be
*eOnce (or zero), in which case the animation will start
from the first frame of LOOP, and go through each frame in turn until
the last frame, where it will stop. If RepeatStyle is
*eRepeat (or 1), then when the last frame is reached, it
will go back to the first frame and start over again with the
animation.***

*direction specifies which way the animation plays. You can
either pass eForwards (the default) or eBackwards.*

For *blocking you can pass either eBlock (in which case the
function will wait for the animation to finish before returning), or
eNoBlock (in which case the animation will start to play, but your
script will continue). The default is eBlock.*

If the character is currently moving, it will be stopped.

    cEgo.LockView(5);
    cEgo.Animate(3, 1, 0, eBlock, eBackwards);
    cEgo.UnlockView();

will animate the character once using loop number 3 of view 5 backwards,
and wait until the animation finishes before returning.

*See Also:*

### ChangeRoom 

*(Formerly known as NewRoom, which is now obsolete) ILBRK
*(Formerly known as NewRoomEx, which is now obsolete) ILBRK
*(Formerly known as NewRoomNPC, which is now obsolete)***

    Character.ChangeRoom(int room_number, optional int x, optional int y, optional CharacterDirection direction)

Changes the room that the character is in.

If you call this on the player character, then the game will move into
the new room with them.

**IMPORTANT: This command does not change the room
immediately; instead, it will perform the actual room change once your
script function has finished (This is to avoid problems with unloading
the script while it is still running). This means that you should not
use any other commands which rely on the new room (object positionings,
and so on) after this command within the same function.**

If you call this on a non-player character, then they are instantly
transported to the new room number.

Optionally, you can include an X and Y co-ordinate (you must include
either both or neither). If you do so, then the character will also be
moved to the specified co-ordinates in the new room.

Optionally, you can also include direction parameter, that determines
which direction this character will be facing after room change.

    player.ChangeRoom(4, 100, 50, eDirectionRight);

will move the player character to room 4 and also place him at
coordinates 100,50. This will also mean that the game moves into room 4.

*Compatibility: Optional *direction parameter
is supported only by **AGS 3.4.0 and later versions.****

*See Also:*

### ChangeRoomAutoPosition 

    Character.ChangeRoomAutoPosition(int room_number, optional int newPosition)

Changes the room that the character is in, and positions him along one
of the room edges.

This command simulates the behaviour of the old “Go to room” interaction
command from AGS 2.72 and previous versions. If
*newPosition is not specified or is 0, the character will
be placed on the opposite side of the new room, if he is within 10
pixels of a room edge in the current room.*

Altenatively, you can specify the position where he will get placed in
the new room. *newPosition can be 1000 for the left edge,
2000 for the right edge, 3000 for the bottom edge and 4000 for the top
edge. Then, add on the offset within that edge where you want to place
the character, in normal room co-ordinates.*

**IMPORTANT: This command does not change the room
immediately; instead, it will perform the actual room change once your
script function has finished (This is to avoid problems with unloading
the script while it is still running). This means that you should not
use any other commands which rely on the new room (object positionings,
and so on) after this command within the same function.**

**NOTE: This command can only be used with the player
character.**

    player.ChangeRoomAutoPosition(4, 2100);

will move the player character to room 4 and place him half way down the
right hand side of the screen. This will also mean that the game moves
into room 4.

*See Also:*

### ChangeView 

*(Formerly known as ChangeCharacterView, which is now
obsolete)*

    Character.ChangeView(int view)

Changes the normal view number of the character to *view.
This is useful if, for example, you want the character to change the
clothes they are wearing, and so permanently alter their view number.*

**NOTE: This command is **not intended to
change the view temporarily to perform an animation. If you want to do
that, use the LockView command instead. This ChangeView command
permanently changes the character's normal walking view.****

    cEgo.ChangeView(5);

will make the EGO character use view number 5 as his walking view.

*See Also: ,*

### FaceCharacter 

*(Formerly known as global function FaceCharacter, which is now
obsolete)*

    Character.FaceCharacter(Character* toFace, optional BlockingStyle)

Turns the graphic of the character so that it looks like he is facing
character TOFACE. This involves changing the current loop to the
appropriate loop number, and setting the frame number to 0 (standing).

If the character has Turning enabled (ie. the “Characters turn to face
direction” game option is turned on, and the character does not have the
“Do not turn before walking” option checked), then the character will
turn on the spot in order to face the new direction. In this case, the
BlockingStyle parameter determines whether the script waits for the
character to finish turning (eBlock, the default) or whether the script
continues immediately and the character finishes turning later on
(eNoBlock).

If the character does not have Turning enabled, he will immediately turn
to face the new direction and the BlockingStyle parameter has no effect.
In this case, the screen will not be refreshed straight away – if you
want to see the character facing his new direction immediately, call
Wait(1);

    cEgo.FaceCharacter(cMan);

will make the character EGO face the character MAN

*See Also: , , ,*

### FaceDirection 

    Character.FaceDirection(CharacterDirection direction, BlockingStyle=eBlock)

Turns the graphic of the character so that it looks like he is facing
direction *direction. This involves changing the current
loop to the appropriate loop number, and setting the frame number to 0
(standing).*

If the character has Turning enabled (ie. the “Characters turn to face
direction” game option is turned on, and the character does not have the
“Do not turn before walking” option checked), then the character will
turn on the spot in order to face the new direction. In this case, the
BlockingStyle parameter determines whether the script waits for the
character to finish turning (eBlock, the default) or whether the script
continues immediately and the character finishes turning later on
(eNoBlock).

If the character does not have Turning enabled, he will immediately turn
to face the new direction and the BlockingStyle parameter has no effect.
In this case, the screen will not be refreshed straight away – if you
want to see the character facing his new direction immediately, call
Wait(1);

    cEgo.FaceDirection(eDirectionUpRight);

will make the character EGO face up-right.

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

*See Also: , , ,*

### FaceLocation 

*(Formerly known as global function FaceLocation, which is now
obsolete)*

    Character.FaceLocation(int x, int y, optional BlockingStyle)

Similar to the FaceCharacter function, except that this faces the
character to room co-ordinates (X,Y). This allows him to face not only
other characters, but also hotspots or anything else as well (you can
get co-ordinates by watching the co-ordinates displayed in the Room
Settings mode as you move the mouse over the room background).

If the character has Turning enabled (ie. the “Characters turn to face
direction” game option is turned on, and the character does not have the
“Do not turn before walking” option checked), then the character will
turn on the spot in order to face the new direction. In this case, the
BlockingStyle parameter determines whether the script waits for the
character to finish turning (eBlock, the default) or whether the script
continues immediately and the character finishes turning later on
(eNoBlock).

If the character does not have Turning enabled, he will immediately turn
to face the new direction and the BlockingStyle parameter has no effect.
In this case, the screen will not be refreshed straight away – if you
want to see the character facing his new direction immediately, call
Wait(1);

    cEgo.FaceLocation(cEgo.x + 50, cEgo.y);

will make the character face to the east.

*See Also: , , ,*

### FaceObject 

    Character.FaceObject(Object* object, optional BlockingStyle)

Similar to the FaceCharacter function, except that this faces the
character to object OBJECT in the current room.

If the character has Turning enabled (ie. the “Characters turn to face
direction” game option is turned on, and the character does not have the
“Do not turn before walking” option checked), then the character will
turn on the spot in order to face the new direction. In this case, the
BlockingStyle parameter determines whether the script waits for the
character to finish turning (eBlock, the default) or whether the script
continues immediately and the character finishes turning later on
(eNoBlock).

If the character does not have Turning enabled, he will immediately turn
to face the new direction and the BlockingStyle parameter has no effect.
In this case, the screen will not be refreshed straight away – if you
want to see the character facing his new direction immediately, call
Wait(1);

    player.FaceObject(object[2]);

will make the player character face object 2.

*See Also: , , ,*

### FollowCharacter 

*(Formerly known as global function FollowCharacter, which is now
obsolete) ILBRK *(Formerly known as global function
FollowCharacterEx, which is now obsolete)**

    Character.FollowCharacter(Character* chartofollow, optional int dist,
                              optional int eagerness)

Tells the character to follow CHARTOFOLLOW around, wherever he goes. You
could use this command to have a group of main characters who go around
together, or for example when the hero has rescued someone from the bad
guy, they can follow the hero home.

Pass CHARTOFOLLOW as *null to stop the character
following.*

There are a couple of extra optional parameters:

DIST sets how far away from CHARTOFOLLOW that CHARID will stand. If DIST
is 1, they will try to stand very close; if DIST is for example 20, they
will stand about 20 pixels away.

EAGERNESS sets on average how long the character will stand around
before checking if he needs to move again. Setting this to 0 means that
he will always be on the move until he reaches CHARTOFOLLOW; setting
this to 99 means that he will pause and think for a while on route.
Values in between specify different lengths of idle time.

The default values are DIST=10 and EAGERNESS=97.

As a special case, setting DIST=0 and EAGERNESS=0 makes CHARID behave as
if it is chasing CHARTOFOLLOW - it will try and get there as quickly as
possible. Setting EAGERNESS=0 also tells the character not to stop when
they reach CHARTOFOLLOW, but instead to randomly wander around the
character - useful perhaps for a very energetic dog or something.

There is also another special use for this command. You can pass the
special value FOLLOW\_EXACTLY as the DIST parameter rather than passing
a number. If you do this, then CHARID will always remain at exactly the
same X and Y co-ordinates as CHARTOFOLLOW. This might be useful for
effects such as a temporary halo over the character and so forth.

If you use FOLLOW\_EXACTLY, then EAGERNESS has another meaning. If you
pass 0, CHARID will be drawn in front of CHARTOFOLLOW; if you pass 1, it
will be drawn behind.

    cMan.FollowCharacter(cEgo, 5, 80);

will make character MAN follow character EGO standing about 5 pixels
near him and waiting for a while before he makes his move.

### GetAtScreenXY (character) 

*(Formerly known as global function GetCharacterAt, which is now
obsolete)*

    static Character* Character.GetAtScreenXY(int x, int y)

Checks if there is a character at SCREEN co-ordinates (X,Y). Returns the
character if there is, or null if there is not. See the description of
GetLocationName for more on screen co-ordinates.

NOTE: Any characters with the “Clickable” property set to false will not
be seen by this function.

    if (Character.GetAtScreenXY(mouse.x, mouse.y) == cEgo) {
      Display("The mouse is over the main character");
    }

will display the message if the mouse cursor is over the EGO character

*See Also: , ,*

### GetProperty (character) 

*(Formerly known as GetCharacterProperty, which is now
obsolete)*

    Character.GetProperty(string property)

Returns the custom property setting of the PROPERTY for the specified
character.

This command works with Number properties (it returns the number), and
with Boolean properties (returns 1 if the box was checked, 0 if not).

Use the equivalent GetTextProperty function to get a text property.

    if (cEgo.GetProperty("Value") > 200)
      Display("EGO's value is over 200!");

will print the message if EGO has its “Value” property set to more than
200.

*See Also:*

### GetTextProperty (character) 

*(Formerly known as GetCharacterPropertyText, which is now
obsolete) ILBRK *(Formerly known as
Character.GetPropertyText, which is now obsolete)**

    String Character.GetTextProperty(string property)

Returns the custom property setting of the PROPERTY for the specified
character.

This command works with Text properties only. The property's text will
be returned from this function.

Use the equivalent GetProperty function to get a non-text property.

    String description = cEgo.GetTextProperty("Description");
    Display("EGO's description: %s", description);

will retrieve EGO's “description” property and display it.

*See Also:*

### SetProperty (character) 

    bool Character.SetProperty(const string property, int value)

Sets the new *value for the custom *property
for the specified character. Returns TRUE if such property exists and
FALSE on failure.**

This command works with Number properties (it sets the numeric value),
and with Boolean properties (sets FALSE is value is equal to 0, or TRUE
otherwise).

Use the equivalent SetTextProperty function to set new text property
value.

    cEgo.SetProperty("XPLevel", 10);

will change EGO character's “XPLevel” custom property to 10.

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

*See Also:*

### SetTextProperty (character) 

    bool Character.SetTextProperty(const string property, const string value)

Sets the new *value text for the custom
*property for the specified character. Returns TRUE if such
property exists and FALSE on failure.**

This command works with Text properties only. The property's text will
be changed to new value.

Use the equivalent SetProperty function to set a non-text property.

    cEgo.SetTextProperty("Description", "I am handsome!");

will change EGO's “description” property.

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

*See Also:*

### HasInventory 

    bool Character.HasInventory(InventoryItem *item)

Checks whether the character currently has the specified inventory item.
Returns *true if they do, or *false if they
don't.**

The parameter is the inventory item's Script O-Name from the editor (for
example, *iPoster).*

    if (player.HasInventory(iKey))
    {
      Display("The player has the key!!");
    }

will display a message if the player has the key.

*Compatibility: Supported by **AGS 3.1.0 and
later versions.***

*See Also: , ,*

### IsCollidingWithChar 

*(Formerly known as AreCharactersColliding, which is now
obsolete)*

    Character.IsCollidingWithChar(Character* otherChar)

Checks if the character is touching OTHERCHAR. This function just checks
the baseline of both characters, so if one is standing a fair distance
behind the other, it will not be marked as colliding.

Returns 1 if the characters feet are touching, 0 otherwise.

    if (cEgo.IsCollidingWithChar(cMan) == 1)
       { colliding code here }

will execute the colliding code only if the characters EGO and MAN are
colliding.

*See Also: , ,*

### IsCollidingWithObject (character) 

*(Formerly known as AreCharObjColliding, which is now
obsolete)*

    Character.IsCollidingWithObject(Object* obj)

Checks whether the character's feet (ie. the bottom third of the
character) are touching OBJ. This can be used to determine if the
character is standing on the object.

Returns 1 if they are, and 0 if they are not.

    if (cEgo.IsCollidingWithObject(object[3]) == 1) {
      // colliding code here
    }

will execute the colliding code only if the character EGO and the object
number 3 are colliding.

*See Also: , ,*

### LockView 

*(Formerly known as SetCharacterView, which is now
obsolete)*

    Character.LockView(int view)

Sets the character's view to VIEW. This can be used to perform
animations with characters, for example bending down to pick something
up, which don't use the default view.

**NOTE: This function locks the character's view to the
specified view, so that it can only be changed by other script commands
(ie. it won't automatically be changed by AGS on walkable areas, screen
changes, etc). When you are done with the animation, call UnlockView to
allow AGS to take control back.**

    cEgo.LockView(12);
    cEgo.Animate(0, 0, eOnce, eBlock, eForwards);
    cEgo.UnlockView();

will change the character's EGO view to view 12, perform an animation
using loop 0, wait until the animation finishes and then return the
character to his normal view.

*See Also: , , , , ,*

### LockViewAligned 

*(Formerly known as SetCharacterViewEx, which is now
obsolete)*

    Character.LockViewAligned(int view, int loop, Alignment)

Sets the character's view to VIEW, and sets the character's current
frame to the first frame in LOOP of VIEW.

The main purpose of this command is that it can align the new frame to
the previous one. This is particularly useful if you want to go from the
character's normal walking view to a specific animation - since
characters have the central point as their 'axis', if you have a wider
animation then it can be difficult to stop yourself getting a jumping
effect when the animation starts.

*Alignment can have one of the following values:*

|l|l|

Note that this only aligns the first frame of the animation, so to get
the full benefit all your frames in the animation loop should be the
same width. All following frames will be shifted by the same amount,
until UnlockView is called.

**NOTE: This function locks the character's view to the
specified view, so that it can only be changed by other script commands
(ie. it won't automatically be changed by the program on regions, screen
changes, etc). When you are done with the animation, call UnlockView to
allow the program to take control back.**

    cEgo.LockViewAligned(12, 1, eAlignLeft);
    cEgo.Animate(1, 5, eOnce, eBlock, eForwards);
    cEgo.UnlockView();

will change the character's EGO view to view 12, perform an animation
using loop 1, wait until the animation finishes and then return the
character to his normal view.

*See Also: , ,*

### LockViewFrame 

*(Formerly known as SetCharacterFrame, which is now
obsolete)*

    Character.LockViewFrame(int view, int loop, int frame)

Sets the character's graphic to frame FRAME of loop LOOP of view number
VIEW. This is useful if you don't want an animation, but just want to
change the character to display a specific frame.

The frame will be locked to the one you specify until you call
UnlockView.

    cEgo.LockViewFrame(AGHAST, 2, 4);
    Wait(40);
    cEgo.UnlockView();

will change EGO to have frame 4 of loop 2 in the AGHAST view, wait for a
second, then return him to normal.

*See Also: , ,*

### LockViewOffset 

*(Formerly known as SetCharacterViewOffset, which is now
obsolete)*

    Character.LockViewOffset(int view, int xOffset, int yOffset)

Sets the character's view to VIEW, in the same way as LockView does.
However, it also adds a specified offset to all the character's frames
until UnlockView is called.

The XOFFSET and YOFFSET parameters specify **in actual game
resolution units how much to move the character's sprite.
Positive values for X move right, for Y move down; negative values do
the opposite.**

This command is designed to allow you to cope with those niggly
situations where animations don't quite line up with the standing frame,
assuming all the frames of the animation are the same size. Note that
LockViewAligned is easier to use if your frames will align at the left
or right hand side.

**NOTE: You should only use this command for minor
adjustments, since the offsets do not affect the clickable area of the
character, what walkable area he is in, and so forth. You should limit
the use of this command to in-game cutscenes where the player has no
control.**

**NOTE: This is the only command in AGS which uses actual
game-resolution co-ordinates. Therefore, specifying an x offset of 1
will actually move 1 pixel in a 640x400 game, and will not be multiplied
up to 2 (they will be automatically adjusted though if the player
chooses to play the game at another resolution).**

**NOTE: This function locks the character's view to the
specified view, so that it can only be changed by other script commands
(ie. it won't automatically be changed by AGS on walkable areas, screen
changes, etc). When you are done with the animation, call UnlockView to
allow AGS to take control back.**

    cEgo.LockViewOffset(12, 1, -1);
    cEgo.Animate(1, 5, eOnce, eBlock, eForwards);
    cEgo.UnlockView();

will change EGO's view to view 12 and animate using loop 1, meanwhile
all frames will be shifted 1 pixel right and 1 pixel up.

*See Also: , ,*

### LoseInventory 

*(Formerly known as global function LoseInventory, which is now
obsolete)ILBRK *(Formerly known as
LoseInventoryFromCharacter, which is now obsolete)**

    Character.LoseInventory(InventoryItem *item)

Removes the specified inventory item from the character's inventory. If
they do not have the item, nothing happens.

The parameter is the inventory item's Script O-Name from the editor.

    cEgo.LoseInventory(iKey);

will make the character EGO lose the inventory item iKey from the
inventory tab

*See Also:*

### Move (character) 

    Character.Move(int x, int y, optional BlockingStyle,
                                 optional WalkWhere);

Starts the character moving from its current location to (X,Y), but does
not play the character's walking animation.

The parameters to this command are identical to the command – see that
page for more details. The only difference is that *Walk
plays the walking animation whereas *Move does not.**

In the vast majority of cases, you will use
**Character.Walk instead.**

    cEgo.Move(155, 122, eBlock);

will make the character move to 155,122 without playing his walking
animation. The script will not continue until the character has reached
his destination.

*Compatibility: Supported by **AGS 3.1.0 and
later versions.***

*See Also: , , , , ,*

### PlaceOnWalkableArea 

*(Formerly known as MoveToWalkableArea, which is now
obsolete)*

    Character.PlaceOnWalkableArea()

Places the character in the nearest walkable area to its current
location. If the character is already on a walkable area, nothing
happens.

This is useful for example in the Player Enters Room event of a room, to
make sure the character can move if a ChangeRoom with co-ordinates has
been issued to get there. You could also use this in on\_event for
eEventEnterRoomBeforeFadein to use whenever a player enters a room.

    cEgo.x = Random(320);
    cEgo.y = Random(200);
    cEgo.PlaceOnWalkableArea();

will move character EGO to a random position but make sure that he is on
a walkable area.

### RemoveTint (character) 

    Character.RemoveTint()

Undoes the effects of calling Tint, and returns the character to using
the room's ambient tint.

    player.Tint(0, 250, 0, 30, 100);
    Wait(40);
    player.RemoveTint();

will tint the player character green for a second, then turn it back to
normal.

*See Also: ,*

### IsInteractionAvailable (character) 

    Character.IsInteractionAvailable(CursorMode)

Checks whether there is an event handler defined for activating the
character in cursor mode MODE.

This function is very similar to RunInteraction, except that rather than
run the event handler script function, it simply returns
*true if something would have happened, or
*false if unhandled\_event would have been run.**

    if (cNPC.IsInteractionAvailable(eModeTalkto) == 0)
      Display("speaking with this character would not do anything.");

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

*See Also: ,*

### RunInteraction (character) 

*(Formerly known as RunCharacterInteraction, which is now
obsolete)*

    Character.RunInteraction(CursorMode)

Fires the event script as if the player had clicked the mouse on the
character in the specified cursor mode. This is one of the mouse cursor
modes, as defined in your Cursors tab in the editor.

    cMan.RunInteraction(eModeTalk);

will execute the code defined in the MAN's “TALK TO CHARACTER” event.

*See Also: , , ,*

### Say 

*(Formerly known as DisplaySpeech, which is now obsolete)*

    Character.Say(string message)

Displays the text MESSAGE as speech above the character's head. The text
will remain on screen for a limited time, and the user may or may not be
able to click it away depending on the setting of “Player can't skip
speech text”. The text displayed by this function looks identical to
that used by the dialog system.

You can insert the value of variables into the message. For more
information, see the section.

    cEgo.Say("My name is ego");

will display the message above the character's EGO head like the LEC
games, whilst playing the character's talking animation.

*See Also: , , ,*

### SayAt 

*(Formerly known as DisplaySpeechAt, which is now
obsolete)*

    SayAt(int x, int y, int width, string message)

Similar to , except that the text is displayed with its top left corner
at (X,Y), in an area WIDTH wide.

You can use this function to write the character's speech text anywhere
you like, and AGS will still play the character's talking animation and
so on if appropriate.

**NOTE: This function does not support Whole-Screen
speech.**

    cEgo.SayAt(220, 20, 100, "My name is ego");

will display the message in the top right corner of the screen, whilst
playing the character's talking animation.

*See Also: ,*

### SayBackground 

*(Formerly known as DisplaySpeechBackground, which is now
obsolete)*

    Overlay* Character.SayBackground(string message)

Similar to Say, except that this function returns immediately and the
game continues while the character is talking. This allows you to have
characters talking in the background while the player does other things.
Note that the character's talking animation is not played if this
function is used.

This command works by creating a text overlay with an automatic removal
time delay. The overlay is returned by this command, so you can save it
for use later with Overlay.IsValid and Overlay.Remove, if you want to
remove the text prematurely.

If background speech is already on-screen for the character, it will be
removed and replaced with the new MESSAGE.

All background speech is automatically removed when a normal Say command
is used (unless you set the global variable to 1).

    cMan.SayBackground("Hey, why won't you talk to me?");

will display the message above character MAN's head without pausing the
game.

*See Also:*

### SetAsPlayer 

*(Formerly known as SetPlayerCharacter, which is now
obsolete)*

    Character.SetAsPlayer()

Changes the character which the player controls to the specified
character. This function will also cause the room to change to the room
which the chosen character is currently in (though as with ChangeRoom,
the change won't happen until the end of the script).

Additionally, calling this command will cause the “player” variable to
be updated to point to the specified character.

    cMan.SetAsPlayer();

will change the character that the player controls to character MAN and
also change to the room that MAN is in, if he is not in the current
room.

*See Also: ,*

### SetLightLevel (character) 

    void Character.SetLightLevel(int light_level)

Sets individual light level for this character.

The light level is from **-100 to 100.**

In 8-bit games you cannot use positive light level for brightening
effect, but you may still use negative values to produce darkening
effect.

To disable character lighting and tinting effects, call .

**NOTE: Setting a light level will disable any RGB tint set
for the character.**

**NOTE: Character's individual light level OVERRIDES both
ambient light level and local region light level.**

    cEgo.SetLightLevel(100);

This will give character EGO maximal individual brightness.

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

*See Also: , , ,*

### SetIdleView 

*(Formerly known as SetCharacterIdle, which is now
obsolete)*

    Character.SetIdleView(int idleview, int delay)

Changes the character's idle view to IDLEVIEW, with a timeout of DELAY
seconds of inactivity before it is played. Inactivity is defined as when
the character is not moving and not being animated.

Setting DELAY to 0 causes the idle view to be looped continuously when
the character is not moving - this is useful when for example the
character is swimming and they need to tread water when idle.

Pass IDLEVIEW as -1 to disable the idle view completely.

**NOTE: The DELAY is actually relative to the game speed.
Setting this to 1 means a one second delay at the default 40 fps, but if
you have adjusted the game speed then the delay will be adjusted
accordingly.**

**NOTE: Due to a quirk in AGS, you cannot set the Idle View
to view 1. In the unlikely event that you created your idle view in View
1, you'll need to move it to another view number.**

    cEgo.SetIdleView(12, 30);

will change/set the character EGO's idle view to 12. The idle view will
be played if the character is idle for 30 seconds.

### SetWalkSpeed 

*(Formerly known as SetCharacterSpeed, which is now
obsolete)ILBRK *(Formerly known as SetCharacterSpeedEx,
which is now obsolete)**

    Character.SetWalkSpeed(int x_speed, int y_speed)

Changes the character to have a walking speed of X\_SPEED in the
horizontal direction and Y\_SPEED in the vertical direction. The values
used for X\_SPEED and Y\_SPEED are identical to those set in the AGS
Editor for walking speed.

X\_SPEED and Y\_SPEED can be identical, in which case the character
moves with the same speed in any direction. (the editor calls this
“Uniform movement speed”)

**NOTE: This function CANNOT be called while the character
is moving, so you must stop him first.**

    cEgo.SetWalkSpeed(10, 10);

will change the character EGO's speed to 10.

*See Also: , , , ,*

### StopMoving (character) 

*(Formerly known as global function StopMoving, which is now
obsolete)*

    Character.StopMoving()

Stops the character moving and sets its graphic to the standing frame of
the current loop.

    if (cEgo.x > 299)
    {
      cEgo.StopMoving();
    }

will stop the character when he reaches the coordinate x=300.

*See Also: ,*

### Think 

*(Formerly known as DisplayThought, which is now obsolete)*

    Character.Think(string message, ...)

Displays the text MESSAGE as a thought above the specified character's
head. The text will remain on screen for a limited time, and the user
may or may not be able to click it away depending on the setting of
“Player can't skip speech text”.

How this function displays the text depends on a few things: the Speech
Style setting, the 'Thought uses bubble GUI' setting, and whether the
character has a thinking animation or not.

If the “Thought uses bubble GUI” setting is not checked, then the
thought will be displayed in the same way as normal speech - the
difference being that the character's thinking animation will play (or
no animation if they don't have one).

If you are using Sierra-style speech and the character doesn't have a
thinking animation, the thought bubble will be displayed in
lucasarts-style.

If the “Thought uses bubble GUI” setting has been set, then the thought
will be displayed like normal speech, except that the bubble GUI will be
used for the window background. In Lucasarts-style speech this means
above the character's head, in Sierra-style it will be done along the
top of the screen as normal.

If the character has a thinking animation, it will just loop through
once (it won't repeat).

You can insert the value of variables into the message. For more
information, see the section.

    cEgo.Think("I wonder what's for dinner.");

will display the message above EGO's head and play the character's
thinking animation.

*See Also: , , , , ,*

### Tint (character) 

    Character.Tint(int red, int green, int blue,
                   int saturation, int luminance)

Tints the character on the screen to (RED, GREEN, BLUE) with SATURATION
percent saturation.

This function applies a tint to a specific character. For the meaning of
all the parameters, see .

The tint set by this function overrides any ambient tint set for the
room. For this reason, passing the SATURATION as 0 to this function does
not turn it off - rather, it ensures that no tint is applied to the
character (even if an ambient tint is set).

To remove the tint set by this function and return to using the ambient
tint for this character, call .

**NOTE: This function only works in hi-colour games and
with hi-colour sprites.**

    cEgo.Tint(0, 250, 0, 30, 100);

will tint the EGO character green.

*See Also: , ,*

### UnlockView 

*(Formerly known as ReleaseCharacterView, which is now
obsolete)*

    Character.UnlockView()

Allows the engine to automatically control the character's view, as
normal. Use this once you have finished doing the animation which you
started with the LockView command.

    cEgo.LockView(12);
    cEgo.Animate(0, 0, eOnce, eBlock, eForwards);
    cEgo.UnlockView();

will play an animation using loop 0 of view 12, then return the
character to its normal view.

*See Also:*

### Walk 

*(Formerly known as MoveCharacter, which is now
obsolete)ILBRK *(Formerly known as MoveCharacterBlocking,
which is now obsolete)ILBRK *(Formerly known as
MoveCharacterDirect, which is now obsolete)***

    Character.Walk(int x, int y, optional BlockingStyle,
                                 optional WalkWhere);

Starts the character moving from its current location to (X,Y), whilst
playing his walking animation.

If *blocking is eNoBlock (the default) then control returns
to the script immediately, and the character will move in the
background.*

If *blocking is eBlock then this command will wait for the
character to finish moving before your script resumes.*

If *walkWhere is eWalkableAreas (the default), then the
character will attempt to get as close a possible to (X,Y) by using the
room's walkable areas.*

If *walkWhere is eAnywhere, then the character will simply
walk directly from its current location to (X,Y), ignoring the room
walkable areas.*

If you don't want the character's walking animation to play, you can use
the command instead.

**NOTE: this function only works with characters which are
on the current screen.**

**NOTE: if you need to find out when the character has
reached its destination, use the property.**

    cEgo.Walk(155, 122, eBlock);

will make the character walk to 155,122. The script will not continue
until the character has reached his destination.

*See Also: , , , , ,*

### WalkStraight 

*(Formerly known as MoveCharacterStraight, which is now
obsolete)*

    Character.WalkStraight(int x, int y, optional BlockingStyle);

Moves the character from its current location towards (X,Y) in a
straight line as far as is possible before hitting a non-walkable area.
This is useful for use with the arrow keys for character movement, since
it guarantees that the character will move in a straight line in the
direction specified.

*blocking determines whether the function waits for the
character to finish moving before your script resumes. eNoBlock is the
default (which means your script resumes straight away, and the
character moves in the background). You can also pass eBlock, in which
case your script will not resume until the character finishes moving.*

    cEgo.WalkStraight(166, 78);

will move the character EGO in a straight line towards co ordinates
166,78 until he hits a non walkable area.

*See Also:*

### ActiveInventory property 

*(Formerly known as SetActiveInventory, which is now
obsolete) ILBRK *(Formerly known as
character\[\].activeinv, which is now obsolete)**

    InventoryItem* Character.ActiveInventory

Gets/sets the character's current active inventory item. Setting it will
update the mouse cursor if appropriate.

This property is useful in “Use inventory on hotspot/character/etc”
events, to find out which inventory item the player is trying to use on
the target.

To deselect the current inventory, set it to *null.*

    cEgo.ActiveInventory = iKey;

will make the inventory item iKey active (before you use it make sure
that the player has the inventory item)

### Animating property (character) 

*(Formerly known as character\[\].animating, which is now
obsolete)*

    readonly bool Character.Animating

Returns 1 if the character is currently animating. ILBRK Returns 0 if
the character has finished its animation.

This property is read-only. To change character animation, use the
command.

    cEgo.Animate(5, 0);
    while (cEgo.Animating) Wait(1);

will animate EGO and wait until the animation finishes.

In reality, you would simply use the Blocking parameter of Animate so
you wouldn't need to do this.

*See Also: , , ,*

### AnimationSpeed property 

*(Formerly known as character\[\].animspeed, which is now
obsolete)*

    int Character.AnimationSpeed;

Gets/sets the character's animation delay, as set in the editor.

    player.AnimationSpeed = 4;

will change the player character's animation speed to 4.

*See Also: ,*

### Baseline property (character) 

*(Formerly known as SetCharacterBaseline, which is now
obsolete)*

    int Character.Baseline

Gets/sets the character's baseline. This allows you to set a specific
base line for the character, which works similarly to walk-behind area
and object baselines.

The baseline can be from 1 to the height of the room (normally 200), or
set it to 0 to go back to using the character's feet as the baseline.

    cEgo.Baseline = 120;

will move the character's baseline (which can be used for testing
collisions, or for walk-behinds) to a line positioned at y coordinate =
120.

*See Also: ,*

### BlinkInterval property 

*(Formerly part of SetCharacterBlinkView, which is now
obsolete)*

    int Character.BlinkInterval

Gets/sets the character's blinking interval, which specifies how long
the game waits between playing the blinking animation. This is specified
in game loops - an interval of 80 would play the blinking animation
about every 2 seconds.

This property has no effect if no has been set.

    cEgo.BlinkView = 10;
    cEgo.BlinkInterval = 160;

will change the character EGO's blink view to view 10, and play the
animation every 4 seconds.

*See Also: ,*

### BlinkView property 

*(Formerly part of SetCharacterBlinkView, which is now
obsolete)*

    int Character.BlinkView

Gets/sets the character's blinking view. To stop the character from
blinking, set this to -1.

The property sets how often the blinking animation is played.

    cEgo.BlinkView = 10;
    cEgo.BlinkInterval = 160;

will change the character EGO's blink view to view 10, and play the
animation every 4 seconds.

*See Also: ,*

### BlinkWhileThinking property 

    bool Character.BlinkWhileThinking

Gets/sets whether the character can blink while thinking. By default
this is set to true, but if your blinking animation only goes with the
talking animation and not the thinking one, you can stop the character
from blinking while Thinking by setting this to false.

    cEgo.BlinkWhileThinking = false;

will stop EGO from blinking while his thinking animation is playing.

*See Also: ,*

### BlockingHeight property (character) 

    int Character.BlockingHeight

Gets/sets the character's blocking height.

The blocking height determines how large of a blocking rectangle the
character exerts to stop other characters walking through it. If this is
set to 0 (the default), then the blocking rectangle is automatically
calculated to be the character's width, and 5 pixels high.

You can manually change the setting by entering a blocking height in
pixels, which is the size of walkable area that the character
effectively removes by standing on it.

**NOTE: This property has no effect unless the property is
set to *true.***

    cEgo.BlockingHeight = 20;

will make EGO block 20 pixels high (10 above and 10 below his baseline)

*See Also: ,*

### BlockingWidth property (character) 

    int Character.BlockingWidth

Gets/sets the character's blocking width.

The blocking width determines how large of a blocking rectangle the
character exerts to stop other characters walking through it. If this is
set to 0 (the default), then the blocking rectangle is automatically
calculated to be the character's width, and 5 pixels high.

You can manually change the setting by entering a blocking width in
pixels, which is the size of walkable area that the character
effectively removes by standing on it.

**NOTE: This property has no effect unless the property is
set to *true.***

    cEgo.BlockingWidth = 50;

will make EGO block 50 pixels wide (25 pixels to the left of his X
co-ordinate, and 25 to the right)

*See Also: ,*

### Clickable property (character) 

*(Formerly known as SetCharacterClickable, which is now
obsolete)*

    bool Character.Clickable

Gets/sets whether the character is recognised as something which the
player can interact with. This allows you to modify the “Clickable”
property set initially in the Editor.

If you set this to *true then the player can look at, speak
to, and so on the character (as with the old Sierra games). If you set
this to *false, then if the player clicks on the character
it will activate whatever is behind them (as with the old Lucasarts
games).**

    cMan.Clickable = 0;

will make the game ignore clicks on the character MAN.

*See Also: , , ,*

### DestinationX property 

    readonly int Character.DestinationX

Gets the X coordinate of the character's final moving destination. If
character is not walking or moving it is equal to its current position.

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

*See Also: , , ,*

### DestinationY property 

    readonly int Character.DestinationY

Gets the Y coordinate of the character's final moving destination. If
character is not walking or moving it is equal to its current position.

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

*See Also: , , ,*

### DiagonalLoops property 

*(Formerly part of SetCharacterProperty, which is now
obsolete)*

    bool Character.DiagonalLoops

Gets/sets whether diagonal walking loops are used for the character. If
this is set to *true, then loops 4-7 will be used as
diagonal walking loops. If this is set to *false, then the
character will only face in 4 directions and you can use loops 4-7 for
other purposes.**

    cEgo.DiagonalLoops = true;

will enable diagonal walking loops for character EGO.

### Frame property (character) 

*(Formerly known as character\[\].frame, which is now
obsolete)*

    int Character.Frame

Gets/sets the character's current frame number. Usually you won't change
this directly, but will use the Animate command to play an animation.

    Display("EGO currently using frame %d.", cEgo.Frame);

displays EGO's current frame number within his view.

*SeeAlso: , ,*

### HasExplicitTint property 

    readonly bool Character.HasExplicitTint

Returns *true if the character has a tint set explicitly
with the command.*

Returns *false if the character has no explicit tint, but
it may still be tinted by or a region tint.*

    if (player.HasExplicitTint)
    {
      player.RemoveTint();
    }

removes the player's tint if it currently has one.

*Compatibility: Supported by **AGS 3.1.0 and
later versions.***

*SeeAlso: ,*

### ID property (character) 

    readonly int Character.ID

Gets the character's ID number. This is the character's number from the
editor, and is useful if you need to interoperate with legacy code that
uses the character's number rather than name.

    MoveCharacter(cEgo.ID, 100, 50);

uses the obsolete MoveCharacter function to move EGO to (100, 50)

### IdleView property 

    readonly int Character.IdleView

Gets the character's current idle view. If the character doesn't have
one, returns -1.

This property is read-only; to change the view, use the function.


    Display("EGO's idle view is currently view %d.", cEgo.IdleView);

will display EGO's current idle view number.

*SeeAlso:*

### IgnoreLighting property 

*(Formerly known as SetCharacterIgnoreLight, which is now
obsolete)*

    bool Character.IgnoreLighting

Allows you to dynamically modify the “ignore lighting” checkbox for the
character. If this is set to 0, the character will be affected by region
light levels and tints; if this is set to 1, then the character will
ignore all region lighting.

    cEgo.IgnoreLighting = 1;

will make the character look the same no matter if he stands on regions
with different light levels.

### IgnoreWalkbehinds property (character) 

*(Formerly known as SetCharacterIgnoreWalkbehinds, which is now
obsolete)*

    bool Character.IgnoreWalkbehinds

Gets/sets whether the character is affected by walkbehind areas. Passing
*false (the default setting) means that the character will
be placed behind walk- behind areas according to the relevant
baselines.*

Passing *true means that the character will never be placed
behind a walk-behind area. This is useful if for example you want to use
the character as an overlay to display rain or snow onto a scene.*

**NOTE: enabling this property does not currently work
properly when using the Direct3D driver.**

    cEgo.IgnoreWalkbehinds = true;

will make the character EGO ignore walk-behinds.

*See Also: ,*

### InventoryQuantity property 

*(Formerly known as character\[\].inv, which is now
obsolete)*

    int Character.InventoryQuantity[]

Gets/sets the quantity of the specified inventory item that the
character currently has. The array index is the inventory item number,
from the Inventory pane in the editor.

Usually, you should use the AddInventory and LoseInventory functions to
modify the character's inventory; however, if you need to add or remove
a large number of items in one go, directly changing this array can be
an easier method.

If you change this array directly, the on-screen inventory will not be
updated. In this case, you must call UpdateInventory to see any new or
removed items.

If you just want to quickly check whether the character has a particular
item or not, use the function instead.

    Display("The player has $%d.", player.InventoryQuantity[iCash.ID]);

will display how many inventory items of type iCash the player has.

*See Also: , , ,*

### Loop property (character) 

*(Formerly known as character\[\].loop, which is now
obsolete)*

    int Character.Loop

Gets/sets the character's current loop number. Usually you won't change
this directly, but will use the Animate command to play an animation.

    Display("EGO currently using loop %d.", cEgo.Loop);

displays EGO's current loop number within his view.

*SeeAlso: , ,*

### ManualScaling property (character) 

*(Formerly known as Character.IgnoreScaling, which is now
obsolete) ILBRK *(Formerly part of SetCharacterProperty,
which is now obsolete)**

    bool Character.ManualScaling

Gets/sets whether the character's scaling level is determined by the
walkable area that he is walking on, or whether it is set manually by
the script. This is equivalent to the “Ignore room area scaling”
checkbox in the editor.

If this is set to *true, then the character's scaling level
is set manually by the property (by default this is `100%`). If it is
set to *false, then the character will be stretched or
shrunk automatically as appropriate on walkable areas.**

    cEgo.ManualScaling = true;
    cEgo.Scaling = 50;

will tell EGO to ignore walkable area scaling levels and be fixed to
`50%` zoom level.

*SeeAlso:*

### MovementLinkedToAnimation property 

    bool Character.MovementLinkedToAnimation

Gets/sets whether the character's movement is linked to their animation.
By default this is *true, which means that when the
character is walking their movement across the screen will be kept in
sync with their animation frame changing. Without this, the character
can appear to “glide” across the screen.*

In some special cases you may wish to turn this off though, and to do so
you can set this property to *false.*

In previous versions of AGS, this setting was known as “Anti-glide mode”
and was a game-wide setting.

    player.MovementLinkedToAnimation = false;
    player.Walk(50, 100, eBlock);
    player.MovementLinkedToAnimation = true;

will turn off movement-linked animation for the player character, walk
him to (50,100), then turn it back on again.

*Compatibility: Supported by **AGS 3.1.1 and
later versions.***

*See Also: , ,*

### Moving property (character) 

*(Formerly known as character\[\].walking, which is now
obsolete)*

    readonly bool Character.Moving

Returns *true if the character is currently moving, or
*false if not.**

This property is read-only; to change the character's movement, use the
, and commands.

    cEgo.Walk(125, 40);
    while (cEgo.Moving) Wait(1);

will move EGO to 125,40 and return control to the player when he gets
there.

*See Also: , , , , ,*

### Name property (character) 

*(Formerly known as character\[\].name, which is now
obsolete)*

    String Character.Name

Gets/sets the name of the character, as set in the AGS Editor. This is
the full name, not the script name.

Note that character names are limited to 40 characters, so if you set
the name it will be truncated to that length.

    Display("You are controlling %s.", player.Name);

will display the name of the player character

### NormalView property 

*(Formerly known as character\[\].defview, which is now
obsolete)*

    readonly int Character.NormalView

Gets the character's normal view. This is the character's standard
walking view, that is used when his view is not locked to something
else.

This property is read-only; to change it, use the command.

    if (cEgo.View == cEgo.NormalView) {
      Display("EGO is not animating, not talking and not idle.");
    }

will display a message if EGO is currently displayed using his normal
view.

*See Also: ,*

### PreviousRoom property 

*(Formerly known as character\[\].prevroom, which is now
obsolete)*

    readonly int Character.PreviousRoom

Gets the room number that the character was previously in. If the
character is still in the room that they started in, this will be -1.
Otherwise, it will be the room number of the room that they were last
in.

This is a read-only property. It is set automatically by .

    Display("EGO's previous room was %d.", cEgo.PreviousRoom);

will display the EGO character's previous room.

### Room property 

*(Formerly known as character\[\].room, which is now
obsolete)*

    readonly int Character.Room

Gets the room number that the character is currently in.

This is a read-only property. It is set by .

    Display("EGO is in room %d.", cEgo.Room);

will display the EGO character's current room.

### ScaleMoveSpeed property 

*(Formerly part of SetCharacterProperty, which is now
obsolete)*

    bool Character.ScaleMoveSpeed

Gets/sets whether the character's movement speed is adjusted in line
with his current scaling level. This allows you to modify the “Adjust
speed with scaling” option from the editor.

If you set this to *true, the character's movement speed
will be adjusted so that he walks at a speed relative to his current
scaling level. If you set this to *false, the character
will always just move at his normal speed.**

    cEgo.ScaleMoveSpeed = true;

will mean that EGO's speed is adjusted in line with his scaling

*See Also:*

### ScaleVolume property 

    bool Character.ScaleVolume

Gets/sets whether the character's volume is adjusted in line with his
current scaling level. This allows you to modify the “Adjust volume with
scaling” option from the editor.

By default, this is *false. If you set it to
*true, then any frame-linked sounds for the character (for
example, footstep sounds) will have their volume automatically adjusted
in line with the character's scaling level. At the normal `100%` zoom
level the sounds will be played at normal volume, but will then get
quieter and louder as appropriate in scaled walkable areas.**

    cEgo.ScaleVolume = true;

will mean that EGO's footstep sounds are adjusted in line with his
scaling

*See Also:*

### Scaling property (character) 

    int Character.Scaling

Gets/sets the character's current scaling level.

This property can always be read, and returns the character's current
zoom level, which will be between 5 and 200 (the default being 100 if
they are not currently scaled).

You can only set the value of this property if is enabled for the
character; otherwise, the scaling is determined automatically based on
the walkable area that the character is on.

    cEgo.ManualScaling = true;
    cEgo.Scaling = 50;

will tell EGO to ignore walkable area scaling levels and be fixed to
`50%` zoom level.

*SeeAlso:*

### Solid property (character) 

*(Formerly part of SetCharacterProperty, which is now
obsolete)*

    bool Character.Solid

Gets/sets whether the character can be walked through by other
characters.

If this is set to *true, then the character is solid and
will block the path of other characters. If this is set to
*false, then the character acts like a hologram, and other
characters can walk straight through him.**

    cEgo.Solid = true;

will mean that EGO blocks the path other characters.

*See Also: ,*

### Speaking property 

    readonly bool Character.Speaking

Returns true if the character is currently talking, or false if not.

This property is read-only. It will **only return true for
the active talking character; that is, it will not return true for any
characters talking with the SayBackground command.**

Since this property will only be true while the character is speaking,
and speaking is a blocking command, this property will probably only be
useful to access from the (late\_)repeatedly\_execute\_always handler.

    if ((cEgo.Speaking) && (!cEgo.Animating)) {
      cEgo.Animate(3, 5, eRepeat, eNoBlock);
    }

will animate the character using loop 3 while they are talking (only
useful with Sierra-style speech).

*See Also: , , , ,*

### SpeakingFrame property 

    readonly int Character.SpeakingFrame

Returns the current frame number of the character's talking animation.
This is useful when using Sierra-style speech, if you want to
synchronize events with the progress of the close-up face talking
animation.

This property is read-only. It is only accessible while the character is
speaking; if you attempt to call it when is *false then it
will raise an error.*

Since speaking is a blocking command, this property will probably only
be useful access from the (late\_)repeatedly\_execute\_always handler.

    if (cEgo.Speaking) {
      if (cEgo.SpeakingFrame == 0) {
        cMan.Move(cMan.x + 10, cMan.y, eNoBlock, eAnywhere);
      }
    }

will move cMan to the right every time the talking animation loops back
to Frame 0.

*See Also: ,*

### SpeechAnimationDelay property 

    int Character.SpeechAnimationDelay;

Gets/sets the character's speech animation delay, as set in the editor.
This specifies how many game loops each frame of the character's speech
animation is shown for.

**NOTE: This property is ignored if lip sync is enabled.**

**NOTE: This property **cannot be used if the
Speech.UseGlobalSpeechAnimationDelay is set to **true. In
that case, the Speech.GlobalSpeechAnimationDelay property value is used
instead.******

    player.SpeechAnimationDelay = 4;

will change the player character's speech animation speed to 4.

*Compatibility: Supported by **AGS 3.1.2 and
later versions.***

*See Also: , , , , ,*

### SpeechColor property 

*(Formerly known as SetTalkingColor, which is now
obsolete)*

    int Character.SpeechColor

Gets/sets the character's speech text color. This is set by default in
the editor.

NEWCOLOR is the colour slot index from the Palette Editor. This can be
0-255 for a 256-colour game, or one of the hi-colour indexes available
from the Palette Editor.

    cEgo.SpeechColor = 14;

will change the character's EGO talking color to yellow.

*See Also:*

### SpeechView property 

*(Formerly known as SetCharacterSpeechView, which is now
obsolete)ILBRK *(Formerly known as character\[\].talkview,
which is now obsolete)**

    int Character.SpeechView

Gets/sets the character's talking view. If you change it, the new view
number will be used as the character's talking view in all future
conversations.

You can set this to -1 to disable the character's speech view.

    cEgo.SpeechView = 10;

will change the character EGO's speech view to view 10.

*See Also: , , ,*

### Thinking property 

    readonly bool Character.Thinking

Returns true if the character is currently thinking, or false if not.

This property is read-only. It will **only return true for
the active thinking character.**

Since this property will only be true while the character is thinking,
and thinking is a blocking command, this property will probably only be
useful to access from the (late\_)repeatedly\_execute\_always handler.

    function repeatedly_execute_always()
    {
      if (cEgo.Thinking) {
        cEgo.Transparency = 50;
      else
        cEgo.Transparency = 0;
    }

this will keep character semi-transparent while he is thinking.

*Compatibility: Supported by **AGS 3.3.4 and
later versions.***

*See Also: , , , ,*

### ThinkingFrame property 

    readonly int Character.ThinkingFrame

Returns the current frame number of the character's thinking animation.
This is useful when using Sierra-style speech, if you want to
synchronize events with the progress of the close-up face talking
animation.

This property is read-only. It is only accessible while the character is
thinking; if you attempt to call it when is *false then it
will raise an error.*

Since thinking is a blocking command, this property will probably only
be useful access from the (late\_)repeatedly\_execute\_always handler.

    if (cEgo.Thinking) {
      if (cEgo.ThinkingFrame == 0) {
        cMan.Move(cMan.x + 10, cMan.y, eNoBlock, eAnywhere);
      }
    }

will move cMan to the right every time the thinking animation loops back
to Frame 0.

*Compatibility: Supported by **AGS 3.3.4 and
later versions.***

*See Also: ,*

### ThinkView property 

*(Formerly known as character\[\].thinkview, which is now
obsolete)*

    int Character.ThinkView

Gets/sets the character's thinking view. This is used to animate the
character when a thought is being displayed.

    cEgo.ThinkView = 14;

will change the character EGO's thinking view to 14.

*See Also:*

### Transparency property (character) 

*(Formerly known as SetCharacterTransparency, which is now
obsolete)*

    int Character.Transparency

Gets/sets the character's transparency. This is specified as a
percentage, from 0 to 100. 100 means fully transparent (ie. invisible),
and 0 is totally opaque (fully visible). Numbers in between represent
varying levels of transparency.

**NOTE: Transparency only works in 16-bit and 32-bit colour
games.**

**NOTE: When using the DirectX 5 driver, a large
transparent character can significantly slow down AGS.**

Some rounding is done internally when the transparency is stored –
therefore, if you get the transparency after setting it, the value you
get back might be one out. Therefore, using a loop with
`cEgo.Transparency++;` is not recommended as it will probably end too
quickly.

In order to fade a character in, the best approach is shown in the
example below:

    int trans = cEgo.Transparency;
    while (trans < 100) {
      trans++;
      cEgo.Transparency = trans;
      Wait(1);
    }

will gradually fade out the character from its current transparency
level to being fully invisible.

*See Also:*

### TurnBeforeWalking property 

*(Formerly part of SetCharacterProperty, which is now
obsolete)*

    bool Character.TurnBeforeWalking

Gets/sets whether the character turns to face his new direction before
walking. This is equivalent (though opposite) to the editor “Do not turn
before walking” tick-box.

If you set this to 1, the character will turn on the spot to face his
new direction before setting off on a walk. If you set this to 0, the
character will instantly face in the correct direction and start
walking.

    cEgo.TurnBeforeWalking = 1;

will tell EGO to turn to face his new direction before setting off,
whenever he walks.

### View property (character) 

    readonly int Character.View

Gets the view that the character is currently displayed using.

This property is read-only; to change the view, use the ChangeView and
LockView functions.

    Display("EGO's view is currently view %d.", cEgo.View);

will display EGO's current view number.

*SeeAlso: , , , ,*

### WalkSpeedX property 

    readonly int Character.WalkSpeedX;

Gets the character's walking speed in the X direction. If using uniform
movement, this will be the same as the Y walking speed.

This property is read-only. To change the walking speed, use the
SetWalkSpeed function.

    Display("player's x speed: %d", player.WalkSpeedX);

will display the player's X speed.

*See Also: ,*

### WalkSpeedY property 

    readonly int Character.WalkSpeedY;

Gets the character's walking speed in the Y direction. If using uniform
movement, this will be the same as the X walking speed.

This property is read-only. To change the walking speed, use the
SetWalkSpeed function.

    Display("player's y speed: %d", player.WalkSpeedY);

will display the player's Y speed.

*See Also: ,*

### x property (character) 

    int Character.x;

Gets/sets the character's current X co-ordinate. This is expressed in
normal room co-ordinates, and specifies the centre-bottom of the
character's sprite.

**NOTE: Do **NOT change this property while
the character is moving. Make sure the character is standing still
before changing his co-ordinates.****

    Display("The player is at %d,%d.", player.x, player.y);

displays the player character's current coordinates.

*See Also: ,*

### y property (character) 

    int Character.y;

Gets/sets the character's current Y co-ordinate. This is expressed in
normal room co-ordinates, and specifies the centre-bottom of the
character's sprite.

**NOTE: Do **NOT change this property while
the character is moving. Make sure the character is standing still
before changing his co-ordinates.****

    Display("The player is at %d,%d.", player.x, player.y);

displays the player character's current coordinates.

*See Also: ,*

### z property (character) 

    int Character.z;

Gets/sets the character's current Z position. This allows the character
to levitate off the ground, whilst still retaining its normal Y
co-ordinate for baseline calculations and regions.

Normally this is set to 0 (ground-level), but you can increase it to
make the character float.

    while (player.z < 20) {
      player.z++;
      Wait(1);
    }

gradually levitates the character up to 20 pixels.

*See Also: ,*

### SetCharacterProperty 

    SetCharacterProperty (CHARID, PROPERTY, int new_value)

**This command is now obsolete. It has been replaced by the
following properties:**

ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK

DateTime functions and properties
---------------------------------

### Now property 

*(Formerly known as GetTime, which is now obsolete)*

    readonly static DateTime* DateTime.Now;

Gets the current system time. You could use this for timing a loop, or
for effects like telling the player to go to bed, and so on.

A *DateTime object is returned, which contains various
properties that you can use.*

Note that the DateTime object that you get will not be kept up to date
with the current time; it will remain static with the time at which you
called DateTime.Now.

    DateTime *dt = DateTime.Now;
    Display("The date is: %02d/%02d/%04d", dt.DayOfMonth, dt.Month, dt.Year);
    Display("The time is: %02d:%02d:%02d", dt.Hour, dt.Minute, dt.Second);

will display the current date and time in 24-hour format

*See Also: , , , , , ,*

### DayOfMonth property 

    readonly int DateTime.DayOfMonth;

Gets the day of the month represented by the DateTime object. This will
be from 1 to 31, representing the current day within the month.

For an example, see .

*See Also:*

### Hour property 

    readonly int DateTime.Hour;

Gets the hour represented by the DateTime object. This will be from 0 to
23, representing the hour in 24-hour format.

For an example, see .

*See Also:*

### Minute property 

    readonly int DateTime.Minute;

Gets the minute represented by the DateTime object. This will be from 0
to 59, representing the minute in 24-hour format.

For an example, see .

*See Also:*

### Month property 

    readonly int DateTime.Month;

Gets the month represented by the DateTime object. This will be from 1
to 12, representing the month of the year.

For an example, see .

*See Also:*

### RawTime property 

*(Formerly known as GetRawTime, which is now obsolete)*

    readonly int DateTime.RawTime;

This function returns the raw system time, as the number of seconds
since January 1970. While this value is not useful in itself, you can
use it to calculate time differences by getting the value at the start
of the game, for example, and then getting the value later on, and the
difference between the two is how much time has elapsed.

**NOTE: Because this accesses the real-time clock on the
users' system, it is not a good idea to use this for long term timing
tasks, since if the user saves the game and then restores it later, the
Time value returned by this function will obviously include the
difference when they were not playing.**

    DateTime *dt = DateTime.Now;
    int start_time = dt.RawTime;
    Wait(120);
    dt = DateTime.Now;
    Display("After the wait it is now %d seconds later.", dt.RawTime - start_time);

should display that 3 seconds have elapsed.

*See Also: ,*

### Second property 

    readonly int DateTime.Second;

Gets the second represented by the DateTime object. This will be from 0
to 59, representing the second.

For an example, see .

*See Also:*

### Year property 

    readonly int DateTime.Year;

Gets the year represented by the DateTime object. This is the full year,
for example *2005.*

For an example, see .

*See Also:*

Dialog functions and properties
-------------------------------

### DisplayOptions (dialog) 

    int Dialog.DisplayOptions(optional DialogOptionSayStyle)

Presents the options for this dialog to the user and waits until they
select one of them. The selected option number is returned.

**NOTE: This command does not run any dialog scripts, it
simply displays the options and waits for the player to choose one. To
run the dialog normally, use the command instead.**

This command is useful if you want to implement your own dialog system,
but still use the standard AGS dialog option selection screens.

The optional *DialogOptionSayStyle parameter determines
whether the chosen option is automatically spoken by the player
character. The default is *eSayUseOptionSetting, which will
use the option's “Say” setting from the dialog editor. You can
alternatively use *eSayAlways, which will speak the chosen
option regardless of its setting in the editor; or
*eSayNever, which will not speak the chosen option.****

If the text parser is enabled for this dialog and the player types
something into it rather than selecting an option, the special value
`DIALOG_PARSER_SELECTED` will be returned, and AGS will have
automatically called with the player's text. Therefore, you can call to
process it.

    int result = dOldMan.DisplayOptions();
    if (result == DIALOG_PARSER_SELECTED)
    {
      Display("They typed something into the parser!!");
    }
    else
    {
      Display("They chose dialog option %d.", result);
    }

will show the options for dialog *dOldMan and display a
message depending on what the player selected.*

*Compatibility: Supported by **AGS 3.0.2 and
later versions.***

*See Also: ,*

### GetOptionState (dialog) 

*(Formerly known as global function GetDialogOption, which is now
obsolete)*

    Dialog.GetOptionState(int option)

Finds out whether an option in a conversation is available to the player
or not.

OPTION is the option number within the dialog, from 1 to whatever the
highest option is for that topic.

The return value can have the following values:

    eOptionOff
      The option is disabled - the player will not see it
    eOptionOn
      The option is enabled - the player can now see and use it
    eOptionOffForever
      The option is permanently disabled - no other command can ever turn
      it back on again.

These are the same as the options passed to Dialog.SetOptionState.

    if (dJoeExcited.GetOptionState(2) != eOptionOn)
      Display("It's turned off");

Will display a message if option 2 of dialog dJoeExcited is not
currently switched on.

*See Also: , ,*

### GetOptionText (dialog) 

    String Dialog.GetOptionText(int option)

Returns the text for the specified dialog option.

OPTION is the option number within the dialog, from 1 to whatever the
highest option is for that topic.

    String optionText = dJoeBloggs.GetOptionText(3);
    Display("Option 3 of dialog dJoeBloggs is %s!", optionText);

will display the text for the third option of the dJoeBloggs dialog.

*Compatibility: Supported by **AGS 3.0.2 and
later versions.***

*See Also: ,*

### HasOptionBeenChosen 

    bool Dialog.HasOptionBeenChosen(int option)

Finds out whether the player has already chosen the specified option in
this dialog. This is mainly useful when drawing your own custom dialog
options display, since it allows you to differentiate options that have
already been chosen.

OPTION is the option number within the dialog, from 1 to whatever the
highest option is for that topic.

    if (dJoeExcited.HasOptionBeenChosen(2))
      Display("The player has chosen option 2 in dialog dJoeExcited!");

will display a message if the player has used option 2 of the dialog
before.

*Compatibility: Supported by **AGS 3.1.1 and
later versions.***

*See Also: , ,*

### ID property (dialog) 

    readonly int Dialog.ID;

Gets the dialog ID number from the editor.

This might be useful if you need to interoperate with legacy scripts
that work with dialog ID numbers.

    Display("dFisherman is Dialog %d!", dFisherman.ID);

will display the ID number of the dFisherman dialog

*Compatibility: Supported by **AGS 3.1.0 and
later versions.***

### OptionCount property (dialog) 

    readonly int Dialog.OptionCount;

Gets the number of options that this dialog has.

This might be useful in a script module if you want to iterate through
all the possible choices in the dialog.

    Display("dFisherman has %d options!", dFisherman.OptionCount);

will display the number of options in the dFisherman dialog.

*Compatibility: Supported by **AGS 3.0.2 and
later versions.***

*See Also: ,*

### SetHasOptionBeenChosen (dialog) 

    Dialog.SetHasOptionBeenChosen(int option, bool chosen)

Changes whether an option in a conversation is marked as previously
chosen by the player. The option is marked as chosen whenever player
selects it during the conversation, and is usually highlighted with
different text colour. This function lets you to reset the option state,
or force it change at any random moment.

OPTION is the option number within the dialog, from 1 to whatever the
highest option is for that topic.

    if (dDialog1.HasOptionBeenChosen(1))
        dDialog1.SetHasOptionBeenChosen(1, false); // reset the option state

will mark option 1 of dialog dDialog1 as “not chosen yet”.

*Compatibility: Supported by **AGS 3.3.0 and
later versions.***

*See Also: ,*

### SetOptionState (dialog) 

*(Formerly known as global function SetDialogOption, which is now
obsolete)*

    Dialog.SetOptionState(int option, DialogOptionState)

Changes whether an option in a conversation is available to the player
or not. This allows you to add extra options to a conversation once the
player has done certain things.

OPTION is the option number within the topic, from 1 to whatever the
highest option is for that topic.

The DialogOptionState controls what happens to this option. It can have
the following values:

    eOptionOff
      The option is disabled - the player will not see it
    eOptionOn
      The option is enabled - the player can now see and use it
    eOptionOffForever
      The option is permanently disabled - no other command can ever turn
      it back on again.

These are equivalent to the option-off, option-on, and
option-off-forever dialog commands.

    if (GetGlobalInt(10)==1)
        dialog[4].SetOptionState(2, eOptionOn);

will enable option 2 of topic number 4 if the Global Integer 10 is 1.

*See Also: , ,*

### ShowTextParser property (dialog) 

    readonly bool Dialog.ShowTextParser;

Gets whether this dialog shows a text box allowing the player to type in
text.

This property is initially set in the Dialog Editor.

    if (dFisherman.ShowTextParser)
    {
      Display("dFisherman has a text box!");
    }

will display a message if dFisherman has the option enabled

*Compatibility: Supported by **AGS 3.2.1 and
later versions.***

### Start (dialog) 

*(Formerly known as global function RunDialog, which is now
obsolete)*

    Dialog.Start()

Starts a conversation from the specified topic.

NOTE: The conversation will not start immediately; instead, it will be
run when the current script function finishes executing.

If you use this command from within the dialog\_request function, it
will specify that the game should return to this new topic when the
script finishes.

    dMerchant.Start();

will start the conversation topic named dMerchant.

*See Also: ,*

### StopDialog 

    StopDialog ()

This command can only be used from within the dialog\_request function.
It tells AGS that when dialog\_request finishes, the whole conversation
should stop rather than continuing with the dialog script.

You can use this function to end the conversation depending on whether
the player has/does a certain thing.

     function dialog_request (int dr) {
     if (dr==1) {
       cEgo.AddInventory(iPoster);
       StopDialog();
     }

will give the player the inventory item 3 and then end the conversation.

*See Also:*

DialogOptionsRenderingInfo functions and properties 
---------------------------------------------------

The DialogOptionsRenderingInfo instance is used by the system. You can
never create one yourself, it will be passed in to the dialog option
functions as described in the linked page.

### RunActiveOption 

    bool DialogOptionsRenderingInfo.RunActiveOption();

Runs the currently selected dialog option, the one set in
ActiveOptionID, and returns **true on success.**

As of AGS 3.4.0 you must call this function for conversation to
continue, most common places for such call are
`dialog_options_mouse_click` and `dialog_options_key_press` functions.

    function dialog_options_key_press(DialogOptionsRenderingInfo *info, eKeyCode key)
    {
      if (keycode == eKeyReturn)
        info.RunActiveOption();
    }

runs selected dialog option when player presses Enter/Return key.

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

*See Also:*

### Update 

    void DialogOptionsRenderingInfo.Update();

Forces dialog options to redraw, eventually leading to be
`dialog_options_render` function run.

Like other elements of interface, dialog options GUI does not redraw
itself every game loop; in attempt to optimize perfomance it aims to do
so only when there are changes to its look. But sometimes you may want
to change GUI looks based on your own decision, and not automatic
behavior. For example, you want to script animated text, or other
element belonging to dialog options. This is when you call
DialogOptionsRenderingInfo.Update().

**IMPORTANT: Keep in mind that calling
**Update does not immediately run `dialog_options_render`,
render function will be run at least after current script ends.****

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

### ActiveOptionID property 

    int DialogOptionsRenderingInfo.ActiveOptionID;

Gets/sets the currently active option on the dialog options screen. You
set this in the `dialog_options_get_active` function to tell AGS which
option the mouse is hovering over. This ensures that the correct option
is activated when the player clicks the mouse button.

You can read this property in the `dialog_options_render` function in
order to highlight the selected option in a different manner to the
others.

This property can be set to **0 which indicates that no
option is selected; otherwise it will be the option number from 1 to the
number of options in the dialog.**

    function dialog_options_get_active(DialogOptionsRenderingInfo *info)
    {
      info.ActiveOptionID = 1;
    }

always selects the first option

*Compatibility: Supported by **AGS 3.1.0 and
later versions.***

*See Also: ,*

### DialogToRender property 

    Dialog* DialogOptionsRenderingInfo.DialogToRender;

Gets the dialog that needs to be rendered. You can loop through all the
options in the dialog in order to decide what to display on the screen.

For an example please see the page.

*Compatibility: Supported by **AGS 3.1.0 and
later versions.***

*See Also: ,*

### HasAlphaChannel property (DialogOptionsRenderingInfo) 

    int DialogOptionsRenderingInfo.HasAlphaChannel;

Gets/sets whether the dialog options's drawing surface will have alpha
channel.

This can only be set within the `dialog_options_get_dimensions`
function, but can be read in other functions in order to render the
options.

    function dialog_options_get_dimensions(DialogOptionsRenderingInfo *info)
    {
      info.Width = 300;
      info.Height = 150;
      info.HasAlphaChannel = true;
    }

creates a 300x150 size area with alpha channel to draw the dialog
options in.

*Compatibility: Supported by **AGS 3.3.0 and
later versions.***

*See Also: ,*

### Height property (DialogOptionsRenderingInfo) 

    int DialogOptionsRenderingInfo.Height;

Gets/sets the height of the area needed to draw the dialog options.

This can only be set within the `dialog_options_get_dimensions`
function, but can be read in other functions in order to render the
options.

    function dialog_options_get_dimensions(DialogOptionsRenderingInfo *info)
    {
      info.Width = 300;
      info.Height = 150;
    }

creates a 300x150 size area to draw the dialog options in

*Compatibility: Supported by **AGS 3.1.0 and
later versions.***

*See Also:*

### ParserTextBoxWidth property 

    int DialogOptionsRenderingInfo.ParserTextBoxWidth;

Gets/sets the width of the text parser textbox on the dialog options. If
the text parser is not enabled for this dialog, this setting will be
ignored.

This can only be set within the `dialog_options_get_dimensions`
function.

    function dialog_options_get_dimensions(DialogOptionsRenderingInfo *info)
    {
      info.Width = 300;
      info.Height = 150;
      // Put the text parser at the bottom (if enabled)
      info.ParserTextBoxX = 10;
      info.ParserTextBoxY = 130;
      info.ParserTextBoxWidth = 180;
    }

positions the parser text box at (10,130) inside the 300x150 dialog
options area

*Compatibility: Supported by **AGS 3.1.0 and
later versions.***

*See Also: , ,*

### ParserTextBoxX property 

    int DialogOptionsRenderingInfo.ParserTextBoxX;

Gets/sets the X-position of the text parser textbox on the dialog
options. If the text parser is not enabled for this dialog, this setting
will be ignored.

This X-position is relative to the dialog options surface. That is, an X
of 10 will position it 10 pixels within the dialog options area, not 10
pixels from the edge of the screen.

This can only be set within the `dialog_options_get_dimensions`
function.

    function dialog_options_get_dimensions(DialogOptionsRenderingInfo *info)
    {
      info.Width = 300;
      info.Height = 150;
      // Put the text parser at the bottom (if enabled)
      info.ParserTextBoxX = 10;
      info.ParserTextBoxY = 130;
      info.ParserTextBoxWidth = 180;
    }

positions the parser text box at (10,130) inside the 300x150 dialog
options area

*Compatibility: Supported by **AGS 3.1.0 and
later versions.***

*See Also: ,*

### ParserTextBoxY property 

    int DialogOptionsRenderingInfo.ParserTextBoxY;

Gets/sets the Y-position of the text parser textbox on the dialog
options. If the text parser is not enabled for this dialog, this setting
will be ignored.

This Y-position is relative to the dialog options surface. That is, a Y
of 10 will position it 10 pixels within the dialog options area, not 10
pixels from the edge of the screen.

This can only be set within the `dialog_options_get_dimensions`
function.

    function dialog_options_get_dimensions(DialogOptionsRenderingInfo *info)
    {
      info.Width = 300;
      info.Height = 150;
      // Put the text parser at the bottom (if enabled)
      info.ParserTextBoxX = 10;
      info.ParserTextBoxY = 130;
      info.ParserTextBoxWidth = 180;
    }

positions the parser text box at (10,130) inside the 300x150 dialog
options area

*Compatibility: Supported by **AGS 3.1.0 and
later versions.***

*See Also:*

### Surface property (DialogOptionsRenderingInfo) 

    DrawingSurface* DialogOptionsRenderingInfo.Surface;

Gets the drawing surface that can be used to draw the dialog options.

This can only be used within the `dialog_options_render` function; in
all other functions it will return *null.*

Unlike most other uses of the DrawingSurface, you do **NOT
have to release this one. AGS will automatically do that for you after
the `dialog_options_render` function has completed.**

The size of the surface should correspond to the Width and Height
requested in the `dialog_options_get_dimensions` function.

    function dialog_options_render(DialogOptionsRenderingInfo *info)
    {
      info.Surface.Clear(14);
    }

clears the dialog options area to yellow.

*Compatibility: Supported by **AGS 3.1.0 and
later versions.***

*See Also:*

### Width property (DialogOptionsRenderingInfo) 

    int DialogOptionsRenderingInfo.Width;

Gets/sets the width of the area needed to draw the dialog options.

This can only be set within the `dialog_options_get_dimensions`
function, but can be read in other functions in order to render the
options.

    function dialog_options_get_dimensions(DialogOptionsRenderingInfo *info)
    {
      info.Width = 300;
      info.Height = 150;
    }

creates a 300x150 size area to draw the dialog options in

*Compatibility: Supported by **AGS 3.1.0 and
later versions.***

*See Also:*

### X property (DialogOptionsRenderingInfo) 

    int DialogOptionsRenderingInfo.X;

Gets/sets the horizontal co-ordinate of the top-left corner of the
dialog options area.

This can only be set within the `dialog_options_get_dimensions`
function, but can be read in other functions in order to render the
options.

    function dialog_options_get_dimensions(DialogOptionsRenderingInfo *info)
    {
      info.X = 50;
      info.Y = 20;
      info.Width = 200;
      info.Height = 150;
    }

creates a 200x150 size area at (50, 20) to draw the dialog options in

*Compatibility: Supported by **AGS 3.1.0 and
later versions.***

*See Also:*

### Y property (DialogOptionsRenderingInfo) 

    int DialogOptionsRenderingInfo.Y;

Gets/sets the vertical co-ordinate of the top-left corner of the dialog
options area.

This can only be set within the `dialog_options_get_dimensions`
function, but can be read in other functions in order to render the
options.

    function dialog_options_get_dimensions(DialogOptionsRenderingInfo *info)
    {
      info.X = 50;
      info.Y = 20;
      info.Width = 200;
      info.Height = 150;
    }

creates a 200x150 size area at (50, 20) to draw the dialog options in

*Compatibility: Supported by **AGS 3.1.0 and
later versions.***

*See Also:*

DrawingSurface functions and properties 
---------------------------------------

The DrawingSurface family of functions allow you to directly draw onto
dynamic sprites and room backgrounds in the game. You get a drawing
surface by calling or , and you can then use the following methods to
draw onto the surface.

**IMPORTANT: You **MUST call the method when
you have finished drawing onto the surface. This allows AGS to update
its cached copies of the image and upload it to video memory if
appropriate.****

### Clear (drawing surface) 

*(Formerly known as RawClearScreen, which is now obsolete)*

    DrawingSurface.Clear(optional int colour)

Clears the surface to the specified COLOUR (this is a number you can
find in the Colours pane of the editor). The current contents of the
surface will be lost.

If you do not supply the COLOUR parameter, or use COLOR\_TRANSPARENT,
the surface will be cleared to be fully transparent.

    DrawingSurface *surface = Room.GetDrawingSurfaceForBackground();
    surface.Clear(14);
    surface.DrawingColor = 13;
    surface.DrawCircle(160,100,50);
    surface.Release();

clears the room background to be fully yellow, then draws a pink circle
in the middle of it.

*See Also:*

### CreateCopy 

*(Formerly known as RawSaveScreen, which is now obsolete)*

    DrawingSurface* DrawingSurface.CreateCopy()

Makes a backup copy of the current surface, in order that it can be
restored later. This could be useful to back up a background scene
before writing over it, or to save a certain state of your drawing to
restore later.

Unlike the obsolete RawSaveScreen command in previous versions of AGS,
backup surfaces created with this command are not lost when the player
changes room or restores a game. However, surfaces containing a copy of
room backgrounds can be **very large, using up a large
amount of memory and can increase the save game sizes significantly.
Therefore, it is **strongly recommended that you Release
any backup copy surfaces as soon as you are done with them.****

    DrawingSurface *surface = Room.GetDrawingSurfaceForBackground();
    DrawingSurface *backup = surface.CreateCopy();
    surface.DrawTriangle(0,0,160,100,0,200);
    Wait(80);
    surface.DrawSurface(backup);
    backup.Release();
    surface.Release();

will save a copy of the room background, draw a triangle onto it, wait
for a while and then restore the original background.

*See Also:*

### DrawCircle 

*(Formerly known as RawDrawCircle, which is now obsolete)*

    DrawingSurface.DrawCircle(int x, int y, int radius)

Draws a filled circle of radius RADIUS with its centre at (X,Y) in the
current drawing colour.

    DrawingSurface *surface = Room.GetDrawingSurfaceForBackground();
    surface.DrawingColor = 14;
    surface.DrawCircle(160,100,50);
    surface.Release();

will draw a circle in the centre of the screen, of 50 pixels radius.

*See Also: ,*

### DrawImage 

*(Formerly known as RawDrawImage, which is now obsolete)
ILBRK *(Formerly known as RawDrawImageResized, which is now
obsolete) ILBRK *(Formerly known as
RawDrawImageTransparent, which is now obsolete)***

    DrawingSurface.DrawImage(int x, int y, int slot, optional int transparency,
                             optional int width, optional int height)

Draws image SLOT from the sprite manager onto the surface at location
(X,Y).

Optionally, you can also specify the transparency of the image. This is
a number from 0-100; using a *transparency of 50 will draw
the image semi-transparent; using 0 means it will not be transparent.*

You can also resize the image as you draw it. In order to do this,
simply specify a *width and *height that you
wish to resize the image to when it is drawn.**

**NOTE: This command only works if the image to be drawn is
the same colour depth as the surface that you are drawing onto.**

**NOTE: Transparency does not work in 256-colour games, or
with 256-colour sprites.**

**NOTE: The X and Y co-ordinates given are ROOM
co-ordinates, not SCREEN co-ordinates. This means that in a scrolling
room you can draw outside the current visible area.**

    DrawingSurface *surface = Room.GetDrawingSurfaceForBackground();
    surface.DrawImage(100, 100, oDoor.Graphic, 40);
    surface.Release();

will draw the *oDoor object's graphic onto the room
background at (100, 100), at `40%` transparency.*

*See Also: , , ,*

### DrawLine 

*(Formerly known as RawDrawLine, which is now obsolete)*

    DrawingSurface.DrawLine(int from_x, int from_y, int to_x, int to_y,
                            optional int thickness)

Draws a line from (FROM\_X, FROM\_Y) to (TO\_X, TO\_Y) in the surface's
current drawing colour.

The *thickness parameter allows you to specify how thick
the line is, the default being 1 pixel.*

**NOTE: The X and Y co-ordinates given are ROOM
co-ordinates, not SCREEN co-ordinates. This means that in a scrolling
room you can draw outside the current visible area.**

    DrawingSurface *surface = Room.GetDrawingSurfaceForBackground();
    surface.DrawingColor = 14;
    surface.DrawLine(0, 0, 160, 100);
    surface.Release();

will draw a line from the left top of the screen (0,0) to the middle of
the screen (160,100);

*See Also: , , ,*

### DrawMessageWrapped 

*(Formerly known as RawPrintMessageWrapped, which is now
obsolete)*

    DrawingSurface.DrawMessageWrapped(int x, int y, int width,
                                      FontType font, int message_number)

Draws the room message MESSAGE\_NUMBER onto the surface at (x,y), using
the specified FONT.

WIDTH is the width of the virtual textbox enclosing the text, and is the
point that the text will wrap at. This command is designed for writing a
long message to the screen with it wrapping normally like a standard
label would do.

The text will be printed using the current drawing colour.

    DrawingSurface *surface = Room.GetDrawingSurfaceForBackground();
    surface.DrawingColor = 14;
    surface.DrawMessageWrapped(80, 40, 160, Game.NormalFont, 10);
    surface.Release();

will display message 10 in the centre of the screen, starting from Y =
40.

*See Also: , ,*

### DrawPixel 

    DrawingSurface.DrawPixel(int x, int y)

Draws a single pixel onto the surface at (X,Y) in the current colour.
The pixel thickness respects the property.

**NOTE: This command is not fast enough to use repeatedly
to build up an image. Only use it for single pixel adjustments.**

    DrawingSurface *surface = Room.GetDrawingSurfaceForBackground();
    surface.DrawingColor = 14;
    surface.DrawPixel(50, 50);
    surface.Release();

draws a yellow pixel in the top left of the room background

*See Also: , , ,*

### DrawRectangle 

*(Formerly known as RawDrawRectangle, which is now
obsolete)*

    DrawingSurface.DrawRectangle(int x1, int y1, int x2, int y2)

Draws a filled rectangle in the current colour with its top-left corner
at (x1,y1) and its bottom right corner at (x2, y2)

**NOTE: The X and Y co-ordinates given are ROOM
co-ordinates, not SCREEN co-ordinates. This means that in a scrolling
room you can draw outside the current visible area.**

    DrawingSurface *surface = Room.GetDrawingSurfaceForBackground();
    surface.DrawingColor = 14;
    surface.DrawRectangle(0, 0, 160, 100);
    surface.Release();

will draw a rectangle over the top left hand quarter of the screen.

*See Also: ,*

### DrawString 

*(Formerly known as RawPrint, which is now obsolete)*

    DrawingSurface.DrawString(int x, int y, FontType font, string text, ...)

Draws the *text onto the surface at (x, y), using the
supplied font number. The text will be drawn in the current drawing
colour.*

You can insert the value of variables into the message. For more
information, see the section.

    DrawingSurface *surface = Room.GetDrawingSurfaceForBackground();
    surface.DrawingColor = 14;
    surface.DrawString(0, 100, Game.NormalFont, "Text written into the background!");
    surface.Release();

will write some text onto the middle-left of the room background

*See Also: , ,*

### DrawStringWrapped 

    DrawingSurface.DrawStringWrapped(int x, int y, int width,
                                     FontType font, Alignment,
                                     const string text)

Draws the *text onto the surface at (x,y), using the
specified FONT.*

*width is the width of the virtual textbox enclosing the
text, and is the point that the text will wrap at. You can use the
*alignment parameter to determine how the text is
horizontally aligned.**

The text will be printed using the current drawing colour.

    DrawingSurface *surface = Room.GetDrawingSurfaceForBackground();
    surface.DrawingColor = 14;
    surface.DrawStringWrapped(80, 40, 160, Game.NormalFont, eAlignCentre, "Hello, my name is Bob.");
    surface.Release();

will display the text in the centre of the screen, starting from Y = 40.

*Compatibility: Supported by **AGS 3.0.1 and
later versions.***

*See Also: , ,*

### DrawSurface 

*(Formerly known as RawDrawFrameTransparent, which is now
obsolete) ILBRK *(Formerly known as RawRestoreScreen, which
is now obsolete)**

    DrawingSurface.DrawSurface(DrawingSurface *source, optional int transparency)

Draws the specified surface on top of this surface, optionally using
*transparency percent transparency.*

This allows you to perform day-to-night fading and other special
effects.

**NOTE: You cannot use the *transparency
parameter with 256-colour surfaces.***

**NOTE: This command can be a bit on the slow side, so
don't call it from repeatedly\_execute.**

**TIP: If you want to gradually fade in a second
background, create a copy of the original surface and then restore it
after each iteration, otherwise the backgrounds will converge too
quickly.**

    DrawingSurface *mainBackground = Room.GetDrawingSurfaceForBackground(0);
    DrawingSurface *nightBackground = Room.GetDrawingSurfaceForBackground(1);
    mainBackground.DrawSurface(nightBackground, 50);
    mainBackground.Release();
    nightBackground.Release();

this will draw background frame 1 onto frame 0 at 50`%` opacity.

*See Also: ,*

### DrawTriangle 

*(Formerly known as RawDrawTriangle, which is now
obsolete)*

    DrawingSurface.DrawTriangle(int x1, int y1, int x2, int y2, int x3, int y3)

Draws a filled triangle in the current colour with corners at the points
(x1,y1), (x2,y2) and (x3,y3).

Well, don't look at me, you might find it useful for something :-)

    DrawingSurface *surface = Room.GetDrawingSurfaceForBackground();
    surface.DrawingColor = 14;
    surface.DrawTriangle(0,0,160,100,0,200);
    surface.Release();

will draw a triangle with corners at the points (0,0),(160,100),(0,200).

*See Also: , ,*

### Release (drawing surface) 

    DrawingSurface.Release()

Tells AGS that you have finished drawing onto this surface, and that AGS
can now upload the changed image into video memory.

After calling this method, you can no longer use the DrawingSurface
instance. To do any further drawing, you need to get the surface again.

    DrawingSurface *surface = Room.GetDrawingSurfaceForBackground();
    surface.DrawingColor = 14;
    surface.DrawLine(0, 0, 50, 50);
    surface.Release();

draws a yellow diagonal line across the top-left of the current room
background, then releases the image.

*See Also: ,*

### DrawingColor property 

*(Formerly known as RawSetColor, which is now obsolete)*

    int DrawingSurface.DrawingColor

Gets/sets the current drawing colour on this surface. Set this before
using commands like , which use this colour for their drawing.

You can set this either to an AGS Colour Number (as you'd get from the
Colours pane in the editor) or to the special constant
COLOR\_TRANSPARENT, which allows you to draw transparent areas onto the
surface.

    DrawingSurface *surface = Room.GetDrawingSurfaceForBackground();
    surface.DrawingColor = 14;
    surface.DrawLine(0, 0, 160, 100);
    surface.DrawingColor = Game.GetColorFromRGB(255, 255, 255);
    surface.DrawLine(0, 199, 160, 100);
    surface.Release();

will draw a yellow line from the left top of the screen (0,0) to the
middle of the screen (160,100), and a white line from the bottom left to
the middle.

*See Also: , , ,*

### GetPixel 

    int DrawingSurface.GetPixel(int x, int y)

Returns the AGS Colour Number of the pixel at (X,Y) on the surface.

**NOTE: In high-colour games, the first 32 colour numbers
have a special meaning due to an AGS feature which maintains
compatibility with 8-bit games. Therefore, if you draw onto the surface
using a blue colour number 0-31 you will get a different number when you
GetPixel – and in fact the colour drawn may not be what you expect. To
get around this, add 1 Red or Green component to adjust the colour
number out of this range.**

**NOTE: This command is relatively slow. Don't use it to
try and process an entire image.**

    DrawingSurface *surface = Room.GetDrawingSurfaceForBackground();
    Display("The colour of the middle pixel is %d.", surface.GetPixel(160, 100));
    surface.Release();

displays the pixel colour of the centre pixel on the screen.

*Compatibility: Supported by **AGS 3.0.1 and
later versions.***

*See Also: , ,*

### Height property (drawing surface) 

    readonly int DrawingSurface.Height

Gets the height of the surface.

    DrawingSurface *surface = Room.GetDrawingSurfaceForBackground();
    Display("The background is %d x %d!", surface.Width, surface.Height);
    surface.Release();

displays the size of the surface to the player

*See Also: ,*

### UseHighResCoordinates property 

    bool DrawingSurface.UseHighResCoordinates

Gets/sets whether you want to use high-resolution co-ordinates with this
surface.

By default, this property will be set such that drawing surface
co-ordinates use the same co-ordinate system as the rest of the game, as
per the “Use low-res co-ordinates in script” game setting. However, if
your game is 640x400 or higher you can customize whether this drawing
surface uses native co-ordinates or the low-res 320x200 co-ordinates by
changing this property.

Setting this property affects **ALL other commands
performed on this drawing surface, including the and properties.**

    DrawingSurface *surface = Room.GetDrawingSurfaceForBackground();
    surface.UseHighResCoordinates = true;
    surface.DrawingColor = 14;
    surface.DrawLine(0, 0, 320, 200);
    surface.Release();

draws a yellow line from the top left of the screen to the middle of the
screen. If we hadn't set *UseHighResCoordinates to true,
this would draw a line from the top left to the bottom right of the
screen.*

*See Also: , , ,*

### Width property (drawing surface) 

    readonly int DrawingSurface.Width

Gets the width of the surface.

    DrawingSurface *surface = Room.GetDrawingSurfaceForBackground();
    Display("The background is %d x %d!", surface.Width, surface.Height);
    surface.Release();

displays the size of the surface to the player

*See Also: ,*

DynamicSprite functions and properties
--------------------------------------

### Create (dynamic sprite) 

    static DynamicSprite* DynamicSprite.Create(int width, int height,
                                               optional bool hasAlphaChannel)

Creates a new blank dynamic sprite of the specified size. It will
initially be fully transparent, and can optionally have an alpha
channel. This command is useful if you just want to create a new sprite
and then use the DrawingSurface commands to draw onto it.

If the game colour depth is lower than 32-bit, then the
*hasAlphaChannel parameter will be ignored.*

Use the property of the DynamicSprite to interface with other commands
and to use the new sprite in the game.

**IMPORTANT: This command loads an extra sprite into memory
which is not controlled by the normal AGS sprite cache and will not be
automatically disposed of. Therefore, when you are finished with the
image you **MUST call Delete on it to free its memory.****

**IMPORTANT: If the DynamicSprite instance is released from
memory (ie. there is no longer a DynamicSprite\* variable pointing to
it), then the sprite will also be removed from memory. Make sure that
you keep a global variable pointer to the sprite until you are finished
with it, and at that point call Delete.**

    DynamicSprite* sprite = DynamicSprite.Create(50, 30);
    DrawingSurface *surface = sprite.GetDrawingSurface();
    surface.DrawingColor = 14;
    surface.DrawPixel(25, 15);
    surface.Release();
    sprite.Delete();

creates a 50x30 sprite, draws a white dot in the middle, then deletes
the sprite.

*See Also: , ,*

### CreateFromBackground 

    static DynamicSprite* DynamicSprite.CreateFromBackground
                          (optional int frame, optional int x, optional int y,
                           optional int width, optional int height)

Creates a new dynamic sprite containing a copy of the specified room
background.

The most basic use of this function is to supply no parameters, in which
case the sprite will contain an exact copy of the current room
background.

If you want, you can supply the *frame only, in which case
you will get a complete copy of that background frame number from the
current room.*

Optionally, you can specify a portion of the background to grab. You
must either supply all or none of the x, y, width and height parameters;
if you do supply them, this allows you to just get a small portion of
the background image into the new sprite. All co-ordinates are in
320x200-resolution room co-ordinates.

Use the property of the DynamicSprite to interface with other commands
and to use the new sprite in the game.

**IMPORTANT: This command loads an extra sprite into memory
which is not controlled by the normal AGS sprite cache and will not be
automatically disposed of. Therefore, when you are finished with the
image you **MUST call Delete on it to free its memory.****

**IMPORTANT: If the DynamicSprite instance is released from
memory (ie. there is no longer a DynamicSprite\* variable pointing to
it), then the sprite will also be removed from memory. Make sure that
you keep a global variable pointer to the sprite until you are finished
with it, and at that point call Delete.**

    DynamicSprite* sprite = DynamicSprite.CreateFromBackground(GetBackgroundFrame(), 130, 70, 60, 60);
    DrawingSurface *surface = Room.GetDrawingSurfaceForBackground();
    surface.DrawImage(0, 0, sprite.Graphic);
    surface.Release();
    sprite.Delete();

creates a copy of the centre 60x60 area on the background, and draws it
onto the top left corner of the background image.

*See Also:*

### CreateFromDrawingSurface 

    static DynamicSprite* DynamicSprite.CreateFromDrawingSurface(
                            DrawingSurface* surface, int x, int y,
                            int width, int height)

Creates a new dynamic sprite containing a copy of the specified portion
of the drawing surface. This allows you to easily create new sprites
from portions of other sprites.

**NOTE: The *x, *y,
*width and *height parameters respect the
DrawingSurface's setting, so make sure that the type of co-ordinates
that you are using match up with what the drawing surface expects.******

Use the property of the DynamicSprite to interface with other commands
and to use the new sprite in the game.

**IMPORTANT: This command loads an extra sprite into memory
which is not controlled by the normal AGS sprite cache and will not be
automatically disposed of. Therefore, when you are finished with the
image you **MUST call Delete on it to free its memory.****

**IMPORTANT: If the DynamicSprite instance is released from
memory (ie. there is no longer a DynamicSprite\* variable pointing to
it), then the sprite will also be removed from memory. Make sure that
you keep a global variable pointer to the sprite until you are finished
with it, and at that point call Delete.**

    DynamicSprite* sprite = DynamicSprite.CreateFromExistingSprite(object[0].Graphic);
    DrawingSurface *surface = sprite.GetDrawingSurface();
    DynamicSprite *newSprite = DynamicSprite.CreateFromDrawingSurface(surface, 0, 0, 10, 10);
    surface.Release();
    sprite.Delete();
    object[0].Graphic = newSprite.Graphic;

changes object 0's image to be just the top-left corner of what it
previously was.

*Compatibility: Supported by **AGS 3.0.2 and
later versions.***

*See Also:*

### CreateFromExistingSprite 

    static DynamicSprite* DynamicSprite.CreateFromExistingSprite(
                            int slot, optional bool preserveAlphaChannel)

Creates a new dynamic sprite containing a copy of the specified sprite
*slot.*

Returns the DynamicSprite instance representing the new sprite. This
function is useful as it effectively allows you to apply transformations
such as resizing to any sprite in the game.

Use the property of the DynamicSprite to interface with other commands
and to use the new sprite in the game.

*preserveAlphaChannel determines whether the sprite's alpha
channel will also be copied across. It is false by default for backwards
compatibility reasons, and is useful because it allows you to strip the
alpha channel in order to do whole image transparency. This parameter
has no effect with sprites that do not have an alpha channel.*

**IMPORTANT: This command loads an extra sprite into memory
which is not controlled by the normal AGS sprite cache and will not be
automatically disposed of. Therefore, when you are finished with the
image you **MUST call Delete on it to free its memory.****

**IMPORTANT: If the DynamicSprite instance is released from
memory (ie. there is no longer a DynamicSprite\* variable pointing to
it), then the sprite will also be removed from memory. Make sure that
you keep a global variable pointer to the sprite until you are finished
with it, and at that point call Delete.**

    DynamicSprite* sprite = DynamicSprite.CreateFromExistingSprite(object[0].Graphic);
    sprite.Resize(20, 20);
    DrawingSurface *surface = Room.GetDrawingSurfaceForBackground();
    surface.DrawImage(100, 80, sprite.Graphic);
    surface.Release();
    sprite.Delete();

creates a copy of object 0's current sprite, resizes it down to 20x20,
and then draws the result onto the background.

*See Also: ,*

### CreateFromFile 

*(Formerly known as LoadImageFile, which is now obsolete)*

    static DynamicSprite* DynamicSprite.CreateFromFile(string filename)

Loads an external image FILENAME into memory as a sprite.

Returns the DynamicSprite instance representing the sprite, or
*null if the image could not be loaded (file not found or
unsupported format).*

Only BMP and PCX files can be loaded with this command.

Use the property of the DynamicSprite to interface with other commands
and to use the new sprite in the game.

**IMPORTANT: This command loads an extra sprite into memory
which is not controlled by the normal AGS sprite cache and will not be
automatically disposed of. Therefore, when you are finished with the
image you **MUST call Delete on it to free its memory.****

**IMPORTANT: If the DynamicSprite instance is released from
memory (ie. there is no longer a DynamicSprite\* variable pointing to
it), then the sprite will also be removed from memory. Make sure that
you keep a global variable pointer to the sprite until you are finished
with it, and at that point call Delete.**

    DynamicSprite* sprite = DynamicSprite.CreateFromFile("CustomAvatar.bmp");
    if (sprite != null) {
      DrawingSurface *surface = Room.GetDrawingSurfaceForBackground();
      surface.DrawImage(100, 80, sprite.Graphic);
      surface.Release();
      sprite.Delete();
    }

will load the file “CustomAvatar.bmp” and if successful draw the image
near the middle of the screen.

Once the image is finished with, Delete should be called on it.

*See Also: ,*

### CreateFromSaveGame 

*(Formerly known as LoadSaveSlotScreenshot, which is now
obsolete)*

    static DynamicSprite* DynamicSprite.CreateFromSaveGame
                            (int saveSlot, int width, int height)

Loads the screenshot for save game SAVESLOT into memory, resizing it to
WIDTH x HEIGHT.

Returns the DynamicSprite instance of the image if successful, or
returns *null if the screenshot could not be loaded
(perhaps the save game didn't include one).*

In order for this to work, the “Save screenshots in save games” option
must be ticked in the main Game Settings pane.

**IMPORTANT: This command loads an extra sprite into memory
which is not controlled by the normal AGS sprite cache and will not be
automatically disposed of. Therefore, when you are finished with the
image you **MUST call Delete on it to free its memory.****

**IMPORTANT: If the DynamicSprite instance is released from
memory (ie. there is no longer a DynamicSprite\* variable pointing to
it), then the sprite will also be removed from memory. Make sure that
you keep a global variable pointer to the sprite until you are finished
with it, and at that point call Delete.**

    // at top of script, outside event functions
    DynamicSprite *buttonSprite;

    // inside an event function
    buttonSprite = DynamicSprite.CreateFromSaveGame(1, 50, 50);
    if (buttonSprite != null) {
      btnScrnshot.NormalGraphic = buttonSprite.Graphic;
    }

will load the screenshot for save game 1 and resize it to 50x50. It then
places it onto the btnScrnshot GUI button.

Once the GUI is disposed of, Delete should be called on the sprite.

*See Also: , , ,*

### CreateFromScreenShot 

    static DynamicSprite* DynamicSprite.CreateFromScreenShot
                            (optional int width, optional int height)

Creates a new DynamicSprite instance with a copy of the current screen
in it, resized to WIDTH x HEIGHT. If you do not supply the width or
height, then a full screen sized sprite will be created.

This command can be useful if you're creating a save game screenshots
GUI, in order to display the current game position as well as the saved
slot positions.

**NOTE: This command can be slow when using the Direct3D
graphics driver.**

**IMPORTANT: This command loads an extra sprite into memory
which is not controlled by the normal AGS sprite cache and will not be
automatically disposed of. Therefore, when you are finished with the
image you **MUST call Delete on it to free its memory.****

**IMPORTANT: If the DynamicSprite instance is released from
memory (ie. there is no longer a DynamicSprite\* variable pointing to
it), then the sprite will also be removed from memory. Make sure that
you keep a global variable pointer to the sprite until you are finished
with it, and at that point call Delete.**

    // at top of script, outside event functions
    DynamicSprite *buttonSprite;

    // inside an event function
    buttonSprite = DynamicSprite.CreateFromScreenShot(80, 50);
    if (buttonSprite != null) {
      btnScrnshot.NormalGraphic = buttonSprite.Graphic;
    }

places a screen grab of the current game session onto btnScrnshot.

Once the GUI is disposed of, Delete should be called on the sprite.

*See Also: , , ,*

### ChangeCanvasSize 

    DynamicSprite.ChangeCanvasSize(int width, int height, int x, int y);

Changes the sprite size to *width x *height,
placing the current image at offset (x, y) within the new canvas. Unlike
the command, the current image is kept at its original size.**

This function allows you to enlarge the sprite background in order to
draw more onto it than its current boundaries allow. It is effectively
the opposite of . The additional surface area will be transparent.

The width and height are specified in 320x200-resolution units.

    DynamicSprite* sprite = DynamicSprite.CreateFromExistingSprite(10);
    sprite.ChangeCanvasSize(sprite.Width + 10, sprite.Height, 5, 0);
    DrawingSurface *surface = sprite.GetDrawingSurface();
    surface.DrawingColor = 14;
    surface.DrawLine(0, 0, 5, surface.Height);
    surface.Release();
    sprite.Delete();

creates a dynamic sprite as a copy of sprite 10, enlarges it by 5 pixels
to the left and right, and draws a line in the new area to the left.

*See Also: , , ,*

### CopyTransparencyMask 

    DynamicSprite.CopyTransparencyMask(int fromSpriteSlot)

Copies the transparency mask from the specified sprite slot onto the
dynamic sprite. The dynamic sprite's transparency and/or alpha channel
will be replaced with the one from the other sprite.

This command is designed for special effects. It is fairly slow since it
involves inspecting each pixel of the image, so it's not recommended
that you use it often.

The source sprite must be the same size and colour depth as the dynamic
sprite.

**NOTE: This command makes all pixels that are transparent
in the source sprite also transparent in the dynamic sprite. It does not
make opaque pixels from the source sprite into opaque pixels on the
dynamic sprite (because it wouldn't know what colour to make them).**

If the source image has an alpha channel, then the dynamic sprite will
have an alpha channel created as a copy of the one from the source
sprite.

    DynamicSprite* sprite = DynamicSprite.CreateFromExistingSprite(10);
    sprite.CopyTransparencyMask(11);
    object[0].Graphic = sprite.Graphic;
    Wait(80);
    sprite.Delete();

creates a dynamic sprite as a copy of sprite 10, changes its
transparency mask to use that of sprite 11, and displays it on object 0.

*See Also:*

### Crop (dynamic sprite) 

    DynamicSprite.Crop(int x, int y, int width, int height);

Crops the sprite down to *width x *height,
starting from (x,y) in the image. The width and height are specified in
320x200-resolution units, as usual.**

This allows you to trim the edges off a sprite, and perform related
tasks. Only the area with its top-left corner as (x,y) and of WIDTH x
HEIGHT in size will remain.

    DynamicSprite* sprite = DynamicSprite.CreateFromFile("CustomAvatar.bmp");
    sprite.Crop(10, 10, sprite.Width - 10, sprite.Height - 10);
    DrawingSurface *surface = Room.GetDrawingSurfaceForBackground();
    surface.DrawImage(100, 100, sprite.Graphic);
    surface.Release();
    sprite.Delete();

will load the CustomAvatar.bmp image, cut off the left and top 10
pixels, and then draw it onto the room background at (100,100).

*See Also: , , ,*

### Delete (dynamic sprite) 

*(Formerly known as DeleteSprite, which is now obsolete)*

    DynamicSprite.Delete();

Deletes the specified dynamic sprite from memory. Use this when you are
no longer displaying the sprite and it can be safely disposed of.

You do not normally need to delete sprites, since the AGS Sprite Cache
manages loading and deleting sprites automatically.

However, when an extra sprite has been loaded into the game (for
example, with the CreateFromFile or CreateFromScreenShot commands) then
AGS does not delete it automatically, and you must call this command
instead.

    DynamicSprite* sprite = DynamicSprite.CreateFromFile("CustomAvatar.bmp");
    object[1].Graphic = sprite.Graphic;
    Wait(200);
    object[1].Graphic = 22;
    sprite.Delete();

will load the file “CustomAvatar.bmp”, change Object 1 to display this
graphic, wait 5 seconds, then change object 1 back to its old sprite 22
and free the new image.

*See Also: ,*

### Flip (dynamic sprite) 

    DynamicSprite.Flip(eFlipDirection);

Flips the dynamic sprite according to the parameter:

*eFlipLeftToRight flips the image from left to right ILBRK
*eFlipUpsideDown flips the image from top to bottom ILBRK
*eFlipBoth flips the image from top to bottom and left to
right***

    DynamicSprite* sprite = DynamicSprite.CreateFromFile("CustomAvatar.bmp");
    sprite.Flip(eFlipUpsideDown);
    DrawingSurface *surface = Room.GetDrawingSurfaceForBackground();
    surface.DrawImage(100, 100, sprite.Graphic);
    surface.Release();
    sprite.Delete();

will load the CustomAvatar.bmp image, flip it upside down, and then draw
it onto the room background at (100,100).

*See Also: , ,*

### GetDrawingSurface (dynamic sprite) 

    DrawingSurface* DynamicSprite.GetDrawingSurface();

Gets the drawing surface for this dynamic sprite, which allows you to
modify the sprite by drawing onto it in various ways.

After calling this method, use the various to modify the sprite, then
call Release on the surface when you are finished.

    DynamicSprite *sprite = DynamicSprite.CreateFromExistingSprite(object[0].Graphic);
    DrawingSurface *surface = sprite.GetDrawingSurface();
    surface.DrawingColor = 13;
    surface.DrawLine(0, 0, 20, 20);
    surface.Release();
    object[0].Graphic = sprite.Graphic;
    Wait(40);
    sprite.Delete();

this creates a dynamic sprite as a copy of Object 0's existing sprite,
draws a pink diagonal line across it, sets this new sprite onto the
object for 1 second and then removes it.

*See Also: , ,*

### Resize (dynamic sprite) 

    DynamicSprite.Resize(int width, int height);

Resizes an existing dynamic sprite to WIDTH x HEIGHT pixels.

The width and height are specified in 320x200-resolution units, as
usual.

**NOTE: Resizing is a relatively slow operation, so do not
attempt to resize sprites every game loop; only do it when necessary.**

    DynamicSprite* sprite = DynamicSprite.CreateFromFile("CustomAvatar.bmp");
    sprite.Resize(sprite.Width * 2, sprite.Height * 2);
    DrawingSurface *surface = Room.GetDrawingSurfaceForBackground();
    surface.DrawImage(100, 100, sprite.Graphic);
    surface.Release();
    sprite.Delete();

will load the CustomAvatar.bmp image, stretch it to double its original
size, and then draw it onto the room background at (100,100).

*See Also: , , , , ,*

### Rotate (dynamic sprite) 

    DynamicSprite.Rotate(int angle, optional int width, optional int height)

Rotates the dynamic sprite by the specified *angle. The
angle is in degrees, and must lie between 1 and 359. The image will be
rotated clockwise by the specified angle.*

Optionally, you can specify the width and height of the rotated image.
By default, AGS will automatically calculate the new size required to
hold the rotated image, but you can override this by passing the
parameters in.

Note that specifying a width/height does not stretch the image, it just
allows you to set the image dimensions to crop the rotation.

**NOTE: Rotating is a relatively slow operation, so do not
attempt to rotate sprites every game loop; only do it when necessary.**

    DynamicSprite* sprite = DynamicSprite.CreateFromFile("CustomAvatar.bmp");
    sprite.Rotate(90);
    DrawingSurface *surface = Room.GetDrawingSurfaceForBackground();
    surface.DrawImage(100, 100, sprite.Graphic);
    surface.Release();
    sprite.Delete();

will load the CustomAvatar.bmp image, rotate it 90 degrees clockwise,
draw the result onto the screen, and then delete the image.

*See Also: , , ,*

### SaveToFile (dynamic sprite) 

    DynamicSprite.SaveToFile(string filename)

Saves the dynamic sprite to the specified file.

The filename you supply must have a .PCX or .BMP extension; they are the
only two file types that the engine supports.

Returns 1 if the sprite was saved successfully, or 0 if it failed.

    DynamicSprite* sprite = DynamicSprite.CreateFromFile("CustomAvatar.bmp");
    sprite.Rotate(90);
    sprite.SaveToFile("RotatedAvatar.bmp");
    sprite.Delete();

will load the CustomAvatar.bmp image, rotate it 90 degrees clockwise,
then save the result back to the disk.

*See Also: ,*

### Tint (dynamic sprite) 

    DynamicSprite.Tint(int red, int green, int blue, int saturation, int luminance)

Tints the dynamic sprite to (RED, GREEN, BLUE) with SATURATION percent
saturation. For the meaning of all the parameters, see .

The tint set by this function is permanent for the dynamic sprite –
after the tint has been set, it is not possible to remove it. If you
call Tint again with different parameters, it will apply the new tint to
the already tinted sprite from the first call.

**NOTE: This function only works with hi-colour sprites.**

    DynamicSprite* sprite = DynamicSprite.CreateFromExistingSprite(object[0].Graphic);
    sprite.Tint(255, 0, 0, 100, 100);
    DrawingSurface *surface = Room.GetDrawingSurfaceForBackground();
    surface.DrawImage(100, 80, sprite.Graphic);
    surface.Release();
    sprite.Delete();

creates a copy of object 0's sprite, tints it red, and draws it onto the
room background.

*See Also: , , ,*

### ColorDepth property (dynamic sprite) 

    readonly int DynamicSprite.ColorDepth;

Gets the colour depth of this dynamic sprite. This can be 8, 16 or 32
and is not necessarily the same as the game colour depth (though this
usually will be the case).

    DynamicSprite* sprite = DynamicSprite.CreateFromFile("CustomAvatar.bmp");
    if (sprite != null) {
      Display("The image is %d x %d pixels, at %d-bit depth.", sprite.Width, sprite.Height, sprite.ColorDepth);
      sprite.Delete();
    }

displays the colour depth of the CustomAvatar.bmp image.

*See Also: ,*

### Graphic property (dynamic sprite) 

    readonly int DynamicSprite.Graphic;

Gets the sprite slot number in which this dynamic sprite is stored. This
value can then be passed to other functions and properties, such as .

    DynamicSprite* ds = DynamicSprite.CreateFromScreenShot(50, 50);
    DrawingSurface *surface = Room.GetDrawingSurfaceForBackground();
    surface.DrawImage(100, 100, ds.Graphic);
    surface.Release();
    ds.Delete();

takes a screen shot, and draws it onto the background scene at
(100,100).

*See Also: ,*

### Height property (dynamic sprite) 

    readonly int DynamicSprite.Height;

Gets the height of this dynamic sprite. The height is always returned in
320x200-resolution units.

    DynamicSprite* sprite = DynamicSprite.CreateFromFile("CustomAvatar.bmp");
    if (sprite != null) {
      Display("The image is %d x %d pixels.", sprite.Width, sprite.Height);
      sprite.Delete();
    }

displays the size of the CustomAvatar.bmp image.

*See Also: ,*

### Width property (dynamic sprite) 

    readonly int DynamicSprite.Width;

Gets the width of this dynamic sprite. The width is always returned in
320x200-resolution units.

    DynamicSprite* sprite = DynamicSprite.CreateFromFile("CustomAvatar.bmp");
    if (sprite != null) {
      Display("The image is %d x %d pixels.", sprite.Width, sprite.Height);
      sprite.Delete();
    }

displays the size of the CustomAvatar.bmp image.

*See Also: ,*

File functions and properties
-----------------------------

### Open 

*(Formerly known as FileOpen, which is now obsolete)*

    static File* File.Open(string filename, FileMode)

Opens a disk file for reading or writing. These disk I/O functions are
only intended for simple tasks like the way the QFG series export the
character when you complete it.

MODE is either eFileRead, eFileWrite or eFileAppend, depending on
whether you want to write to or read from the file. If you pass
eFileWrite and a file called FILENAME already exists, it will be
overwritten.

eFileAppend opens an existing file for writing and starts adding
information at the end (ie. the existing contents are not deleted).

This function returns a File object, which you use to perform operations
on the file. *null is returned if there was a problem (eg.
file not existing when MODE is eFileRead).*

When specifying file path you may use special location tags: ILBRK
`$INSTALLDIR$`, which allows you to explicitly read files in the game
installation directory. ILBRK `$SAVEGAMEDIR$`, which allows you to
write/read files in the save game directory. ILBRK `$APPDATADIR$`, which
allows you to write/read files to a folder on the system which is
accessible by and shared by all users. The example of their use is
below.

**IMPORTANT: For security reasons, if you open the file for
writing, then you can ONLY work with files in either `$SAVEGAMEDIR$` or
`$APPDATADIR$` locations. An attempt to write file in `$INSTALLDIR$`
will result in failure, and *null is returned. An attempt
to write file into relative path without specifying any location tag
will make AGS to automatically remap such path into `$APPDATADIR$`. This
is done for backwards-compatibility. On other hand, if you open file for
writing using an absolute path, or relative path that points to location
outside of game directory, it will automatically be rejected, and
*null is returned.****

**NOTE: You **MUST close the file with the
Close function when you have finished using it. There are only a limited
number of file handles, and forgetting to close the file can lead to
problems later on.****

**NOTE: Open file pointers are not persisted across save
games. That is, if you open a file, then save the game; then when you
restore the game, the File will not be usable and you'll have to open it
again to continue any I/O. The safest practice is not to declare any
global File variables.**

    File *output = File.Open("$SAVEGAMEDIR$/temp.tmp", eFileWrite);
    if (output == null)
      Display("Error opening file.");
    else {
      output.WriteString("test string");
      output.Close();
    }

will open the file temp.tmp in the save game folder for writing. An
error message is displayed if the file could not be created. Otherwise,
it will write the string “test string” to the file and close it.

*See Also: , , ,*

### Close 

*(Formerly known as FileClose, which is now obsolete)*

    File.Close()

Closes the file, and commits all changes to disk. You
**must call this function when you have finished
reading/writing the file.**

    File *output = File.Open("test.dat", eFileWrite);
    output.WriteString("test string");
    output.Close();

will open the file test.dat, write the string “test string”, and close
it.

*See Also:*

### Delete (file) 

    static File.Delete(string filename)

Deletes the specified file from the disk.

For security reasons this command only works with files in the
`$SAVEGAMEDIR$` and `$APPDATADIR$` directories.

**NOTE: This is a static function, therefore you don't need
an open File pointer to use it. See the example below.**

    File.Delete("$APPDATADIR$/temp.tmp");

will delete the file “temp.tmp” from the app data directory, if it
exists.

*Compatibility: Supported by **AGS 3.0.1 and
later versions.***

*See Also: ,*

### Exists 

    static bool File.Exists(string filename)

Checks if the specified file exists on the file system.

When specifying file path you may use special location tags: ILBRK
`$INSTALLDIR$`, which allows you to explicitly read files in the game
installation directory. ILBRK `$SAVEGAMEDIR$`, which allows you to
access files in the save game directory. ILBRK `$APPDATADIR$`, which
allows you to write/read files to a folder on the system which is
accessible by and shared by all users.

**NOTE: This is a static function, therefore you don't need
an open File pointer to use it. See the example below.**

    if (!File.Exists("temp.tmp"))
    {
      File *output = File.Open("temp.tmp", eFileWrite);
      output.WriteString("some text");
      output.Close();
    }

will create the file “temp.tmp” if it doesn't exist

*Compatibility: Supported by **AGS 3.0.1 and
later versions.***

*See Also: ,*

### ReadInt 

*(Formerly known as FileReadInt, which is now obsolete)*

    File.ReadInt()

Reads an integer from the file, and returns it to the script. Only
integers written with File.WriteInt can be read back.

    int number;
    File *input = File.Open("stats.dat", eFileRead);
    number = input.ReadInt();
    input.Close();

will open the file stats.dat, read an integer into number and then close
the file.

*See Also: ,*

### ReadRawChar 

*(Formerly known as FileReadRawChar, which is now
obsolete)*

    File.ReadRawChar()

Reads a raw character from the input file and returns it. This function
allows you to read from files that weren't created by your game, however
it is recommended for expert users only.

    File *input = File.Open("stats.txt", eFileRead);
    String buffer = String.Format("%c", input.ReadRawChar());
    input.Close();

will read a raw character from file stats.txt and writes it to the
string 'buffer'.

*See Also: , ,*

### ReadRawInt 

*(Formerly known as FileReadRawInt, which is now obsolete)*

    File.ReadRawInt()

Reads a raw 32-bit integer from the input file and returns it to the
script. This allows you to read from files created by other programs -
however, it should only be used by experts as no error-checking is
performed.

    int number;
    File *input = File.Open("stats.txt", eFileRead);
    number = input.ReadRawInt();
    input.Close();

will read a raw integer from file stats.txt and put it into the integer
number.

*See Also: ,*

### ReadRawLineBack 

*(Formerly known as File.ReadRawLine, which is now
obsolete)*

    String File.ReadRawLineBack()

Reads a line of text back in from the file and returns it. This enables
you to read in lines from text files and use them in your game.

**NOTE: this command can only read back plain text lines
from text files. If you attempt to use it with binary files or files
written with commands like WriteString, WriteInt, etc then the results
are unpredictable.**

    File *input = File.Open("error.log", eFileRead);
    if (input != null) {
      while (!input.EOF) {
        String line = input.ReadRawLineBack();
        Display("%s", line);
      }
      input.Close();
    }

will display the contents of the 'error.log' file, if it exists

*See Also:*

### ReadStringBack 

*(Formerly known as FileRead, which is now obsolete) ILBRK
*(Formerly known as File.ReadString, which is now
obsolete)**

    String File.ReadStringBack()

Reads a string back in from a file previously opened with File.Open, and
returns it. You should only use this with files which you previously
wrote out with File.WriteString. Do NOT use this function with any other
files, even text files.

    File *input = File.Open("test.dat", eFileRead);
    String buffer = input.ReadStringBack();
    input.Close();

will open the file test.dat (which you have previously written with
File.WriteString) and read a string into the buffer. Then close the
file.

*See Also: ,*

### Seek (file) 

    int Seek(int offset, optional FileSeek origin);

Moves read/write position by *offset bytes related to
*origin. Returns new read/write position. This is usually
used when you are reading file and want to skip over some data, or
writing a file and want to move back and overwrite a piece of data in
the previous section for some reason.**

The *origin is determined by one of the FileSeek types:
eSeekBegin - counts *offset bytes starting from the file's
beginning; *offset must be positive. ILBRK eSeekCurrent -
counts *offset bytes starting from the current position;
*offset may be either positive or negative. ILBRK eSeekEnd
- counts *offset bytes starting from the file's end, going
backwards; *offset must be positive.*******

If optional *origin parameter is not specified,
eSeekCurrent type is used by default.*

**IMPORTANT: Do not use Seek on files which you have
written with safe data writing functions, such as WriteInt and
WriteString. These functions add additional data for the purpose of
protection against incorrect reading, and Seek ignores that protection.
If you use Seek and then try to ReadIntBack, for example, most probably
you will receive a reading error. Only use it on files that contain
“raw” data, or when you know written format precisely.**

    File *input = File.Open("test.dat", eFileRead);
    int first_value = input.ReadRawInt();
    input.Seek(256);
    int second_value = input.ReadRawInt();
    input.Close();

will open the file test.dat, read `first_value`, skip 256 bytes, read
`second_value`, and close the file.

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

*See Also:*

### WriteInt 

*(Formerly known as FileWriteInt, which is now obsolete)*

    File.WriteInt(int value)

Writes VALUE to the file. This allows you to save the contents of
variables to disk. The file must have been previously opened with
File.Open, and you can read the value back later with File.ReadInt.

    int number = 6;
    File *output = File.Open("stats.dat", eFileWrite);
    output.WriteInt(number);
    output.Close();

will open the file stats.dat and write the integer number in it.

*See Also: ,*

### WriteRawChar 

*(Formerly known as FileWriteRawChar, which is now
obsolete)*

    File.WriteRawChar(int value)

Writes a single character to the specified file, in raw mode so that
other applications can read it back. If you are just creating a file for
your game to read back in, use File.WriteInt instead because it offers
additional protection. Only use this function if you need other
applications to be able to read the file in.

This command writes a single byte to the output file - therefore, VALUE
can contain any value from 0 to 255.

    File *output = File.Open("output.txt", eFileWrite);
    output.WriteRawChar('A');
    output.WriteRawChar('B');
    output.WriteRawChar(13);
    output.Close();

will write the text “AB”, followed by a carriage return character, to
the file.

*See Also: ,*

### WriteRawLine 

*(Formerly known as FileWriteRawLine, which is now
obsolete)*

    File.WriteRawLine(string text)

Writes a string of text to the file in plain text format. This enables
you to read it back in Notepad or any text editor. This is useful for
generating logs and such like.

The TEXT will be printed to the file, followed by the standard newline
characters.

    File *output = File.Open("error.log", eFileAppend);
    output.WriteRawLine("There was an error playing sound1.wav");
    output.Close();

will write an error line in the file error.log.

*See Also: ,*

### WriteString 

*(Formerly known as FileWrite, which is now obsolete)*

    File.WriteString(string text)

Writes TEXT to the file, which must have been previously opened with
File.Open for writing. The string is written using a custom format to
the file, which can only be read back by using File.ReadStringBack.

    File *output = File.Open("temp.tmp", eFileWrite);
    if (output == null) Display("Error opening file.");
    else {
      output.WriteString("test string");
      output.Close();
    }

will open the file temp.tmp for writing. If it cannot create the file,
it will display an error message. Otherwise, it will write the string
“test string” and close it.

*See Also: , ,*

### EOF property 

*(Formerly known as FileIsEOF, which is now obsolete)*

    readonly bool File.EOF

Checks whether the specified file has had all its data read. This is
only useful with files opened for **reading. It returns 1
if the entire contents of the file has now been read, or 0 if not.**

    File *output = File.Open("test.dat", eFileRead);
    while (!output.EOF) {
      int temp = output.ReadRawChar();
      Display("%c", temp);
    }
    output.Close();

will display every character in the file test.dat, one by one, to the
screen.

*See Also: , ,*

### Error property 

*(Formerly known as FileIsError, which is now obsolete)*

    readonly bool File.Error

Checks whether an error has occurred reading from or writing to the
specified file.

An error can occur if, for example, you run out of disk space or the
user removes the disk that is being read from.

This function only checks for errors while actually reading/writing
data. The File.Open function will return null if there was an error
actually opening or creating the file.

To find out whether all data has been read from a file, use instead.

    File *output = File.Open("test.dat", eFileWrite);
    output.WriteInt(51);
    if (output.Error) {
      Display("Error writing the data!");
    }
    output.Close();

will write a number to the file 'test.dat', and display a message if
there was a problem.

*See Also: ,*

### Position property (file) 

    readonly int File.Position

Gets current File's reading or writing position. This value means number
of bytes between file's beginning and current place you are reading from
or writing to.

This may be useful, for example, if you are passing the file pointer to
another script module function and want to know how much data that
function has read or written.

    File *output = File.Open("test.dat", eFileWrite);
    int old_pos = output.Position;
    WriteCustomModuleData(output);
    int new_pos = output.Position;
    Display("Custom module has written %d bytes", new_pos - old_pos);
    output.Close();

will open file, pass the file pointer to some custom function, then
display amount of data that function wrote.

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

*See Also:*

Game / Global functions 
-----------------------

### AbortGame 

    AbortGame(string message, ...)

Aborts the game and returns to the operating system.

The standard AGS error dialog is displayed, with the script line numbers
and call stack, along with *message (which can include `%d`
and `%s` Display-style tokens).*

You can use this function rather than QuitGame if you are writing some
debugging checks into your script, to make sure that the user calls your
functions in the correct way.

This command should ideally never be called in the final release of a
game.

    function MakeWider(int newWidth) {
      if (newWidth < 10)
        AbortGame("newWidth expects a width of at least 10!");
    }

will abort the game if MakeWider is called with a parameter less than
10.

SeeAlso:

### CallRoomScript 

    CallRoomScript (int value)

Calls the `on_call` function in the current room script. This is useful
for things like the text parser, where you want to check for general
game sentences, and then ask the current room if the sentence was
relevant to it.

The on\_call function will be called in the current room script, with
its `value` parameter having the value you pass here. This allows it to
distinguish between different tasks, and saves you having to use a
GlobalInt to tell it what to do.

If the current room has no on\_call function, nothing will happen. No
error will occur.

You write the on\_call function into the room script (“Edit script”
button on Room Settings pane), similar to the way you do dialog\_request
in the global script:

    function on_call (int value) {
      if (value == 1) {
        // Check text input
        if (Parser.Said("get apple"))
          Display("No, leave the tree alone.");
      }
    }

The function doesn't get called immediately; instead, the engine will
run it in due course, probably during the next game loop, so you can't
use any values set by it immediately.

Once the on\_call function has executed (or not if there isn't one), the
game.roomscript\_finished variable will be set to 1, so you can check
for that in your repeatedly\_execute script if you need to do something
afterwards.

SeeAlso:

### ChangeTranslation 

    static bool Game.ChangeTranslation(string newTranslationName)

Changes the active translation to *newTranslationName. This
must be the file name without the extension, for example “French” or
“Spanish”. It can also be a blank string, in which case the current
translation will be switched off and the game will revert to the default
language.*

Returns *true if the translation was changed successfully,
or *false if there was a problem (for example, you
specified an invalid translation).**

**NOTE: This is a static function, and thus need to be
called with `Game.` in front of it. See the example below.**

    if (Game.ChangeTranslation("Spanish") == true)
    {
      Display("Changed the translation to Spanish!");
    }
    else
    {
      Display("Unable to change the translation");
    }

will attempt to change the translation to Spanish

*Compatibility: Supported by **AGS 3.1.0 and
later versions.***

*See Also: ,*

### ClaimEvent 

    ClaimEvent()

This command is used in a room script or script module's
*on\_key\_press or *on\_mouse\_click function,
and it tells AGS not to run the global script afterwards.**

For example, if your room script responds to the player pressing the
space bar, and you don't want the global script's on\_key\_press to
handle it as well, then use this command.

This is useful if you have for example a mini-game in the room, and you
want to use some keys for a different purpose to what they normally do.

The normal order in which scripts are called for
*on\_key\_press and *on\_mouse\_click is as
follows:**

-   room script

-   script modules, in order

-   global script

If any of these scripts calls ClaimEvent, then the chain is aborted at
that point.

    if (keycode == ' ') {
      Display("You pressed space in this room!");
      ClaimEvent();
    }

prevents the global script on\_key\_press from running if the player
pressed the space bar.

SeeAlso:

### Debug 

    Debug (int command, int data)

This function provides all the debug services in the system. It performs
various different tasks, depending on the value of the COMMAND
parameter. If debug mode is off, then this function does nothing. This
allows you to leave your script unaltered when you distribute your game,
so you just have to turn off debug mode in the AGS Editor.

The DATA parameter depends on the command - pass 0 if it is not used.
All the valid values for the COMMAND parameter are listed below along
with what they do:

    0   All inventory - gives the current player character one of every
        inventory item. This is useful for testing so that you don't have to
        go and pick up items every time you test part of the game where they
        are required.
    1   Display interpreter version - the engine will display its version
        number and build date.
    2   Walkable from here - fills in the parts of the screen where the player
        can walk from their current location. This is useful if you think the
        path-finder is not working properly. All walkable areas are drawn in
        their respective colours, but with blocking areas at characters feet
        removed.
    3   Teleport - displays a dialog box asking for what room you want to go
        to, and then calls ChangeRoom to teleport you there. Useful for skipping
        parts of the game or going to a specific point to test something.
    4   Show FPS - toggles whether the current frames per second is displayed
        on the screen. Pass DATA as 1 to turn this on, 0 to turn it off.

*See Also: ,*

### DeleteSaveSlot 

    DeleteSaveSlot (int slot)

Deletes the save game in save slot number SLOT.

NOTE: if you specify one of the standard slots (1-50), then AGS will
rearrange the other save games to make sure there is a sequence of slots
from 1 upwards. Therefore, you will need to refresh any save game lists
you have after calling this function.

    DeleteSaveSlot (130);

deletes save game slot 130 (which we should have saved earlier).

*See Also: ,*

### DisableInterface 

    DisableInterface ()

Disables the player interface. This works the same way as it is disabled
while an animation is running: the mouse cursor is changed to the Wait
cursor, and mouse clicks will not be sent through to the
“on\_mouse\_click” function. Also, all interface buttons will be
disabled.

**NOTE: AGS keeps a count of the number of times
DisableInterface is called. Every call to DisableInterface must be
matched by a later call to EnableInterface, otherwise the interface will
get permanently disabled.**

    DisableInterface();

will disable the user's interface.

*See Also: ,*

### DoOnceOnly 

    static bool Game.DoOnceOnly(const string token)

This function gives you an easy way of making some code run only the
first time that the player encounters it. It is commonly used for
awarding points.

The *token parameter is an arbitrary string. You can pass
whatever you like in for this, but **IT MUST BE UNIQUE. It
is this string that allows AGS to determine whether this section of code
has been run before, therefore you should make sure that **you do
not use the same token string in two different places in your
game.*****

Returns *true the first time that it is called with this
token, and *false thereafter.**

**NOTE: This is a static function, and thus need to be
called with `Game.` in front of it. See the example below.**

    if (Game.DoOnceOnly("open cupboard")) {
      GiveScore(5);
    }

will give the player 5 points the first time this script is run.

*See Also:*

### EnableInterface 

    EnableInterface ()

Re-enables the player interface, which was previously disabled with the
DisableInterface function. Everything which was disabled is returned to
normal.

    EnableInterface();

will enable the user's interface.

*See Also: ,*

### EndCutscene 

    EndCutscene()

Marks the end of a cutscene. If the player skips the cutscene, the game
will fast-forward to this point. This function returns 0 if the player
watched the cutscene, or 1 if they skipped it.

*See Also: , ,*

### GetColorFromRGB 

*(Formerly known as RawSetColorRGB, which is now obsolete)*

    static int Game.GetColorFromRGB(int red, int green, int blue)

Gets the AGS Colour Number for the specified RGB colour. The red, green
and blue components are values from 0 to 255. This function gives you a
run-time equivalent to the Colour Finder in the editor.

This command is slow in 256-colour games, since the palette has to be
scanned to find the nearest matching colour.

**NOTE: This is a static function, and thus need to be
called with `Game.` in front of it. See the example below.**

    DrawingSurface *surface = Room.GetDrawingSurfaceForBackground();
    surface.DrawingColor = Game.GetColorFromRGB(0, 255, 0);
    surface.DrawLine(0, 0, 50, 50);
    surface.Release();

will draw a bright green line onto the room background

*See Also:*

### GetFrameCountForLoop 

*(Formerly part of GetGameParameter, which is now
obsolete)*

    static int Game.GetFrameCountForLoop(int view, int loop)

Returns the number of frames in the specified loop of the specified
view.

**NOTE: This is a static function, and thus need to be
called with `Game.` in front of it. See the example for more.**

    int frameCount = Game.GetFrameCountForLoop(SWIMMING, 2);
    Display("Loop 2 in SWIMMING view has %d frames.", frameCount);

*See Also: , ,*

### GetGameOption 

    GetGameOption (option)

Gets the current setting of one of the game options, originally set in
the AGS Editor Game Settings pane.

OPTION specifies which option to get, and its current value is returned.

The valid values for OPTION are listed in .

    if (GetGameOption(OPT_PIXELPERFECT) == 1) {
      Display("pixel-perfect click deteciton is on!");
    }

*See Also:*

### GetGameParameter 

The *GetGameParameter function is now obsolete.*

It has been replaced with the following functions and properties:

(was GP\_SPRITEWIDTH) ILBRK (was GP\_SPRITEHEIGHT) ILBRK (was
GP\_NUMLOOPS) ILBRK (was GP\_NUMFRAMES) ILBRK (was GP\_ISRUNNEXTLOOP)
ILBRK (was GP\_FRAMExxx, GP\_ISFRAMEFLIPPED) ILBRK (was GP\_NUMGUIS)
ILBRK (was GP\_NUMOBJECTS) ILBRK (was GP\_NUMCHARACTERS) ILBRK (was
GP\_NUMINVITEMS)

### GetGameSpeed 

    GetGameSpeed ()

Returns the current game speed (number of cycles per second).

    if (GetGameSpeed() > 40) {
      SetGameSpeed(40);
    }

will always keep the game speed at 40 cycles per second (in case the
user has raised it )

*See Also:*

### GetGlobalInt 

    GetGlobalInt (int index)

Returns the value of global int INDEX.

**NOTE: GlobalInts are now considered obsolete. Consider
using instead, which allow you to name the variables.**

    if (GetGlobalInt(20) == 1) {
      // code here
    }

will execute the code only if Global Integer 20 is 1.

*See Also: ,*

### GetGraphicalVariable 

    GetGraphicalVariable (string variable_name);

Returns the value of the interaction editor VARIABLE\_NAME variable.
This allows your script to access the values of variables set in the
interaction editor.

**NOTE: This command is obsolete, and is only provided for
backwards compatibility with AGS 2.x. When writing new code, use
instead.**

    if (GetGraphicalVariable("climbed rock")==1)
       { code here }

will execute the code only if interaction variable “climbed rock” is 1.

*See Also: ,*

### GetLocationName 

*(Formerly known as global function GetLocationName, which is now
obsolete)*

    static String Game.GetLocationName(int x, int y)

Returns the name of whatever is on the screen at (X,Y). This allows you
to create the Lucasarts-style status lines reading “Look at xxx” as the
player moves the cursor over them.

**NOTE: Unlike Room.ProcessClick, this function actually
works on what the player can see on the screen - therefore, if the
co-ordinates are on a GUI, a blank string is returned.**

**NOTE: The co-ordinates are SCREEN co-ordinates, NOT ROOM
co-ordinates. This means that with a scrolling room, the co-ordinates
you pass are relative to the screen's current position, and NOT absolute
room co-ordinates. This means that this function is suitable for use
with the mouse cursor position variables.**

    String location = Game.GetLocationName(mouse.x, mouse.y);

will get the name of whatever the mouse is over into the string
variable.

*See Also: , , ,*

### GetLocationType 

    GetLocationType(int x, int y)

Returns what type of thing is at location (X,Y); whether it is a
character, object, hotspot or nothing at all. This may be useful if you
want to process a mouse click differently depending on what the player
clicks on.

**NOTE: The co-ordinates are screen co-ordinates, NOT room
co-ordinates. See description of GetLocationName for more info.**

The value returned is one of the following:

    eLocationNothing    nothing, GUI or inventory
    eLocationHotspot    a hotspot
    eLocationCharacter  a character
    eLocationObject     an object

    if (GetLocationType(mouse.x,mouse.y) == eLocationCharacter)
        mouse.Mode = eModeTalk;

will set the cursor mode to talk if the cursor is over a character.

*See Also: , ,*

### GetLoopCountForView 

*(Formerly part of GetGameParameter, which is now
obsolete)*

    static int Game.GetLoopCountForView(int view)

Returns the number of loops in the specified view.

**NOTE: This is a static function, and thus need to be
called with `Game.` in front of it. See the example for more.**

    int loops = Game.GetLoopCountForView(SWIMMING);
    Display("The SWIMMING view (view %d) has %d loops.", SWIMMING, loops);

*See Also: , ,*

### GetRunNextSettingForLoop 

*(Formerly part of GetGameParameter, which is now
obsolete)*

    static bool Game.GetRunNextSettingForLoop(int view, int loop)

Returns whether the specified loop in the specified view has the “Run
the next loop after this one” option checked.

**NOTE: This is a static function, and thus need to be
called with `Game.` in front of it. See the example for more.**

    if (Game.GetRunNextSettingForLoop(SWIMMING, 5) == true) {
      Display("Loop 5 in view SWIMMING does have Run Next Loop set.");
    }
    else {
      Display("Loop 5 in view SWIMMING does not have Run Next Loop set.");
    }

*See Also: , ,*

### GetSaveSlotDescription 

*(Formerly known as global function GetSaveSlotDescription, which
is now obsolete)*

    static String Game.GetSaveSlotDescription(int slot)

Gets the text description of save game slot SLOT.

If the slot number provided does not exist, returns *null.*

    String description = Game.GetSaveSlotDescription(10);

will get the description of save slot 10 into the variable.

*See Also: , ,*

### GetTextHeight 

    GetTextHeight(string text, FontType font, int width)

Calculates the height on the screen that drawing TEXT in FONT within an
area of WIDTH would take up.

This allows you to work out how tall a message displayed with a command
like will be. WIDTH is the width of the area in which the text will be
displayed.

The height is returned in normal 320-resolution pixels, so it can be
used with the screen display commands.

    int height = GetTextHeight("The message on the GUI!", Game.NormalFont, 100);
    gBottomLine.SetPosition(0, 200 - height);

will move the BOTTOMLINE GUI so that it can display the text within the
screen.

*See Also: ,*

### GetTextWidth 

    GetTextWidth(string text, FontType font)

Returns the width on the screen that drawing TEXT in FONT on one line
would take up.

This could be useful if you manually need to centre or right-align some
text, for example with the raw drawing routines.

The width is returned in normal 320-resolution pixels, so it can be used
with the screen display commands.

    DrawingSurface *surface = Room.GetDrawingSurfaceForBackground();
    surface.DrawingColor = 14;
    int width = GetTextWidth("Hello!", Game.NormalFont);
    surface.DrawString(160 - (width / 2), 100, Game.NormalFont, "Hello!");
    surface.Release();

will print “Hello!” onto the middle of the background scene.

*See Also: ,*

### GetTranslation 

    String GetTranslation(string original)

Gets the translated equivalent of the supplied string. You do not
normally need to use this since the game translates most things for you.
However, if you have used an InputBox or other form of user input, and
want to compare the user's input to a particular string, it cannot be
translated automatically. So, you can do this instead.

    String buffer = Game.InputBox("Enter the password:");
    if (buffer.CompareTo(GetTranslation("secret")) == 0) {
      // it matched the current translation of "secret"
    }

If there is no translation for the supplied string, it will be returned
unchanged, so it is always safe to use this function.

*See Also:*

### GetViewFrame 

*(Formerly part of GetGameParameter, which is now
obsolete)*

    static ViewFrame* Game.GetViewFrame(int view, int loop, int frame)

Returns a *ViewFrame instance for the specified frame in
the specified loop of the specified view.*

This instance allows you to query properties of the frame itself, such
as its graphic, its frame-linked sound setting, and so forth.

**NOTE: This is a static function, and thus need to be
called with `Game.` in front of it. See the example for more.**

    ViewFrame *frame = Game.GetViewFrame(SWIMMING, 2, 3);
    Display("Frame 3 in loop 2 of view SWIMMING has sprite slot %d.", frame.Graphic);

*See Also: , , , ,*

### GiveScore 

    GiveScore (int score)

Adds SCORE to the player's score. This is preferable to directly
modifying the variable since it will play the score sound, update any
status lines and call the GOT\_SCORE on\_event function.

Note that SCORE can be negative, in which case the score sound is NOT
played.

    GiveScore(5);

will give 5 points to the player.

*See Also:*

### InputBox 

*(Formerly known as global function InputBox, which is now
obsolete)*

    static String Game.InputBox(string prompt)

Pops up a window asking the user to type in a string, with PROMPT as the
text in the window. Whatever they type in will be returned from this
function.

This command displays a very basic input box, mainly useful for
debugging purposes. Due to the size of the window, only small strings up
to about 20 characters can be typed in.

The recommended way to obtain user input is to create your own GUI with
a text box on it, which allows you full customization of the look of the
window.

**TIP: If you add a '!' character to the start of the
prompt, then a Cancel button will be available in the input box. If the
player presses this Cancel button (or the ESC key), a blank string is
returned.**

    String name = Game.InputBox("!What is your name?");

will prompt the user for his name and store it in the string NAME. If
the user presses Cancel, the NAME string will be blank.

*See Also:*

### InventoryScreen 

    InventoryScreen ()

This command is obsolete.

**This command was used for displaying a default inventory window
in previous versions of AGS, but is no longer supported.**

Instead of using this command, you should create your own Inventory GUI.
The Default Game template comes with an example.

### IsGamePaused 

    IsGamePaused ()

Returns *true if the game is currently paused, or
*false otherwise. The game is paused when either the icon
bar interface has been popped up, or a “script-only” interface has been
displayed with GUI.Visible=true. While the game is paused, no animations
or other updates take place.**

    if (IsGamePaused()) UnPauseGame();

will unpause the game if it's paused.

*See Also:*

### IsInterfaceEnabled 

    IsInterfaceEnabled()

Returns 1 if the player interface is currently enabled, 0 if it is
disabled. The user interface is disabled while the cursor is set to the
Wait cursor - ie. while the character is performing a blocking Walk, or
other blocking action.

    if (IsInterfaceEnabled())
        DisableInterface();

will disable the user interface if it's enabled.

*See Also: ,*

### IsInteractionAvailable 

    IsInteractionAvailable (int x, int y, int mode)

Checks whether there is an interaction defined for clicking on the
screen at (X,Y) in cursor mode MODE.

This function is very similar to Room.ProcessClick, except that rather
than carry out any interactions it encounters, it simply returns 1 if
something would have happened, or 0 if unhandled\_event would have been
run.

This is useful for enabling options on a verb-coin style GUI, for
example.

    if (IsInteractionAvailable(mouse.x,mouse.y, eModeLookat) == 0)
      Display("looking here would not do anything.");

*See Also: , , , ,*

### IsKeyPressed 

    IsKeyPressed(eKeyCode)

Tests whether the supplied key on the keyboard is currently pressed down
or not. You could use this to move an object while the player holds an
arrow key down, for instance.

KEYCODE is one of the , with some limitations: since it tests the raw
state of the key, you CANNOT pass the Ctrl+(A-Z) or Alt+(A-Z) codes
(since they are key combinations). You can, however, use some extra
codes which are listed at the bottom of the section.

Returns 1 if the key is currently pressed, 0 if not.

**NOTE: The numeric keypad can have inconsistent keycodes
between IsKeyPressed and on\_key\_press. With IsKeyPressed, the numeric
keypad always uses keycodes in the 370-381 range. on\_key\_press,
however, passes different values if Num Lock is on since the key presses
are interpreted as the number key rather than the arrow key.**

    if (IsKeyPressed(eKeyUpArrow) == 1)
      cEgo.Walk(cEgo.x, cEgo.y+3);

will move the character EGO upwards 3 pixels when the up arrow is
pressed.

*See Also:*

### IsPluginLoaded 

    static bool Game.IsPluginLoaded(const string name)

Checks whether the plugin of the given *name was present
and loaded for the game.*

**IMPORTANT: If the plugin exports its own script functions
that you used in your game script, and not found when the game is
launched, then the game won't start up at all, exiting with error.
IsPluginLoaded may therefore be useful to check for plugins that are not
interacted with from game script, but just run on their own.**

    if (Game.IsPluginLoaded("my_plugin")) {
      Display("My plugin is found and running!");
    }

will display a message if plugin is present.

### IsTimerExpired 

    bool IsTimerExpired(int timer_id)

Checks whether the timer TIMER\_ID has expired. If the timeout set with
SetTimer has elapsed, returns *true. Otherwise, returns
*false.**

Note that this function will only return *true once - after
that, the timer is placed into an OFF state where it will always return
*false until restarted.**

    if (IsTimerExpired(1)) {
      Display("Timer 1 expired");
    }

will display a message when timer 1 expires.

*See Also:*

### IsTranslationAvailable 

    IsTranslationAvailable ()

Finds out whether the player is using a game translation or not.

Returns 1 if a translation is in use, 0 if not.

*See Also: , ,*

### MoveCharacterToHotspot 

**This function is now obsolete. Use Character.Walk
instead**

    MoveCharacterToHotspot (CHARID, int hotspot)

Moves the character CHARID from its current location to the walk-to
point for the specified hotspot. If the hotspot has no walk-to point,
nothing happens.

This is a blocking call - control is not returned to the script until
the character has reached its destination.

    MoveCharacterToHotspot(EGO,6);

will move the character EGO to the hotspot's 6 “walk to point”.

*See Also: , , ,*

### MoveCharacterToObject 

**This function is now obsolete. Use Character.Walk
instead**

    MoveCharacterToObject (CHARID, int object)

Moves the character CHARID from its current location to a position just
below the object OBJECT. This is useful for example, if you want the man
to pick up an object. This is a blocking call - control is not returned
to the script until the character has reached its destination.

    MoveCharacterToObject (EGO, 0);
    object[0].Visible = false;

Will move the character EGO below object number 0, then turn off object
0.

*See Also: ,*

### PauseGame 

    PauseGame ()

Stops AGS processing character movement and animations. This has the
same effect on the game as happens when a modal GUI is popped up. Game
processing will not resume until you call the UnPauseGame function.

**NOTE: When the game is paused, game cycles will continue
to run but no animations or movement will be performed, and timers will
not count down. Apart from that, your scripts will continue to run as
normal.**

**NOTE: GUI button animations will not be paused by this
command, so that you can run animations on a pop-up GUI while the rest
of the game is paused.**

    if (IsKeyPressed(32)==1) PauseGame();

will pause the game if the player presses the space bar

*See Also:*

### QuitGame 

    QuitGame(int ask_first)

Exits the game and returns to the operating system.

If ASK\_FIRST is zero, it will exit immediately. If ASK\_FIRST is not
zero, it will first display a message box asking the user if they are
sure they want to quit.

    QuitGame(0);

will quit the game without asking the player to confirm.

*See Also:*

### Random 

    Random (int max)

Returns a random number between 0 and MAX. This could be useful to do
various effects in your game. MAX must be a positive value in range
0-32767.

**NOTE: Because of the way Random is implemented in AGS,
the return value will never be higher than 32767.**

**NOTE: The range returned is inclusive - ie. if you do
Random(3); then it can return 0, 1, 2 or 3.**

    int ran=Random(2);
    if (ran==0) cEgo.ChangeRoom(1);
    else if (ran==1) cEgo.ChangeRoom(2);
    else cEgo.ChangeRoom(3);

will change the current room to room 1,2 or 3 depending on a random
result.

### RestartGame 

    RestartGame ()

Restarts the game from the beginning.

    if (IsKeyPressed(365) == 1) RestartGame();

will restart the game if the player presses the F7 key.

*SeeAlso:*

### RestoreGameDialog 

    RestoreGameDialog ()

Displays the restore game dialog, where the player can select a
previously saved game position to restore.

The dialog is not displayed immediately; instead, it will be displayed
when the script function finishes executing.

    if (IsKeyPressed(363) == 1) RestoreGameDialog();

will bring up the restore game dialog if the player presses the F5 key.

*See Also: ,*

### RestoreGameSlot 

    RestoreGameSlot (int slot)

Restores the game position saved into slot number SLOT. You might want
to use these specific slot functions if for example you only want to
allow the player to have one save game position rather than the usual
20. If this slot number does not exist, an error message is displayed to
the player but the game continues. To avoid the error, use the
GetSaveSlotDescription function to see if the position exists before
restoring it.

**NOTE: The game will not be restored immediately; instead,
it will be restored when the script function finishes executing.**

    RestoreGameSlot(30);

will restore game slot 30 if this slot number exists.

*See Also: , ,*

### RunAGSGame 

    RunAGSGame (string filename, int mode, int data)

Quits the current game, and loads up FILENAME instead. FILENAME must be
an AGS game EXE or AC2GAME.AGS file, and it must be in the current
directory.

MODE specifies various options about how you want to run the game.
Currently the supported values are:

    0   Current game is completely exited, new game runs as if it had been launched separately
    1   GlobalInt values are preserved and are not set to 0 for the new game.

DATA allows you to pass an integer through to the next game. The value
you pass here will be accessible to the loaded game by it reading the
game.previous\_game\_data variable.

The save game slots are shared between the two games, and if you load a
save slot that was saved in the other game, it will automatically be
loaded.

Bear in mind that because the games must be in the same folder, they
will also share the audio.vox, speech.vox and so forth. This is a
limitation of this command.

**NOTE: The game you run will be loaded at the same
resolution and colour depth as the current game; if you mismatch colour
depths some nasty results will occur.**

**NOTE: Make sure that the game you want to run has a
filename of 8 characters or less, or this command will fail in the DOS
engine.**

**NOTE: The game you want to launch must have been created
with the same point-version of AGS as the one you are launching it from.
(version 2.xy - the X must be the same version between the two games).**

    RunAGSGame ("MyGame.exe", 0, 51);

will run the MyGame game, passing it the value 51.

### SaveGameDialog 

    SaveGameDialog ()

Displays the save game dialog, where the player can save their current
game position. If they select to save, then the game position will be
saved.

**NOTE: The dialog will not be displayed immediately;
instead, it will be shown when the script function finishes executing.**

    if (keycode == 361) SaveGameDialog();

will bring up the save game dialog if the player presses the F3 key.

*See Also: ,*

### SaveGameSlot 

    SaveGameSlot (int slot, string description)

Saves the current game position to the save game number specified by
SLOT, using DESCRIPTION as the textual description of the save position.
Be careful using this function, because you could overwrite one of the
player's save slots if you aren't careful.

The SaveGameDialog function uses slots numbered from 1 to 20, so if you
don't want to interfere with the player's saves, I would recommend
saving to slot numbers of 100 and above.

**NOTE: The game will not be saved immediately; instead, it
will be saved when the script function finishes executing.**

    SaveGameSlot(30, "save game");

will save the current game position to slot 30 with the description
“Save game”.

*See Also: , ,*

### SaveScreenShot 

    SaveScreenShot (string filename)

Takes a screen capture and saves it to disk. The FILENAME must end in
either “.BMP” or “.PCX”, as those are the types of files which can be
saved. Returns 1 if the shot was successfully saved, or 0 if an invalid
file extension was provided.

**NOTE: The screenshot will be saved to the Saved Games
folder.**

**NOTE: This command can be slow when using the Direct3D
graphics driver.**

    String input = Game.InputBox("Type the filename:");
    input = input.Append(".pcx");
    SaveScreenShot(input);

will prompt the player for a filename and then save the screenshot with
the filename the player typed.

*See Also:*

### SetAmbientLightLevel 

    void SetAmbientTint(int light_level);

Sets an ambient light level that affects all objects and characters in
the room.

The light level is from **-100 to 100, where 0 means that
no adjustment will be applied to sprites.**

In 8-bit games you cannot use positive light level for brightening
effect, but you may still use negative values to produce darkening
effect.

To turn light level off, call this command again but pass the
*light\_level as 0.*

**NOTE: This function overrides any specific region light
levels or tints on the screen, but does NOT override individual
character and object light levels.**

**NOTE: Setting an ambient light level will disable ambient
RGB tint, if there one was previously set.**

    SetAmbientLightLevel(50);

will apply light level 50 to every character and object on screen (which
do not have individual light levels).

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

*See Also: , , ,*

### SetAmbientTint 

    SetAmbientTint(int red, int green, int blue, int saturation, int luminance)

Tints all objects and characters on the screen to (RED, GREEN, BLUE)
with SATURATION percent saturation.

This allows you to apply a global tint to everything on the screen. The
RED, GREEN and BLUE parameters are from 0-255, and specify the colour of
the tint.

The SATURATION parameter defines how much the tint is applied, and is
from 0-100. A saturation of 100 will completely re-colourize the sprites
to the supplied colour, and a saturation of 1 will give them a very
minor tint towards the specified colour.

The LUMINANCE parameter allows you to adjust the brightness of the
sprites at the same time. It ranges from 0-100. Passing 100 will draw
the sprites at normal brightness. Lower numbers will darken the images
accordingly, right down to 0 which will draw everything black.

The tint applied by this function is global. To turn it off, call this
command again but pass the saturation as 0.

**NOTE: This function only works in hi-colour games and
with hi-colour sprites.**

**NOTE: This function overrides any specific region light
levels or tints on the screen.**

    SetAmbientTint(0, 0, 250, 30, 100);

will tint everything on the screen with a hint of blue.

*See Also: , , ,*

### SetGameOption 

    SetGameOption (option, int value)

Changes one of the game options, originally set in the AGS Editor Game
Settings pane.

OPTION specifies which option to change, and VALUE is its new value.
Valid OPTIONs are listed below:

|l|l|

The game settings which are not listed here either have a separate
command to change them (such as Speech.Style), or simply cannot be
changed at run-time.

This command returns the old value of the setting.

    SetGameOption (OPT_PIXELPERFECT, 0);

will disable pixel-perfect click detection.

*See Also: , ,*

### SetGameSpeed 


    SetGameSpeed (int new_speed)

Sets the maximum game frame rate to NEW\_SPEED frames per second, or as
near as possible to that speed. The default frame rate is 40 fps, but
you can speed up or slow down the game by using this function. Note that
this speed is also the rate at which the Repeatedly\_Execute functions
are triggered.

The NEW\_SPEED must lie between 10 and 1000. If it does not, it will be
rounded to 10 or 1000. Note that if you set a speed which the player's
computer cannot handle (for example, a 486 will not be able to manage 80
fps), then it will go as fast as possible.

NOTE: Because the mouse cursor is repainted at the game frame rate, at
very low speeds, like 10 to 20 fps, the mouse will appear to be jumpy
and not very responsive.

NOTE: If you set the property to *true, the game speed will
be capped at the screen's refresh rate, so you will be unable to set it
higher than 60-85 (depending on the player's screen refresh).*

    SetGameSpeed(80);

will set the game speed to 80.

*See Also:*

### SetGlobalInt 

    SetGlobalInt (int index, int value)

Sets the global int INDEX to VALUE. You can then retrieve this value
from any other script using GetGlobalInt.

There are 500 available global variables, from index 0 to 499.

**NOTE: GlobalInts are now considered obsolete. Consider
using instead, which allow you to name the variables.**

    SetGlobalInt(10,1);

will set the Global Integer 10 to 1.

*See Also:*

### SetGraphicalVariable 

    SetGraphicalVariable(string variable_name, int value);

Sets the interaction editor VARIABLE\_NAME variable to VALUE. This
allows your script to change the values of variables set in the
interaction editor.

**NOTE: This command is obsolete, and is only provided for
backwards compatibility with AGS 2.x. When writing new code, use
instead.**

    SetGraphicalVariable("climbed rock", 1);

will set the interaction editor “climbed rock” variable to 1.

*See Also:*

### SetMultitaskingMode 

    SetMultitaskingMode (int mode)

Allows you to set what happens when the user switches away from your
game.

If MODE is 0 (the default), then if the user Alt+Tabs out of your game,
or clicks on another window, the game will pause and not continue until
they switch back into the game.

If MODE is 1, then the game will continue to run in the background if
the user switches away (useful if, for example, you are just making some
sort of jukebox music player with AGS).

Note that mode 1 does not work with some graphics cards in full-screen
mode, so you should only rely on it working when your game is run in
windowed mode.

**Cross-Platform Support**

Windows: ** Yes ILBRK MS-DOS: ** No ILBRK
Linux: ** Yes ILBRK MacOS: ** Yes ********

    SetMultitaskingMode (1);

will mean that the game continues to run in the background.

### SetRestartPoint 

    SetRestartPoint ()

Changes the game restart point to the current position. This means that
from now on, if the player chooses the Restart Game option, it will
return here.

This function is useful if the default restart point doesn't work
properly in your game - just use this function to move it.

**NOTE: The restart point cannot be set while a script is
running – therefore, when you call this it will actually set the restart
point at the next game loop where there is not a blocking script running
in the background.**

*SeeAlso:*

### SetSaveGameDirectory 

    static bool Game.SetSaveGameDirectory(string directory)

Changes the directory where save game files are stored to the supplied
*directory. If the directory does not exist, AGS will
attempt to create it.*

You cannot use fully qualified directories with this command (eg.
`C:\Games\Cool\Saves`), because the player might have installed your
game to any folder, and they might not be running Windows.

Therefore, only two types of path are supported: ILBRK 1. Relative paths
(eg. “Saves”). This will create a subfolder inside **default game
save folder ILBRK 2. The special tag `$MYDOCS$` which allows you
to explicitly create a different folder for your save games inside the
user's documents folder.**

The actual folder referenced with `$MYDOCS$` is different on every
platform: Windows XP: “My Documents”ILBRK Windows Vista and later:
“Saved Games”ILBRK Linux: `$XDG_DATA_HOME`/agsILBRK MacOS: game
installation folder.

Returns *true if the save game directory has been changed
successfully; *false if not.**

**NOTE: We advise you against using this function without
strong need. In the most cases setting the “Save games folder name”
property in the General Settings of the editor should be sufficient.**

    Game.SetSaveGameDirectory("$MYDOCS$/My Cool Game Saves");

will change the save game directory to “My Cool Game Saves” in My
Documents, and create the folder if it does not exist (might be useful
to do this in game\_start).

*See Also: ,*

### SetTextWindowGUI 

    SetTextWindowGUI (int gui)

Changes the GUI used for text windows to the specified GUI. This
overrides the “text windows use GUI” setting in the editor.

You can pass -1 as the GUI number to go back to using the default white
text box.

    SetTextWindowGUI (4);

will change Textwindow GUI 4 to be used for displaying text windows in
future.

### SetTimer 

    SetTimer (int timer_id, int timeout)

Starts timer TIMER\_ID ticking - it will tick once every game loop
(normally 40 times per second), until TIMEOUT loops, after which it will
stop. You can check whether the timer has finished by calling the
IsTimerExpired function.

Pass TIMEOUT as 0 to disable a currently running timer.

There are 20 available timers, with TIMER\_IDs from 1 to 20.

**NOTE: the timer will not tick while the game is paused.**

    SetTimer(1,1000);

will set the timer 1 to expire after 1000 game cycles.

*See Also:*

### SkipUntilCharacterStops 

    SkipUntilCharacterStops(CHARID)

Skips through the game until the specified character stops walking, a
blocking script runs, or a message box is displayed.

The purpose of this command is to mimic the functionality in games such
as The Longest Journey, where the player can press ESC to instantly get
the character to its destination. It serves as a handy feature to allow
you to give the player character a relatively slow walking speed,
without annoying the player by making them wait ages just to get from A
to B.

If the specified character is not moving when this function is called,
nothing happens.

    if (keycode == eKeyEscape) SkipUntilCharacterStops(EGO);

This means that if the player presses ESC, the game will skip ahead
until EGO finishes moving, or is interrupted by a Display command or a
blocking cutscene.

*See Also:*

### StartCutscene 

    StartCutscene(CutsceneSkipType)

Marks the start of a cutscene. Once your script passes this point, the
player can choose to skip a portion by pressing a key or the mouse
button. This is useful for things like introduction sequences, where you
want the player to be able to skip over an intro that they've seen
before.

The CutsceneSkipType determines how they can skip the cutscene:

    eSkipESCOnly
      by pressing ESC only
    eSkipAnyKey
      by pressing any key
    eSkipMouseClick
      by clicking a mouse button
    eSkipAnyKeyOrMouseClick
      by pressing any key or clicking a mouse button
    eSkipESCOrRightButton
      by pressing ESC or clicking the right mouse button

You need to mark the end of the cutscene with the EndCutscene command.

Be **very careful with where you place the corresponding
EndCutscene command. The script **must pass through
EndCutscene in its normal run in order for the skipping to work -
otherwise, when the player presses ESC the game could appear to
hang.****

*See Also: , , ,*

### UpdateInventory 

    UpdateInventory ()

Updates the on-screen inventory display. If you add or remove inventory
items manually (ie. by using the InventoryQuantity array rather than the
AddInventory/LoseInventory functions), the display may not get updated.
In this case call this function after making your changes, to update
what is displayed to the player.

Note that using this function will reset the order that items are
displayed in the inventory window to the same order they were created in
the editor.

*See Also: , ,*

### UnPauseGame 

    UnPauseGame ()

Resumes the game.

    if (IsGamePaused() == 1)
        UnPauseGame();

will unpause the game if it is paused.

*See Also:*

### Wait 

    Wait (int time)

Pauses the script and lets the game continue for TIME loops. There are
normally 40 loops/second (unless you change it with SetGameSpeed), so
using a value of 80 will wait 2 seconds. Note that no other scripts can
run while the Wait function is in the background.

    cEgo.Walk(120, 140, eBlock, eWalkableAreas);
    Wait(80);
    cEgo.FaceLocation(1000,100);

will move the character EGO to 120,140, wait until he gets there then
wait for 2 seconds (80 game cycles) and then face right.

*See Also: ,*

### WaitKey 

    WaitKey (int time)

Pauses the script and lets the game continue until EITHER:

\(a) TIME loops have elapsed, or

\(b) the player presses a key

Returns 0 if the time elapsed, or 1 if the player interrupted it.

    WaitKey(200);

will pause the script and wait until 5 seconds have passed or the player
presses a key.

*See Also: ,*

### WaitMouseKey 

    WaitMouseKey (int time)

Pauses the script and lets the game continue until EITHER:

\(a) TIME loops have elapsed, or

\(b) the player presses a key, or

\(c) the player clicks a mouse button

Returns 0 if the time elapsed, or 1 if the player interrupted it.

    WaitMouseKey(200);

will pause the script and wait until 5 seconds have passed or the player
presses a key or clicks the mouse.

*See Also: ,*

### AudioClipCount property 

    readonly static int Game.AudioClipCount

Returns the number of audio clips in the game.

This is useful for script modules if you need to iterate through all the
audio clips for some reason.

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

*See Also:*

### AudioClips property 

    readonly static int Game.AudioClips[int slot]

Returns the AudioClip\* pointer by its index in game resources.

    int i = 0;
    int music_count = 0;
    while (i < Game.AudioClipCount)
    {
      if (Game.AudioClips[i].Type == eAudioTypeMusic)
        music_count++;
      i++;
    }
    Display("We have %d musical clips in our game", music_count);

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

*See Also:*

### CharacterCount property 

*(Formerly part of GetGameParameter, which is now
obsolete)*

    readonly static int Game.CharacterCount

Returns the number of characters in the game.

This is useful for script modules if you need to iterate through all the
characters for some reason.

    Display("The game has %d characters.", Game.CharacterCount);

### DialogCount property 

    readonly static int Game.DialogCount

Returns the number of dialogs in the game.

This is useful for script modules if you need to iterate through all the
dialogs for some reason. Valid dialogs are numbered from 0 to
DialogCount - 1.

    Display("The game has %d dialogs.", Game.DialogCount);

*Compatibility: Supported by **AGS 3.0.2 and
later versions.***

### FileName property 

    readonly static String Game.FileName

Gets the filename that the game is running from. This will usually be
the name of the EXE file, but could also be “ac2game.dat” if you are
just running the game using ACWIN.EXE.

    Display("The main game file is: %s", Game.FileName);

will display the game filename.

*See Also:*

### FontCount property 

    readonly static int Game.FontCount

Returns the number of fonts in the game.

This is useful for script modules if you need to iterate through all the
fonts for some reason.

    Display("The game has %d fonts.", Game.FontCount);

### GlobalMessages property 

*(Formerly known as global function GetMessageText, which is now
obsolete)*

    readonly static String Game.GlobalMessages[int message]

Gets the text of the specified global message. The message number is one
of the global message numbers from 500 to 999.

If an invalid message number is supplied, *null will be
returned. Otherwise, the message contents will be returned.*

**NOTE: Global Messages were a feature of AGS 2.x and are
now obsolete. You will not need to use this property in new games.**

    String message = Game.GlobalMessages[997];
    Display("Global message 997 says: %s", message);

will display global message 997.

### GlobalStrings property 

*(Formerly known as GetGlobalString, which is now obsolete)
ILBRK *(Formerly known as SetGlobalString, which is now
obsolete)**

    static String Game.GlobalStrings[index]

Gets/sets global string *index. Global strings provide you
with an easy way to share string variables between scripts. There are 50
available global strings, with *index values from 0 to
49.**

    Game.GlobalStrings[15] = "Joe";
    Display("Global string 15 is now: %s", Game.GlobalStrings[15]);

will set global string 15 to contain “Joe”.

*See Also: ,*

### GUICount property 

*(Formerly part of GetGameParameter, which is now
obsolete)*

    readonly static int Game.GUICount

Returns the number of GUIs in the game.

This is useful for script modules if you need to iterate through all the
GUIs for some reason. Valid GUIs are numbered from 0 to GUICount minus
1.

    Display("The game has %d GUIs.", Game.GUICount);

### IgnoreUserInputAfterTextTimeoutMs property 

    static int Game.IgnoreUserInputAfterTextTimeoutMs;

Gets/sets the length of time for which user input is ignored after some
text is automatically removed from the screen.

When AGS is configured to automatically remove text after a certain time
on the screen, sometimes the player might try to manually skip the text
by pressing a key just as it is removed automatically, and thus they end
up skipping the next text line by accident. This property is designed to
eliminate this problem.

This property is specified in milliseconds (1000 = 1 second), and is set
to 500 by default.

    Game.IgnoreUserInputAfterTextTimeoutMs = 1000;

will tell AGS to ignore mouse clicks and key presses for 1 second after
text is automatically removed from the screen.

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also: , ,*

### InSkippableCutscene property 

*(Formerly known as game.in\_cutscene, which is now
obsolete)*

    static bool Game.InSkippableCutscene

Returns whether the game is currently between a StartCutscene and
EndCutscene, and therefore whether the player is able to skip over this
part of the game.

When the player chooses to skip a cutscene all of the script code is run
as usual, but any blocking commands are run through without the usual
game cycle delays. Therefore, you should never normally need to use this
property since cutscenes should all be handled automatically, but it
could be useful for script modules.

**NOTE: This is a static function, and thus need to be
called with `Game.` in front of it. See the example below.**

    if (Game.InSkippableCutscene)
    {
      Display("The player might never see this message!");
    }

will display a message if we are within a cutscene

*Compatibility: Supported by **AGS 3.0.1 and
later versions.***

*See Also: , ,*

### InventoryItemCount property 

*(Formerly part of GetGameParameter, which is now
obsolete)*

    readonly static int Game.InventoryItemCount

Returns the number of inventory items in the game. This is the total
number of items that you created in the Inventory Items pane of the
editor, not how many the player is currently carrying.

    Display("The game has %d inventory items.", Game.InventoryItemCount);

### MinimumTextDisplayTimeMs property 

    static int Game.MinimumTextDisplayTimeMs;

Gets/sets the minimum length of time that text is displayed on the
screen. AGS automatically adjusts the length of time that text is
displayed for depending on the length of the text (and you can customize
this calculation with ), but for very short statements like “Hi!”, you
might want the text to remain for longer.

This property is specified in milliseconds (1000 = 1 second), and is set
to 1000 by default.

**NOTE: This property is ignored if lip-sync is enabled, or
if the General Settings are set not to allow text to be automatically
removed.**

    Game.MinimumTextDisplayTimeMs = 2000;

will ensure that even the shortest “Hi!” text line will be displayed for
at least 2 seconds

*Compatibility: Supported by **AGS 3.1.2 and
later versions.***

*See Also: ,*

### MouseCursorCount property 

    readonly static int Game.MouseCursorCount

Returns the number of mouse cursors in the game.

This is useful for script modules if you need to iterate through all the
cursors for some reason.

    Display("The game has %d cursors.", Game.MouseCursorCount);

### Name property (game) 

    static String Game.Name

Gets/sets the game's name. This is initially set in the General Settings
pane of the editor, but you can change it at run-time in order to change
the window title of your game.

    Display("The game name is: %s", Game.Name);

will display the game name.

*See Also:*

### NormalFont property 

*(Formerly known as global function SetNormalFont, which is now
obsolete)*

    static FontType Game.NormalFont

Gets/sets the font used for all in-game text, except speech. The font
number must be a valid number from the Fonts pane of the editor.

More specifically, AGS uses the Normal Font for the following:

-   Display

-   DisplayTopBar

-   dialog options text

-   the built-in save and restore dialogs

The Normal Font is font 0 by default.

    Game.NormalFont = eFontSpecial;

will change the normal font to the font “Special”.

*See Also:*

### SkippingCutscene property 

*(Formerly known as game.skipping\_cutscene, which is now
obsolete)*

    static bool Game.SkippingCutscene

Returns whether the player has elected to skip the current cutscene.
This will return true if the game is between a StartCutscene and
EndCutscene command, and the player has chosen to skip it.

Although cutscene skipping is handled automatically by AGS, you can use
this property to optimise the process by bypassing any lengthy blocks of
code that don't need to be run if the cutscene is being skipped over.

**NOTE: This is a static function, and thus need to be
called with `Game.` in front of it. See the example below.**

    if (!Game.SkippingCutscene)
    {
      aScaryMusic.Play();
      Wait(100);
      Game.StopAudio();
    }

will only attempt to play the music if the player is not skipping the
cutscene.

*Compatibility: Supported by **AGS 3.0.1 and
later versions.***

*See Also: , ,*

### SpeechFont property 

*(Formerly known as global function SetSpeechFont, which is now
obsolete)*

    static FontType Game.SpeechFont;

Gets/sets the font used for character speech. The font number you supply
must be a valid number from the Fonts pane of the editor.

The Speech Font is font 1 by default.

    Game.SpeechFont = eFontStandard;

will change the speech font to “Standard”.

*See Also:*

### SpriteHeight property 

*(Formerly part of GetGameParameter, which is now
obsolete)*

    readonly static int Game.SpriteHeight[int slot]

Returns the height of the specified sprite.

The height will be returned in the usual 320x200-resolution
co-ordinates. If an invalid sprite slot is supplied, 0 will be returned.

    Display("Object 0's sprite is sized %d x %d.", Game.SpriteWidth[object[0].Graphic],
                                                   Game.SpriteHeight[object[0].Graphic]);

*See Also:*

### SpriteWidth property 

*(Formerly part of GetGameParameter, which is now
obsolete)*

    readonly static int Game.SpriteWidth[int slot]

Returns the width of the specified sprite.

The width will be returned in the usual 320x200-resolution co-ordinates.
If an invalid sprite slot is supplied, 0 will be returned.

    Display("Object 0's sprite is sized %d x %d.", Game.SpriteWidth[object[0].Graphic],
                                                   Game.SpriteHeight[object[0].Graphic]);

*See Also:*

### TextReadingSpeed property 

*(Formerly known as game.text\_speed, which is now
obsolete)*

    static int Game.TextReadingSpeed;

Gets/sets the speed at which AGS assumes the player can read text, and
therefore how long speech stays on the screen before it is automatically
removed.

Specifically, the TextReadingSpeed is the number of characters of text
that the player can read in a second. It is 15 by default. A higher
number will therefore lead to the text being removed more quickly.

It is useful to link this setting to a GUI Slider on some sort of
Control Panel GUI so that the player can adjust it depending on their
reading speed.

**NOTE: This property is ignored if lip-sync is enabled, or
if the General Settings are set not to allow text to be automatically
removed.**

    Game.TextReadingSpeed = 7;

sets the text reading speed to half the default, which will leave speech
on-screen for twice as long as usual.

*Compatibility: Supported by **AGS 3.1.2 and
later versions.***

*See Also: , ,*

### TranslationFilename property 

*(Formerly known as GetTranslationName, which is now
obsolete)*

    readonly static String Game.TranslationFilename;

Gets the name of the current translation filename (without the “.tra”
extension). This may be useful if you want to use a different graphic
somewhere depending on which translation is being used.

If no translation is in use, a blank string is returned.

    if (Game.TranslationFilename == "German") {
      Display("You are using the German translation.");
    }

*See Also: ,*

### UseNativeCoordinates property 

    readonly static bool Game.UseNativeCoordinates

Returns whether the game is using native co-ordinates. If native
co-ordinates are in use, then all X, Y, Top, Bottom, Width and Height
variables in the game will be expected to reflect the resolution of the
game.

If this is *false, then the game is operating in
backwards-compatible mode where all co-ordinates are low-res.*

If the game resolution is 320x200 or 320x240, this setting has no
effect.

This property is read-only; it is not possible to change this setting at
run-time.

    if (Game.UseNativeCoordinates)
    {
      Display("The player is at %d, %d -- REALLY!", player.x, player.y);
    }
    else
    {
      Display("The player is at %d, %d in the old-school system", player.x, player.y);
    }

*Compatibility: Supported by **AGS 3.1.0 and
later versions.***

### ViewCount property 

*(Formerly part of GetGameParameter, which is now
obsolete)*

    readonly static int Game.ViewCount

Returns the number of views in the game.

This is useful for script modules if you need to iterate through all the
views for some reason. Valid views are numbered from 1 to ViewCount.

    Display("The game has %d views.", Game.ViewCount);

GUI functions and properties 
----------------------------

### Centre 

*(Formerly known as CentreGUI, which is now obsolete)*

    GUI.Centre()

Centres the specified GUI in the middle of the screen. Useful if you've
been moving it around with SetPosition and just want to return it to the
centre.

    gControlpanel.Centre();

will centre the CONTROLPANEL GUI in the middle of the screen.

*See Also:*

### Click (gui) 

    GUI.Click()

Forces GUI's OnClick event. If there is a script function bound to that
event it will be run, otherwise nothing happens.

**NOTE: GUI.Click should not to be confused with
**static function GUI.ProcessClick. GUI.Click is called for
specific GUI and does not impose any other conditions, while
GUI.ProcessClick is called for “any GUI element that happen to be at the
given coordinates”.****

    gMainMenu.Click();

triggers OnClick event for gMainMenu.

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

*See Also: ,*

### GetAtScreenXY (GUI) 

*(Formerly known as GetGUIAt, which is now obsolete)*

    static GUI* GUI.GetAtScreenXY(int x, int y)

Checks whether there is currently a GUI at screen co-ordinates (X,Y). If
there is, returns its GUI. If two GUIs overlap, the frontmost one will
be returned - this can be changed with the GUI.ZOrder property.

If there is not currently a displayed, clickable GUI at the location
then *null is returned. If null is returned, do NOT attempt
to call any methods or use any properties of the GUI (since it does not
actually exist).*

**NOTE: This command will not find any GUIs that are set as
Non-Clickable (ie. the “Clickable” checkbox not checked).**

    GUI *theGui = GUI.GetAtScreenXY(mouse.x, mouse.y);
    if (theGui == gInventory) {
      Display("Inventory GUI at mouse location.");
    }
    else if (theGui == null) {
      Display("No GUI at mouse location");
    }
    else {
      Display("GUI %d at mouse location.", theGui.ID);
    }

will display the number of the GUI that the mouse is over.

*See Also: , ,*

### ProcessClick (GUI) 

    static void GUI.ProcessClick(int x, int y, CursorMode)

Simulates clicking the mouse on the location (X,Y) on the screen, in the
specified cursor mode. This “click” has special behavior in that it
**only affects GUI and GUI controls under given
coordinates. Any conditions attached to the first interface elements on
given coordinates will be executed. Other game elements (room objects,
hotspots, characters) will be **ignored.****

The available cursor modes are the ones you define on your Cursors tab
(but with eMode prepended to them). Usually these are eModeWalkto,
eModeLookat, etc.

    ProcessClick(100, 50, eModePointer);

will simulate clicking the mouse on co-ordinates (100, 50) in the
Pointer mode, which will ignore anything but interface.

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

*See Also: ,*

### SetPosition (GUI) 

*(Formerly known as SetGUIPosition, which is now obsolete)*

    GUI.SetPosition(int x, int y)

Moves the top-left corner of GUI to the new location (X,Y) on the
screen. This allows you to dynamically move GUIs around on the screen
while the game is running. The co-ordinates are screen co-ordinates, not
room co-ordinates, and use the same scale as in the editor.

    gVerbcoin.SetPosition(mouse.x, mouse.y);

will move the VERBCOIN GUI to the position where the cursor is.

*See Also: , , , , ,*

### SetSize (GUI) 

*(Formerly known as SetGUISize, which is now obsolete)*

    GUI.SetSize(int width, int height)

Changes the GUI to have the new size WIDTH x HEIGHT

This could be useful for initially hiding an 'Advanced' part of an
options screen and such like.

The size is in the normal 320x200-resolution pixels. Setting the size to
320, 200 will cause the GUI to take up the entire screen.

    gIconbar.SetSize(160, 100);

changes the ICONBAR GUI to be the size of half the screen

*See Also: , , , ,*

### BackgroundGraphic property (GUI) 

*(Formerly known as SetGUIBackgroundPic, which is now
obsolete)*

    int GUI.BackgroundGraphic

Gets/sets the background image of the GUI.

You can set this to 0 to remove the background image from the GUI.

*See Also: ,*

### Clickable property (GUI) 

*(Formerly known as SetGUIClickable, which is now
obsolete)*

    bool GUI.Clickable

Gets/sets whether the GUI is clickable or not. This allows you to modify
the “Clickable” checkbox from the GUI Editor.

If this is set to 1, then the GUI will respond to mouse clicks as
normal.

If this is set to 0, then this GUI cannot be clicked on by the mouse.
This might be useful for a transparent overlay GUI which displays
information, and you want the player to be able to click on whatever is
underneath.

    gStatusline.Clickable = false;

sets the STATUSLINE GUI to no longer respond to mouse clicks.

*See Also:*

### ControlCount property 

    readonly int GUI.ControlCount;

Gets the number of controls on the GUI. You won't normally need to use
this property, but in some circumstances you may wish to iterate through
all the GUI's controls, and this allows you to determine where to stop.

    int i = 0;
    while (i < gInventory.ControlCount) {
      gInventory.Controls[i].Enabled = false;
      i++;
    }

disables all controls on the INVENTORY GUI.

*See Also:*

### Controls property (GUI) 

    GUIControl* GUI.Controls[index]

Provides an array which allows you to access controls on the GUI by
their index. You should not normally need to do this, since accessing
the controls by their name is far easier; however, if you need to
interoperate with legacy code that uses the control number, this can
come in useful.

Returns the GUIControl object for the specified control index, or
*null if you give an invalid control index.*

You can cast the GUIControl to the appropriate type using the AsButton,
AsListBox, etc methods on it.

    GUIControl *control = gInventory.Controls[4];
    if (control == null) {
      Display("The inventory GUI doesn't have a control number 4.");
    }
    else {
      control.Enabled = true;
      control.AsListBox.AddItem("New item!!");
    }

gets list box number 4 from the INVENTORY GUI, and then adds an item to
it. If control 4 isn't a listbox, you will get a Null Reference error.

*See Also: ,*

### Height property (GUI) 

    int GUI.Height

Gets/sets the height of the GUI. This allows you to dynamically change
the size of the GUI on the screen.

The height is specified in the normal 320-resolution style.

    Display("The icon bar GUI is %d pixels high.", gIconbar.Height);

displays the height of the ICONBAR GUI.

*See Also: ,*

### ID property (GUI) 

    readonly int GUI.ID

Gets the GUI's ID number. This is the GUI's number from the editor, and
is useful if you need to interoperate with legacy code that uses the
GUI's number rather than object name.

    SetGUIClickable(gIconbar.ID, 1);
    gIconbar.Clickable = false;

uses the obsolete SetGUIClickable function to make the ICONBAR GUI
clickable, and then uses the equivalent modern property to stop it being
clickable.

*See Also:*

### Transparency property (GUI) 

*(Formerly known as SetGUITransparency, which is now
obsolete)*

    int GUI.Transparency

Gets/sets the GUI translucency, in percent.

Setting this to 100 means the GUI is totally invisible, and lower values
represent varying levels of translucency. Set it to 0 to stop the GUI
being translucent.

**NOTE: Transparency only works in 16-bit and 32-bit colour
games.**

**NOTE: When using the DirectX 5 driver, a large
transparent GUI can significantly slow down AGS.**

Some rounding is done internally when the transparency is stored –
therefore, if you get the transparency after setting it, the value you
get back might be one out. Therefore, using a loop with
`gInventory.Transparency++;` is not recommended as it will probably end
too quickly.

In order to fade a GUI in/out, the best approach is shown in the example
below:

    int trans = gInventory.Transparency;
    while (trans < 100) {
      trans++;
      gInventory.Transparency = trans;
      Wait(1);
    }

will gradually fade the INVENTORY GUI out until it is invisible.

*See Also:*

### Visible property (GUI) 

*(Formerly known as GUIOff, which is now obsolete)ILBRK
*(Formerly known as GUIOn, which is now obsolete)ILBRK
*(Formerly known as InterfaceOff, which is now
obsolete)ILBRK *(Formerly known as InterfaceOn, which is
now obsolete)ILBRK *(Formerly known as IsGUIOn, which is
now obsolete)*****

    bool GUI.Visible

Gets/sets whether the GUI is visible or not. This property has behaves
differently depending on the GUI popup style.

For “Normal” and “Persistent” GUIs, this property simply switches the
GUI on and off, and has no further effects.

For “Popup modal” GUIs, setting Visible to true causes the game to
become paused until the GUI is removed by setting Visible back to false
(eg. when the user presses an OK button or something similar).

For “Mouse Ypos” GUIs, the Visible property does not actually determine
whether the GUI can be seen, but instead it controls whether the GUI
**is allowed to pop up. If Visible is *false,
then moving the mouse to the top of the screen will not activate the
GUI; if it is *true, then the GUI will be allowed to be
popped up.****

    gSettings.Visible = true;

will turn on the SETTINGS GUI.

*See Also:*

### Width property (GUI) 

    int GUI.Width

Gets/sets the width of the GUI. This allows you to dynamically change
the size of the GUI on the screen.

The width is specified in the normal 320-resolution style.

    gInventory.Width += 5;

makes the INVENTORY GUI 5 pixels wider.

*See Also: ,*

### X property (GUI) 

    int GUI.X

Gets/sets the X position of the GUI. This allows you to dynamically
change the position of the GUI on the screen.

The X position is the left-hand side of the GUI, and can be between 0
and 320. The co-ordinates used are screen co-ordinates, not room
co-ordinates, and are in the normal 320-resolution style.

    gVerbcoin.X += 5;

moves the VERBCOIN GUI right 5 pixels.

*See Also: ,*

### Y property (GUI) 

    int GUI.Y

Gets/sets the Y position of the GUI. This allows you to dynamically
change the position of the GUI on the screen.

The Y position is the top edge of the GUI, and can be between 0 and 200
(or 240, depending on room height). The co-ordinates used are screen
co-ordinates, not room co-ordinates, and are in the normal
320x200-resolution style.

    gVerbcoin.Y += 5;

moves the VERBCOIN GUI down 5 pixels.

*See Also: ,*

### ZOrder property (gui) 

*(Formerly known as SetGUIZOrder, which is now obsolete)*

    int GUI.ZOrder

Gets/sets the z-order of the GUI. This allows you to dynamically change
the ordering of GUIs on the screen.

The Z-order setting is an arbitrary number between 0 and 1000. AGS draws
the GUIs in order, from the lowest numbered at the back to the highest
numbered at the front.

    gStatusline.ZOrder = 0;

sets the STATUSLINE GUI to be behind all other GUIs.

*See Also:*

GUI control functions and properties
------------------------------------

This section lists the functions and properties common to all types of
GUI control. Each individual control type (Button, ListBox, etc) also
has its own specific section.

### GetAtScreenXY (GUI control) 

*(Formerly known as GetGUIObjectAt, which is now obsolete)*

    static GUIControl* GUIControl.GetAtScreenXY(int x, int y)

Checks whether there is a GUI control at screen co-ordinates (X,Y).
Returns the control object if there is, or null if there is not. You
probably want to use this in conjunction with GetGUIAtLocation.

    GUIControl *theControl = GUIControl.GetAtScreenXY(mouse.x, mouse.y);
    if (theControl == lstSaveGames) {
      Display("The mouse is over the Save Games list box.");
    }
    else if (theControl == null) {
      Display("The mouse is not over a control.");
    }
    else {
      GUI *onGui = theControl.OwningGUI;
      Display("The mouse is over control %d on GUI %d.", theControl.ID, onGui.ID);
    }

will display what control the mouse is over.

*See Also:*

### AsType properties (GUI controls) 

    Button*  GUIControl.AsButton;
    InvWindow* GUIControl.AsInvWindow;
    Label*   GUIControl.AsLabel;
    ListBox* GUIControl.AsListBox;
    Slider*  GUIControl.AsSlider;
    TextBox* GUIControl.AsTextBox;

Converts a generic GUIControl\* pointer into a variable of the correct
type, and returns it. If the control is not of the requested type,
returns *null.*

    Button *theButton = gIconbar.Controls[2].AsButton;
    if (theButton == null) {
      Display("Control 2 is not a button!!!!");
    }
    else {
      theButton.NormalGraphic = 44;
    }

attempts to set Button 2 on GUI ICONBAR to have NormalGraphic 44, but if
that control is not a button, prints a message.

*See Also:*

### BringToFront (GUI controls) 

    GUIControl.BringToFront()

Brings this control to the front of the Z-order. This allows you to
rearrange the display order of controls within the GUI.

**Applies To**

Inherited by the Button, InvWindow, Label, ListBox, Slider and TextBox.

    btnBigButton.BringToFront();

will move the *btnBigButton button to be in front of all
other controls on the GUI.*

*See Also: ,*

### Clickable property (GUI controls) 

    bool GUIControl.Clickable

Gets/sets whether the GUI control is clickable.

This property determines whether the player can click the mouse on the
control. If it is set to *false, then any mouse clicks will
go straight through the control onto whatever is behind it. Unlike the
Enabled property though, setting Clickable to false does not alter the
appearance of the control.*

Note that disabling the control by setting Enabled to false overrides
this setting – that is, if Enabled is false then the control will not be
clickable, regardless of the *Clickable setting.*

Also, bear in mind that if you set *Clickable to false then
any mouse clicks will go through the control onto whatever is behind. On
the other hand, if *Enabled is set to false then the
control “absorbs” the mouse click but does not do anything with it.**

**Applies To**

Inherited by the Button, InvWindow, Label, ListBox, Slider and TextBox.

    btnSaveGame.Clickable = false;

will make the *btnSaveGame button non-clickable.*

*See Also:*

### Enabled property (GUI controls) 

*(Formerly known as SetGUIObjectEnabled, which is now
obsolete)*

    bool GUIControl.Enabled

Enables or disables a GUI control.

Normally, all your GUI controls (such as buttons, sliders, etc) are
enabled at all times except during a cutscene, when they are disabled.
This command allows you to explicitly disable a control at your script's
discretion.

If you set this to true, the control will be enabled; set to false to
disable it.

Whether you set it as enabled or not, it will **always be
disabled during a blocking cutscene, along with all the other
controls.**

While a control is disabled, it will not respond to mouse clicks. If it
is a button, its mouseover and pushed pictures will not be shown. The
control will be drawn according to the game “When GUI Disabled”
settings, as usual.

**Applies To**

Inherited by the Button, InvWindow, Label, ListBox, Slider and TextBox.

    btnSaveGame.Enabled = false;

will disable the *btnSaveGame button.*

*See Also: ,*

### Height property (GUI controls) 

    int GUIControl.Height;

Gets/sets the height of the GUI control. This allows you to dynamically
resize GUI controls while the game is running.

**Applies To**

Inherited by the Button, InvWindow, Label, ListBox, Slider and TextBox.

    btnConfirm.Height = 20;

makes the *btnConfirm button 20 pixels high.*

*See Also: ,*

### ID property (GUI controls) 

    readonly int GUIControl.ID

Gets the GUI control's ID number. This is the control's object number
from the GUI editor, and is useful if you need to interoperate with
legacy code that uses the control's number rather than object name.

**Applies To**

Inherited by the Button, InvWindow, Label, ListBox, Slider and TextBox.

    SetGUIObjectEnabled(lstSaves.OwningGUI.ID, lstSaves.ID, 1);
    lstSaves.Enabled = false;

uses the obsolete SetGUIObjectEnabled function to enable the lstSaves
list box, and then uses the equivalent modern property to disable it.

*See Also: ,*

### OwningGUI property (GUI controls) 

    readonly GUI* GUIControl.OwningGUI

Gets the GUI control's owning GUI, which is the GUI that contains the
control.

Returns a GUI, which allows you to use all the usual .

**Applies To**

Inherited by the Button, InvWindow, Label, ListBox, Slider and TextBox.

    GUI *thegui = lstSaves.OwningGUI;
    thegui.Visible = false;

    lstSaves.OwningGUI.Visible = true;

turns off the GUI that contains the lstSaves list box, then turns it on
again using the niftier full pathing approach.

*See Also: ,*

### SendToBack (GUI controls) 

    GUIControl.SendToBack()

Sends this control to the back of the Z-order. This allows you to
rearrange the display order of controls within the GUI.

**Applies To**

Inherited by the Button, InvWindow, Label, ListBox, Slider and TextBox.

    btnBigButton.SendToBack();

will move the *btnBigButton button to be behind all other
controls on the GUI.*

*See Also: ,*

### SetPosition (GUI controls) 

*(Formerly known as SetGUIObjectPosition, which is now
obsolete)*

    GUIControl.SetPosition(int x, int y)

Moves the top-left corner of the GUI control to be at (X,Y). These
co-ordinates are relative to the GUI which contains the control.

This allows you to dynamically move GUI controls around on the screen
while the game is running, and this may well be useful in conjunction
with GUI.SetSize if you want to create dynamically resizable GUIs.

**Applies To**

Inherited by the Button, InvWindow, Label, ListBox, Slider and TextBox.

    btnConfirm.SetPosition(40, 10);

will move the *btnConfirm button to be positioned at
(40,10) within the GUI.*

*See Also: , , , ,*

### SetSize (GUI controls) 

*(Formerly known as SetGUIObjectSize, which is now
obsolete)*

    GUIControl.SetSize(int width, int height)

Adjusts the specified GUI control to have the new size WIDTH x HEIGHT.

This allows you to dynamically resize GUI controls on the screen while
the game is running, and this may well be useful in conjunction with
GUI.SetSize and GUIControl.SetPosition if you want to create dynamically
resizable GUIs.

**Applies To**

Inherited by the Button, InvWindow, Label, ListBox, Slider and TextBox.

    invMain.SetSize(160, 100);

will resize the *invMain control to have a size of 160 x
100.*

*See Also: , , , ,*

### Visible property (GUI controls) 

    bool GUIControl.Visible

Gets/sets whether the GUI control is visible. This is *true
by default, but you can set it to *false in order to
temporarily remove the GUI control from the GUI.**

While the control is invisible, it will not be drawn on the screen, and
will not register clicks or otherwise respond to any user input.

**Applies To**

Inherited by the Button, InvWindow, Label, ListBox, Slider and TextBox.

    btnSaveGame.Visible = false;

will make the *btnSaveGame button invisible.*

*See Also:*

### Width property (GUI controls) 

    int GUIControl.Width;

Gets/sets the width of the GUI control. This allows you to dynamically
resize GUI controls while the game is running.

**Applies To**

Inherited by the Button, InvWindow, Label, ListBox, Slider and TextBox.

    btnConfirm.Width = 110;

makes the *btnConfirm button 110 pixels wide.*

*See Also: ,*

### X property (GUI controls) 

    int GUIControl.X;

Gets/sets the X position of the GUI control. This specifies its left
edge, and is relative to the GUI which contains the control.

This allows you to dynamically move GUI controls around on their parent
GUI while the game is running.

**Applies To**

Inherited by the Button, InvWindow, Label, ListBox, Slider and TextBox.

    btnConfirm.X = 10;

will move the *btnConfirm button to be positioned 10 pixels
from the left of its GUI.*

*See Also: ,*

### Y property (GUI controls) 

    int GUIControl.Y;

Gets/sets the Y position of the GUI control. This specifies its top
edge, and is relative to the GUI which contains the control.

This allows you to dynamically move GUI controls around on their parent
GUI while the game is running.

**Applies To**

Inherited by the Button, InvWindow, Label, ListBox, Slider and TextBox.

    btnConfirm.Y = 20;

will move the *btnConfirm button to be positioned 20 pixels
from the top of its GUI.*

*See Also: ,*

### ZOrder property (GUI controls) 

    int GUIControl.ZOrder;

Gets/sets the control's Z-order relative to other controls within the
same owning GUI. This allows you to precisely arrange the display order
of controls at runtime and to know which position the control had at
certain moment in time.

For AGS GUI Z-order means the order in wich controls are displayed from
bottom to top. That means that control at the bottom has Z-order equal
to 0, and control at the top has highest Z-order, equal to (number of
controls - 1).

Setting `GUIControl.ZOrder = 0;` will do same thing as calling
`GUIControl.SendToBack()`, and setting
`GUIControl.ZOrder = GUIControl.OwningGUI.ControlCount - 1;` will do
same thing as calling `GUIControl.BringToFront()`.

If you try to set inappropriate ZOrder, the nearest acceptable one will
be applied instead.

**Applies To**

Inherited by the Button, InvWindow, Label, ListBox, Slider and TextBox.

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

*See Also: ,*

GUI Button functions and properties
-----------------------------------

ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK
ILBRK

### Click (button) 

    Button.Click()

Forces Button's OnClick event. If there is a script function bound to
that event it will be run, otherwise nothing happens.

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

*See Also: ,*

### Animate (button) 

*(Formerly known as AnimateButton, which is now obsolete)*

    Button.Animate(int view, int loop, int delay, RepeatStyle)

Animates a GUI button by playing the specified view loop on it. This
could be useful for Sierra-style death animations and other effects.

LOOP from VIEW will be played on the button. The DELAY specifies the
speed of the animation - larger numbers are slower. This has the same
values you use with the Character.Animate and Object.Animate commands.

REPEAT determines whether the animation will loop repeatedly, or just
play once and stop with the last frame showing (eOnce or eRepeat are the
possible values).

You can abort an animation at any time by setting the button's
NormalGraphic property, or starting a new animation on the same button.

**NOTE: This command destroys the button's normal, pushed
and mouseover images. If you want to return the button to normal usage
after playing an animation, you will have to set the Graphic properties
to restore the images.**

**NOTE: This command does not support flipped view frames.
Any frames marked as “Flipped” will in fact be drawn normally when on a
button.**

    btnDeathAnim.Animate(6, 2, 4, eRepeat);

will animate the 'btnDeathAnim' button using loop 2 of view 6, with a
delay of 4 cycles per frame, and repeat the animation continually.

*See Also:*

### ClipImage property 

    bool Button.ClipImage;

Gets/sets whether the button clips its image to the button boundaries.

For example, if the button is sized 30x30, but its Graphic is a 50x50
image, then this property controls whether the image is allowed to spill
over the edge of the button.

The default is false, ie. the image is not clipped.

Setting this to true can be useful in that it ensures that the button's
image is not larger than the button's clickable area, which can cause
confusion when it happens.

    btnOK.ClipImage = true;

sets the *btnOK button so that its image will be restrained
to the button's clickable area.*

*See Also:*

### Font property (button) 

    FontType Button.Font

Gets/sets the font used by the button to display text.

The font number must correspond to one of the fonts from the Fonts pane
in the AGS Editor.

    btnOK.Font = eFontMain;

will change the *btnOK button to use Font “Main”.*

*See Also: ,*

### Graphic property (button) 

*(Formerly part of GetButtonPic, which is now obsolete)*

    readonly int Button.Graphic;

Gets the current image on a GUI button. If a value less than 1 is
returned, then no image is currently displayed on the button.

This property is read-only; in order to set the image, you must use one
of the , or properties.

    Display("The button is currently using sprite %d.", btnPlay.Graphic);

will display btnPlay's current sprite number.

*See Also: , , ,*

### MouseOverGraphic property (button) 

*(Formerly part of GetButtonPic, which is now obsolete)
ILBRK *(Formerly part of SetButtonPic, which is now
obsolete)**

    int Button.MouseOverGraphic;

Gets/sets the button's mouse-over sprite. This can be -1, which
indicates that the button does not have a mouse-over graphic.

    Display("The button's mouse-over image is sprite %d.", btnPlay.MouseOverGraphic);

will display btnPlay's mouse-over sprite number.

*See Also: , ,*

### NormalGraphic property (button) 

*(Formerly part of GetButtonPic, which is now obsolete)
ILBRK *(Formerly part of SetButtonPic, which is now
obsolete)**

    int Button.NormalGraphic;

Gets/sets the button's normal sprite (ie. the graphic used when the
button is not pushed and the mouse is not over it).

Note that setting this to a different sprite will change the button's
size to match the size of the new sprite.

    Display("The button's normal image is sprite %d.", btnPlay.NormalGraphic);

will display btnPlay's normal sprite number.

*See Also: , , ,*

### PushedGraphic property (button) 

*(Formerly part of GetButtonPic, which is now obsolete)
ILBRK *(Formerly part of SetButtonPic, which is now
obsolete)**

    int Button.PushedGraphic;

Gets/sets the button's pushed sprite (ie. the graphic used when the
button is pushed in by the user). This can be -1, which indicates that
the button does not have a pushed image.

    Display("The button's pushed image is sprite %d.", btnPlay.PushedGraphic);

will display btnPlay's pushed sprite number.

*See Also: , ,*

### Text property (button) 

*(Formerly known as SetButtonText, which is now obsolete)
ILBRK *(Formerly known as Button.GetText, which is now
obsolete) ILBRK *(Formerly known as Button.SetText, which
is now obsolete)***

    String Button.Text;

Gets/sets the text displayed on the button.

    Display("Button displayed: %s", btnController.Text);
    btnController.Text = "Enable jibble";

will display the old text, then change button btnController to read
'Enable jibble'.

*See Also: ,*

### TextColor property (button) 

    int Button.TextColor;

Gets/sets the text colour used to display the button's text.

If the button is displaying an image rather than text, then this
property has no effect.

    btnRestart.TextColor = 15;

will change button 'btnRestart' to have white text.

*See Also:*

GUI InvWindow functions and properties 
--------------------------------------

ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK
ILBRK

### ScrollDown (inv window) 

    InvWindow.ScrollDown()

Scrolls the inventory window down one line, if there are more items to
display. If the inventory window is already at the bottom, then nothing
happens.

You would usually use this in response to a GUI button press on a Down
arrow button on your GUI.

    invMain.ScrollDown();

will scroll the *invMain inv window down one row.*

*See Also: ,*

### ScrollUp (inv window) 

    InvWindow.ScrollUp()

Scrolls the inventory window up one line, if there are more items to
display. If the inventory window is already at the top, then nothing
happens.

You would usually use this in response to a GUI button press on an Up
arrow button on your GUI.

    invMain.ScrollUp();

will scroll the *invMain inv window up one row.*

*See Also: ,*

### CharacterToUse property 

    Character* InvWindow.CharacterToUse;

Gets/sets which character the inventory window is currently displaying
the inventory for. This is either set to a specific character, or it can
be set to *null, in which case the inventory window will
track the current player character (this is the default).*

    invMain.CharacterToUse = cJack;

will change the *invMain inventory window to display
character JACK's inventory.*

### ItemAtIndex property 

    readonly InventoryItem* InvWindow.ItemAtIndex[];

Gets the inventory item that is currently displayed at the specified
index in this inventory window. The number of items in the window can be
retrieved with the property. Indexes range from 0 to ItemCount - 1.

If an invalid index is supplied, *null is returned.*

    String firstOne = invMain.ItemAtIndex[0].Name;
    Display("First item is %s.", firstOne);

will display the name of the first item displayed in the
*invMain inventory window.*

*See Also:*

### ItemCount property (inv window) 

*(Formerly known as game.num\_inv\_items, which is now
obsolete)*

    readonly int InvWindow.ItemCount;

Gets the total number of items contained in the inventory window. This
will tend to equal the total number of items that the character has
(though it may not if the “Display multiple items multiple times” game
setting is not checked).

    if (invMain.ItemCount > (invMain.ItemsPerRow * invMain.RowCount)) {
      btnInvUp.Enabled = true;
      btnInvDown.Enabled = false;
    }

will enable the GUI buttons *btnInvUp and
*btnInvDown if there are more inventory items than will fit
in the inventory window.**

*See Also: , ,*

### ItemHeight property 

*(Formerly known as SetInvDimensions, which is now
obsolete)*

    int InvWindow.ItemHeight;

Gets/sets the height of the rows in the inventory window. You should
generally set this up in game\_start to the height of your largest
inventory item. The default is 22.

    invMain.ItemWidth = 50;
    invMain.ItemHeight = 30;

sets the *invMain inventory window to use item cells 50x30
large.*

*See Also: ,*

### ItemWidth property 

*(Formerly known as SetInvDimensions, which is now
obsolete)*

    int InvWindow.ItemWidth;

Gets/sets the width of the items in the inventory window. You should
generally set this up in game\_start to the width of your largest
inventory item. The default is 40.

    invMain.ItemWidth = 50;
    invMain.ItemHeight = 30;

sets the *invMain inventory window to use item cells 50x30
large.*

*See Also: ,*

### ItemsPerRow property 

*(Formerly known as game.items\_per\_line, which is now
obsolete)*

    readonly int InvWindow.ItemsPerRow;

Gets the number of items that can be displayed in each row of the
inventory window. This is calculated by the width of the inventory
window divided by the individual ItemWidth.

    Display("The inventory window can show %d items at a time", invMain.ItemsPerRow * invMain.RowCount);

displays how many items can be visible in the invMain window at once.

*See Also: ,*

### RowCount property (inv window) 

    readonly int InvWindow.RowCount;

Gets the number of rows that can be displayed within the inventory
window. This is calculated by dividing the height of the window by the
individual ItemHeight.

    Display("The inventory window can show %d items at a time", invMain.ItemsPerRow * invMain.RowCount);

displays how many items can be visible in the invMain window at once.

*See Also: ,*

### TopItem property (inv window) 

*(Formerly known as game.top\_inv\_item, which is now
obsolete)*

    int InvWindow.TopItem;

Gets/sets the index of the first item currently displayed in the
inventory window. The first item is represented by 0, and the last item
is has an index of - 1.

You can use this to work out whether to display scroll arrows or not.

    if (invMain.TopItem > 0) {
      btnScrollUp.Visible = true;
    }
    else {
      btnScrollUp.Visible = false;
    }

makes the *btnScrollUp button visible or invisible
depending on whether the inventory list can be scrolled up.*

*See Also:*

GUI Label functions and properties
----------------------------------

ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK
ILBRK

### Font property (label) 

*(Formerly known as SetLabelFont, which is now obsolete)*

    FontType Label.Font;

Gets/sets the font used to display the label's text. This is useful if
you have a standard SCI font for your English version, but want to
change to a TTF font for foreign language versions.

    if (IsTranslationAvailable()) {
      lblStatus.Font = eFontForeign;
    }

will change label 'lblStatus' to use font “Foreign” if a game
translation is in use.

*See Also: , ,*

### Text property (label) 

*(Formerly known as SetLabelText, which is now obsolete)
ILBRK *(Formerly known as Label.GetText, which is now
obsolete) ILBRK *(Formerly known as Label.SetText, which is
now obsolete)***

    String Label.Text;

Gets/sets the text displayed in the specified label. This allows you to
change the text during the game, for example to create a Lucasarts-style
status line.

    lblStatus.Text = Game.GetLocationName(mouse.x, mouse.y);

will display the name of the location the cursor is over on label
'lblStatus'

*See Also: , , ,*

### TextColor property (label) 

*(Formerly known as SetLabelColor, which is now obsolete)*

    int Label.TextColor;

Gets/sets the text colour used to display the label's text.

    lblStatus.TextColor = 14;

will change label 'lblStatus' to have yellow text.

*See Also: ,*

GUI List Box functions and properties
-------------------------------------

ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK
ILBRK

### AddItem 

*(Formerly known as ListBoxAdd, which is now obsolete)*

    ListBox.AddItem(string newitem)

Adds NEWITEM to the specified list box. The item will be appended to the
end of the list.

**NOTE: List boxes have a limit of 200 items. If you try to
add more than that, this function will return *false and
the item will not be added.***

    String input = txtUserInput.Text;
    lstChoices.AddItem(input);

will take the input from the user and add it to the listbox.

*See Also: , , , ,*

### Clear (list box) 

*(Formerly known as ListBoxClear, which is now obsolete)*

    ListBox.Clear()

Removes all items from the specified list box.

    lstNoteBook.Clear();

will remove all the items from listbox *lstNoteBook.*

*See Also:*

### FillDirList 

*(Formerly known as ListBoxDirList, which is now obsolete)*

    ListBox.FillDirList(string filemask)

Fills the list box with a list of filenames matching FILEMASK in the
current directory. This could be useful if you have various data files
and the player can choose which one to load.

FILEMASK is a standard DOS/Windows search expression such as “\*.dat” or
“data\*.\*”

When specifying file path you may use special location tags: ILBRK
`$INSTALLDIR$`, which allows you to explicitly access files in the game
installation directory. ILBRK `$SAVEGAMEDIR$`, which allows you to
access files in the save game directory. ILBRK `$APPDATADIR$`, which
allows you to access files to a folder on the system which is accessible
by and shared by all users.

    lstSaveGames.FillDirList("agssave.*");

will fill the listbox with the list of the saved games. Note that
actually for this task you would use FillSaveGameList instead.

*See Also: , ,*

### FillSaveGameList 

*(Formerly known as ListBoxSaveGameList, which is now
obsolete)*

    ListBox.FillSaveGameList()

Fills the specified listbox with the save game list, sorted correctly
with the most recent game at the top of the list.

The property is updated to contain the save game slot number for each
index in the list, so that you can do:

    int index = lstSaveGames.SelectedIndex;
    RestoreGameSlot(lstSaveGames.SaveGameSlots[index]);

**NOTE: The save game list can only hold 50 save games. If
ListBox.ItemCount returns 50 and you are doing a Save dialog box, you
may want to make the user replace an existing file rather than saving a
new one.**

    lstSaveGames.FillSaveGameList();

will fill listbox *lstSaveGames with the list of the saved
games.*

*See Also: , , ,*

### GetItemAtLocation 

    ListBox.GetItemAtLocation(int x, int y)

Determines which item in the list box is at the screen co-ordinates
(X,Y). This allows you to find out which item the mouse is hovering
over, for instance.

Returns the item index (where the first item is 0), or -1 if the
specified co-ordinates are not over any item or are outside the list
box.

    int index = lstOptions.GetItemAtLocation(mouse.x, mouse.y);
    if (index < 0) {
      Display("The mouse is not over an item!");
    }
    else {
      String selectedItem = lstOptions.Items[index];
      Display("The mouse is over item '%s'.", selectedItem);
    }

will display the item text that the mouse is currently hovering over.

*See Also:*

### InsertItemAt 

    ListBox.InsertItemAt(int index, string newitem)

Inserts NEWITEM into the specified list box. The item will be inserted
**before the specified index.**

Listbox indexes go from 0 (the first item) to ItemCount - 1 (the last
item). The new item will be inserted before the index you specify.

**NOTE: List boxes have a limit of 200 items. If you try to
add more than that, this function will return *false and
the item will not be added.***

    lstChoices.AddItem("First item");
    lstChoices.AddItem("Second item");
    lstChoices.InsertItemAt(1, "Third item");

will insert the Third Item in between the First and Second items.

*See Also: ,*

### RemoveItem 

*(Formerly known as ListBoxRemove, which is now obsolete)*

    ListBox.RemoveItem(int item)

Removes ITEM from the specified list box. ITEM is the list index of the
item to remove, starting with 0 for the top item.

If you want to remove all items from the list, then use instead.

**NOTE: Calling this function causes other items in the
list to get re-numbered, so make sure you don't keep around any
references from ListBox.SelectedIndex and related functions while using
this command.**

    lstTest.AddItem("First item");
    lstTest.AddItem("Second item");
    lstTest.RemoveItem(0);

the list box will now just contain “Second item”.

*See Also: ,*

### ScrollDown (list box) 

    ListBox.ScrollDown()

Scrolls the list box down one row. If it is already at the bottom,
nothing happens.

    lstTest.ScrollDown();

will scroll the *lstTest list box down one row.*

*See Also:*

### ScrollUp (list box) 

    ListBox.ScrollUp()

Scrolls the list box up one row. If it is already at the top, nothing
happens.

    lstTest.ScrollUp();

will scroll the *lstTest list box up one row.*

*See Also:*

### Font property (list box) 

    FontType ListBox.Font

Gets/sets the font used by the specified list box.

    lstSaveGames.Font = eFontSpeech;

will change the *lstSaveGames list box to use Font
“Speech”.*

*See Also: ,*

### HideBorder property (list box) 

    bool ListBox.HideBorder

Gets/sets whether the list box's border is hidden.

Note that hiding the border will also implicitly hide the up/down scroll
arrows for the list box.

    lstSaveGames.HideBorder = true;

will hide the border around the Save Games list box.

*See Also:*

### HideScrollArrows property (list box) 

    bool ListBox.HideScrollArrows

Gets/sets whether the built-in up/down scroll arrows are hidden.

Because the appearance of the scroll arrows is not customizable, you may
wish to use this to hide them and provide your own arrows using GUI
Button controls.

**NOTE: If the list box's “Hide Border” setting is enabled,
then the scroll arrows will also be hidden, since “Hide Border”
supersedes “Hide Scroll Arrows”. You only need to use this
HideScrollArrows property if you want the border to be shown but the
arrows hidden.**

    lstSaveGames.HideScrollArrows = true;

will hide the built-in scroll arrows on the list box.

*See Also:*

### ItemCount property (list box) 

*(Formerly known as ListBoxGetNumItems, which is now
obsolete)*

    readonly int ListBox.ItemCount

Gets the number of items in the specified listbox. Valid item indexes
range from 0 to (numItems - 1).

This property is read-only. To change the item count, use the AddItem
and RemoveItem methods.

    int saves = lstSaveGames.ItemCount;

will pass the number of saved games to the int saves.

*See Also:*

### Items property 

*(Formerly known as ListBoxGetItemText, which is now
obsolete) ILBRK *(Formerly known as ListBox.GetItemText,
which is now obsolete) ILBRK *(Formerly known as
ListBox.SetItemText, which is now obsolete)***

    String ListBox.Items[index]

Gets/sets the text of the list box item at INDEX.

List box items are numbered starting from 0, so the first item is 0, the
second is 1, and so on. The highest allowable index is ItemCount minus
1.

If you want to add a new item to the listbox, use the method.

    String selectedItemText = lstOptions.Items[lstOptions.SelectedIndex];

will get the text of the selected item in the list box.

*See Also: , ,*

### RowCount property (list box) 

    readonly int ListBox.RowCount

Gets the number of rows that can be shown within the list box. This
depends on the size of the list box, and **does not depend
on how many items are actually stored in the list box.**

This property is read-only. To change the row count, adjust the height
of the list box.

    Display("You can currently see %d items from the listbox's contents", lstSaveGames.RowCount);

will display the number of rows that the listbox can display.

*See Also: , ,*

### SaveGameSlots property 

*(Formerly known as global array savegameindex, which is now
obsolete)*

    readonly int ListBox.SaveGameSlots[];

Contains the corresponding save game slot for each item in the list.

This is necessary because the FillSaveGameList command sorts the list of
save games to put the most recent first. Therefore, you can use this
array to map the list box indexes back to the corresponding save game
slot.

**NOTE: You must use the FillSaveGameList command in order
to populate this array.**

    int index = lstSaveGames.SelectedIndex;
    RestoreGameSlot(lstSaveGames.SaveGameSlots[index]);

will restore the currently selected game in the list, assuming
FillSaveGameList had been used previously.

*See Also: ,*

### SelectedIndex property 

*(Formerly known as ListBoxGetSelected, which is now
obsolete) ILBRK *(Formerly known as ListBoxSetSelected,
which is now obsolete)**

    int ListBox.SelectedIndex

Gets/sets the index into the list of the currently selected item. The
first item is 0, second is 1, and so on. If no item is selected, this is
set to -1.

You can set this to -1 to remove the highlight (ie. un-select all
items).

    String selectedText = lstOptions.Items[lstOptions.SelectedIndex];

will get the text of the selected item in the listbox.

### TopItem property (list box) 

*(Formerly known as ListBoxSetTopItem, which is now
obsolete)*

    int ListBox.TopItem

Gets/sets the top item in the list box. The top item is the first item
that is visible within the list box, so changing this effectively
scrolls the list up and down.

Indexes for TopItem start from 0 for the first item in the list.

    lstSaveGames.TopItem = 0;

will automatically scroll listbox *lstSaveGames back to the
top of the list.*

### Translated property (list box) 

    bool ListBox.Translated

Gets/sets whether the list box's items are translated to the selected
game language at runtime.

*Compatibility: Supported by **AGS 3.3.0 and
later versions.***

GUI Slider properties
---------------------

ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK
ILBRK

### BackgroundGraphic property (slider) 

    int Slider.BackgroundGraphic;

Gets/sets the sprite used to draw the slider background. This image is
tiled along the length of the slider.

The background graphic can be set to 0, which will draw the default grey
slider background.

    Display("sldHealth's background is sprite %d", sldHealth.BackgroundGraphic);

displays the *sldHealth slider's background image*

*Compatibility: Supported by **AGS 3.1.0 and
later versions.***

*See Also:*

### HandleGraphic property 

    int Slider.HandleGraphic;

Gets/sets the sprite used to draw the handle on the slider. The handle
represents the slider's current position, and can be dragged around by
the player.

The handle graphic can be set to 0, which will draw the default grey
handle.

    Display("sldHealth's handle is sprite %d", sldHealth.HandleGraphic);

displays the *sldHealth slider's handle image*

*Compatibility: Supported by **AGS 3.1.0 and
later versions.***

*See Also: ,*

### HandleOffset property 

    int Slider.HandleOffset;

Gets/sets the offset at which the handle image is drawn. This value is
initially set up in the editor.

    sldHealth.HandleOffset = 2;

sets the *sldHealth slider's handle to be drawn an extra 2
pixels to the right.*

*Compatibility: Supported by **AGS 3.1.0 and
later versions.***

*See Also:*

### Max property 

    int Slider.Max;

Gets/sets the maximum value of the specified GUI slider.

When changing the maximum, the slider's Value will be adjusted if
necessary so that it lies within the Min - Max range.

An error occurs if you try to set the Max to a lower value than the Min.

    sldHealth.Max = 200;

sets the maximum value of the *sldHealth slider to 200.*

*See Also: ,*

### Min property 

    int Slider.Min;

Gets/sets the minimum value of the specified GUI slider.

When changing the minimum, the slider's Value will be adjusted if
necessary so that it lies within the Min - Max range.

An error occurs if you try to set the Min to a higher value than the
Max.

    sldHealth.Min = 0;

sets the minimum value of the *sldHealth slider to 0.*

*See Also: ,*

### Value property 

*(Formerly known as GetSliderValue, which is now obsolete)
ILBRK *(Formerly known as SetSliderValue, which is now
obsolete)**

    int Slider.Value;

Gets/sets the value of the specified GUI slider. You would usually use
this in the slider's OnChange event handler to find out what value the
player has changed the slider to, in order to process their command.

When setting the value, the new value must lie between the MIN and MAX
settings for the slider, as set up in the GUI editor.

    System.Volume = sldVolume.Value;

will set the audio volume to the value of the slider
*sldVolume.*

*See Also:*

GUI Text Box functions and properties
-------------------------------------

ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK ILBRK
ILBRK

### Font property (text box) 

*(Formerly known as SetTextBoxFont, which is now obsolete)*

    FontType TextBox.Font

Gets/sets the font used by the specified text box. This might be useful
if you need a player input text box to use a different font with foreign
language translations, for example.

    txtUserInput.Font = eFontNormal;

will change the *txtUserInput text box to use Font
“Normal”.*

*See Also: ,*

### Text property (text box) 

*(Formerly known as GetTextBoxText, which is now obsolete)
ILBRK *(Formerly known as SetTextBoxText, which is now
obsolete) ILBRK *(Formerly known as TextBox.GetText, which
is now obsolete) ILBRK *(Formerly known as TextBox.SetText,
which is now obsolete)****

    String TextBox.Text;

Gets/sets the text box contents. This might be useful to reset the text
box to blank after the user has typed something in, or to fill in a
default value.

    txtUserInput.Text = "";

will clear the txtUserInput text box.

*See Also: , ,*

### TextColor property (text box) 

    int TextBox.TextColor;

Gets/sets the text colour used to draw the text box. This affects both
the text in the text box, and also the text box's border.

    txtInput.TextColor = 14;

will change text box 'txtInput' to have yellow text.

*Compatibility: Supported by **AGS 3.1.0 and
later versions.***

*See Also:*

Hotspot functions and properties
--------------------------------

### GetAtScreenXY (hotspot) 

*(Formerly known as global function GetHotspotAt, which is now
obsolete)*

    static Hotspot* Hotspot.GetAtScreenXY(int x, int y)

Returns the hotspot at SCREEN co-ordinates (X,Y). If there is no hotspot
there, or if invalid co-ordinates are specified, the Hotspot\*
representing hotspot 0 will be returned.

**NOTE: The co-ordinates are SCREEN co-ordinates, NOT ROOM
co-ordinates. This means that with a scrolling room, the co-ordinates
you pass are relative to the screen's current position, and NOT absolute
room co-ordinates. This means that this function is suitable for use
with the mouse cursor position variables.**

    if (Hotspot.GetAtScreenXY(mouse.x, mouse.y) == hDoor)
      Display("Mouse on the door");
    else if (Hotspot.GetAtScreenXY(mouse.x, mouse.y) != hotspot[0])
      Display("Mouse is on something (but not the door)!");
    else
      Display("Mouse not on a hotspot");

will display a message depending on what the mouse is on.

*See Also: ,*

### GetProperty (hotspot) 

*(Formerly known as GetHotspotProperty, which is now
obsolete)*

    Hotspot.GetProperty(string property)

Returns the custom property setting of the PROPERTY for the hotspot.

This command works with Number properties (it returns the number), and
with Boolean properties (returns 1 if the box was checked, 0 if not).

Use the equivalent GetTextProperty function to get a text property.

    if (hotspot[1].GetProperty("Value") > 200)
      Display("Hotspot 1's value is over 200!");

will print the message if hotspot 1 has its “Value” property set to more
than 200.

*See Also:*

### GetTextProperty (hotspot) 

*(Formerly known as GetHotspotPropertyText, which is now
obsolete) ILBRK *(Formerly known as
Hotspot.GetPropertyText, which is now obsolete)**

    String Hotspot.GetTextProperty(string property)

Returns the custom property setting of the PROPERTY for the hotspot.

This command works with Text properties only. The property's text will
be returned from this function.

Use the equivalent GetProperty function to get a non-text property.

    String description = hotspot[2].GetTextProperty("Description");
    Display("Hotspot 2's description: %s", description);

will retrieve hotspot 2's “description” property and display it.

*See Also:*

### SetProperty (hotspot) 

    bool Hotspot.SetProperty(const string property, int value)

Sets the new *value for the custom *property
for the specified hotspot. Returns TRUE if such property exists and
FALSE on failure.**

This command works with Number properties (it sets the numeric value),
and with Boolean properties (sets FALSE is value is equal to 0, or TRUE
otherwise).

Use the equivalent SetTextProperty function to set new text property
value.

    hDoor.SetProperty("LockDifficulty", 5);

will change Door hotspot's “LockDifficulty” custom property to 5.

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

*See Also:*

### SetTextProperty (hotspot) 

    bool Hotspot.SetTextProperty(const string property, const string value)

Sets the new *value text for the custom
*property for the specified hotspot. Returns TRUE if such
property exists and FALSE on failure.**

This command works with Text properties only. The property's text will
be changed to new value.

Use the equivalent SetProperty function to set a non-text property.

    hDoor.SetTextProperty("Description", "The sturdy door");

will change Door's “description” property.

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

*See Also:*

### IsInteractionAvailable (hotspot) 

    Hotspot.IsInteractionAvailable(CursorMode)

Checks whether there is an event handler defined for activating the
hotspot in cursor mode MODE.

This function is very similar to RunInteraction, except that rather than
run the event handler script function, it simply returns
*true if something would have happened, or
*false if unhandled\_event would have been run.**

    if (hTable.IsInteractionAvailable(eModeLookat) == 0)
      Display("looking on this table would not do anything.");

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

*See Also: ,*

### RunInteraction (hotspot) 

*(Formerly known as RunHotspotInteraction, which is now
obsolete)*

    Hotspot.RunInteraction(CursorMode)

Processes the event handler as if the player had clicked the mouse on
the hotspot using the specified cursor mode.

    hDoor.RunInteraction(eModeLookat);

will run the code defined in the “LOOK AT HOTSPOT” event for hotspot
hDoor.

*See Also: , , ,*

### Enabled property (hotspot) 

*(Formerly known as DisableHotspot, which is now obsolete)
ILBRK *(Formerly known as EnableHotspot, which is now
obsolete)**

    bool Hotspot.Enabled

Enables/disables the specified hotspot. If you set this to false, then
all areas of the screen that were previously made up of the hotspot now
act as type 0 (no hotspot). You can turn the hotspot back on later by
setting this back to true.

This setting is persisted in-game; that is, it will not be reset when
the player re-enters the room.

The default value of this property is always *true.*

    hBrownTree.Enabled = false;

will disable the hBrownTree hotspot.

*See Also: , ,*

### ID property (hotspot) 

    readonly int Hotspot.ID

Gets the hotspot number of this hotspot. This allows you to interoperate
with old script using the number-based hotspot functions.

    Display("Hotspot hDoor is hotspot number %d.", hDoor.ID);
    Display("Hotspot 3 is number %d.", hotspot[3].ID);

displays hDoor's hotspot number, and then displays hotspot 3's number
(which will be 3).

*See Also:*

### Name property (hotspot) 

*(Formerly known as GetHotspotName, which is now obsolete)
ILBRK *(Formerly known as Hotspot.GetName, which is now
obsolete)**

    readonly String Hotspot.Name;

Gets the name of the hotspot.

This property is read-only; it is currently not possible to change
hotspot names at run-time.

    Display("Hotspot 3's name is %s.", hotspot[3].Name);

will retrieve and then display hotspot 3's name.

*See Also:*

### WalkToX property 

*(Formerly known as GetHotspotPointX, which is now
obsolete)*

    readonly int Hotspot.WalkToX

Gets the X room co-ordinate of the hotspot's walk-to point. If the
hotspot does not have a walk-to point, returns -1.

    player.Walk(hTable.WalkToX, hTable.WalkToY, eBlock, eWalkableAreas);

will move the character to hotspot hTable's walk-to point.

*See Also: ,*

### WalkToY property 

*(Formerly known as GetHotspotPointY, which is now
obsolete)*

    readonly int Hotspot.WalkToY

Gets the Y room co-ordinate of the hotspot's walk-to point. If the
hotspot does not have a walk-to point, returns -1.

    player.Walk(hTable.WalkToX, hTable.WalkToY, eBlock, eWalkableAreas);

will move the character to hotspot hTable's walk-to point.

*See Also: ,*

Inventory item functions and properties
---------------------------------------

### GetAtScreenXY (inventory) 

*(Formerly known as global function GetInvAt, which is now
obsolete)*

    static InventoryItem* InventoryItem.GetAtScreenXY(int x, int y)

Returns the inventory item at SCREEN co-ordinates (X,Y). Note that this
only detects inventory items on custom Inventory windows (that are
switched on when this function is called), and is intended to allow you
to do Verb Coin style GUIs and so on.

If there is no inventory item there, or if invalid co-ordinates are
specified, returns null.

**NOTE: The co-ordinates are SCREEN co-ordinates, NOT ROOM
co-ordinates. This means that with a scrolling room, the co-ordinates
you pass are relative to the screen's current position, and NOT absolute
room co-ordinates. This means that this function is suitable for use
with the mouse cursor position variables.**

    InventoryItem *item = InventoryItem.GetAtScreenXY(mouse.x, mouse.y);
    if (item == null) {
      Display("No inventory item at the mouse co-ordinates");
    }
    else {
      Display("Inventory item number %d at the mouse.", item.ID);
    }

will display the number of the inv item that the mouse is over

*See Also: ,*

### GetProperty (inventory) 

*(Formerly known as GetInvProperty, which is now obsolete)*

    InventoryItem.GetProperty(string property)

Returns the custom property setting PROPERTY for the inventory item.

This command works with Number properties (it returns the number), and
with Boolean properties (returns 1 if the box was checked, 0 if not).

Use the equivalent GetTextProperty function to get a text property.

    if (inventory[1].GetProperty("Value") > 200)
      Display("Inventory item 1's value is over 200!");

will print the message if inventory item 1 has its “Value” property set
to more than 200.

*See Also:*

### GetTextProperty (inventory) 

*(Formerly known as GetInvPropertyText, which is now
obsolete) ILBRK *(Formerly known as
InventoryItem.GetPropertyText, which is now obsolete)**

    String InventoryItem.GetTextProperty(string property)

Returns the custom property setting PROPERTY for the inventory item.

This command works with Text properties only. The property's text will
be returned from this function.

Use the equivalent GetProperty function to get a non-text property.

    String description = inventory[2].GetTextProperty("Description");
    Display("Inv item 2's description: %s", description);

will retrieve inv item 2's “description” property and display it.

*See Also:*

### SetProperty (inventory) 

    bool InventoryItem.SetProperty(const string property, int value)

Sets the new *value for the custom *property
for the specified inventory item. Returns TRUE if such property exists
and FALSE on failure.**

This command works with Number properties (it sets the numeric value),
and with Boolean properties (sets FALSE is value is equal to 0, or TRUE
otherwise).

Use the equivalent SetTextProperty function to set new text property
value.

    iStone.SetProperty("Weight", 120);

will change Stone's “weight” custom property to 120.

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

*See Also:*

### SetTextProperty (inventory) 

    bool InventoryItem.SetTextProperty(const string property, const string value)

Sets the new *value text for the custom
*property for the specified inventory item. Returns TRUE if
such property exists and FALSE on failure.**

This command works with Text properties only. The property's text will
be changed to new value.

Use the equivalent SetProperty function to set a non-text property.

    iKey.SetTextProperty("Description", "A rusty key");

will change key's “description” property.

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

*See Also:*

### IsInteractionAvailable (inventory) 

*(Formerly known as IsInventoryInteractionAvailable, which is now
obsolete)*

    InventoryItem.IsInteractionAvailable(CursorMode)

Checks whether there is an event handler defined for activating the
inventory item in cursor mode MODE.

This function is very similar to RunInteraction, except that rather than
run the event handler script function, it simply returns
*true if something would have happened, or
*false if unhandled\_event would have been run.**

This is useful for enabling options on a verb-coin style GUI, for
example.

    if (iKeyring.IsInteractionAvailable(eModeLookat) == 0)
      Display("looking at this item would not do anything.");

*See Also: ,*

### RunInteraction (inventory) 

*(Formerly known as RunInventoryInteraction, which is now
obsolete)*

    InventoryItem.RunInteraction(CursorMode)

Runs the event handler as if the player had clicked the mouse on the
inventory item, using the specified cursor mode.

    if (button == eMouseLeftInv)
      inventory[game.inv_activated].RunInteraction(mouse.Mode);

will run the inventory event handler for the current cursor mode when
the player clicks on the item (Handle Inv Clicks needs to be enabled for
this to work)

*See Also: , ,*

### CursorGraphic property (inventory) 

    int InventoryItem.CursorGraphic

Gets/sets the sprite slot number of the inventory item's mouse cursor.
This is the sprite used as the mouse cursor when this inventory item is
selected.

**NOTE: This property is only used if the “Use selected
inventory graphic for cursor” setting in General Settings is turned
on.**

    Display("The key's cursor graphic is %d", iKey.CursorGraphic);

will display inventory item *iKey's cursor graphic.*

*Compatibility: Supported by **AGS 3.1.2 and
later versions.***

*See Also:*

### Graphic property (inventory) 

*(Formerly known as GetInvGraphic, which is now
obsolete)ILBRK *(Formerly known as SetInvItemPic, which is
now obsolete)**

    int InventoryItem.Graphic

Gets/sets the sprite slot number of the inventory item. You could use
this with the Object.Graphic property as a means of the player
'dropping' an inventory item, or it may be useful if you want to do a
Raw Drawn inventory window.

**NOTE: For backwards compatibility, if you change this
property and the CursorGraphic currently has the same sprite as the main
Graphic, then the CursorGraphic will be changed too.**

    int slot = player.ActiveInventory.Graphic;

will place the sprite number of the player's current inventory item into
slot.

*See Also: , ,*

### ID property (inventory) 

    readonly int InventoryItem.ID

Gets the inventory item's ID number. This is the item's number from the
editor, and is useful with commands such as Character.AddInventory which
require an inventory number to add.

    AddInventory(EGO, iShovel.ID);

uses the obsolete AddInventory command to add the shovel to EGO's
inventory

*See Also: ,*

### Name property (inventory) 

*(Formerly known as GetInvName, which is now obsolete)
ILBRK *(Formerly known as SetInvItemName, which is now
obsolete) ILBRK *(Formerly known as InventoryItem.GetName,
which is now obsolete) ILBRK *(Formerly known as
InventoryItem.SetName, which is now obsolete)****

    String InventoryItem.Name;

Gets/sets the name of the inventory item. This is the name which is
initially set under the Game tab, Inventory mode of the AGS Editor.

You can change this property if for example you want to change a 'bowl'
to a 'bowl with water in' but want to use the same inventory item for
it.

Note that the maximum length for the name of an inventory item is 24
characters - if the name you set is longer than this, it will be
truncated.

    Display("Active inventory: %s", player.ActiveInventory.Name);

will display the name of the player's current inventory item.

*See Also: , ,*

Maths functions and properties
------------------------------

### FloatToInt 

    int FloatToInt(float value, optional RoundDirection)

Converts the supplied floating point value into an integer.

This function is necessary because implicit conversions in the script
are not supported.

RoundDirection can be either *eRoundDown (the default),
*eRoundUp or *eRoundNearest, which specifies
what direction to round the floating point number in.***

    Display("Round down: %d", FloatToInt(10.7));
    Display("Round up: %d", FloatToInt(10.7, eRoundUp));
    Display("Round nearest: %d", FloatToInt(10.7, eRoundNearest));

displays the integer value of 10.7, rounded in the three different ways.

*See Also:*

### IntToFloat 

    float IntToFloat(int value)

Converts the supplied integer value into a floating point number.

This function is necessary because implicit conversions in the script
are not supported.

    float number = IntToFloat(10);

loads 10.0 into the variable *number.*

*See Also:*

### ArcCos 

    float Maths.ArcCos(float value)

Calculates the arc-cosine, in radians, of the specified value.

To convert an angle in radians to degrees, use .

    float angle = Maths.ArcCos(1.0);

calculates the arc-cosine of 1.0 and places it into variable
*angle.*

*See Also: , ,*

### ArcSin 

    float Maths.ArcSin(float value)

Calculates the arc-sine, in radians, of the specified value.

To convert an angle in radians to degrees, use .

    float angle = Maths.ArcSin(0.5);

calculates the arc-sine of 0.5 and places it into variable
*angle.*

*See Also: , ,*

### ArcTan 

    float Maths.ArcTan(float value)

Calculates the arc-tan, in radians, of the specified value.

To convert an angle in radians to degrees, use .

    float angle = Maths.ArcTan(0.5);

calculates the arc-tan of 0.5 and places it into variable
*angle.*

*See Also: , ,*

### ArcTan2 

    float Maths.ArcTan2(float y, float x)

Calculates the arctangent of y/x. This is well defined for every point
other than the origin, even if x equals 0 and y does not equal 0. The
result is returned in radians.

To convert an angle in radians to degrees, use .

    float angle = Maths.ArcTan2(-862.42, 78.5149);

calculates the arc-tan of -862.42 / 78.5149 and places it into variable
*angle.*

*See Also: ,*

### Cos 

    float Maths.Cos(float radians)

Calculates the cosine of the specified angle (in radians).

To convert an angle in degrees to radians, use .

    float cosine = Maths.Cos(Maths.DegreesToRadians(360.0));

calculates the cosine of 360 degrees (which is 1.0) and places it into
variable *cosine.*

*See Also: , , , ,*

### Cosh 

    float Maths.Cosh(float radians)

Calculates the hyperbolic cosine of the specified angle (in radians).

To convert an angle in degrees to radians, use .

    float hcos = Maths.Cosh(Maths.DegreesToRadians(360.0));

calculates the hyperbolic cosine of 360 degrees and places it into
variable *hcos.*

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also: , , ,*

### DegreesToRadians 

    float Maths.DegreesToRadians(float degrees)

Converts the supplied angle in degrees, to the equivalent angle in
radians.

Since the trigonometric functions such as Sin, Cos and Tan work in
radians, this function is handy if you know the angle you want in
degrees.

    float cosine = Maths.Cos(Maths.DegreesToRadians(360.0));

calculates the cosine of 360 degrees (which is 1.0) and places it into
variable *cosine.*

*See Also: , , ,*

### Exp 

    float Maths.Exp(float x)

Returns the exponential value of the floating-point parameter, x

The result is e to the power x, where e is the base of the natural
logarithm. On overflow, the function returns infinite and on underflow,
returns 0.

    float expValue = Maths.Exp(2.302585093);

calculates Exp of 2.302585093 (which should be 10) and places it into
the variable.

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also: ,*

### Log 

    float Maths.Log(float x)

Returns the natural logarithm (base e) of x.

x must be a positive non-zero number.

    float logVal = Maths.Log(9000.0);

calculates Log of 9000 (which should be 9.104980) and places it into the
variable.

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also: ,*

### Log10 

    float Maths.Log10(float x)

Returns the base-10 logarithm of x.

x must be a positive non-zero number.

    float logVal = Maths.Log(9000.0);

calculates Log10 of 9000 (which should be 3.954243) and places it into
the variable.

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also: ,*

### RadiansToDegrees 

    float Maths.RadiansToDegrees(float radians)

Converts the supplied angle in radians, to the equivalent angle in
degrees.

Since the trigonometic functions such as Sin, Cos and Tan work in
radians, this function is handy to convert the results of one of those
functions back to degrees.

    float halfCircle = Maths.RadiansToDegrees(Maths.Pi);

converts *PI radians into degrees (which is 180).*

*See Also: , , ,*

### RaiseToPower 

    float Maths.RaiseToPower(float base, float exponent)

Calculates the value of *base raised to the power
*exponent.**

This means that *base is multiplied by itself
*exponent times.**

    float value = Maths.RaiseToPower(4.0, 3.0);

calculates 4 to the power 3 (which is 64).

*See Also:*

### Sin 

    float Maths.Sin(float radians)

Calculates the sine of the specified angle (in radians).

To convert an angle in degrees to radians, use .

    float sine = Maths.Sin(Maths.DegreesToRadians(360.0));

calculates the sine of 360 degrees (which is 0) and places it into
variable *sine.*

*See Also: , , , ,*

### Sinh 

    float Maths.Sinh(float radians)

Calculates the hyperbolic sine of the specified angle (in radians).

To convert an angle in degrees to radians, use .

    float hsine = Maths.Sinh(Maths.DegreesToRadians(360.0));

calculates the hyperbolic sine of 360 degrees and places it into
variable *hsine.*

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also: , , , ,*

### Sqrt 

    float Maths.Sqrt(float value)

Calculates the square root of the supplied value.

The square root is the number which, when multiplied by itself, equals
*value.*

    Display("The square root of 4 is %d!", FloatToInt(Maths.Sqrt(4.0)));

displays the square root of 4 (rounded down to the nearest integer).

*See Also: , , ,*

### Tan 

    float Maths.Tan(float radians)

Calculates the tangent of the specified angle (in radians).

To convert an angle in degrees to radians, use .

    float tan = Maths.Tan(Maths.DegreesToRadians(45.0));

calculates the tan of 45 degrees (which is 1.0) and places it into
variable *tan.*

*See Also: , , , ,*

### Tanh 

    float Maths.Tanh(float radians)

Calculates the hyperbolic tangent of the specified angle (in radians).

To convert an angle in degrees to radians, use .

    float htan = Maths.Tanh(Maths.DegreesToRadians(45.0));

calculates the hyperbolic tan of 45 degrees and places it into variable
*htan.*

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also: , , , ,*

### Pi property 

    readonly float Maths.Pi

Gets the value of Pi (defined as 3.14159265358979323846).

    Display("Pi is %f!", Maths.Pi);

displays the value of Pi.

*See Also: , ,*

Mouse functions and properties
------------------------------

### ChangeModeGraphic 

*(Formerly known as ChangeCursorGraphic, which is now
obsolete)*

    Mouse.ChangeModeGraphic(CursorMode, int slot)

Changes the specified mouse cursor mode's cursor graphic to SLOT. This
allows you to dynamically change what a mouse cursor looks like.

**NOTE: To change what the Use Inventory cursor looks like,
you should change the active inventory item's property instead of using
this function.**

    mouse.ChangeModeGraphic(eModeLookat, 120);

will change the cursor's graphic for look mode to the image that's
imported in the sprite's manager slot 120.

*See Also: , , ,*

### ChangeModeHotspot 

*(Formerly known as ChangeCursorHotspot, which is now
obsolete)*

    Mouse.ChangeModeHotspot(CursorMode, int x, int y)

Permanently changes the specified mouse cursor mode's hotspot on the
cursor graphic to (X,Y). This is the offset into the graphic where the
click takes effect. (0,0) is the upper left corner of the cursor
graphic.

    mouse.ChangeModeHotspot(eModeWalkto, 10, 10);

will change the cursor's hotspot for walk mode to coordinates 10,10.

*See Also: ,*

### ChangeModeView 

    Mouse.ChangeModeView(CursorMode, int view)

Changes the specified mouse cursor mode's animation view to VIEW.

You can pass *view as -1 to stop the cursor from
animating.*

This allows you to dynamically change the view used for the cursor's
animation while the game is running.

    mouse.ChangeModeView(eModeLookat, ROLLEYES);

will change the Look cursor's view to ROLLEYES.

*See Also: ,*

### Click (mouse) 

    static void Click(MouseButton)

Fires mouse click event at current mouse position (at mouse.x /
mouse.y). This is in all aspects identical to what would happen if a
player clicked actual mouse button. This function may be useful to
simulate player actions in game, or create automatic demonstrations
(like tutorials).

    Mouse.SetPosition(100, 100);
    Mouse.Click(eMouseLeft);

This will simulate user click at (100,100).

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

*See Also: ,*

### ControlEnabled property 

    readonly static bool Mouse.ControlEnabled;

Tells if the mouse cursor movement is currently being controlled by AGS
engine; otherwise it is controlled by operation system. This is usually
true only when game is run in fullscreen mode.

This property may be useful to know if custom mouse speed setting is
applied or not.

    sldMouseSpeed.Visible = Mouse.ControlEnabled;

makes mouse speed slider visible only if the mouse is controlled by the
game.

*Compatibility: Supported by **AGS 3.3.5 and
later versions.***

*See Also:*

### DisableMode 

*(Formerly known as DisableCursorMode, which is now
obsolete)*

    Mouse.DisableMode(int mode)

Disables the mouse cursor MODE. Any attempts to set the cursor to this
mode while it is disabled (such as using UseModeGraphic) will fail. This
function also greys out and disables any interface buttons whose
left-click command is set as “Set mode X”, where X is equal to MODE.

If the current cursor mode is MODE, then the engine will change it to
the next enabled standard cursor.

    mouse.DisableMode(eModeWalkto);

will make the walk mode unavailable until it's enabled again.

*See Also:*

### EnableMode 

*(Formerly known as EnableCursorMode, which is now
obsolete)*

    Mouse.EnableMode(int mode)

Re-enables the mouse cursor mode MODE. This function also enables any
interface buttons which were disabled by the DisableMode command.

    mouse.EnableMode(eModeWalkto);

will enable cursor mode walk which was disabled before.

*See Also:*

### GetModeGraphic 

    static int Mouse.GetModeGraphic(CursorMode)

Returns the sprite slot number of the specified mouse cursor mode.

This could be useful if you want to change it manually with
ChangeModeGraphic but be able to remember what it was before.

    Display("The current mouse cursor sprite is %d.", mouse.GetModeGraphic(mouse.Mode));

will display the sprite slot number of the current mouse cursor.

*See Also:*

### IsButtonDown 

*(Formerly known as global function IsButtonDown, which is now
obsolete)*

    Mouse.IsButtonDown(MouseButton)

Tests whether the user has the specified mouse button down. BUTTON must
either be eMouseLeft, eMouseRight or eMouseMiddle.

Returns *true if the button is currently pressed,
*false if not. This could be used to test the length of a
mouse click and similar effects.**

    int timer=0;  // (at top of script file)
    if (mouse.IsButtonDown(eMouseRight)) {
      if (timer == 40) {
        Display("You pressed the right button for 1 sec");
        timer = 0;
      }
      else {
        timer++;
      }
    }

will display the message if the player presses the right button for 1
sec.

*Compatibility: *eMouseMiddle supported by
**AGS 3.2.0 and later versions. ILBRK
*eMouseLeft and *eMouseRight supported by all
versions.******

*See Also:*

### SaveCursorUntilItLeaves 

*(Formerly known as SaveCursorForLocationChange, which is now
obsolete)*

    Mouse.SaveCursorUntilItLeaves()

Saves the current mouse cursor, and restores it when the mouse leaves
the current hotspot, object or character.

This allows you to temporarily change the mouse cursor when the mouse
moves over a hotspot, and have it automatically change back to the old
cursor when the player moves the mouse away.

**NOTE: You must call this **BEFORE you change
to your new temporary cursor, or the new cursor will be saved by this
command.****

    mouse.SaveCursorUntilItLeaves();
    mouse.Mode = eModeTalk;

will change the cursor mode to Talk for as long as the mouse is over the
current object

*See Also:*

### SelectNextMode 

*(Formerly known as SetNextCursorMode, which is now
obsolete)*

    Mouse.SelectNextMode()

Selects the next enabled mouse cursor mode. This is useful for
Sierra-style right-click cycling through modes. This function will
choose the next mode marked as a Standard Mode, and will also use the
Use Inventory mode if the player has an active inventory item.

*See Also:*

### SetBounds 

*(Formerly known as SetMouseBounds, which is now obsolete)*

    Mouse.SetBounds(int left, int top, int right, int bottom)

Restricts the area where the mouse can move on screen. The four
parameters are the relevant pixel co-ordinates of that edge of the
bounding rectangle. They are in the usual range (0,0) - (320,200).

You can pass (0,0,0,0) to disable the bounding rectangle and allow the
mouse to move everywhere, as usual.

*NOTE: The effect of this function only lasts until the
player leaves the screen, at which point the cursor bounds will be
reset.*

    mouse.SetBounds(160, 100, 320, 200);

will restrict the mouse cursor to the bottom-right quarter of the
screen.

*See Also:*

### SetPosition (mouse) 

*(Formerly known as SetMousePosition, which is now
obsolete)*

    Mouse.SetPosition(int x, int y)

Moves the mouse pointer to screen co-ordinates (X,Y). They are in the
usual range (0,0) - (320,200/240). The mouse.x and mouse.y variables
will be updated to reflect the new position.

**NOTE: Only use this command when absolutely necessary.
Moving the mouse cursor for the player is a sure way to irritate them if
you do it too often during the game.**

    mouse.SetPosition(160, 100);

will place the mouse cursor in the centre of the screen.

*See Also:*

### Speed property (mouse) 

    static float Mouse.Speed;

Gets/sets in-game mouse cursor speed. 1.0 is default, values in the
range 0-1 make cursor movement slower, values higher than 1 make cursor
movement faster.

Mouse speed changed this way will be saved to the configuration file
when player exits the game. Next time game starts it will restore the
last value you applied, unless player has modified it in the setup
program.

The custom mouse speed is only applied if mouse cursor movement is
currently being controlled by the game, which is usually true only when
game is run in fullscreen mode. Setting this property has no effect
otherwise. You can use to know if speed will be applied.

**NOTE: It is strongly advised to **NEVER use
this parameter to achieve gameplay effect (such as character's loss of
coordination, and so forth).****

    Mouse.Speed = IntToFloat(sldMouseSpeed.Value) / 10.0;

converts slider control's position into mouse speed.

*Compatibility: Supported by **AGS 3.3.5 and
later versions.***

*See Also: ,*

### Update 

*(Formerly known as RefreshMouse, which is now obsolete)*

    Mouse.Update();

Updates the global variables “mouse.x” and “mouse.y” with the current
position of the mouse. Normally, these variables are set just before
each script function is executed. However, if you have a very long
script where the mouse may have moved since the start of the function,
and you need the exact current location, then this command will update
the variables.

    Display("The mouse was at: %d, %d.", mouse.x, mouse.y);
    mouse.Update();
    Display("The mouse is now at: %d, %d.", mouse.x, mouse.y);

will display the mouse position just before each dialog box is displayed

### UseDefaultGraphic 

*(Formerly known as SetDefaultCursor, which is now
obsolete)*

    Mouse.UseDefaultGraphic()

Changes the appearance of the mouse cursor to the default for the
current cursor mode. Use this to restore the cursor picture after you
changed it with the UseModeGraphic function.

*See Also:*

### UseModeGraphic 

*(Formerly known as SetMouseCursor, which is now obsolete)*

    Mouse.UseModeGraphic(CursorMode)

Changes the appearance of the mouse cursor to use the specified cursor.
Unlike the Mouse.Mode property, this does not change the mode used if
the user clicks on a hotspot. This is useful for displaying a “wait”
cursor temporarily.

    mouse.UseModeGraphic(eModeWait);

will change the mouse cursor to the cursor 'Wait' specified in the
Cursors tab.

*See Also: , ,*

### Mode property (mouse) 

*(Formerly known as GetCursorMode, which is now
obsolete)ILBRK *(Formerly known as SetCursorMode, which is
now obsolete)**

    int Mouse.Mode;

Gets/sets the current mode of the mouse cursor. This is one of the
cursor modes from your Cursors tab (but with eMode prepended). For
example, a cursor mode called “Walk to” on your cursors tab would be
eModeWalkto.

Setting this changes both the appearance of the cursor and the Cursor
Mode used if the player clicks on a hotspot.

    if (mouse.Mode == eModeWalkto)
    {
       // code here
    }

will execute the code only if the current cursor mode is MODE 0 (WALK).

*See Also: , ,*

### Visible property (mouse) 

*(Formerly known as HideMouseCursor, which is now
obsolete)ILBRK *(Formerly known as ShowMouseCursor, which
is now obsolete)**

    bool Mouse.Visible;

Gets/sets whether the mouse cursor is visible. This is initially true by
default, but setting this to false is useful for briefly hiding the
cursor on occasions when you don't want it around.

If you want the Lucasarts-style where the mouse cursor is never visible
during cutscenes then a much easier solution is simply to import a
transparent graphic over the default wait cursor, so that the Wait
cursor becomes invisible.

    mouse.Visible = false;
    Wait(40);
    mouse.Visible = true;

hides the mouse, waits for a second, then turns it back on again

*See Also:*

Multimedia functions
--------------------

### CDAudio 

    CDAudio (eCDAudioFunction, int param)

This function allows you to play and control an audio CD in your game.
Different tasks are performed, depending on the value of the
AudioFunction parameter. If there is no CD-ROM drive on the system, the
function does nothing.

The PARAM parameter is used by some of the functions for various
reasons; if it is not needed for the particular function you are
calling, pass zero instead.

The tasks performed are as follows depending on the COMMAND parameter:

    eCDIsDriverPresent - checks if there is a CD-ROM driver available on
       the system. Returns 1 if there is, and 0 if there is not.
    eCDGetPlayingStatus - checks whether the CD drive is currently playing
       an audio track. Returns 1 if it is, and 0 if it is not.
    eCDPlayTrack - starts playback from track PARAM on the CD. If the track
       does not exist, or if it is a data track, nothing happens.
    eCDPausePlayback - pauses the currently playing audio track.
    eCDResumePlayback - continues from where the track was paused.
    eCDGetNumTracks - returns the number of tracks on the CD
       currently in the drive. If the drive is empty, returns 0.
    eCDEject - ejects the drive tray if the drive has the ability. This is
       a feature you'll play with to start off because it's neat, and then
       realize that it has no real use in your game.
       Your script does not continue until the drive is fully ejected.
    eCDCloseTray - the reverse of Eject. This will pull the drive tray back
       in again. Your script does not continue until the drive has been
       fully closed.
    eCDGetCDDriveCount - returns the number of CD drives in the
       system, normally 1.
    eCDSelectActiveCDDrive - changes the current CD drive to PARAM,
       where PARAM ranges from 1 to (number of CD drives). All the other
       CD Audio functions operate on the current CD drive.

NOTE: These CD Audio functions are slow compared to all the other script
functions. This will not be noticeable if you call them from most
scripts, but using CDAudio in a repeatedly\_execute script will
noticeably slow down the game.

**Cross-Platform Support**

Windows: ** Yes, but supports 1 CD-ROM drive only ILBRK
MS-DOS: ** Yes, if CD-ROM device driver loaded ILBRK Linux:
** Yes, but supports 1 CD-ROM drive only ILBRK MacOS:
** No ********

    CDAudio(eCDPlayTrack, 3);

will play track 3 of the CD that's in the CD ROM drive.

### IsAudioPlaying 

*(Formerly known as IsMusicPlaying, which is now obsolete)
ILBRK *(Formerly known as IsSoundPlaying, which is now
obsolete)**

    static bool Game.IsAudioPlaying(optional AudioType)

Returns *true if there is currently audio playing of the
specified type. If you don't supply an audio type, then
*true will be returned if there is any audio at all playing
in the game.**

If no audio of the specified type is playing, returns
*false. You can use this to wait for some music to finish
playing, for example.*

    while (Game.IsAudioPlaying(eAudioTypeMusic))
    {
      Wait(1);
    }

waits for any currently playing music to finish.

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also:*

### IsSpeechVoxAvailable 

    IsSpeechVoxAvailable()

Returns whether the SPEECH.VOX file is being used by the game. This
could be useful if you have an optional speech download pack, and you
want to know whether the player has it or not.

Returns 1 if the speech files are available, 0 if not.

    if (IsSpeechVoxAvailable()==0)
        Display ("You don't have the voice pack");

will display a message if the voice pack is not available.

**NOTE: This function used to be called IsVoxAvailable, but
has now been renamed to avoid confusion.**

*See Also:*

### PlayFlic 

    PlayFlic (int flic_number, int options)

Plays a FLI or FLC animation. The game checks for FLICx.FLC and
FLICx.FLI (where X is FLIC\_NUMBER) and if it finds one, plays it.

OPTIONS has these meanings:

    0  player can't skip animation
    1  player can press ESC to skip animation
    2  player can press any key or click mouse to skip animation
    +10 (ie.10,11,12) do not stretch to full-screen, just play at flc size
    +100 do not clear the screen before starting playback

The game is paused while the animation plays.

    PlayFlic(2, 1);

will play flic2 and the player will be able to skip the flic by pressing
the ESC key.

*See Also:*

### PlaySilentMIDI 

    PlaySilentMIDI (int music_number)

This command is obsolete.

Use the AudioClip.Play command and set its Volume property to 0 to
simulate this effect.

*See Also: ,*

### PlayVideo 

    PlayVideo (string filename, VideoSkipStyle, int flags)

Plays an AVI, MPG or OGG Theora file, or any other file type supported
by Media Player. The game is paused while the video plays.

*VideoSkipStyle defines how the player can skip the video:*

    eVideoSkipNotAllowed     player can't skip video
    eVideoSkipEscKey         player can press ESC to skip video
    eVideoSkipAnyKey         player can press any key to skip video
    eVideoSkipAnyKeyOrMouse  player can press any key or click mouse to skip

FLAGS can be one of the following:

    0: the video will be played at original size, with AVI audio
    1: the video will be stretched to full screen, with appropriate
       black borders to maintain its aspect ratio and AVI audio.
    10: original size, with game audio continuing (AVI audio muted)
    11: stretched to full screen, with game audio continuing (AVI audio muted)

There are two distinct type of videos that the PlayVideo function can
play.

The first is OGG Theora, which is a recently introduced video file
format. AGS has built-in support for playing these videos, so everyone
who plays your game will be able to see the video. OGG Theora videos are
also built into the game EXE file when you compile the game (just make
sure the file has a .OGV extension and is placed in your main game
folder).

The second type of files that AGS can play is anything supported by
Windows Media Player. This includes AVI, MPG and more. However, in order
for these to work on the player's system, they will need to have the
correct codecs installed. For example, if you create your video with the
XVid codec, the player will need to have XVid installed to be able to
view it. These types of video cannot be included into the game EXE, so
you will have to place them separately in the Compiled folder for them
to work.

**NOTE: In 256-colour games, PlayVideo is not supported.
Please use a FLC/FLI video with the command instead.**

**Cross-Platform Support**

Windows: ** Yes ILBRK MS-DOS: ** No ILBRK
Linux: ** No ILBRK MacOS: ** Yes ********

    PlayVideo("intro.mpg", eVideoSkipEscKey, 1);

will play the video Intro.mpg, allowing the player to skip with ESC if
they've seen it before.

*Compatibility: OGG Theora supported by **AGS
3.1.1 and later versions.***

*See Also:*

### SetAudioTypeSpeechVolumeDrop 

*(Formerly known as game.speech\_music\_drop, which is now
obsolete)*

    static Game.SetAudioTypeSpeechVolumeDrop(AudioType, int volumeReduction)

Changes the VolumeReductionWhileSpeechPlaying of the specified
*AudioType. This changes the setting, initially set in the
Audio Types part of the editor. It specifies how much the volume of
clips of this type will be reduced by while speech is playing.*

Specify 0 for no volume adjustment, up to 100 which will completely
silence these audio clips while speech is playing.

    Game.SetAudioTypeSpeechVolumeDrop(eAudioTypeMusic, 25);

will reduce the volume of Music audio clips by 25 percentage points
while speech is playing.

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also:*

### SetAudioTypeVolume 

*(Formerly known as SetSoundVolume, which is now obsolete)*

    static Game.SetAudioTypeVolume(AudioType, int volume, ChangeVolumeType)

Changes the default volume of the specified *AudioType.
This allows you to change the volume of all audio clips of a particular
type, so that you can easily control sound and music volume separately,
for example.*

VOLUME ranges from 0-100, where 100 is the loudest, and 0 will mute
sound of that type completely.

Possible values for *ChangeVolumeType are:*

    eVolChangeExisting      change the volume of currently playing audio clips
    eVolSetFutureDefault    change the default volume for clips of this type
    eVolExistingAndFuture   change both currently playing and future audio

Initially general AudioType volume is not set, meaning that all future
audio will be playing using their own custom volumes. If you use the
*eVolSetFutureDefault or
*eVolExistingAndFuture, then the DefaultVolume property for
all audio clips of this type will be overridden. This means that any
DefaultVolume set up in the editor will be lost.**

    Game.SetAudioTypeVolume(eAudioTypeMusic, 20, eVolExistingAndFuture);

will change the volume of all currently playing and future music to
`20%`.

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also: , ,*

### SetSpeechVolume 

    SetSpeechVolume (int volume)

Sets the volume for in-game speech. VOLUME ranges from 0-255, where 255
is the loudest. The default speech volume is 255 so this function can
only be used to reduce the volume.

    SetSpeechVolume(200);

will set the speech volume to 200.

*See Also:*

### StopAudio 

*(Formerly known as Game.StopSound, which is now obsolete)
ILBRK *(Formerly known as StopMusic, which is now
obsolete)**

    static Game.StopAudio(optional AudioType)

Stops all currently playing audio. If you pass no parameters, then all
audio will be stopped. Alternatively, you can pass one of the AudioTypes
which will only stop audio clips of that type.

If there are any audio clips queued up with PlayQueued, they will also
be cancelled.

    Game.StopAudio();

will stop all currently playing audio.

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also: , ,*

Object functions and properties
-------------------------------

### Animate (object) 

*(Formerly known as AnimateObject, which is now obsolete)
ILBRK *(Formerly known as AnimateObjectEx, which is now
obsolete)**

    Object.Animate(int loop, int delay, optional RepeatStyle,
                   optional BlockingStyle, optional Direction)

Starts the object animating, using loop number LOOP of its current view.
The overall speed of the animation is set with DELAY, where 0 is the
fastest, and increasing numbers mean slower. The delay for each frame is
worked out as DELAY + FRAME SPD, so the individual frame speeds are
relative to this overall speed.

The *RepeatStyle parameter sets whether the animation will
continuously repeat the cycling through the frames. This can be
*eOnce (or zero), in which case the animation will start
from the first frame of LOOP, and go through each frame in turn until
the last frame, where it will stop. If RepeatStyle is
*eRepeat (or 1), then when the last frame is reached, it
will go back to the first frame and start over again with the animation.
If RepeatStyle is 2 then it will do the animation once, but then return
the graphic to the first frame and stop (whereas repeat=0 will leave the
graphic on the last frame).***

For *blocking you can pass either eBlock (in which case the
function will wait for the animation to finish before returning), or
eNoBlock (in which case the animation will start to play, but your
script will continue). The default is eBlock.*

*direction specifies which way the animation plays. You can
either pass eForwards (the default) or eBackwards.*

You need to use SetView at some stage before this command, in order to
set up the object's current view.

    object[0].Animate(2, 5);
    object[1].Animate(1, 3, eOnce, eBlock, eBackwards);

will animate object 0 using loop 2 of its current view, at speed 5, and
play the animation once only. This happens in the background. Then,
object 1 will animate backwards using loop 1 of its current view, at
speed 3. The function won't return until the animation is finished.

*See Also: , , ,*

### GetAtScreenXY (object) 

*(Formerly known as global function GetObjectAt, which is now
obsolete)*

    static Object* Object.GetAtScreenXY(int x, int y)

Checks if there is a room object at SCREEN co-ordinates (X,Y). Returns
the object if there is, or *null if there is not.*

See the description of GetLocationName for more on screen co-ordinates.

    if (Object.GetAtScreenXY(211,145) == oRock) {
      // code here
    }

will execute the code only if object oRock is on the screen coordinates
211,145.

*See Also: ,*

### GetProperty (object) 

*(Formerly known as GetObjectProperty, which is now
obsolete)*

    Object.GetProperty(string property)

Returns the custom property setting of the PROPERTY for the specified
object.

This command works with Number properties (it returns the number), and
with Boolean properties (returns 1 if the box was checked, 0 if not).

Use the equivalent GetTextProperty function to get a text property.

    if (object[0].GetProperty("Value") > 200)
      Display("Object 0's value is over 200!");

will print the message if object 0 has its “Value” property set to more
than 200.

*See Also:*

### GetTextProperty (object) 

*(Formerly known as GetObjectPropertyText, which is now
obsolete) ILBRK *(Formerly known as Object.GetPropertyText,
which is now obsolete)**

    String Object.GetTextProperty(string property)

Returns the custom property setting of the PROPERTY for the specified
object.

This command works with Text properties only. The property's text will
be returned from this function.

Use the equivalent GetProperty function to get a non-text property.

    String description = object[0].GetTextProperty("Description");
    Display("Object 0's description: %s", description);

will retrieve Object 0's “description” property then display it.

*See Also:*

### SetProperty (object) 

    bool Object.SetProperty(const string property, int value)

Sets the new *value for the custom *property
for the specified room object. Returns TRUE if such property exists and
FALSE on failure.**

This command works with Number properties (it sets the numeric value),
and with Boolean properties (sets FALSE is value is equal to 0, or TRUE
otherwise).

Use the equivalent SetTextProperty function to set new text property
value.

    oTable.SetProperty("ItemCapacity", 5);

will change Table's “ItemCapacity” custom property to 5.

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

*See Also:*

### SetTextProperty (object) 

    void Object.SetTextProperty(const string property, const string value)

Sets the new *value text for the custom
*property for the specified room object.**

This command works with Text properties only. The property's text will
be changed to new value.

Use the equivalent SetProperty function to set a non-text property.

    oTable.SetTextProperty("Description", "A dull furniture");

will change table's “description” property.

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

*See Also:*

### IsCollidingWithObject (object) 

*(Formerly known as AreObjectsColliding, which is now
obsolete)*

    bool Object.IsCollidingWithObject(Object* obj2)

Checks if the specified object and OBJ2 are touching each other. Returns
*true if they are, and *false if they are
not.**

**NOTE: This function only performs a rectangular check,
even when pixel-perfect click detection is turned on.**

    if (object[2].IsCollidingWithObject(object[3]))
    {
      Display("object 2 and 3 are colliding!");
    }

will display the message if the objects 2 and 3 are colliding.

*See Also:*

### MergeIntoBackground 

*(Formerly known as MergeObject, which is now obsolete)*

    Object.MergeIntoBackground()

Merges the object into the background scene for this room. By doing
this, the object becomes part of the background and so does not slow the
game down. This is a 1-way operation - once the object has been merged,
it cannot be changed back and the state of the room is permanently
altered. Therefore you should only use this function if a game event has
occurred that means the room is permanently changed.

**NOTE: after calling this function, you cannot use the
object any more and it is permanently removed from the game.**

**NOTE: objects can only be merged if the object graphic
was imported at the same colour depth as the background graphic.**

    object[3].MergeIntoBackground();

will merge the object's image into the room's background image and make
the object unusable.

### Move (object) 

*(Formerly known as MoveObject, which is now obsolete)
ILBRK *(Formerly known as MoveObjectDirect, which is now
obsolete)**

    Object.Move(int x, int y, int speed, optional BlockingStyle,
                optional WalkWhere);

Starts the object moving from its current location to (X,Y). It will
move at speed SPEED, which uses the same scale as the character Walk
Speed values in the AGS Editor.

If *BlockingStyle is eNoBlock (the default), then control
returns to the script immediately, and the object will move in the
background.*

If *BlockingStyle is eBlock then this command will wait for
the object to finish moving before your script resumes.*

If *WalkWhere is eWalkableAreas (the default), then the
object will attempt to get as close a possible to (X,Y) by using the
room's walkable areas.*

If *WalkWhere is eAnywhere, then the object will simply
walk directly from its current location to (X,Y), ignoring the room
walkable areas.*

    object[2].Move(125, 40, 4, eBlock);

will move object 2 to 125,40 and return control to the player when the
object gets there.

*See Also: , ,*

### RemoveTint (object) 

*(Formerly known as RemoveObjectTint, which is now
obsolete)*

    Object.RemoveTint()

Undoes the effects of calling Tint, and returns the object to using the
room's ambient tint.

    object[1].Tint(0, 250, 0, 30, 100);
    Wait(40);
    object[1].RemoveTint();

will tint object 1 green for a second, then turn it back to normal.

*See Also:*

### IsInteractionAvailable (object) 

    Object.IsInteractionAvailable(CursorMode)

Checks whether there is an event handler defined for activating the room
object in cursor mode MODE.

This function is very similar to RunInteraction, except that rather than
run the event handler script function, it simply returns
*true if something would have happened, or
*false if unhandled\_event would have been run.**

    if (oDoor.IsInteractionAvailable(eModeInteract) == 0)
      Display("interacting with this door would not do anything.");

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

*See Also: ,*

### RunInteraction (object) 

*(Formerly known as RunObjectInteraction, which is now
obsolete)*

    Object.RunInteraction(CursorMode)

Runs the event handler as if the player had clicked the mouse on the
object in the current room, using the specified cursor mode.

    object[3].RunInteraction(eModeInteract);

will execute the code defined in object 3's “Interact with object” event
handler.

*See Also: , , ,*

### SetLightLevel (object) 

    void Object.SetLightLevel(int light_level)

Sets individual light level for this room object.

The light level is from **-100 to 100.**

In 8-bit games you cannot use positive light level for brightening
effect, but you may still use negative values to produce darkening
effect.

To disable object lighting and tinting effects, call SetLightLevel with
parameter *light\_level 0.*

**NOTE: Setting a light level will disable any RGB tint set
for the object.**

**NOTE: Object's individual light level OVERRIDES both
ambient light level and local region light level.**

    oLamp.LightLevel = 100;

This will give the lamp maximal individual brightness.

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

*See Also: , , ,*

### SetPosition (object) 

*(Formerly known as SetObjectPosition, which is now
obsolete)*

    Object.SetPosition(int x, int y)

Changes the object's position to (X,Y). These co-ordinates specify the
lower-left hand corner of the object.

This command is equivalent to setting the object.X and object.Y
separately, but provides a more convenient way of doing so.

**NOTE: This command cannot be used while the object is
moving.**

    object[2].SetPosition(50, 100);

will change object's 2 position to 50,100.

*See Also: ,*

### SetView 

*(Formerly known as SetObjectFrame, which is now obsolete)
ILBRK *(Formerly known as SetObjectView, which is now
obsolete)**

    Object.SetView(int view, optional int loop, optional int frame)

Sets the object's view to VIEW, and changes the object's graphic to
FRAME of LOOP in VIEW. If you do not supply the loop or frame, they will
be left unchanged.

You must use this command before calling Animate, so that AGS knows
which view to animate the object with.

    object[3].SetView(14);
    object[1].SetView(5, 2, 0);

will change object 3's view to view number 14, and change object 1 to
view 5, loop 2, frame 0.

*See Also:*

### StopAnimating (object) 

    Object.StopAnimating()

Stops the object from animating. It will remain on its current frame
until you change it or start a new animation.

    if (object[2].Animating) {
      object[2].StopAnimating();
    }

will stop object 2 animating if it currently is doing so.

*See Also: ,*

### StopMoving (object) 

*(Formerly known as StopObjectMoving, which is now
obsolete)*

    Object.StopMoving()

Stops the object from moving. It will remain in its current position
until any further commands are issued.

    if (object[2].Moving) {
      object[2].StopMoving();
    }

will stop object 2 moving if it currently is doing so.

*See Also: , ,*

### Tint (object) 

*(Formerly known as SetObjectTint, which is now obsolete)*

    Object.Tint(int red, int green, int blue,
                int saturation, int luminance)

Tints the object on the screen to (RED, GREEN, BLUE) with SATURATION
percent saturation.

This function applies a tint to a specific object. For the meaning of
all the parameters, see .

The tint set by this function overrides any ambient tint set for the
room. For this reason, passing the SATURATION as 0 to this function does
not turn it off - rather, it ensures that no tint is applied to the
object (even if an ambient tint is set).

To remove the tint set by this function and return to using the ambient
tint for this object, call .

**NOTE: This function only works in hi-colour games and
with hi-colour sprites.**

    object[1].Tint(0, 250, 0, 30, 100);

will tint object 1 green.

*See Also: ,*

### Animating property (object) 

*(Formerly known as IsObjectAnimating, which is now
obsolete)*

    readonly bool Object.Animating

Returns 1 if the specified object is currently animating. ILBRK Returns
0 if the object has finished its animation.

This property is read-only. To change object animation, use the command.

    object[2].Animate(5, 0);
    while (object[2].Animating) Wait(1);

will animate object 2 and wait until the animation finishes.

In reality, you would simply use the Blocking parameter of Animate so
you wouldn't need to do this.

*See Also: , , , ,*

### Baseline property (object) 

*(Formerly known as GetObjectBaseline, which is now
obsolete) ILBRK *(Formerly known as SetObjectBaseline,
which is now obsolete)**

    int Object.Baseline

Gets/sets the object's baseline. This allows you to modify the line you
can set in the editor. You can disable the baseline (and revert to using
the base of the object's image on the screen) by setting it to 0.

Otherwise, set it to the Y screen co-ordinate you want to use, normally
from 1 to 200 unless you have a taller than usual room.

If you want to get the baseline and it returns 0, then the baseline is
the object's Y co-ordinate.

    object[4].Baseline = 100;

will change object's 4 baseline to a line positioned at y coordinate
100.

*See Also: , ,*

### BlockingHeight property (object) 

    int Object.BlockingHeight

Gets/sets the object's blocking height.

The blocking height determines how large of a blocking rectangle the
object exerts to stop characters walking through it. If this is set to 0
(the default), then the blocking rectangle is automatically calculated
to be the object's width, and 5 pixels high.

You can manually change the setting by entering a blocking height in
pixels, which is the size of walkable area that the object effectively
removes by being there.

**NOTE: This property has no effect unless the property is
set to *true.***

    oRock.BlockingHeight = 20;

will make the Rock object block 20 pixels high (10 above and 10 below
its baseline)

*See Also: ,*

### BlockingWidth property (object) 

    int Character.BlockingWidth

Gets/sets the object's blocking width.

The blocking width determines how large of a blocking rectangle the
object exerts to stop characters walking through it. If this is set to 0
(the default), then the blocking rectangle is automatically calculated
to be the object's width, and 5 pixels high.

You can manually change the setting by entering a blocking width in
pixels, which is the size of walkable area that the object effectively
removes by being there.

**NOTE: This property has no effect unless the property is
set to *true.***

    oRock.BlockingWidth = 50;

will make the Rock object block 50 pixels wide (25 pixels to the left of
his centre, and 25 to the right)

*See Also: ,*

### Clickable property (object) 

*(Formerly known as SetObjectClickable, which is now
obsolete)*

    bool Object.Clickable

Gets/sets whether the object is recognised as something which the player
can interact with.

If this is set to 1, then the player can look at, speak to, and so on
the object. If it is set to 0, then the object will not respond to
clicks and the mouse will activate whatever is behind the object. This
is useful if you are using the object for visual effects and don't want
it to be clicked on by the player.

    object[2].Clickable = 0;

will make object 2 ignore clicks from the player.

*See Also: ,*

### Frame property (object) 

    readonly int Object.Frame

Gets the frame number that the object is currently set to. If the object
is not currently assigned a view, this will be 0 (in which case the
Graphic property will hold its sprite number).

This property is read-only. To change the frame, use the animation
functions.

    Display("Object oDoor's frame is currently %d.", oDoor.Frame);

will display the oDoor object's current frame number

*SeeAlso: , ,*

### Graphic property (object) 

*(Formerly known as GetObjectGraphic, which is now
obsolete) ILBRK *(Formerly known as SetObjectGraphic, which
is now obsolete)**

    int Object.Graphic

Gets/sets the sprite slot number that the object is currently displayed
as. You can get the slot number from the Sprite Manager. If the object
is currently animating (from an Animate command) and you change the
Graphic, then the animation will be stopped.

    object[2].Graphic = 100;

will change the object 2's image to the image stored in the sprite
manager's slot 100.

*See Also:*

### ID property (object) 

    readonly int Object.ID

Gets the object's ID number. This is the object's number from the
editor, and is useful if you need to interoperate with legacy code that
uses the object's number rather than name.

    MoveObject(oRock.ID, 100, 50, 5);

uses the obsolete MoveObject function to move the Rock object to (100,
50) at speed 5.

### IgnoreScaling property (object) 

    bool Object.IgnoreScaling

Gets/sets whether the object is affected by walkable area scaling. This
is equivalent, **though opposite, to the “Use walkable area
scaling” checkbox in the Objects pane of the editor.**

If this is set to true, the object will always be the same size. If it
is set to false, then the object will be stretched or shrunk as
appropriate on walkable areas.

    oDoor.IgnoreScaling = true;

will tell the Door object not to be scaled on walkable areas.

*See Also:*

### IgnoreWalkbehinds property (object) 

*(Formerly known as SetObjectIgnoreWalkbehinds, which is now
obsolete)*

    bool Object.IgnoreWalkbehinds

Sets whether the object is affected by walkbehind areas. Setting this to
*false (the default setting) means that the object will be
placed behind walk-behind areas according to the relevant baselines.*

If this is set to *true, then the object will never be
placed behind a walk-behind area. This is useful if for example you want
an object to be a picture on a wall, and the wall can be walked behind -
but you also want it to act correctly in relation to characters, so
changing its baseline wouldn't work.*

**NOTE: enabling this property does not currently work
properly when using the Direct3D driver.**

    object[1].IgnoreWalkbehinds = true;

will make object 1 ignore walk behinds.

*See Also: , ,*

### Loop property (object) 

    readonly int Object.Loop

Gets the loop that the object is currently set to. If the object is not
currently assigned a view, this will be 0 (in which case the Graphic
property will hold its sprite number).

This property is read-only. To change the loop, use the animation
functions.

    Display("Object oDoor's loop is currently %d.", oDoor.Loop);

will display the oDoor object's current loop number

*SeeAlso: , ,*

### Moving property (object) 

*(Formerly known as IsObjectMoving, which is now obsolete)*

    readonly bool Object.Moving

Returns 1 if the object is currently moving, or 0 if not.

This property is read-only; to change the object's movement, use the and
commands.

    object[2].Move(125,40,3);
    while (object[2].Moving) Wait(1);

will move object 2 to 125,40 and return control to the player when the
object gets there.

*See Also: ,*

### Name property (object) 

*(Formerly known as GetObjectName, which is now obsolete)
ILBRK *(Formerly known as Object.GetName, which is now
obsolete)**

    readonly String Object.Name;

Gets the name of the object.

**NOTE: This property is read-only. It is not currently
possible to change the name of an object at run-time.**

    Display("Object 0's name is %s.", object[0].Name);

will retrieve and then display object 0's name.

*See Also:*

### Solid property (object) 

    bool Object.Solid

Gets/sets whether the object can be walked through by characters.

If this is set to true, then the object is solid and will block the path
of solid characters. If this is set to false, then the object can be
walked through by characters.

**NOTE: solid objects only block characters, they don't
block other objects from moving through them.**

    oSmallrock.Solid = true;

will mean that the Smallrock object blocks the path of characters.

*See Also: ,*

### Transparency property (object) 

*(Formerly known as SetObjectTransparency, which is now
obsolete)*

    int Object.Transparency

Gets/sets the object's transparency level.

If this is set to 100, it means that the object is totally invisible,
and lower values represent varying levels of transparency. Set this to 0
to stop the object being transparent.

**NOTE: Transparency only works in 16-bit and 32-bit colour
games.**

**NOTE: When using the DirectX 5 driver, a large
transparent object can significantly slow down AGS.**

Some rounding is done internally when the transparency is stored –
therefore, if you get the transparency after setting it, the value you
get back might be one out. Therefore, using a loop with
`object[0].Transparency++;` is not recommended as it will probably end
too quickly.

In order to fade an object in/out, the best approach is shown in the
example below:

    int trans = object[0].Transparency;
    while (trans < 100) {
      trans++;
      object[0].Transparency = trans;
      Wait(1);
    }

will gradually fade out the object from its current transparency level
to being fully invisible.

*See Also: ,*

### View property (object) 

    readonly int Object.View

Gets the view that the object is currently set to. This is either the
view number, or 0 if the object is not currently assigned a view (in
which case the Graphic property will hold its sprite number instead).

This property is read-only. To change the view, use the SetView
function. To remove the view, set the Graphic property to a sprite slot.

    Display("Object oDoor's view is currently view %d.", oDoor.View);

will display the oDoor object's current view number

*SeeAlso: , , ,*

### Visible property (object) 

*(Formerly known as IsObjectOn, which is now obsolete)
ILBRK *(Formerly known as ObjectOff, which is now obsolete)
ILBRK *(Formerly known as ObjectOn, which is now
obsolete)***

    bool Object.Visible

Gets/sets the visible state of the object. If this is 1 (true), the
object is switched on and visible in the room. If you set this to 0
(false), the object disappears and no longer appears in the room.

    object[5].Visible = false;

will make object number 5 in the current room disappear.

### X property (object) 

*(Formerly known as GetObjectX, which is now obsolete)*

    int Object.X

Gets/sets the X co-ordinate of the object.

**NOTE: This property cannot be changed while the object is
moving.**

    Display("Object 1's X co-ordinate is %d.", object[1].X);

will display the X co-ordinate of object 1.

*See Also: , , ,*

### Y property (object) 

*(Formerly known as GetObjectY, which is now obsolete)*

    int Object.Y

Gets/sets the Y co-ordinate of the object, which is the bottom of the
object's image.

**NOTE: This property cannot be changed while the object is
moving.**

**NOTE: If you try to use this co-ordinate with
Object.GetAtScreenXY, you will find that the object does not get picked
up. The object's sprite is drawn from the Y co-ordinate at (Object.Y -
Height) to (Object.Y - 1).**

    Display("Object 1's Y co-ordinate is %d.", object[1].Y);

will display the Y co-ordinate of object 1.

*See Also: , , ,*

Overlay functions and properties
--------------------------------

### CreateGraphical 

*(Formerly known as CreateGraphicOverlay, which is now
obsolete)*

    static Overlay* Overlay.CreateGraphical(int x, int y, int slot, bool transparent)

Creates a screen overlay containing a copy of the image from SLOT in the
Sprite Manager. The image is placed at (X,Y) on the screen (these are
screen co-ordinates, not room co-ordinates).

If *transparent is true then the overlay will be drawn in
the same way as characters/objects, if it is false then a black
rectangle will be painted behind the sprite.*

See the description of for more on overlays.

    Overlay* myOverlay = Overlay.CreateGraphical(100, 100, 300, true);
    Wait(40);
    myOverlay.Remove();

will create an overlay of the image stored in sprite manager's slot 300,
at the coordinates 100,100. It will display for 1 second, then remove
it.

*See Also: ,*

### CreateTextual 

*(Formerly known as CreateTextOverlay, which is now
obsolete)*

    static Overlay* Overlay.CreateTextual(int x, int y, int width,
                                          FontType font, int color, string text)

Creates a screen overlay containing the text you pass at the position
specified. A screen overlay looks identical to the way speech text is
displayed in conversations, except that with this command the text stays
on the screen until either you remove it with the Remove command, or the
player goes to a different room, in which case it is automatically
removed.

The X and Y parameters specify the upper-left corner of where the text
will be written. WIDTH is the width, in pixels, of the text area. FONT
is the font number from the editor to use (0 is the normal font, 1 is
the speech font). COLOR is the text color - use one of the colours from
1 to 15. Finally, TEXT is obviously the text that gets displayed.

The function returns the Overlay, which you use later to reposition and
remove the overlay.

You can insert the value of variables into the message. For more
information, see the section.

**NOTE: large overlays, in the same way as objects, can
impact performance while displayed.**

**NOTE: there is currently a maximum of 10 overlays
displayed at any one time. Some other commands such as Say and
SayBackground create overlays internally, so don't rely on being able to
create 10 with CreateTextual.**

**NOTE: if the Overlay object goes out of scope, the
overlay will be removed. Hence, if you want the overlay to last
on-screen outside of the script function where it was created, the
`Overlay*` variable declaration needs to be at the top of the script and
outside any script functions.**

    Overlay* myOverlay = Overlay.CreateTextual(50,80,120, Game.SpeechFont, 15,"This is a text overlay");
    Wait(40);
    myOverlay.Remove();

will display a 120 pixels text area with its upper left corner at
coordinates 50,80 containing the string “This is a text overlay” using
the speech font and white color. It will be displayed for 1 second, then
removed.

*See Also: , , ,*

### Remove (overlay) 

*(Formerly known as RemoveOverlay, which is now obsolete)*

    Overlay.Remove()

Removes the specified overlay from the screen. Use this when you are
done using the overlay.

    Overlay* myOverlay = Overlay.CreateTextual(50,80,120,2,15,"This is a text overlay");
    Wait(200);
    myOverlay.Remove();

will create a text overlay , wait for 200 game cycles (about 5 seconds)
and then remove the overlay from the screen.

*See Also:*

### SetText (overlay) 

*(Formerly known as SetTextOverlay, which is now obsolete)*

    Overlay.SetText(int width, FontType font, int color, string text, ...)

Replaces the specified overlay with a new one, at the same co-ordinates
but with the new specified text, width, font and colour.

You can insert the value of variables into the message. For more
information, see the section.

    Overlay* myOverlay = Overlay.CreateTextual(50,80,120,Game.SpeechFont,15,"This is a text overlay");
    Wait(200);
    myOverlay.SetText(120,Game.SpeechFont,15,"This is another text overlay");

will create a text overlay , wait for 200 game cycles (about 5 seconds)
and then replace the overlay with another one.

*See Also: ,*

### Valid property (overlay) 

*(Formerly known as IsOverlayValid, which is now obsolete)*

    readonly bool Overlay.Valid;

Checks whether the overlay is a current overlay or not. Returns 1 if it
is, 0 if it isn't.

    Overlay* myOverlay = Overlay.CreateTextual(50,80,120,2,15,"This is a text overlay");
    Display("Overlay valid before: %d", myOverlay.Valid);
    myOverlay.Remove();
    Display("Overlay valid after: %d", myOverlay.Valid);

creates an overlay, and prints out the Valid property (which will be 1).
Then, removes the overlay and prints Valid again (which will now be 0).

*See Also: ,*

### X property (overlay) 

*(Formerly known as MoveOverlay, which is now obsolete)*

    int Overlay.X;

Gets/sets the X co-ordinate of the overlay (ie. the left hand side of
the overlay).

This allows you to dynamically move overlays around the screen.

    Overlay* testOverlay = Overlay.CreateTextual(50,80,120,2,15,"This is a text overlay");
    while (testOverlay.X < 100) {
      testOverlay.X++;
      Wait(1);
    }
    testOverlay.Remove();

creates a text overlay, then gradually slides it across the screen.

*See Also: , ,*

### Y property (overlay) 

*(Formerly known as MoveOverlay, which is now obsolete)*

    int Overlay.Y;

Gets/sets the Y co-ordinate of the overlay (ie. the top edge of the
overlay).

This allows you to dynamically move overlays around the screen.

    Overlay* testOverlay = Overlay.CreateTextual(50,50,120,2,15,"This is a text overlay");
    while (testOverlay.Y < 100) {
      testOverlay.Y++;
      Wait(1);
    }
    testOverlay.Remove();

creates a text overlay, then gradually slides it down the screen.

*See Also: , ,*

Palette functions
-----------------

### CyclePalette 

    CyclePalette (int start, int end)

This is used for special effects, like the flowing colours on the Space
Quest 4 title screen, and the Sierra logo of the later Sierra games. The
palette indexes from START to END are cycled around one slot. Using this
call in a repeatedly\_execute function gives the effect of animation.

By default, the colours rotate leftwards through the palette. If you
pass the arguments the other way round (ie. START being larger than END)
then the colours will rotate in the opposite direction.

**NOTE: This command only works in 256-colour games.**

    CyclePalette(10,200);

will cause the palette indexes from 10 to 200 cycle around one slot and
give a color effect.

*See Also: , ,*

### SetPalRGB 

    SetPalRGB (int slot, int red, int green, int blue)

Changes the RGB components of one of the palette slots. The palette is
initially set up in the Palette Editor, but you can override it during
the game using this function for special effects. The RED, GREEN and
BLUE parameters each range from 0 to 63 (as used in the Palette Editor).

If SLOT is a background slot, then this function's effect will last
until the player changes screen, when the palette is changed to the new
room's palette. If SLOT is not a background slot, the effect of this
function is permanent.

NOTE: This function will allow you to change the colours which are
“locked” in the AGS Editor. However, you should not normally do this as
it can cause strange colours in the game.

    SetPalRGB(10,63,63,21);

will change palette slot number 10 from light green to yellow

*See Also: , , ,*

### UpdatePalette 

    UpdatePalette()

Commits the changes you made to the game palette. The script global
variable palette\[\] stores the state of all the colours of the palette.
You can access the red, green and blue components with .r, .g and .b.
The values range from 0 to 63.

    palette[16].r = 60;
    UpdatePalette();

will make the black colour turn bright red. When you actually change the
variable, nothing happens. Call this function to update the screen.

*See Also:*

Parser functions
----------------

### FindWordID 

    static int Parser.FindWordID(string wordToFind)

Looks up *wordToFind in the text parser dictionary, and
returns the ID number.*

If the word is not found, returns -1. ILBRK Otherwise, the Word Group
number is returned, as seen in the Text Parser tab in the editor.

You can determine if two words are synonyms by looking them both up and
seeing if the returned IDs are the same.

Ignore words are returned as ID 0.

This function is useful if you want to use the AGS Text Parser
dictionary, but implement some custom parsing functionality instead of
using the standard ParseText function.

     if (Parser.FindWordID("machine") > 0)
     {
       Display("machine is in the game dictionary");
     }

will display a message if the game dictionary includes “machine”

*Compatibility: Supported by **AGS 3.1.0 and
later versions.***

*See Also:*

### ParseText 

    static Parser.ParseText(string text)

Stores the supplied user text string for later use by Said. You need to
call this command first with the user's input before using the Said
command. You would usually call this inside the text box's OnActivate
event handler.

     String command = txtParser.Text;
     Parser.ParseText(command);

will get the players input and store it in string “command” for use with
the said command.

*See Also: ,*

### Said 

    static bool Parser.Said(string text)

Checks whether the player typed in TEXT in their input passed to
ParseText. Returns *true if it matches, *false
otherwise.**

See for a more detailed description.

    String input = txtParserInput.Text;
    Parser.ParseText(input);
    if (Parser.Said("load")) {
      txtParserInput.Text = "";
      RestoreGameDialog();
    }

will bring up the restore game dialogue if the player types “load” in
the text parser.

*See Also: ,*

### SaidUnknownWord 

    static String Parser.SaidUnknownWord()

If a word not in the game dictionary was submitted to the last ParseText
call, then the word is returned by this command. This allows you to
display a message like “Sorry, this game doesn't recognise 'XXXX'.”

If all the words were recognised, this returns null.

    String badWord = Parser.SaidUnknownWord();
    if (badWord != null)
       Display("You can't use '%s' in this game.", badWord);

will display the message if the player types a word that's not in the
vocabulary.

*See Also: ,*

Region functions and properties
-------------------------------

### GetAtRoomXY (region) 

*(Formerly known as global function GetRegionAt, which is now
obsolete)*

    static Region* Region.GetAtRoomXY(int x, int y)

Returns the region at ROOM co-ordinates (X,Y). If there is no region
there, or if invalid co-ordinates are specified, the Region\*
representing region 0 will be returned.

**NOTE: Unlike GetHotspotAtLocation, the co-ordinates
specified are ROOM co-ordinates. This means that if you want to use the
mouse cursor location, you have to add the screen offset to make it work
in scrolling rooms.**

    if (Region.GetAtRoomXY(player.x, player.y) == region[0])
      Display("The player is not currently standing on a region.");

*See Also:*

### RunInteraction (region) 

*(Formerly known as RunRegionInteraction, which is now
obsolete)*

    Region.RunInteraction(int event)

Runs the event handler as if the EVENT for the region had been
activated.

**NOTE: Unlike the other RunInteraction commands, this one
does not take a cursor mode. Instead, it uses an event type as
follows:**

0 While player stands on region ILBRK 1 Player walks onto region ILBRK 2
Player walks off region

    region[4].RunInteraction(1);

will run the actions defined in the event handler script for “Player
walks onto region” for region 4.

*See Also: ,*

### Tint (region) 

*(Formerly known as SetRegionTint, which is now obsolete)*

    Region.Tint(int red, int green, int blue, int amount, optional int luminance)

Changes the region to have RGB tint (RED, GREEN, BLUE) with AMOUNT
percent saturation.

The red, green and blue values are between 0 and 255, and you supply the
same values that you would use in the editor.

For the meaning of all the parameters, see .

**NOTE: The tint will be reset when the player leaves the
room, so you need to use it in Player Enters Room if you want a
permanent change.**

**NOTE: This function only works in hi-colour games.**

**NOTE: To remove the region tint, set the LightLevel
property to 0.**

    region[2].Tint(180, 20, 20, 50);

will set region 2's RGB tint to (180, 20, 20) with 50`%` opacity.

*Compatibility: Optional *luminance parameter
is supported only by **AGS 3.4.0 and later versions.****

*See Also: ,*

### Enabled property (region) 

*(Formerly known as DisableRegion, which is now obsolete)
ILBRK *(Formerly known as EnableRegion, which is now
obsolete)**

    bool Region.Enabled

Enables/disables the specified region. If you set this to false, then
all areas of the screen that were previously part of the region now act
as type 0 (no region). You can turn the region back on later by setting
this to true.

While a region is disabled, it will not be returned by
Region.GetAtRoomXY, and if the character walks onto the region then its
events will not get run.

    region[3].Enabled = false;

will disable region number 3.

*See Also: , ,*

### ID property (region) 

    readonly int Region.ID

Gets the region number of this region. This allows you to interoperate
with old script using the number-based region functions.

    Display("Region 3 is number %d.", region[3].ID);

displays region 3's number (which will be 3).

*See Also:*

### LightLevel property 

*(Formerly known as SetAreaLightLevel, which is now
obsolete)*

    int Region.LightLevel

Gets/sets the region's light level. This does the same thing as the
Light Level textbox in the editor, but allows you to change it at
run-time.

The light level is from **-100 to 100. This is different
from the editor, which takes values from 0 to 200. Subtract 100 from the
value you would use in the editor when calling this function. The reason
for this discrepancy is legacy reasons from the DOS editor days.**

In 8-bit games you cannot use positive light level for brightening
effect, but you may still use negative values to produce darkening
effect.

To disable region lighting and tinting effects, set LightLevel to 0.

**NOTE: The light level will be reset to the editor
settings when the player leaves the room, so you need to use it in
Player Enters Room if you want a permanent change.**

**NOTE: Setting a light level will disable any RGB tint set
for the region.**

**NOTE: Region's light level does NOT override individual
character and object light levels.**

    if (GetGlobalInt(10)==1)
        region[2].LightLevel = 100;

will set region 2's level light to 100 if the Global Integer 10 is 1.

*See Also: , , ,*

### TintEnabled property 

    readonly bool Region.TintEnabled

Gets whether the region currently has an RGB tint enabled for it.

Returns *true if it does, and *false if it
does not. If it does not, then the LightLevel property reflects the
region lighting.**

If this property is *false, then the TintRed, TintGreen,
TintBlue, TintSaturation and TintLuminance properties are invalid.*

    if (region[4].TintEnabled) {
      Display("Region 4 is tinted!!");
    }

will display a message if region 4 is tinted

*See Also:*

### TintBlue property 

    readonly int Region.TintBlue

Gets the *Blue setting for the region's current tint.*

This property is read-only; to change it, use the command.

**NOTE: If the property is false, then this value is
meaningless.**

    if (region[4].TintEnabled) {
      Display("Region 4 is tinted RGB (%d,%d,%d) Saturation %d.",
              region[4].TintRed, region[4].TintGreen,
              region[4].TintBlue, region[4].TintSaturation);
    }

will display a message with the region's tints.

*See Also: , , , ,*

### TintGreen property 

    readonly int Region.TintGreen

Gets the *Green setting for the region's current tint.*

This property is read-only; to change it, use the command.

**NOTE: If the property is false, then this value is
meaningless.**

    if (region[4].TintEnabled) {
      Display("Region 4 is tinted RGB (%d,%d,%d) Saturation %d.",
              region[4].TintRed, region[4].TintGreen,
              region[4].TintBlue, region[4].TintSaturation);
    }

will display a message with the region's tints.

*See Also: , , , , ,*

### TintRed property 

    readonly int Region.TintRed

Gets the *Red setting for the region's current tint.*

This property is read-only; to change it, use the command.

**NOTE: If the property is false, then this value is
meaningless.**

    if (region[4].TintEnabled) {
      Display("Region 4 is tinted RGB (%d,%d,%d) Saturation %d.",
              region[4].TintRed, region[4].TintGreen,
              region[4].TintBlue, region[4].TintSaturation);
    }

will display a message with the region's tints.

*See Also: , , , , ,*

### TintSaturation property 

    readonly int Region.TintSaturation

Gets the *saturation setting for the region's current
tint.*

This property is read-only; to change it, use the command.

**NOTE: If the property is false, then this value is
meaningless.**

    if (region[4].TintEnabled) {
      Display("Region 4 is tinted RGB (%d,%d,%d) Saturation %d.",
              region[4].TintRed, region[4].TintGreen,
              region[4].TintBlue, region[4].TintSaturation);
    }

will display a message with the region's tints.

*See Also: , , , , ,*

### TintLuminance property 

    readonly int Region.TintLuminance

Gets the *luminance setting for the region's current tint.*

This property is read-only; to change it, use the command.

**NOTE: If the property is false, then this value is
meaningless.**

*See Also: , , , , ,*

Room functions
--------------

### AreThingsOverlapping 

    AreThingsOverlapping(int thing1, int thing2)

Checks whether two characters or objects are overlapping each other on
screen. This simply carries out a quick rectangular check on the two
things to decide - so if they have large transparent regions around the
edges, it may seem to be overlapping too soon.

THING1 and THING2 can either be a CHARID, or can be an object number
PLUS 1000. So for example, passing EGO as THING1, and 1004 as THING2,
will compare the character EGO with Object 4 in the current room.

Returns 0 if they are not overlapping, or the overlapping amount if they
are. This amount is an arbitrary scale, but 1 means they are just about
touching, all the way up to higher numbers for more overlappingness.

Calling this function with both the parameters as objects is the same as
calling Object.IsCollidingWithObject.

    if (AreThingsOverlapping(1002, EGO)) {
      // code here
    }

will run the code if object 2 is overlapping EGO. This could be useful
if object 2 was a bullet, for instance.

*See Also: ,*

### DisableGroundLevelAreas 

    DisableGroundLevelAreas(int disableTints)

Disables all ground-level events. This means that all Region events, the
Player Stands On Hotspot event, and the room edges become disabled.

This command is useful in conjunction with the character\[\].z variable,
if you want the player to be able to temporarily fly or levitate, for
example. It allows you to stop the character from triggering Player
Stands On events while they are in the air.

This command is also useful during some cutscenes, if you don't want the
player to trigger events as they walk around the room while in the
cutscene.

The DISABLETINTS parameter specifies whether the visual effects of the
regions (ie. light levels and tints) are also disabled. If you pass this
as 0, then just the events will be turned off.

    DisableGroundLevelAreas(0);

will disable all ground-level events, but leave light levels working

*See Also: , ,*

### EnableGroundLevelAreas 

    EnableGroundLevelAreas()

Re-enables all ground-level events. This is used to reverse the effects
of using the DisableGroundLevelAreas command, and will return things to
normal.

    EnableGroundLevelAreas();

will re-enable all ground-level events.

*See Also: , ,*

### GetBackgroundFrame 

    GetBackgroundFrame()

Returns the number of the current background being displayed. In a room
without animating backgrounds, this will always return 0. Otherwise, the
current frame number is returned from 0 to 4.

    if (GetBackgroundFrame()==4)
      object[2].Visible = true;

will turn on object 2 if the background frame of the room is frame 4.

*See Also:*

### GetDrawingSurfaceForBackground 

    static DrawingSurface* Room.GetDrawingSurfaceForBackground(optional int backgroundNumber)

Gets a drawing surface for a room background, which allows you to
directly draw onto the room's background image. You can provide a
background frame number if you want to modify a specific frame;
otherwise, the current background's surface will be returned.

After calling this method, use the various to modify the background,
then call Release on the surface when you are finished.

Any changes you make will only last until the player leaves the room, at
which point they will be lost. If you need to make long-lasting changes,
you can either use this method in the Player Enters Room event, or
consider using an alternate background frame for the changed image.

**NOTE: Drawing onto the room background can be slow,
especially when using the Direct3D driver. Do not use this command in
repeatedly\_execute; make sure you only use this command when absolutely
necessary.**

    DrawingSurface *surface = Room.GetDrawingSurfaceForBackground();
    surface.DrawingColor = 14;
    surface.DrawLine(0, 0, 50, 50);
    surface.Release();

draws a yellow diagonal line across the top-left of the current room
background, then releases the image.

*See Also: ,*

### GetPlayerCharacter 

    GetPlayerCharacter ()

**THIS COMMAND IS NOW OBSOLETE. ILBRK The recommended
replacement is to use the player character's ID property, as follows:**

    Display("The player character number is %d", player.ID);

*See Also:*

### GetProperty (room) 

*(Formerly known as global function GetRoomProperty, which is now
obsolete)*

    Room.GetProperty(string property)

Returns the custom property setting of the PROPERTY for the current
room.

This command works with Number properties (it returns the number), and
with Boolean properties (returns 1 if the box was checked, 0 if not).

Use the equivalent Room.GetTextProperty function to get a text property.

Note that you cannot retrieve room properties of other rooms - only the
current room can be checked.

    if (Room.GetProperty("CanBeAttackedHere"))
      Display("An evil monster lunges at you!");

will print the message if the current room has its “CanBeAttackedHere”
box ticked.

*See Also:*

### GetTextProperty (room) 

*(Formerly known as global function GetRoomPropertyText, which is
now obsolete)*

    static String Room.GetTextProperty(string property)

Returns the custom property setting of the PROPERTY for the current
room.

This command works with Text properties only. The property's text will
be returned from this function.

Use the equivalent Room.GetProperty function to get a non-text property.

Note that you cannot retrieve room properties of other rooms - only the
current room can be checked.

    String description = Room.GetTextProperty("Description");
    Display("The room's description: %s", description);

will retrieve the room's “description” property then display it.

*See Also:*

### SetProperty (room) 

    static bool Room.SetProperty(const string property, int value)

Sets the new *value for the custom *property
for the specified room. Returns TRUE if such property exists and FALSE
on failure.**

This command works with Number properties (it sets the numeric value),
and with Boolean properties (sets FALSE is value is equal to 0, or TRUE
otherwise).

Use the equivalent SetTextProperty function to set new text property
value.

Note that you cannot set room properties of other rooms - only the
current room.

    Room.SetProperty("Darkness", 10);

will change room's “Darkness” custom property to 10.

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

*See Also:*

### SetTextProperty (room) 

    bool Room.SetTextProperty(const string property, const string value)

Sets the new *value text for the custom
*property for the specified room. Returns TRUE if such
property exists and FALSE on failure.**

This command works with Text properties only. The property's text will
be changed to new value.

Use the equivalent SetProperty function to set a non-text property.

Note that you cannot set room properties of other rooms - only the
current room.

    Room.SetTextProperty("Description", "The Throne Room");

will change room's “description” property.

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

*See Also:*

### GetScalingAt 

    GetScalingAt (int x, int y)

Returns the room area scaling at room co-ordinates (X,Y).

The value returned is from 1 to 200, with 100 being the normal un-scaled
setting.

    if (GetScalingAt(player.x, player.y) == 100)
        Display ("The player is currently at normal size.");

*See Also: ,*

### GetViewportX 

    GetViewportX ()

Returns the X-offset of the current viewport in a scrolling room. This
allows you to find out what part of the room the player is looking at.
The co-ordinate returned is the left edge of the screen, and so it can
have a value between 0 and (ROOM WIDTH - 320).

If the room is a non-scrolling room, returns 0.

See the SetViewport function description for more information.

    if (GetViewportX()>100)
        object[2].Visible = true;

will turn object 2 on if the player has scrolled the room by 100 pixels
to the right.

*See Also: ,*

### GetViewportY 

    GetViewportY ()

Returns the Y-offset of the current viewport in a scrolling room. This
allows you to find out what part of the room the player is looking at.
The co-ordinate returned is the top edge of the screen, and so it can
have a value between 0 and (ROOM HEIGHT - 200).

If the room is a non-scrolling room, returns 0.

    if (GetViewportY()>20)
        object[2].Visible = true;

will turn object 2 on if the player has scrolled the room by 20 pixels
to the bottom.

*See Also: ,*

### GetWalkableAreaAt 

    GetWalkableAreaAt (int x, int y)

Returns the number of the walkable area at SCREEN co-ordinates (X,Y). If
there is no walkable area there, or if invalid co-ordinates are
specified, returns 0.

NOTE: The co-ordinates are SCREEN co-ordinates, NOT ROOM co-ordinates.
This means that with a scrolling room, the co-ordinates you pass are
relative to the screen's current position, and NOT absolute room
co-ordinates. This means that this function is suitable for use with the
mouse cursor position variables.

    if (GetWalkableAreaAt(mouse.x,mouse.y) == 0)
        Display ("You can't walk there.");

*See Also: , ,*

### HasPlayerBeenInRoom 

    HasPlayerBeenInRoom(int room_number)

Checks whether the player has ever been in ROOM\_NUMBER (ie. has the
'First Time Player Enters Room' event there ever been run). Returns 1 if
they have, and 0 if they haven't.

You can use this function to determine whether the player has been to a
particular location previously. If you reset the room with ResetRoom,
then this command will return 0 until they enter the room again.

This command will always return 1 if you ask it about the current room;
and it will always return 0 if you ask it about a non-state saving room
(ie. rooms numbered &gt; 300).

    if (HasPlayerBeenInRoom(14)) {
      Display("The player has been to room 14 before.");
    }

will display a message if the player has been to room 14.

*See Also:*

### ProcessClick (Room) 

*(Formerly known as global function ProcessClick, which is now
obsolete)*

    static void Room.ProcessClick(int x, int y, CursorMode)

Simulates clicking the mouse on the location (X,Y) on the screen, in the
specified cursor mode. This “click” has special behavior in that it
**only affects Room elements and characters under given
coordinates. Any conditions attached to the first object found on given
coordinates will be executed. Game interface (buttons, sliders, and so
on) will be **ignored. Even if the coordinates happen to
lie on a button, the simulated click will “pass through” that button as
if it was not present.****

The available cursor modes are the ones you define on your Cursors tab
(but with eMode prepended to them). Usually these are eModeWalkto,
eModeLookat, etc.

    Room.ProcessClick(100, 50, eModeLookat);

will simulate a click in the Look mode on co-ordinates (100, 50).

*See Also: , , ,*

### ReleaseViewport 

    ReleaseViewport ()

Releases the lock on the screen viewport, allowing it to automatically
scroll around following the player character as normal.

    int x;
    while (x<100) {
       SetViewport(x,0);
       x++;
       Wait(1);
    }
    ReleaseViewport();

will scroll the room 100 pixels to the right and then return the screen
to its original position and unlock the screen viewport.

*See Also:*

### RemoveWalkableArea 

    RemoveWalkableArea (int areanum)

Removes the walkable areas in colour AREANUM from the current room. You
can put the area back with RestoreWalkableArea.

NOTE: When the player leaves the screen, all the walkable areas are
reset. Therefore, if you want an area to remain off when they leave the
screen, you will need to set a flag, then run the RemoveWalkableArea
command in the “Player enters room” event when they return.

    RemoveWalkableArea(5);

will make the walking area 5 unwalkable.

*See Also:*

### ResetRoom 

    ResetRoom (int room_number)

Discards all the data that the engine has in memory about when the
player last visited ROOM\_NUMBER, and resets it as if they'd never been
there. The next time the player goes to that room, all the objects and
scripts will be in their initial state (as set up in the editor), and
not how they were when the player left the room. The “First time enters
room” event will be run when they enter this room again.

This function is useful if you want to have a “View intro” option to
allow the player to watch an intro again - this function can reset all
the objects in the intro rooms to their starting positions.

NOTE: You cannot reset the current room (ie. the room that the player is
in).

    ResetRoom(0);

will reset the intro room so it can be played again if the player wants
to.

*See Also:*

### RestoreWalkableArea 

    RestoreWalkableArea (int areanum)

Makes the area AREANUM walkable again.

    RestoreWalkableArea(4);

will make the walking area 4 walkable again.

*See Also:*

### SetAreaScaling 

    SetAreaScaling(int area, int min, int max)

Changes walkable area number AREA's scaling.

There are two ways to use this command: ILBRK 1. Pass the same value for
MIN and MAX. This will give the walkable area fixed scaling (same as
setting it in the editor with “Use continuous scaling” un-ticked). ILBRK
2. Pass different values for MIN and MAX. In this case, continuous
scaling is enabled for the walkable area, and will go from MIN at the
top to MAX at the bottom.

MIN and MAX have ranges from 5 to 200, the same as in the editor. Pass
100 for both values to revert to the normal zoom level (100`%`) for that
area.

    SetAreaScaling(5, 120, 170);

will set walkable area 5 to use continuous scaling from 120 to 170
percent.

*See Also: ,*

### SetBackgroundFrame 

    SetBackgroundFrame (int frame)

Locks the background to frame number FRAME of an animating-background
screen. (Values for FRAME are from 0 to 4). This allows you to use the
animating backgrounds feature for another purpose - you can have two
frames of the background, one for example with a spaceship crashed on
it. Then, once the right event has happened, call SetBackgroundFrame in
the Player Enters Room event to set the background before the screen
fades in.

Pass the *frame as -1 to return to the default behaviour of
automatically cycling through all the background frames.*

The frame lock is released when the game changes rooms.

    if (GetGlobalInt(20)==1)
        SetBackgroundFrame(4);

will change the current room's background frame to 4 if the global
integer 20 is 1.

*See Also:*

### SetViewport 

    SetViewport (int x, int y)

Locks the screen viewport to having the top-left hand corner at (X,Y) in
a scrolling room. This allows you to manually pan across a scrolling
room or to have the screen follow a non-player character.

The lock is released when you either call ReleaseViewport or the player
changes rooms.

**NOTE: The co-ordinates supplied are 320x200-scale
co-ordinates, and will be automatically multiplied up by the engine.**

**NOTE: This function has no effect if the current room
isn't a scrolling room.**

    int ypos = 0;
    while (ypos < 60) {
      SetViewport(0, ypos);
      Wait(1);
      ypos++;
    }
    ReleaseViewport();

will scroll the screen down from the top 60 pixels, then release it back
to follow the player around.

*See Also: , ,*

### SetWalkBehindBase 

    SetWalkBehindBase (int area, int baseline)

Changes the walk-behind AREA to have new BASELINE. This effectively
allows you to turn walk-behinds on and off, although you can do other
tricks with it as well. BASELINE is from 1 to the height of the room
(normally 200) and moves the line which you set originally in the
editor.

Passing BASELINE as 0 disables the walk-behind area, so that the player
will always walk in front of it.

Basically, if the character's feet are below BASELINE, he will be drawn
in front of it, otherwise he will be drawn behind it.

    SetWalkBehindBase (3,0);

will disable the walkbehind area number 3.

*See Also:*

### BottomEdge property 

    readonly static int Room.BottomEdge

Returns the Y co-ordinate of the bottom edge of the room, as set in the
Room Settings pane of the editor.

    Display("The current room's bottom edge is at %d.", Room.BottomEdge);

*See Also: , ,*

### ColorDepth property (room) 

    readonly static int Room.ColorDepth

Returns the colour depth of the room's background scene. This is
important if you want to use DrawImage, since any sprites that you draw
must be the same colour depth as the room itself.

    Display("The current room background is %d-bit colour.", Room.ColorDepth);

*See Also:*

### Height property (room) 

*(Formerly known as game.room\_height, which is now
obsolete)*

    readonly static int Room.Height

Returns the height of the room, in 320x200-style co-ordinates. This is
the same height as is displayed as the “Relative size” in the Editor.

    Display("The current room size is %d x %d.", Room.Width, Room.Height);

*See Also:*

### LeftEdge property 

    readonly static int Room.LeftEdge

Returns the X co-ordinate of the left edge of the room, as set in the
Room Settings pane of the editor.

    Display("The current room's left edge is at %d.", Room.LeftEdge);

*See Also: , ,*

### Messages property 

*(Formerly known as global function GetMessageText, which is now
obsolete)*

    readonly static String Room.Messages[int message]

Gets the text of the specified room message. This is useful if you want
to store, for example, a room description in Message 1 in each room –
this property allows you to retrieve the text for that message from the
current room.

If an invalid message number is supplied, *null will be
returned. Otherwise, the message contents will be returned.*

    String message1 = Room.Messages[1];
    Display("Message 1 says: %s", message1);

will print the contents of room message 1.

### MusicOnLoad property 

    readonly static int Room.MusicOnLoad

**This property is now obsolete. It is still accessible for
backwards compatibility with old games.**

Returns the music number that is set to play when the player enters this
room, as set in the “Room Settings” pane in the editor. If no music is
set for this room, returns 0.

    Display("The current room plays music %d when the player enters.", Room.MusicOnLoad);

### ObjectCount property 

*(Formerly part of GetGameParameter, which is now
obsolete)*

    readonly static int Room.ObjectCount

Returns the number of objects in the room.

    Display("The current room contains %d objects.", Room.ObjectCount);

### RightEdge property 

    readonly static int Room.RightEdge

Returns the X co-ordinate of the right edge of the room, as set in the
Room Settings pane of the editor.

    Display("The current room's right edge is at %d.", Room.RightEdge);

*See Also: , ,*

### TopEdge property 

    readonly static int Room.TopEdge

Returns the Y co-ordinate of the top edge of the room, as set in the
Room Settings pane of the editor.

    Display("The current room's top edge is at %d.", Room.TopEdge);

*See Also: , ,*

### Width property (room) 

*(Formerly known as game.room\_width, which is now
obsolete)*

    readonly static int Room.Width

Returns the width of the room, in 320x200-style co-ordinates. This is
the same width as is displayed as the “Relative size” in the Editor.

    Display("The current room size is %d x %d.", Room.Width, Room.Height);

*See Also:*

Screen functions
----------------

### FadeIn 

    FadeIn (int speed)

Fades in from a black screen to the current palette. This is used to
restore the screen after a FadeOut call. SPEED is from 1 (slowest) to 64
(fastest).

*NOTE: This is a blocking function.*

    FadeOut(30);
    Wait(40);
    FadeIn(10);

will fade the screen to black, wait 1 sec (40 game cycles) and then fade
in again.

*See Also: , ,*

### FadeOut 

    FadeOut (int speed)

Fades the screen out to black. SPEED is the speed of the fade, from 1
(slowest) to 64 (instant). You can restore the screen with FadeIn.

*NOTE: This is a blocking function.*

    FadeOut(30);
    Wait(40);
    FadeIn(10);

will fade the screen to black, wait 1 sec (40 game cycles) and then fade
in again.

*See Also: , ,*

### FlipScreen 

    FlipScreen (int way)

Flips the screen round either the horizontal or vertical axis, or both.
This function is for special effects only - all co-ordinates remain the
same and it doesn't effect any other script functions.

The value of WAY selects:

    0  normal
    1  horizontal-flip (upside-down)
    2  vertical-flip  (left-to-right)
    3  both (upside-down and backwards)

**NOTE: This function is still a bit buggy - black parts of
the screen may show up wrong, and and pop-up messages will flip the
screen back to normal.**

    FlipScreen(1);

will flip the screen upside down.

### SetFadeColor 

    SetFadeColor(int red, int green, int blue)

Changes the colour which the screen fades out to, to have the specified
RGB value. Each of the parameters can range from 0-255. The default is
black, ie. (0, 0, 0)

The colour that you set here will be used in all future calls to
FadeIn/FadeOut, and also for the screen transition if it is set to Fade
In/Out.

    SetFadeColor(200, 0, 0);

will mean that next time the screen fades out, it fades to red instead
of black.

SeeAlso: , ,

### SetNextScreenTransition 

    SetNextScreenTransition(TransitionStyle)

Sets the room transition type to *TransitionStyle, but ONLY
for the next room change. After that, it will revert back to the normal
transition type specified in the editor or with SetScreenTransition.*

For the possible values for TransitionStyle, see .

    SetNextScreenTransition(eTransitionBoxout);
    cEgo.ChangeRoom(10);

will go to room 10 with a box-out effect, but then return to the normal
transition type from then on.

SeeAlso:

### SetScreenTransition 

    SetScreenTransition(TransitionStyle)

Changes the default screen transition. TransitionStyle can be one of the
following:

    eTransitionFade
    eTransitionInstant
    eTransitionDissolve
    eTransitionBoxout
    eTransitionCrossfade

All future transitions will be done as specified until you call this
function again.

    SetScreenTransition(eTransitionFade);

will change the room transitions to Fade.

SeeAlso:

### ShakeScreen 

    ShakeScreen (int amount)

Shakes the screen to simulate, for example, an earthquake. AMOUNT is how
much the screen shakes: 1 is hardly anything, and 25 is a lot.

    ShakeScreen(5);

will shake the screen a little.

*See Also:*

### ShakeScreenBackground 

    ShakeScreenBackground (int delay, int amount, int length)

Shakes the screen to simulate, for example, an earthquake. The game is
not paused while the screen shakes - it will continue in the background.

DELAY specifies the 'shakiness' of the shake - 2 is the lowest you can
pass for this, and will create the most shaky screen.

AMOUNT specifies the ferociousness of the shake - ie. how much the
screen moves by when it does shake. Here, 1 is a very tiny shake, up to
about 30 for a ferocious shake.

LENGTH specifies how long the shake lasts for, in game loops. For
example, 80 would be equivalent to 2 seconds at the default game speed.

You can abort any current background shake that is in progress by
calling this command with the LENGTH parameter as zero.

    ShakeScreenBackground (4, 10, 80);

will shake the screen a little for 2 seconds.

*See Also:*

### TintScreen 

    TintScreen (int red, int green, int blue)

Tints the screen with the specified RGB values. RED, GREEN and BLUE
range from 1 to 100.

Pass (0, 0, 0) to turn off the tinting and go back to how the screen
normally looks.

For historical reasons, the tint works by applying a 50`%`-transparent
layer of the specified colour to the screen after everything else has
been drawn. Therefore, it may not lead to the sort of results you might
expect.

**NOTE: This command is currently experimental, since it
causes a massive slowdown in the engine, especially at high resolutions.
If you use it, you should provide an option for the player to turn it
off.**

**NOTE: This feature does not work in 256-colour games.**

    TintScreen (100, 50, 50);

will tint a heavy dose of red.

Speech functions and properties 
-------------------------------

### AnimationStopTimeMargin 

*(Formerly known as game.close\_mouth\_end\_speech\_time, which is
now obsolete)*

    static int Speech.AnimationStopTimeMargin

Gets/sets the time margin at which the character talking animation
should stop before before speech time ends. This property is specified
in **game loops and is set to 10 by default.**

**NOTE: This property only affects the animation if voice
mode is disabled.**

    Speech.AnimationStopTimeMargin = 40;

will stop talking animation 40 game loops (1 second with the default
game speed) before speech time ends.

*See Also:*

### CustomPortraitPlacement 

    static bool Speech.CustomPortraitPlacement

Enables/disables the custom speech portrait placement. When set to
**true the character portraits are positioned at screen
coordinates defined by and . When set to **false the
portraits will be automatically aligned again.****

**NOTE: This property has no effect if the Lucas-Arts
speech style is used.**

*Compatibility: Supported by **AGS 3.3.0 and
later versions.***

*See Also: ,*

### DisplayPostTimeMs 

    static int Speech.DisplayPostTimeMs

Gets/sets the extra time the speech will stay on screen after its base
time runs out. Commonly the time the speech lines and portrait stay on
screen is calculated based on the text length - if the text mode is on,
or voice clip length - if the voice mode is on. This property prolongs
the time the speech text and/or portrait is displayed. This property
does not interfere with speech skipping by key or mouse click: players
will still be able to skip speech any time they want (if appropriate
skip mode is enabled). This property is specified in
**milliseconds and is set to zero by default.**

*Compatibility: Supported by **AGS 3.3.0 and
later versions.***

*See Also:*

### GlobalSpeechAnimationDelay 

*(Formerly known as game.talkanim\_speed, which is now
obsolete)*

    static int Speech.GlobalSpeechAnimationDelay

Gets/sets global speech animation delay which affects every character in
game. This property is specified in **game loops and is set
to 5 by default.**

**NOTE: This property is ignored if lip sync is enabled.**

**NOTE: The property is only used when the
**Speech.UseGlobalSpeechAnimationDelay is set to
**true. This property **cannot be used if the
global speech animation delay is disabled. In that case, the individual
character's animation delay is used instead.********

*See Also: ,*

### PortraitXOffset 

    static int Speech.PortraitXOffset

Gets/sets the character's speech portrait **horizontal
offset relative to screen side. The actual x coordinate of the portrait
is calculated based on whether portrait is to be displayed at the left
or right side of the screen. This property specifies the distance
between the screen side and respected portrait's border.**

**NOTE:The property is only used when the
**Speech.CustomPortraitPlacement is set to
**true.******

*Compatibility: Supported by **AGS 3.3.0 and
later versions.***

*See Also: ,*

### PortraitY 

    static int Speech.PortraitY

Gets/sets the character's speech portrait **y coordinate on
screen.**

**NOTE:The property is only used when the
**Speech.CustomPortraitPlacement is set to
**true.******

*Compatibility: Supported by **AGS 3.3.0 and
later versions.***

*See Also: ,*

### SkipKey 

*(Formerly known as game.skip\_speech\_specific\_key, which is now
obsolete)*

    static eKeyCode Speech.SkipKey

Gets/sets special key which can skip speech text. This makes all other
keys ignored when speech is displayed on screen, unless eKeyNone is
assigned, in which case any key can be used again.

**NOTE:The specified key will only skip speech if the
appropriate speech skip style is enabled.**

    Speech.SkipKey = eKeySpace;

will assign the “space” key to skip the speech.

*See Also:*

### SkipStyle 

*(Formerly known as SetSkipSpeech, which is now obsolete)
ILBRK*

    static SkipSpeechStyle Speech.SkipStyle

Gets/sets how the player can skip speech lines.

The accepted values are

    eSkipKeyMouseTime  player can skip text by clicking mouse or pressing key
    eSkipKeyTime       player can skip text by pressing key only, not by clicking mouse
    eSkipTime          player cannot skip text with mouse or keyboard
    eSkipKeyMouse      text does not time-out; player must click mouse or press key each time
    eSkipMouseTime     player can skip text by clicking mouse only, not by pressing key
    eSkipKey           text does not time-out; player can skip text by pressing key only
    eSkipMouse         text does not time-out; player can skip text by clicking mouse only

    Speech.SkipStyle = eSkipTime;

will make the player unable to skip the text by pressing a mouse button
or a key.

*See Also: , ,*

### Style 

*(Formerly known as SetSpeechStyle, which is now obsolete)
ILBRK*

    static eSpeechStyle Speech.Style

Gets/sets theway in which speech text is displayed. This modifies the
setting originally set in the editor. SpeechStyle can be:

    eSpeechLucasarts
      speech text over character's head
    eSpeechSierra
      close-up portrait of character
    eSpeechSierraWithBackground
      close-up portrait + background window for text
    eSpeechFullScreen
      QFG4-style full screen dialog pictures

    Speech.Style = eSpeechSierra;

will change the speech style to a close up portrait of the character.

### TextAlignment 

*(Formerly known as game.speech\_text\_align, which is now
obsolete)*

    static Alignment Speech.TextAlignment

Sets how text in Lucasarts-style speech is aligned.

The accepted values are

    eAlignLeft
    eAlignCentre
    eAlignRight

The default is eAlignCentre.

    Speech.TextAlignment = eAlignRight;

will align the speech text at the right side.

### UseGlobalSpeechAnimationDelay 

    static bool Speech.UseGlobalSpeechAnimationDelay

Gets/sets whether speech animation delay should use global setting, as
opposed to individual character's setting. The actual global delay value
is specified with **Speech.GlobalSpeechAnimationDelay.**

    Speech.UseGlobalSpeechAnimationDelay = true;

will make the game use global speech animation delay.

*Compatibility: Supported by **AGS 3.3.0 and
later versions.***

*See Also: ,*

### VoiceMode 

*(Formerly known as SetVoiceMode, which is now obsolete)*

    static eVoiceMode Speech.VoiceMode

Gets/sets whether voice and/or text captions are used in the game.

Valid values for VoiceMode are:

    eSpeechTextOnly      no voice, text only
    eSpeechVoiceAndText  both voice and text
    eSpeechVoiceOnly     voice only, no text

The default is *eSpeechVoiceAndText if in-game speech is
enabled, and *eSpeechTextOnly if it is not. Changing this
setting changes the behaviour of all and commands which have a speech
file assigned to them.**

**WARNING: you should only ever use
*eSpeechVoiceOnly at the player's request to do so, because
there is no guarantee that they even have a sound card and so may not
understand what is going on.***

    if (IsSpeechVoxAvailable()==1)
        Speech.VoiceMode = eSpeechVoiceAndText;

will set the voice mode to voice and text if the voice pack is
available.

String functions
----------------

### Append 

*(Formerly known as global function StrCat, which is now
obsolete)*

    String.Append(string str2)

Appends the string STR2 to the end of the specified string, and returns
the result.

**IMPORTANT: The result of joining the strings together is
returned as a new string from this command. The original string will
**NOT be changed. For example, the following script will
not do anything: ILBRK `mytext.Append("World");` ILBRK what you probably
want instead is: ILBRK `mytext = mytext.Append("World");`****

    String mytext = "Hello";
    mytext = mytext.Append("World");
    Display(mytext);

will display “HelloWorld”.

*See Also: , ,*

### AppendChar 

    String.AppendChar(char extraChar)

Appends a single character to the end of the specified string, and
returns the result.

**IMPORTANT: The newly extended text is returned as a new
string from this command. The original string will **NOT be
changed. For example, the following script will not do anything: ILBRK
`mytext.AppendChar('o');` ILBRK what you probably want instead is: ILBRK
`mytext = mytext.AppendChar('o');`****

    String mytext = "Hell";
    mytext = mytext.AppendChar('o');
    Display(mytext);

will display “Hello”.

*See Also:*

### CompareTo 

*(Formerly known as global function StrCaseComp, which is now
obsolete) ILBRK *(Formerly known as global function
StrComp, which is now obsolete)**

    String.CompareTo(string str2, optional bool caseSensitive)

Compares the specified string to STR2. *caseSensitive
determines whether “Dog” and “dog” are equivalent; case sensitivity is
off by default.*

Returns 0 if the strings match, a number less than 0 if this string is
earlier in the alphabet than STR2, and a number greater than 0 if this
string is later in the alphabet than STR2.

**TIP: To do a case-sensitive comparison of two strings,
it's easier to just use the == operator.**

    String mytext = "Hello";
    if (mytext.CompareTo("hello") == 0) {
      Display("Strings match with case sensitivity off!");
    }
    else {
      Display("Strings don't match with case sensitivity off!");
    }

    if (mytext == "hello") {
      Display("Strings match with case sensitivity on!");
    }
    else {
      Display("Strings don't match with case sensitivity on!");
    }

will display “Strings match with case sensitivity off!”, and then
“Strings don't match with case sensitivity on!”.

### Copy 

*(Formerly known as global function StrCopy, which is now
obsolete)*

    String.Copy()

Returns a new copy of the specified string. You should not normally need
to use this, since strings can be assigned using the = operator.

    String mystring = "This is a test string.";
    String newstring = mystring.Copy();
    Display(newstring);

will display “This is a test string”.

### EndsWith 

    bool String.EndsWith(string lookForText, optional bool caseSensitive)

Returns *true if this string ends with
*lookForText, or *false if not.***

*caseSensitive is *false by default, but you
can set it to true so that the function will only return
*true for an exact-case match.***

    String myString = "Hello from the script!";
    if (myString.EndsWith("script!"))
    {
      Display("Ends with script!");
    }

will display the “Ends with script!” message.

*Compatibility: Supported by **AGS 3.1.0 and
later versions.***

*See Also: ,*

### Format 

*(Formerly known as global function StrFormat, which is now
obsolete)*

    static String.Format(string fmt, ...)

Processes the string FMT in the same way as the Display function does
but instead of displaying it on the screen, returns the result as a new
string.

You can insert the value of variables into the message. For more
information, see the section.

**NOTE: This function is static, which means you do not
call it on an existing string variable, but use `String.Format()`
instead.**

    int health=10;
    String text = String.Format("%d", health);

will create a text string containing “10”.

*See Also:*

### IndexOf 

*(Formerly known as global function StrContains, which is now
obsolete) ILBRK *(Formerly known as String.Contains, which
is now obsolete)**

    String.IndexOf(string needle)

Checks to see if NEEDLE is contained within the specified string.
Returns the character position of the match if it is, or -1 if it is
not.

This function is not case sensitive; ie. testing “test string” for
“sTRiN” would match.

    String haystack = "The haystack had a needle in it somewhere.";
    int result = haystack.IndexOf("a needle");

    if (result == -1) {
      Display("The string didn't contain the needle.");
    }
    else {
      Display("a needle was found starting at character %d in the string.", result);
    }

*See Also: ,*

### IsNullOrEmpty 

    static bool String.IsNullOrEmpty(String stringToCheck)

Returns whether the supplied string is null or empty. This is simply
shorthand for the following:

    if ((stringToCheck == null) || (stringToCheck == ""))

in other words, you can easily use this to check whether a string has
any text in it or not.

**NOTE: This function is static, which means you do not
call it on an existing string variable, but use `String.IsNullOrEmpty()`
instead. See the example.**

    String myString;
    if (String.IsNullOrEmpty(myString))
    {
      myString = "Some text";
    }

will set the myString variable to “Some text” if it is null or empty
(which it is).

*Compatibility: Supported by **AGS 3.0.1 and
later versions.***

### LowerCase 

*(Formerly known as global function StrToLowerCase, which is now
obsolete)*

    String.LowerCase()

Returns a lower case version of the specified string.

**NOTE: The new string is returned from this function; it
does **NOT modify the original string.****

    String mystring = "THIS is a test string";
    String lowercased = mystring.LowerCase();
    Display("Old: %s, new: %s", mystring, lowercased);

will display “Old: THIS is a test string, new: this is a test string”.

*See Also:*

### Replace 

    String.Replace(string lookForText, string replaceWithText,
                   optional bool caseSensitive)

Creates a copy of this string, with all instances of
*lookForText replaced with the
*replaceWithText.**

*caseSensitive is *false by default, but you
can set it to true so that only case-sensitive matches of the
*lookForText will be replaced.***

**NOTE: The new string is returned from this function; it
does **NOT modify the original string.****

    String original = "Hello from the script!";
    String changed = original.Replace("hello", "goodbye");
    Display("Old: %s, new: %s", original, changed);

will display “Old: Hello from the script!, new: goodbye from the
script!”.

*Compatibility: Supported by **AGS 3.1.0 and
later versions.***

*See Also:*

### ReplaceCharAt 

*(Formerly known as global function StrSetCharAt, which is now
obsolete)*

    String.ReplaceCharAt(int index, char newChar)

Changes the character at INDEX in the string to NEWCHAR.

INDEX is the character index into the string (where 0 is the first
character, and the last allowable value is the string's Length minus 1).

**NOTE: The new string is returned from this function; it
does **NOT modify the original string.****

    String mystring = "Hello";
    String changed = mystring.ReplaceCharAt(2, 'm');
    Display("Old: %s, new: %s", newstring, changed);

will display “Old: Hello, new: Hemlo”.

*See Also: ,*

### StartsWith 

    bool String.StartsWith(string lookForText, optional bool caseSensitive)

Returns *true if this string starts with
*lookForText, or *false if not.***

*caseSensitive is *false by default, but you
can set it to true so that the function will only return
*true for an exact-case match.***

    String myString = "Hello from the script!";
    if (myString.StartsWith("hello"))
    {
      Display("Starts with hello!");
    }

will display the “Starts with hello!” message.

*Compatibility: Supported by **AGS 3.1.0 and
later versions.***

*See Also: ,*

### Substring 

    String.Substring(int index, int length)

Returns part of the string, starting from character *index
and *length characters long.**

*index is the initial character index, where 0 is the first
character and (Length - 1) is the last. *length specifies
how many characters to retrieve.**

    String mystring = "Hello World!";
    String substring = mystring.Substring(3, 5);
    Display("Original: %s, Substring: %s", mystring, substring);

will display “Original: Hello World!, Substring: lo Wo”.

*See Also: ,*

### Truncate 

    String.Truncate(int length)

Returns a version of the string that has been truncated down to
*length characters.*

**NOTE: The new string is returned from this function; it
does **NOT modify the original string.****

    String mystring = "Hello World!";
    String truncated = mystring.Truncate(4);
    Display("Original: %s, Truncated: %s", mystring, truncated);

will display “Original: Hello World!, Truncated: Hell”.

*See Also: ,*

### UpperCase 

*(Formerly known as global function StrToUpperCase, which is now
obsolete)*

    String.UpperCase()

Returns an upper case version of the specified string.

**NOTE: The new string is returned from this function; it
does **NOT modify the original string.****

    String mystring = "THIS is a test string";
    String uppercased = mystring.UpperCase();
    Display("Old: %s, new: %s", mystring, uppercased);

will display “Old: THIS is a test string, new: THIS IS A TEST STRING”.

*See Also:*

### AsFloat property 

    readonly float String.AsFloat;

Converts the string into a float, and returns that value. Returns 0.0 if
the string does not contain a number.

    String text1, text2;
    float number1,number2;
    text1 = "57.362";
    text2 = "Hello";
    number1 = text1.AsFloat;
    number2 = text2.AsFloat;

will set number1 value to 57.362 and number2 value to 0.0 This function
is useful for processing strings input from the user.

**NOTE: To convert a float to a string, you can use the
command.**

*See Also: , ,*

### AsInt property 

*(Formerly known as global function StringToInt, which is now
obsolete)*

    readonly int String.AsInt;

Converts the string into an integer, and returns that value. Returns
zero if the string does not present a number.

**NOTE: This operation takes just the leading sequence of
the characters from the string, if it contains digits and other symbols
which could be a part of number. If the string has the valid number only
in the middle, it will not work.**

    String text1, text2;
    int number1,number2;
    text1 = "53";
    text2 = "Hello";
    number1 = text1.AsInt;
    number2 = text2.AsInt;

will set number1 value to 53 and number2 value to 0. This function is
useful for processing strings input from the user.

**NOTE: To convert an integer to a string, you can use the
command.**

*See Also: , ,*

### Chars property 

*(Formerly known as global function StrGetCharAt, which is now
obsolete)*

    readonly char String.Chars[position];

Returns the character at POSITION within the string.

POSITION is the character index (where 0 is the first character, and the
last allowable value is the Length minus 1).

If POSITION is outside the string, this function returns 0.

**NOTE: The *Chars array is read-only. If you
want to change one of the characters in the string, use .***

    String text = "This is my string.";
    Display("The 4th character is: %c", text.Chars[3]);

will display “The 4th character is: s”.

*See Also: ,*

### Length property 

*(Formerly known as global function StrLen, which is now
obsolete)*

    readonly int String.Length;

Returns the length of the string, in characters.

    String text = "This is my string.";
    Display("Length: %d", text.Length);

will display “Length: 18”.

System functions and properties
-------------------------------

### AudioChannelCount property 

    readonly static int System.AudioChannelCount;

Gets the number of Audio Channels available to the game (in the current
version of AGS this is 8).

This is useful if you want to loop through all the audio channels and
check what is playing on them.

    Display("There are %d audio channels.", System.AudioChannelCount);

will display a message with the number of audio channels.

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also:*

### AudioChannels property 

    readonly static AudioChannel* System.AudioChannels[];

Gets the AudioChannel instance for the specified channel number. This
allows you to query the audio channel and find out what is playing on
it.

    AudioChannel *channel = System.AudioChannels[2];
    Display("Channel 2's current volume is %d.", channel.Volume);

will display a message with Audio Channel 2's current volume.

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also: ,*

### CapsLock property 

    readonly static bool System.CapsLock;

Gets whether Caps Lock is active on the player's system.

You might want to use this to warn the player to switch it off before
typing a password in, for example.

    if (System.CapsLock)
    {
      Display("The CAPS LOCK light is on.");
    }

will display a message if Caps Lock is on.

*Compatibility: Supported by **AGS 3.0.1 and
later versions.***

*See Also: ,*

### ColorDepth property (system) 

*(Formerly known as system.color\_depth, which is now
obsolete)*

    readonly static int System.ColorDepth;

Returns the colour depth at which the game is running. This is the
overall game colour depth setting, and it is possible for individual
sprites or backgrounds to be different.

    Display("Game is running at: %d x %d, %d-bit colour", System.ScreenWidth,
                                      System.ScreenHeight, System.ColorDepth);

will display the current resolution and colour depth

*See Also: ,*

### Gamma property 

    static int System.Gamma;

Gets/sets the current screen Gamma level. This is 100 by default, and
you can set it anywhere from 0 (pitch black) to 200 (double normal
brightness).

must return *true in order for this property to have any
effect.*

Because every player's monitor will be different, you should normally
use this property linked to a GUI Slider in order to allow the player to
adjust it to suit their system.

    if (System.SupportsGammaControl) {
      System.Gamma = 150;
    }

will turn the screen brightness up to `50%` higher than normal

*See Also:*

### HardwareAcceleration property 

    readonly static bool System.HardwareAcceleration;

Returns whether the game is running with hardware acceleration (eg.
Direct3D). If this is the case then RawDrawing is likely to be slower,
but alpha blending and large sprites are likely to be faster, than when
the non-accelerated driver is used.

**Cross-Platform Support**

Windows: ** Direct3D driver ILBRK MS-DOS: ** No
ILBRK Linux: ** No ILBRK MacOS: ** No
********

    if (System.HardwareAcceleration) {
      Display("Yay, we can draw loads of alpha blended sprites fast!");
    }

will display a message if the game is being run with hardware
acceleration

See Also:

### HasInputFocus property 

    readonly static bool System.HasInputFocus;

Tells whether the game window currently has input focus, meaning it is
active and player can control the game.

If your game is made to continue running in the background, when the
user switches out from game, you may use this property in scripts to
know if that actually happened.

    if (!System.HasInputFocus)
      return;

skips the rest of the function if player has switched out from the game.

    function repeatedly_execute()
    {
      if (!System.HasInputFocus && IsGamePaused() == 0) {
        PauseGame();
      } else if (System.HasInputFocus && IsGamePaused() == 1) {
        UnPauseGame();
      }
    }

pauses game when player switches out, and unpauses it when player
switches back to game.

*Compatibility: Supported by **AGS 3.3.5 and
later versions.***

*See Also:*

### NumLock property 

    readonly static bool System.NumLock;

Gets whether Num Lock is active on the player's system.

You might want to use this to warn the player to switch it off before
using the numeric keypad arrow keys, for example.

    if (System.NumLock)
    {
      Display("The NUM LOCK light is on.");
    }

will display a message if Num Lock is on.

*Compatibility: Supported by **AGS 3.0.1 and
later versions.***

*See Also: ,*

### OperatingSystem property 

*(Formerly known as system.os, which is now obsolete)*

    readonly static eOperatingSystem System.OperatingSystem;

Returns which operating system the game is currently running under. It
can be one of the following values:

    eOSDOS
    eOSWindows
    eOSLinux
    eOSMacOS
    eOSAndroid
    eOSiOS
    eOSPSP

    if (System.OperatingSystem == eOSWindows) {
      Display("Running on Windows!");
    }
    else {
      Display("Not running on Windows!");
    }

### RuntimeInfo property 

    readonly static String System.RuntimeInfo;

Returns the string containing short description of the enviroment the
game is currently running in, such as engine version, graphics mode, and
available game resources.

This is meant mainly for debug purposes.

**NOTE: System.RuntimeInfo is a more convenient analogue of
Debug(1, 0) command, being more explicit and working on both release and
debug modes of the game.**

    function on_key_press(eKeyCode keycode) {
      if (keycode == eKeyCtrlV) {
        Display(System.RuntimeInfo);
    }

*Compatibility: Supported by **AGS 3.4.0 and
later versions.***

*See Also:*

### ScreenHeight property 

*(Formerly known as system.screen\_height, which is now
obsolete)*

    readonly static int System.ScreenHeight;

Returns the actual screen height that the game is running at. If a
graphic filter is in use, the resolution returned will be that before
any stretching by the filter has been applied. If letterbox borders are
enabled, the screen size reported will include the size of these
borders.

**NOTE: Do **NOT use this to calculate the
centre of the screen when working with co-ordinates. Co-ordinates are
relative to the viewport, so you should use instead. Use the
ScreenHeight property only for reporting purposes.****

    Display("Game is running at: %d x %d, %d-bit colour", System.ScreenWidth,
                                      System.ScreenHeight, System.ColorDepth);

will display the current resolution and colour depth

*See Also: , ,*

### ScreenWidth property 

*(Formerly known as system.screen\_width, which is now
obsolete)*

    readonly static int System.ScreenWidth;

Returns the actual screen width that the game is running at. If a
graphic filter is in use, the resolution returned will be that before
any stretching by the filter has been applied. If widescreen side
borders are enabled, the screen width reported will include the size of
these borders.

**NOTE: Do **NOT use this to calculate the
centre of the screen when working with co-ordinates. Co-ordinates are
relative to the viewport, so you should use instead. Use the ScreenWidth
property only for reporting purposes.****

    Display("Game is running at: %d x %d, %d-bit colour", System.ScreenWidth,
                                      System.ScreenHeight, System.ColorDepth);

will display the current resolution and colour depth

*See Also: ,*

### ScrollLock property 

    readonly static bool System.ScrollLock;

Gets whether Scroll Lock is active on the player's system.

Note that when running your game under the debugger, the Scroll Lock key
will break out of the game into the debugger, so it is not advised that
you use it for any other purpose in your game.

    if (System.ScrollLock)
    {
      Display("The SCROLL LOCK light is on.");
    }

will display a message if Scroll Lock is on.

*Compatibility: Supported by **AGS 3.0.1 and
later versions.***

*See Also: ,*

### SupportsGammaControl property 

    readonly static bool System.SupportsGammaControl;

Gets whether the player's PC supports changing the screen's gamma
control settings.

This must return *true before you try and change the
property. The situations in which this will be supported are listed
below.*

**Cross-Platform Support**

Windows: ** Full-screen only ILBRK MS-DOS: ** No
ILBRK Linux: ** No ILBRK MacOS: ** No
********

    if (System.SupportsGammaControl) {
      Display("We can change the system gamma level!");
    }

will display a message if the system supports changing the gamma

*See Also:*

### Version property 

*(Formerly known as system.version, which is now obsolete)*

    readonly static String System.Version;

Returns the AGS engine version number. This could be useful from within
script modules in order to use features available on a particular engine
version, or work around any known bugs.

The string returned is the full version number, for example “2.71.833”.

    Display("AGS version: %s", System.Version);

will display the AGS version number

### ViewportHeight property 

*(Formerly known as system.viewport\_height, which is now
obsolete)*

    readonly static int System.ViewportHeight;

Returns the height of the current viewport. This is reported in the same
co-ordinate system that the game is using, so you can use this to find
out what the maximum possible Y co-ordinate is within the screen.

    Display("Game viewport: %d x %d", System.ViewportWidth, System.ViewportHeight);

will display the current viewport size

*See Also: ,*

### ViewportWidth property 

*(Formerly known as system.viewport\_width, which is now
obsolete)*

    readonly static int System.ViewportWidth;

Returns the width of the current viewport. This is reported in the same
co-ordinate system that the game is using, so you can use this to find
out what the maximum possible X co-ordinate is within the screen.

    Display("Game viewport: %d x %d", System.ViewportWidth, System.ViewportHeight);

will display the current viewport size

*See Also: ,*

### Volume property (system) 

*(Formerly known as SetDigitalMasterVolume, which is now
obsolete) ILBRK *(Formerly known as SetMusicMasterVolume,
which is now obsolete)**

    static int System.Volume;

Gets/sets the overall system volume, from 0 to 100. This is the master
volume control, that affects all audio in the game. You would usually
attach this to a GUI Slider to enable the player to control the volume
from some sort of Control Panel GUI.

    System.Volume = 80;

will set the overall output volume to 80.

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also: ,*

### VSync property 

*(Formerly known as system.vsync, which is now obsolete)*

    static bool System.VSync;

Gets/sets whether AGS waits for the vertical retrace before rendering
each frame. This is off by default.

If you switch this on, it can help to reduce the “tearing” effect that
you can get when the screen scrolls. However, doing so will lock the
game frame rate to the monitor's refresh rate, which will mean you
cannot reliably set a game speed higher than 60 fps.

**NOTE: This property has no effect with the Direct3D
driver.**

    if (System.VSync) {
      Display("Vertical retrace sync is enabled!");
    }

will display a message if vsync is on

### Windowed property 

*(Formerly known as system.windowed, which is now
obsolete)*

    readonly static bool System.Windowed;

Returns whether the game is currently running in a window
(*true) or full-screen (*false).**

    if (System.Windowed) {
      Display("Game is running in a window!");
    }

will display a message if the game is running in a window

Text display / Speech functions
-------------------------------

### Display 

    Display (string message, ...)

Displays a message to the screen. It will be displayed in the standard
message box, and centred in the middle of the screen.

You can insert the value of variables into the message. For more
information, see the section.

    int my_counter;
    Display ("The counter is currently set to %d.", my_counter);

will replace the '`%d`' with the value of the variable “my\_counter”.

NOTE: Display is a blocking function - that is, control will not return
to the script until the player has removed the text window (by pressing
a key or clicking the mouse). While the window is displayed, all other
processing, like animations and interface display, are disabled. This is
usually used for responses to the player LOOKing at things.

*See Also: , , , ,*

### DisplayAt 

    DisplayAt(int x, int y, int width, string message, ...)

Identical to the “Display” function, only this allows you to define the
position and size of the window where the text is displayed. The X and Y
variables define the co-ordinates of the upper-left corner of the
window.

The WIDTH variable defines the maximum width of the window. The height
is then automatically calculated so that the message fits into the
window.

You can insert the value of variables into the message. For more
information, see the section.

Note: This is a blocking call. See the “Display” help for more
information.

    DisplayAt (50,50,100, "This is a message");

will display the message at coordinates 50,50 in a box 100 pixels wide.

*See Also: ,*

### DisplayAtY 

    DisplayAtY (int y, string message)

Similar to the Display function, except that this will display the
message box at the specified Y location on the screen. The Y defines the
co-ordinate of the top of the message box. The horizontal positioning
will be automatically calculated as usual.

    DisplayAt (50, "This is a message");

will display the message at y coordinate 50.

*See Also: ,*

### DisplayMessage 

    DisplayMessage (int message_number)

Identical to the Display function, but this uses a message text defined
in the AGS Editor rather than in the script. It will either use a
message from the current room, or a global message (if message\_number
&gt;= 500).

    DisplayMessage(220);

will display the message 220 of the Room message editor.

*See Also: ,*

### DisplayMessageAtY 

    DisplayMessageAtY (int message_number, int yposition)

Identical to the DisplayMessage function, except that the text box is
positioned with its top at YPOSITION, the same way as DisplayAtY works.

This is useful if you have an important graphic in the middle of the
screen that the text box would normally cover up - with this function
you can place the message above or below it.

    DisplayMessageAtY(527, 200);

will display global message 527, in the lower half of the screen.

*See Also: ,*

### DisplayTopBar 

    DisplayTopBar(int y, int text_color, int back_color, string titleText, string message, ...)

Displays a message in a text window, with a caption bar on top of it.

This displays MESSAGE in a similar way to the normal Display command,
but above the text window a caption bar will be displayed with TITLETEXT
in it. This method was used in some early Sierra games to indicate who
was talking by having their name in the caption, and can be handy if you
don't want to draw a talking view for a character.

You can insert the value of variables into the message. For more
information, see the section.

The Y parameter specifies the Y location on the screen where the message
box will appear. The default is 25.

The TEXT\_COLOR parameter specifies the text colour of the top bar, and
the BACK\_COLOR specifies the background colour of the top bar.

You can pass 0 for Y, TEXT\_COLOR or BACK\_COLOR - if you do, it will
use the setting you used last time.

There are a couple of game variables available which can further
customize the look of the bar. You can change these before calling
DisplayTopBar.

**game.top\_bar\_bordercolor sets the colour used for the
bar's border (set to the same colour as the backcolor if you don't want
a border) ILBRK **game.top\_bar\_borderwidth sets the width
of the bar's border, in pixels (default 1) ILBRK
**game.top\_bar\_font sets the font to use for the top bar.
The default is -1, which means that the current Normal font is used. Set
it to a specific number to use that font instead.******

    DisplayTopBar(25, 8, 7, "Evil wizard", "Get out of my house and never return!");

will display “Get out of my house and never return!” in the message box,
with the caption bar reading “Evil wizard”. The message box will have
dark grey text on a light gray background.

*See Also: ,*

ViewFrame functions and properties
----------------------------------

### Flipped property 

*(Formerly part of GetGameParameter, which is now
obsolete)*

    readonly bool ViewFrame.Flipped

Gets whether the frame was set to Flipped in the editor.

    ViewFrame *frame = Game.GetViewFrame(WALKING, 2, 4);
    if (frame.Flipped) {
      Display("This frame is flipped");
    }
    else {
      Display("This frame is not flipped");
    }

*See Also: ,*

### Frame property (view frame) 

*(Formerly part of GetGameParameter, which is now
obsolete)*

    readonly int ViewFrame.Frame

Returns the frame number represented by this ViewFrame.

    ViewFrame *frame = Game.GetViewFrame(WALKING, 2, 4);
    Display("This ViewFrame is view %d, loop %d, frame %d",
      frame.View, frame.Loop, frame.Frame);

*See Also: , ,*

### Graphic property (view frame) 

*(Formerly part of GetGameParameter, which is now
obsolete)*

    int ViewFrame.Graphic

Gets/sets the sprite slot number that this view frame displays.

    ViewFrame *frame = Game.GetViewFrame(WALKING, 2, 4);
    Display("This frame uses sprite %d", frame.Graphic);

*See Also:*

### LinkedAudio property (view frame) 

*(Formerly known as ViewFrame.Sound, which is now obsolete)
ILBRK *(Formerly known as SetFrameSound, which is now
obsolete) ILBRK *(Formerly part of GetGameParameter, which
is now obsolete)***

    AudioClip* ViewFrame.LinkedAudio

Gets/sets the audio clip that plays when this frame comes around in
animations.

If there is no linked sound, this should be *null.*

    ViewFrame *frame = Game.GetViewFrame(WALKING, 2, 4);
    if (frame.LinkedAudio == null)
    {
      Display("This frame has no frame-linked audio.");
    }
    else
    {
      frame.LinkedAudio.Play();
    }

checks view WALKING to see if frame 4 in loop 2 has a linked audio clip;
if so, plays it.

*Compatibility: Supported by **AGS 3.2.0 and
later versions.***

*See Also:*

### Loop property (view frame) 

*(Formerly part of GetGameParameter, which is now
obsolete)*

    readonly int ViewFrame.Loop

Returns the loop number represented by this ViewFrame.

    ViewFrame *frame = Game.GetViewFrame(WALKING, 2, 4);
    Display("This ViewFrame is view %d, loop %d, frame %d",
      frame.View, frame.Loop, frame.Frame);

*See Also: , ,*

### Speed property (view frame) 

*(Formerly part of GetGameParameter, which is now
obsolete)*

    readonly int ViewFrame.Speed

Gets the speed setting of the view frame. This is 0 by default but may
have been changed in the AGS Editor.

    ViewFrame *frame = Game.GetViewFrame(WALKING, 2, 4);
    Display("This frame has speed %d.", frame.Speed);

*See Also:*

### View property (view frame) 

*(Formerly part of GetGameParameter, which is now
obsolete)*

    readonly int ViewFrame.View

Returns the view number represented by this ViewFrame.

    ViewFrame *frame = Game.GetViewFrame(WALKING, 2, 4);
    Display("This ViewFrame is view %d, loop %d, frame %d",
      frame.View, frame.Loop, frame.Frame);

*See Also: , ,*

SCUMM\_VERBCOIN\_GUI functions
------------------------------

SCUMM\_VERBCOIN\_GUI is a script module that is included with the Verb
Coin template. The functions in this section are only available if you
have created your game using that template.

### SCUMM\_VERBCOIN\_GUI Deselect {#SCUMM_VERBCOIN_GUI.Deselect}

    static SCUMM_VERBCOIN_GUI.Deselect()

Deselect an item if it is active or quit the inventory. Used for
keyboard support.

**NOTE: This function is part of the Verb Coin template and
is only available if you used this template to create your game.**

*See Also: ,*

### SCUMM\_VERBCOIN\_GUI DisableVerbCoinGUI {#SCUMM_VERBCOIN_GUI.DisableVerbCoinGUI}

    static SCUMM_VERBCOIN_GUI.DisableVerbCoinGUI(bool disabled)

Activates/deactivates the SCUMM Verbcoin GUI system. This can be used to
turn the SCUMM VerbCoin system on and off at runtime.

**NOTE: This function is part of the Verb Coin template and
is only available if you used this template to create your game.**

    SCUMM_VERBCOIN_GUI.DisableVerbCoinGUI(true);

will disable all verbcoin processing code.

### SCUMM\_VERBCOIN\_GUI DoubleClickSpeed {#SCUMM_VERBCOIN_GUI.DoubleClickSpeed}

    static SCUMM_VERBCOIN_GUI.DoubleClickSpeed(int speed)

Sets the time frame in which a double-click can be registered. Increase
this value for slower double-clicks, decrease this value for quicker
double-clicks.

**NOTE: This function is part of the Verb Coin template and
is only available if you used this template to create your game.**

    SCUMM_VERBCOIN_GUI.DoubleClickSpeed(GetGameSpeed()/4);

will set the double-click speed to 1/4 of a second. (This is a good
default)

*See Also:*

### SCUMM\_VERBCOIN\_GUI GoInventory {#SCUMM_VERBCOIN_GUI.GoInventory}

    static SCUMM_VERBCOIN_GUI.GoInventory()

This function opens and closes your inventory.

**NOTE: This function is part of the Verb Coin template and
is only available if you used this template to create your game.**

### SCUMM\_VERBCOIN\_GUI Item\_Count {#SCUMM_VERBCOIN_GUI.Item_Count}

    static SCUMM_VERBCOIN_GUI.Item_Count(int count)

Sets the number of items that inventory scrolling will use to position
to the next x amount of items.

This value should equal the amount of items that fit in your inventory
window.

**NOTE: This function is part of the Verb Coin template and
is only available if you used this template to create your game.**

    SCUMM_VERBCOIN_GUI.Item_Count(10);

will make sure that on the next inventory scroll you will start with
item 11, 21, 31, ...

*See Also: ,*

### SCUMM\_VERBCOIN\_GUI InvScroll\_Left {#SCUMM_VERBCOIN_GUI.InvScroll_Left}

    static SCUMM_VERBCOIN_GUI.InvScroll_Left()

Scrolls the inventory to the left, by the number of items set with
Item\_Count.

**NOTE: This function is part of the Verb Coin template and
is only available if you used this template to create your game.**

*See Also: ,*

### SCUMM\_VERBCOIN\_GUI InvScroll\_Right {#SCUMM_VERBCOIN_GUI.InvScroll_Right}

    static SCUMM_VERBCOIN_GUI.InvScroll_Right()

Scrolls the inventory to the right, by the number of items set with
Item\_Count.

**NOTE: This function is part of the Verb Coin template and
is only available if you used this template to create your game.**

*See Also: ,*

### SCUMM\_VERBCOIN\_GUI Inv\_Border\_active {#SCUMM_VERBCOIN_GUI.Inv_Border_active}

    static SCUMM_VERBCOIN_GUI.Inv_Border_active(bool x_borders, bool y_borders)

Sets which inventory exit borders are active.

Inventory exit borders determine where the inventory will exit when
moving over a line.

**NOTE: This function is part of the Verb Coin template and
is only available if you used this template to create your game.**

    SCUMM_VERBCOIN_GUI.Inv_Border_active(false, true);

will make the game exit the inventory when moving the mouse over either
the top or the bottom of the screen.

*See Also:*

### SCUMM\_VERBCOIN\_GUI Inv\_Border\_SetPos {#SCUMM_VERBCOIN_GUI.Inv_Border_SetPos}

    static SCUMM_VERBCOIN_GUI.Inv_Border_SetPos(int top, int bottom,
                                                int left, int right)

Sets the inventory exit border positions.

Inventory exit borders determine where the inventory will exit when
moving over a line.

**NOTE: This function is part of the Verb Coin template and
is only available if you used this template to create your game.**

    SCUMM_VERBCOIN_GUI.Inv_Border_SetPos(20, 220, 20, 295);

will set the top exit border to y-coordinate 20, the bottom border to
y-coordinate 220, the left border to x-coordinate 20 and the right
border to x-coordinate 295

*See Also:*

### SCUMM\_VERBCOIN\_GUI Inventory\_GUI {#SCUMM_VERBCOIN_GUI.Inventory_GUI}

    static SCUMM_VERBCOIN_GUI.Inventory_GUI(int gInventory_ID,int gInvUnderlay_ID)

Sets the inventory gui ID's, so the module will know which GUI is your
inventory and which GUI is the inventory underlay.

This allows you to change your inventory GUI's on the fly, which is
particularly interesting if you have a game with multiple playable
characters. You could have a different inventory for each character!

If the game is 32-bit with alpha-blended (transparent) GUI buttons on
the inventory, you need to use an Underlay gui which contains the actual
inventory background, and the regular gui which is empty except for the
inventory window and the gui buttons.

If your game does not use alpha-blended GUI buttons, leave the underlay
inventory empty. (use sprite 0 for its background)

**NOTE: This function is part of the Verb Coin template and
is only available if you used this template to create your game.**

    SCUMM_VERBCOIN_GUI.Inventory_GUI(2, 3);

will tell the module your inventory gui is GUI nr.2 and that the
underlay gui is GUI nr.3

### SCUMM\_VERBCOIN\_GUI RunInteraction {#SCUMM_VERBCOIN_GUI.RunInteraction}

    static SCUMM_VERBCOIN_GUI.RunInteraction(CursorMode)

Runs the event of choice. Used for keyboard support.

**NOTE: This function is part of the Verb Coin template and
is only available if you used this template to create your game.**

    SCUMM_VERBCOIN_GUI.RunInteraction(eModeTalkto);

*See Also: ,*

### SCUMM\_VERBCOIN\_GUI Select {#SCUMM_VERBCOIN_GUI.Select}

    static SCUMM_VERBCOIN_GUI.Select()

Selects an item, or if an item is active tries to use it. Used for
keyboard support.

**NOTE: This function is part of the Verb Coin template and
is only available if you used this template to create your game.**

*See Also: ,*

### SCUMM\_VERBCOIN\_GUI Verbcoin\_GUI {#SCUMM_VERBCOIN_GUI.Verbcoin_GUI}

    static SCUMM_VERBCOIN_GUI.Verbcoin_GUI(int gVerbcoin_ID)

Sets the verbcoin gui ID, so the module will know which GUI is your
verbcoin GUI.

This is particularly useful if you have a game with multiple playable
characters, where you could have a different verbcoin for each
character.

**NOTE: This function is part of the Verb Coin template and
is only available if you used this template to create your game.**

    SCUMM_VERBCOIN_GUI.Verbcoin_GUI(1);

will tell the module your verbcoin gui is GUI nr.1

### SCUMM\_VERBCOIN\_GUI verbgraphic {#SCUMM_VERBCOIN_GUI.verbgraphic}

    static SCUMM_VERBCOIN_GUI.verbgraphic(ButtonChoice, int sprite_number)

Attaches a verbcoin sprite to a button. This sprite will be displayed
when moving over the button.

The only exception is the 'bIdle' button, which is not a button but the
default verbcoin graphic with no buttons active.

**NOTE: This function is part of the Verb Coin template and
is only available if you used this template to create your game.**

    SCUMM_VERBCOIN_GUI.verbgraphic(bTalk, 2);

will set the sprite for moving over the talk button to sprite 2

### SCUMM\_VERBCOIN\_GUI doubleclick variable {#SCUMM_VERBCOIN_GUI.doubleclick}

    global bool doubleclick

Used to determine when a double-click has occured.

**NOTE: This variable is part of the Verb Coin template and
is only available if you used this template to create your game.**

      if (doubleclick == false){
        Display("You made a single-click");
      }
      else{
        Display("You just made a double-click!");
      }

will display “You made a single-click” when you made a single-click on
the object/hotspot/character/...

*See Also:*

Reference
=========

This section contains a reference for various parts of the system except
the scripting language, which has its own separate Scripting section.

Event Types
-----------

The following events are available in the “Events” section of the
Properties Window (when clicking the lightning bolt icon).

### Hotspot events

Player stands on hotspot

:   occurs repeatedly while the player character is standing on
    the hotspot.

Look at hotspot

:   occurs when the player clicks on the hotspot while in the “Look”
    mode (cursor mode 1).

Interact with hotspot

:   occurs when the player clicks on the hotspot while in the “Interact”
    mode (cursor mode 2).

Use inventory on hotspot

:   occurs when the player clicks on the hotspot while in the “Use
    inventory” mode (cursor mode 4). You can use the property to
    distinguish which item they used. ILBRK

Speak to hotspot

:   occurs when the player clicks on the hotspot while in the “Talk”
    mode (cursor mode 3).

Any click on hotspot

:   occurs when the player clicks on the hotspot in any cursor mode
    (except Walk). This allows you to add extra modes like smell, taste,
    push, pull, and so on. This event also occurs as well as the other
    event for the Look, Interact and Talk modes.

Mouse moves over hotspot

:   occurs repeatedly while the mouse cursor is over the hotspot. You
    can use this to highlight the cursor, and for other various effects.

### Object events

Look at object

:   occurs when the player clicks on the object while in the “Look” mode
    (cursor mode 1).

Interact with object

:   occurs when the player clicks on the object in the “Interact” mode
    (cursor mode 2).

Speak to object

:   occurs when the player clicks on the object in the “Talk” mode
    (cursor mode 3).

Use inventory on object

:   works like “Use inventory on hotspot” - see that description (above)
    for more information.

### Room events

Walk off left

:   occurs when the player character walks off the left edge of
    the screen.

Walk off right

:   occurs when the player walks off the right edge of the screen.

Walk off bottom

:   occurs when the player character walks off the bottom edge of
    the screen.

Walk off top

:   occurs when the player character walks off the top edge of
    the screen.

First time enters room

:   occurs the first time the player enters the room. This event occurs
    AFTER the screen has faded in, so it allows you to display a message
    describing the scene.

Player enters room (before fadein)

:   occurs just after the room is loaded into memory. This event occurs
    every time the player enters the screen, and it happens BEFORE the
    screen has faded in, which allows you to change object graphics and
    do other things to the screen which the player won't notice.

    *NOTE: This event is ONLY meant for adjusting things such as
    object and character placement. Do NOT use this event for any sort
    of automated intro to the room - use the “Enters Room After Fade In”
    event for that instead.*

Repeatedly execute

:   occurs repeatedly on every interpreter cycle. The normal game speed
    is 40 cycles per second, so this event occurs about every
    25 milliseconds.

Player enters room (after fadein)

:   occurs every time the player enters the room, AFTER the screen
    has faded-in. Suitable for displaying text descriptions and so on,
    that you want the player to see.

Player leaves room

:   occurs when the player leaves the screen, just before the screen
    fades out.

### Inventory item events

Look at inventory

:   occurs when the player clicks on the inventory item while in the
    “look” mode.

Interact with inventory

:   currently, because the Interact mode selects the inventory item,
    this event can only be triggered by manually calling the
    InventoryItem.RunInteraction script function (ie. you have to use
    the Handle Inv Clicks in Script option).

Speak to inventory

:   only applies to the Lucasarts-style inventory, occurs when the
    player clicks the Talk icon on the inventory item.

Use inventory on inv

:   occurs when the player uses another inventory object on this one.
    You can use the property to distinguish which item they used. ILBRK
    This event allows the player to combine items, and so on. For
    example, if they had picked up a laptop computer and a battery
    separately, then you could use this to allow them to insert the
    battery into the computer.

Other click on inventory

:   only applies to the Lucasarts-style inventory, occurs when the
    player clicks any other cursor mode (apart from look, talk
    and use\_inv) on the item.

### Character events

Look at character

:   occurs when the player clicks on a character while in the
    “look” mode.

Interact with character

:   occurs when the player clicks on a character while in the
    “interact” mode.

Speak to character

:   occurs when the player clicks on a character while in the
    “talk” mode.

Use inventory on character

:   occurs when the player uses an inventory object on a character. This
    event could be used to allow the player to give items to characters.

Any click on character

:   occurs when the player clicks any other cursor mode (apart from
    look, talk and use\_inv) on the character.

### Region events

While player stands on region

:   occurs repeatedly while the player character stands on this region

Player walks onto region

:   occurs when the player moves from another region onto this one. Will
    also activate on whichever region they start on when they enter
    the screen.

Player walks off region

:   occurs when the player leaves the current region. Does not occur if
    they go to a different room.

System limits
-------------

This section tells you the maximums for various parts of the system. If
you have been wondering “How many rooms can I have?” or something
similar, chances are this section will answer it.

There are maximum...

          40  objects per room
         299  state-saving rooms per game
         300  inventory items
       30000  imported sprites
         500  dialog topics
          30  options per dialog topic
          20  screen overlays at a time
           5  background frames per room
          20  mouse cursors
           8  audio channels
         100  local messages per room (excluding script)
          30  fonts
    unlimited words in the text parser dictionary
    unlimited characters
    unlimited views
    unlimited GUIs
    unlimited controls on each GUI
    unlimited loops per view
    unlimited frames per loop
    unlimited custom properties

We are working on removing existing limitations in the AGS, so some of
the remaining restrictions might be loosened or eliminated in the
following updates.

Keyboard Shortcuts 
------------------

The AGS Editor provides various keyboard shortcuts to help you get your
work done quickly. These are summarized below:

    F1       Help
    F2       Game Statistics
    F3       Find Next
    Ctrl+F4  Close tab
    F5       Run with Debugger
    Ctrl+F5  Run without Debugger
    F7       Build EXE
    F9       Toggle Breakpoint
    F11      Step Into

    Ctrl+A   Select All
    Ctrl+B   Match Brace
    Ctrl+C   Copy
    Ctrl+D   Duplicate line to next
    Ctrl+E   Replace
    Ctrl+F   Find
    Ctrl+G   Open GlobalScript.asc
    Ctrl+H   Open GlobalScript.ash
    Ctrl+L   Open Game
    Ctrl+Q   Quit
    Ctrl+R   Save Room
    Ctrl+S   Save Game
    Ctrl+V   Paste
    Ctrl+W   Close Tab
    Ctrl+X   Cut
    Ctrl+Y   Redo
    Ctrl+Z   Undo

    Ctrl+Space      Show Autocomplete
    Ctrl+Tab        Next tab
    Ctrl+Shift+Tab  Previous tab

    Tab         Indent selected lines
    Shift+Tab   Un-indent selected lines

ASCII code table 
----------------

This section lists the key codes which can be passed to on\_key\_press
and which keys they represent:

    AGS KeyCode       Key         ASCII code
    eKeyNone          none          0
    eKeyCtrlA         Ctrl+A        1
    eKeyCtrlB         Ctrl+B        2
    eKeyCtrlC         Ctrl+C        3
    eKeyCtrlD         Ctrl+D        4
    eKeyCtrlE         Ctrl+E        5
    eKeyCtrlF         Ctrl+F        6
    eKeyCtrlG         Ctrl+G        7
    eKeyCtrlH         Ctrl+H        8
    eKeyCtrlI         Ctrl+I        9
    eKeyCtrlJ         Ctrl+J       10
    eKeyCtrlK         Ctrl+K       11
    eKeyCtrlL         Ctrl+L       12
    eKeyCtrlM         Ctrl+M       13
    eKeyCtrlN         Ctrl+N       14
    eKeyCtrlO         Ctrl+O       15
    eKeyCtrlP         Ctrl+P       16
    eKeyCtrlQ         Ctrl+Q       17
    eKeyCtrlR         Ctrl+R       18
    eKeyCtrlS         Ctrl+S       19
    eKeyCtrlT         Ctrl+T       20
    eKeyCtrlU         Ctrl+U       21
    eKeyCtrlV         Ctrl+V       22
    eKeyCtrlW         Ctrl+W       23
    eKeyCtrlX         Ctrl+X       24
    eKeyCtrlY         Ctrl+Y       25
    eKeyCtrlZ         Ctrl+Z       26
    eKey0             0            48
    eKey1             1            49
    eKey2             2            50
    eKey3             3            51
    eKey4             4            52
    eKey5             5            53
    eKey6             6            54
    eKey7             7            55
    eKey8             8            56
    eKey9             9            57
    eKeyA             A            65
    eKeyB             B            66
    eKeyC             C            67
    eKeyD             D            68
    eKeyE             E            69
    eKeyF             F            70
    eKeyG             G            71
    eKeyH             H            72
    eKeyI             I            73
    eKeyJ             J            74
    eKeyK             K            75
    eKeyL             L            76
    eKeyM             M            77
    eKeyN             N            78
    eKeyO             O            79
    eKeyP             P            80
    eKeyQ             Q            81
    eKeyR             R            82
    eKeyS             S            83
    eKeyT             T            84
    eKeyU             U            85
    eKeyV             V            86
    eKeyW             W            87
    eKeyX             X            88
    eKeyY             Y            89
    eKeyZ             Z            90
    eKeyAmpersand         &            38
    eKeyAsterisk          *            42
    eKeyAt                @            64
    eKeyBackSlash         \            92
    eKeyBackspace         Backspace     8
    eKeyCloseBracket      ]            93
    eKeyCloseParenthesis  )            41
    eKeyColon             :            58
    eKeyComma             ,            44
    eKeyDelete            Delete      383
    eKeyDollar            $            36
    eKeyDoubleQuote       "            34
    eKeyEquals            =            61
    eKeyEscape            ESC          27
    eKeyExclamationMark   !            33
    eKeyForwardSlash      /            47
    eKeyGreaterThan       >            62
    eKeyHash              #            35
    eKeyHyphen            -            45
    eKeyInsert            Insert      382
    eKeyLessThan          <            60
    eKeyOpenBracket       [            91
    eKeyOpenParenthesis   (            40
    eKeyPercent           %            37
    eKeyPeriod            .            46
    eKeyPlus              +            43
    eKeyQuestionMark      ?            63
    eKeyReturn            RETURN       13
    eKeySemiColon         ;            59
    eKeySingleQuote       '            39
    eKeySpace             SPACE        32
    eKeyTab               TAB           9
    eKeyUnderscore        _            95
    eKeyF1                F1          359
    eKeyF2                F2          360
    eKeyF3                F3          361
    eKeyF4                F4          362
    eKeyF5                F5          363
    eKeyF6                F6          364
    eKeyF7                F7          365
    eKeyF8                F8          366
    eKeyF9                F9          367
    eKeyF10               F10         368
    eKeyF11               F11         433
    eKeyF12               F12         434
    eKeyHome              Home        371
    eKeyUpArrow           UpArrow     372
    eKeyPageUp            PageUp      373
    eKeyLeftArrow         LeftArrow   375
    eKeyNumPad5           NumPad 5    376
    eKeyRightArrow        RightArrow  377
    eKeyEnd               End         379
    eKeyDownArrow         DownArrow   380
    eKeyPageDown          PageDown    381

Use these key codes in your on\_key\_press function to process player
input. For example:

    if (keycode == eKeyA) Display("You pressed A");
    if (keycode == eKeyPlus) Display("You pressed the Plus key");

The following extra codes can only be used with IsKeyPressed (ie.
on\_key\_press is never called with these codes):

     403       Left shift
     404       Right shift
     405       Left ctrl
     406       Right ctrl
     407       Alt

Frequently Asked Questions
==========================

This section of the manual is very rarely updated. Please consult the
AGS Forums on the website – in particular, the Beginners Technical Forum
has an excellent Beginners FAQ (the “BFAQ”) which is much more extensive
and is updated regularly with all sorts of Q&A's.

**Q. What's the deal with the license? What does it mean in plain
English?**

A. Adventure Game Studio is pretty much freeware. That means you may use
it freely for non-commerical games, and you don't have to send me
anything in return. There is one requirement - if you want to SELL a
game you make, for profit, then you must contact me beforehand as there
are some licensing issues which you may need to be aware of. When you
finish your game, please do post it on the Announcements Forum and the
Games Database so that everyone can give it a go.

**Q. Why the swapware license? Why aren't you charging for
it?**

A. Because I don't want to. There's no need to be suspicious, the fact
that it's free doesn't necessarily mean that it's rubbish.

**Q. On my screen, I can't move the main character. Wherever I
click to move him, he just stands there.**

A. If the main character isn't on a walkable area, he will not be able
to move. Load the room in the editor, and check that the location where
the character starts is on a walkable area.

**Q. When I enter a certain room, I just get a black
screen.**

A. Make sure that you haven't used a Display Message command in the
“Enters room before fade-in” event for that room. Remember that this
event happens BEFORE the screen fades in.

To make sure, when you get the black screen, try pressing enter, or
clicking the left mouse button. If nothing happens then something more
serious may have happened. If this is the case, press Alt+X, which
should exit the program and allow you to trace which line of script it
has stopped on.

**Q. The character isn't drawn behind my walk-behind
areas!**

A. You need to define the base line for the area, or he will always be
drawn in front. See the tutorial for more information.

**Q. My game EXE file seems to have disappeared.**

A. Because this file is your entire game, including the room files, when
you save a room in the Room Editor it will delete the exe file (because
the room contained in the exe is out of date). To get it back, simply
build the game again by using the “Build EXE” command on the Build menu.

Upgrading to AGS 2.7 
====================

The script language in AGS 2.7 has changed quite significantly from
previous versions. Many of the script commands have become
*object-based, which has several advantages over the
previous approach. This page will attempt to introduce you to the new
method and explain its benefits.*

Firstly, so that you can get an idea of the changes, here's an example
of some old-style script commands and their new equivalents:

    AnimateObjectEx(0,2,0,0,0,1);
    ListBoxAdd(3, 5, "New item");

becomes:

    oWaterfall.Animate(2, 0, eOnce, eForwards, eBlock);
    lstTest.AddItem("New item");

Just from looking at that example the advantages should be obvious; the
script is more intuitive for people to learn, much easier to read (no
guessing what all the numbers mean in the AnimateObjectEx call), and
therefore you're less likely to make mistakes when using it. GUI
controls having names brings it much more into line with Visual
Basic-style GUI development, so you don't have to remember what control
number all your buttons are.

The script editor's autocomplete functionality has been significantly
enhanced to aid in all this as well. You'll see as you start to
experiment that autocomplete pops up more often and lists only the
relevant commands thanks to object-based scripting.

**So does this mean I have to throw out all my scripts?**

No, certainly not! The new version is fully backwards compatible, so all
your existing scripts will continue to work just fine. However, for any
new scripts that you write, it's strongly recommended that you use the
new object-based commands.

**Ok, so uh... what's changed exactly?**

The script language syntax hasn't changed at all (that's the way you use
semicolons, brackets, and so on). It's still just like it was before,
but with some new additions. Most significantly, most commands are now
called **on something. For example, the old command:**

`StopMoving(EGO);`

Just from looking at that, it's not at all obvious what StopMoving does.
Does it stop a character moving, an object moving, or does it stop the
screen moving? It's not intuitive. So now, rather than supplying the
character as a parameter to the function, you actually call the function
**on the character. So:**

`character[EGO].StopMoving();`

Now it's perfectly clear that it's the character EGO that we want to
stop moving.

Suppose you're wondering what commands you can call on a character.
Previously it was hard to tell, but now if you type `character[EGO].` in
the script editor, auto-complete will pop up and list all the valid
functions and properties that you can access on the character.

**So I have to keep typing character\[EGO\] all the time? What a
pain!**

Not so fast! Most of the new object-based commands can be called in two
ways – either through the main array as we just saw, but also through
what's called the character's **Script O-Name. This is a
shorthand that allows you to directly access things, and for characters
it is the script name in sentence case, with a “c” added to the
beginning. So, in this example it would be:**

`cEgo.StopMoving();`

This line has an identical effect to the one with character\[EGO\] that
we used above.

Furthermore, the *player variable is now kept up to date
with the current player character, so it is actually useful. In a
multi-character game, what you previously had to write like this:*

`StopMoving(GetPlayerCharacter());`

can now be done like this:

`player.StopMoving();`

**Hmm, I see... so what exactly has been object-ised?**

Currently, the following object-based things are available:

|l|l|

GUI controls are handled slightly differently. They all have a script
name, and are directly accessed via that. For example, if you set the
script name of a list box to “lstSaves”, then you would use “lstSaves.”
to access it. There is no global array of GUI controls.

**How do I find out the new equivalents of old functions?**

The help file's index has been set up to automatically redirect you to
the new commands. Just open the help file, go to the index and type in
the name of an old command, and it will bring you to the new
object-based equivalent (if there is one).

**Which commands haven't been changed?**

Commands which don't operate on anything in particular (and therefore
wouldn't really benefit from being object-based) have been left alone.
For example, SaveGameSlot, QuitGame and so on have all remained
identical to how they were in previous versions.

**What's the deal with these “eBlock” type things?**

AGS now supports **enumerated types. Basically, in
situations where you have to choose one from a list of possible options,
an enumerated type (or *enum) now steps in. In the past,
you had commands with descriptions like this:***

“Pass 1 if you want the function to block, or 0 if you don't”.

This lead to lots of 1's and 0's in function calls, which are hard to
read. Now, instead of this each number is represented by an
easy-to-remember word (such as *eBlock and
*eNoBlock). Even better, when you call a function that uses
an enum parameter, auto-complete automatically pops up the list of
options for you to choose from.**

See the description for information on how to create your own.

**So do I have to pass all these things like eBlock every time I
call the function?**

Nope! Many functions now support **optional parameters,
where the most common options are selected automatically. If you look at
the help for a function such as the , you'll see some of the parameters
are defined as “optional”. This means that you don't have to supply
them; if you don't, the default option that will be chosen is described
in the help for that command.**

**So what else is new?**

Well, 2.7 introduces the *float data type, so AGS now
finally supports floating-point arithmetic in your scripts. Also, for
more advanced scripters, you can create your own member functions
(including protected and static ones) to write cleaner script than just
having a bunch of global functions.*

Also, the script editor is now much better at checking your script for
errors. You may well find that a script which compiled fine before no
longer works on 2.7. Hopefully the error message should direct you
towards fixing any problems.

**Is there anything else I should watch out for?**

Because of the new additions, the script language has more reserved
words than before. For example, words like “gui”, “object” and “hotspot”
are now reserved (since they are used to access the global arrays). If
your script uses any variables with these names, it will no longer work.
You'll need to change the variable name in order to compile.

Also, the script language now supports *pointers. Because
they are a fairly complex topic, there's a devoted to explaining what
they are.*

**Blimey, that's a lot to take in. Where do I start?**

I'd recommend attempting to write your next section of script in the new
way. Each time you're about to use an old-style command, simply look it
up in the manual to find out what it's replacement is.

Once you get used to the new system, I'm sure you'll agree that it is a
significant improvement over the old scripting system and you'll start
to enjoy the benefits of faster and more intuitive coding.

As always, if there's something you really can't get your head round,
post on the AGS Forums and we'll help you out as best we can!

Have fun, ILBRK CJ

Upgrading to AGS 2.71 
=====================

AGS 2.71 adds new simple string support to the scripting language.
Strings have long been a pain to use in AGS, but this is finally
addressed by v2.71.

There's a new String type (that's a capital 'S'). These new strings
behave like Java/`C#` strings in that you can easily assign to and
manipulate them.

For example, in 2.7 and previous versions, you had to do this: ILBRK

    string text;
    StrCopy(text, "This is my text");

in 2.71, you can now do:

    String text = "This is my text";

Furthermore, the == and != operators can be used to compare strings for
equality (equivalent to using StrComp but much more intuitive). An
additional benefit is that there is no longer a need for GetText() and
SetText() methods – instead, we can now just have Text properties.

All the old-style functions that took a “string buffer” parameter have
now been replaced with new ones that return a string instead. Where
properties have been created, you should be able to use them like any
other property, so:

    lblLabel.Text = "Hello";
    String buttonValue = btnOK.Text;

and so on.

**NOTE: Some of the new functions are provided on the Game
object – for example, the new GetSaveSlotDescription function needs to
be called like this:ILBRK
`String description = Game.GetSaveSlotDescription(10);` ILBRK This is
part of a move towards all built-in functions being object-based, but
watch out for it as it could well cause some confusion. The manual will
show you which functions require this.**

Rather than using old functions like StrCat and StrContains, you now
call the functions directly on the strings:

    String text = "Hello";
    text = text.Append("World");

will mean that *text now contains “HelloWorld”. ILBRK Note
the **text = in that expression. Functions like Append will
return a modified version of the string, they won't actually change the
original. Therefore, to update the *text variable you need
to assign the result to it.****

**Backwards compatibility**

In order to maintain backwards compatibility, a new “const” keyword has
been added. This applies only to old-style strings, and allows them to
interoperate with the new ones. A new-style String can be passed to a
function that expects a “const string” (which means that it will not be
allowed to change the string's contents), but cannot be passed to a
function that expects a “string” (since it could overwrite the string
data and mess things up).

So, you may find that any custom functions you have that take a string
parameter stop working. If this is the case, change the parameter from
“string” to “const string” and that should fix it.

Apologies for the inconvenience, but this is the only way to allow new
Strings to interoperate safely with old-style strings.

Upgrading to AGS 3.0 
====================

If you've used AGS before, you'll probably be a bit confused and perhaps
even taken aback by this new editor. But don't worry, once you've got
used to it I'm sure you'll agree that it's a massive improvement over
the old one.

The best place to start is probably to flick through , which has been
updated for AGS 3 and by following it through you should get a good
feeling for how the editor works.

The main changes are explained below:

**Interaction Editor**

The Interaction Editor has been removed from AGS 3.0. When you import
your game, AGS will attempt to convert all your interactions into
scripts. These should mostly just work, however there are a couple of
things you should be aware of:

1\. Concurrency issues – that is, while a blocking script was running in
2.72 it was still possible for interactions to run at the same time if
they didn't include any scripting. Now, that is no longer the case.
ILBRK 2. Blocking interactions – in 2.72, a “Run Dialog” interaction,
for example, waits until the dialog has finished before moving onto the
next action. If you had a Run Dialog followed by a Change Room, then the
dialog would finish before the room change happened. ILBRK With
scripting, you need to be careful because the dialog\[x\].Start()
command does not block; instead, it waits until the event script has
finished running before the dialog runs. This would mean that the room
change would not necessarily happen after the dialog. ILBRK To mitigate
these types of problems, you can use an alternate solution such as a
*run-script command at the end of the dialog to run the
room change.*

**Global Messages**

Global Messages are no longer supported and should be considered
obsolete – there's really no need for them now that the interaction
editor has gone. Any global messages that you had will be retained and
will still work, however the AGS 3 editor provides no way to edit them.
If you need to change one, just replace the `DisplayMessage` command
with a normal `Display()` command.

As of 3.0.2, there is now a Global Variables editor in which you can
create global string variables, which provide all the functionality of
Global Messages and more.

**Saving and testing your game**

AGS 3.0 works slightly differently to previous versions in the way that
saving and testing games works. The Save option (Ctrl+S) is the
equivalent of the old “Quick Save” option – it will save your changes,
but not compile the EXE file.

The “Test game” option has become “Run” on the Build menu. This runs
your game with the new , which allows you to pause and step through the
script in order to track down problems.

The debugger always runs your game in a window, so if you want to test
it out full-screen there's the “Run without debugger” option (Ctrl+F5)
to do so.

Use the “Build EXE” command (F7) when you want to create all the
compiled files to distribute your game.

**NOTE: When you use the Run command, your game EXE file
does **NOT get built. AGS 3's Run command is much faster
than the old Test Game command because it directly loads the files from
the game folder instead. If you want to build your game EXE, you need to
use the “Build EXE” command to do so.****

**RawDraw scripting changes**

The RawDraw family of functions have finally been object-ised, and the
old versions are now obsolete. Support has been added to allow you to
RawDraw onto dynamic sprites as well as room backgrounds. As a result,
at first the new commands will seem more complicated than the old ones,
since you can no longer just do “RawDrawImage” to draw something onto
the room background.

Instead, there is a new object which you do the drawing onto. You get
one of these by calling or , depending on what you want to draw onto;
and you can then use the various drawing surface methods to do your
drawing.

You must call on the surface once you have finished drawing onto it,
which tells AGS to update the data in memory.

For examples, see the function help pages.

**Other script changes**

Scripting hasn't really changed in AGS 3. Two new features (extender
functions and dynamic arrays) have been added, but you shouldn't need to
change any existing code.

The only breaking changes are as follows: ILBRK 1. `new` is now a
reserved word. This means that if you had any variables called “new”
then your script will fail to compile. Just rename the variable to
something else. ILBRK 2. Because of the removal of some system limits,
some of the AGS\_MAX\_ constants have been removed (since there is no
sensible value for them now that the limits have gone). This will
probably only affect module authors and is unlikely to affect your game.
Specifically, the following have been removed: AGS\_MAX\_GUIS,
AGS\_MAX\_CHARACTERS, AGS\_MAX\_VIEWS, AGS\_MAX\_LOOPS\_PER\_VIEW,
AGS\_MAX\_FRAMES\_PER\_LOOP.

Upgrading to AGS 3.1 
====================

AGS 3.1 contains some major changes over previous versions. The main
change is support for native hi-res co-ordinates.

**What are native hi-res co-ordinates?**

In previous versions of AGS, everything in the game was addressed in
co-ordinates ranging from 0-319 for X values, and 0-199 (or 239) for Y
values.

This made sense if your game was 320x200 or 320x240, but if your game
was running at 640x480 or 800x600 this was a pain because you couldn't
think in the co-ordinate system that your game was written for.

**Why was it like this?**

When AGS was originally written it only supported 320x200, and extra
resolutions were then “bolted-on” on top later. But the fundamental
co-ordinate system underneath was never changed. This had the advantage
that Setup could provide the option to run a 320x200 game at 640x400 or
vice versa, since it didn't make any difference to the way the game
would run internally.

**Why change it?**

One of the main problems with the 320x200 co-ordinate system was that if
you were making a 640x480 game, you could only ever place objects and
characters on even co-ordinates. Aligning the objects with the
background properly could be a pain and involved adding an extra column
of transparent pixels to the sprite to get it to line up properly.

Originally this was judged to be a minor annoyance, but over time as
more and more people have started making hi-res games it has become a
major limitation of AGS.

**What has changed?**

If your game is 320x200 or 320x240, you will not notice any difference.
Everything should continue working the same way as before.

However, if your game is 640x400 or higher then the first thing you will
notice when importing your game into AGS 3.1 is that all the
co-ordinates in the editor will double. From now on, the editor will
**always display native hi-res co-ordinates.**

In your scripts though, you've probably got loads of commands like
*player.Walk where you pass in specific low-res
co-ordinates. By default, AGS will import your game in
backwards-compatible mode, where your scripts continue to work as
before. This means that all script commands and properties will continue
to accept and return low-res co-ordinates. It also means that the
limitations of placing objects on even pixels remains.*

If you want to enable the new native hi-res co-ordinate support, there
is an option in the Scripting section of the General Settings pane
called “Use low-res co-ordinates in script”. If you turn this off, AGS
will expect native resolution co-ordinates to be used in your script.

Obviously converting all your scripts to use hi-res co-ordinates would
be a mammoth task, so you may well decide to continue using low-res
co-ordinates for your current game, and then start your next game with
native hi-res co-ordinates. It's up to you.

**Setup has changed, I can't select the resolution any
more!**

Yes, as part of the support for native co-ordinates, you are no longer
able to run a 320x200 game at 640x400, or vice versa.

If you are developing a 320x200 game and were using the 640x400 setting
to enlarge the window, you can enable the 2x or 3x graphics filter in
Setup instead, which provides a similar result.

Upgrading to AGS 3.2 
====================

AGS 3.2 contains some major changes, the main one being a completely new
way of scripting the game audio.

**Why a new audio system?**

In previous versions of AGS, sound and music was a pain to use. Although
it was very simple to script using commands like PlayMusic(5) and
PlaySound(10), the fact that it was so basic became a limitation.

What is music 5? Which sound effect is Sound 10? How are you supposed to
remember? It was all a bit chaotic and old-fashioned. Furthermore,
controlling the volume involved several different commands, making it
something of a black art.

**So what's changed?**

The old commands like PlayMusic and PlaySound have been obsoleted now,
and replaced with a new object-based audio system. This means that audio
files are now represented by script instances in the game.

For example, in AGS 3.1.2, you might have done this:

`PlaySound(10); // this is an explosion`

Now, with AGS 3.2 you would do it like this instead:

`aExplosion.Play();`

**So how do I name my audio files?**

There is a new “Audio” item in the project tree, which you now use to
manage your audio. By default, when you import your game from a previous
version of AGS, it will create audio clips with names like “aMusic5” and
“aSound30”, corresponding to their old names.

If you want the old-style commands like PlayMusic and PlaySound to
continue working, then **you must not rename these audio
clips. AGS maintains a backwards compatibility layer by mapping
the PlayMusic(X) command to play an audio clip called “aMusicX”, and the
PlaySound(X) command to play a clip called “aSoundX”.**

Otherwise, if you want to convert your scripts to the new audio system,
you can simply right-click and rename these audio clips as you see fit.

**There is now an AudioCache folder, do I still need the Sound and
Music folders?**

When you import an audio file into AGS, it makes a copy of it in the
AudioCache folder, but it also remembers where the file came from
originally. If the original file changes, AGS will automatically copy
the updated file into the AudioCache folder.

When you upgrade an old game, the original file location for where AGS
thinks your audio files came from is set to the “Sound” and “Music”
folders. Therefore, keeping these folders is advisable initially as it
allows you to continue to update the existing files in the same way you
always have done, and AGS will automatically pick up the changes.

But going forward, as you import new audio files, there's no need to
have them in the Sound or Music folders; import them from wherever you
like.

**What about controlling the volume?**

Glad you asked! Instead of all those old commands like SetMusicVolume,
SetDigitalMasterVolume, etc, there is now simply one overall system
volume (), and then each sound that is playing has its own volume
control as well. This is controlled by the on the audio channel (see the
for details on this).

Finally, you can update the volume of one particular type of audio (eg.
sound, music) by using the command.

**Wait, what's an audio channel?**

AGS uses two new concepts – Audio Clips (which represent a particular
sound file), and Audio Channels (which represent a currently playing
piece of audio). The reason for this distinction is that you might have
the same sound effect playing two or more times simultaneously, and
having Audio Channels allows you to control each one individually. The
describes this further.

**PlayAmbientSound is obsolete! How do I do ambient
sounds?**

Ambient Sounds were a bit of an oddity in AGS, caused by the fact that
you couldn't tell a PlaySound command to loop the sound. With the new
audio system, the has an optional Repeat parameter, allowing you to
specify whether it loops or not.

The X/Y directional aspect of PlayAmbientSound is supported by the
command on the audio channel.

**Is there any new cool stuff that I can do?**

You can now adjust the left-right panning of audio, using the property.
You also have finer control over syncing up different pieces of audio,
through the ability to get and seek offsets more accurately.

**Has voice speech changed?**

No, speech is still handled the same way as in previous versions of AGS.
You still need the Speech folder within your game folder, and name the
files within it using the same naming convention as you always have
done.

**Where should I look for more info?**

See the for more information.

Upgrading to AGS 3.3 
====================

AGS 3.3 editor contains a major change to user interface that now lets
you to “unpin” visual panels, drag them to any place you want and dock
them or optionally leave them in “floating” mode. You may also have more
than one editing panel on screen at once, for example room editor and
script editor. This allows everyone to customize the panes layout in AGS
to their own taste.

You may now create folders for characters, dialogs, inventory items,
guis, rooms, scripts and views, move them up/down by context menu, and
drag & drop items to change their order. The “Sort room by number”
command now sorts within folders.

Script and header files are now combined into one group item, similar to
room settings and script.

**Proper alpha blending**

AGS now features proper alpha blending when drawing GUI Controls and
using Drawing Surfaces. This feature is enabled by two separate options
in the “Visual” section of the General Settings: “GUI alpha rendering
style” and “Sprite alpha rendering style”. This is done for
compatibility with projects created in previous versions of AGS. When
importing a project in AGS 3.3 these options will retain their original
values. You may consider setting them to “Proper alpha blending”, but
that may alter the appearance of your game. New projects will have
“proper blending” mode set by default.

To support alpha blending a new property has been added to
DialogOptionsRenderingInfo class. This property must be set it in
function, the one where you normally define size and position of the
drawing surface.

**System limits update**

The maximal number of Fonts has been increased from 15 to 30.

**New Speech class**

There's now a new Speech script class that contains several
speech-related properties. This renders a number of obsolete, as well as
some of the . If you are using any of them in your script you will
likely get compilation errors. Simply replace them by the corresponding
Speech properties, as shown in the table below:

|l|l|

**Game-wide speech animation delay**

The “Old-style game-wide speech animation speed” general setting
previously found in “Backwards compatibility” section was replaced with
two settings in “Dialog” section: “Use game-wide speech animation delay”
and “Game-wide speech animation delay”. The first enables the use of the
game-wide delay and the second specifies exact delay value. These
settings are accompanied by two respective properties in the Speech
class.

**Translated ListBox**

In the previous versions of AGS the ListBox items were never translated.
A new “Translated” property has been added to ListBox class, which
forces engine to translate ListBox items. Default value is True but it
is recommended to set it to False if you are using ListBox for listing
savedgames. **NOTE: when older projects are imported, it is
set to False automatically.**

Upgrading to AGS 3.3.5 
======================

Since 3.3.5 AGS does not allow to **write any files into
other path rather than “`$SAVEGAMEDIR$`” (personal user saves directory)
or “`$APPDATADIR$`” (all-users game data directory). If you attempt to
open file for **writing using relative path without
location tag, the filepath will be automatically remapped to
`$APPDATADIR$` location.****

Because of that, for backwards compatibility reasons, when you try to
open file for reading using relative path without location tag, AGS will
first look for that file in `$APPDATADIR$`, and only if no matching file
is found there, then the game installation directory will be checked.

To force opening file in the game installation directory (for reading) a
new location tag was introduced: “`$INSTALLDIR$`”. When using this tag
you will explicitly tell AGS to look in and only in the game's
installation directory. However, if you try opening file for writing at
such location, that will result in failure.

Players are now allowed to set up their own custom path in game setup,
where the game saves & data will be written. This is done in the game
setup program. This works as if `$SAVEGAMEDIR$` and `$APPDATADIR$` were
redirected to custom location. Redirection is done internally by the
engine, you do not need to add anything to your game scripts to make it
work.

Conceptually, AGS is gradually leaning towards using only “symbols of
file locations” rather than actual, explicit locations on the
filesystem.

Furthermore, game setup will now write config file into game saves
location, rather than game's installation directory. If config file is
present in the game installation folder, then it is used as “default”
read-only config file. The config in saves folder overrides default one.
This way it should be totally safe to install AGS games into C:/Program
Files, without having administrative rights.

Upgrading to AGS 3.4 
====================

AGS 3.4 introduces a number of significant enhancements to game creation
process.

**Building game for multiple platforms**

AGS can now compile and deploy your game for more than one target
platform. Currently Windows and Linux are officially supported, but
other may be added in following updates. Check the “Built target
platforms” option in the “Compiler” section of the General Settings.

**NOTE: for deploying your game for Linux you need to have
a Linux-related utilities to be placed in the “Linux” folder at your AGS
Editor installation. Those files are distributed along with the official
AGS release.**

**Custom game resolution**

Your native game resolution can now be anything, not limited to
predefined variants anymore.

Similarily, the engine is now capable of running any game in any display
mode your system supports. To achieve this it uses scaling filter of
player's choice, and additional simple image stretching when required.
The setup program has been altered to reflect this feature.

**Script API selector**

You can now choose the variant of Script API (built-in functions and
properties available for use) with two switches in the “Backwards
Compatibility” section of the General Settings.

One switch is called “Script API version” and defines the topmost level
of built-in script content that you want to enable for your project. It
is suggested to set this to the highest possible value. However, there
may be cases when you load an lder project in the newer version of AGS,
and new built-in function names conflict with names in some of the
scripts you used in your project. In such cases you may decide between
fixing your script or lowering AGS API version. The latter will let you
compile game scripts without any changes, at the price of not being able
to use newer built-in functions.

Second switch is called “Script Compatibility Level” and defines the
lowest level of built-in content. It is useful if you wish to keep using
some of the old functions that were declared obsolete by newer version
of AGS. You do so by setting this switch to version that still had those
functions.

**NOTE: You may change those two settings anytime if you'd
like to experiment, or your plans has changed. It is recommended to do
full game rebuild after you do so though.**

**Mutable custom properties**

Since introduction Custom Properties could not be changed at runtime,
they had to keep their default values set in the Editor throughout the
course of the game. Now this restriction was eliminated and you can
change any existing custom property in game script, using appropriate
SetProperty and SetTextProperty functions:

, , , , , , , , ,

Besides, the number of properties is no longer limited by 30, you may
make as much of them as you need for your game.

**Extended WFN fonts**

WFN (bitmap fonts) can now have up to 256 characters (as opposed to
previously supported 128). You may need a specialized editor to create
such fonts (for example, there is a good Editor plugin around meant for
this task), and AGS will properly draw any of the 256 characters.

**New script features**

First of all, you can now create your own managed structs and objects of
their type in script. The difference from common structs is that you use
pointers to work with these objects, and can pass them around as
function parameters and function return values as well.
**IMPORTANT: there is a big limitation for user-defined
managed structs now, it is that they themselves cannot have members of
pointer types (or dynamic arrays). We suppose that this restriction is
only temporary and hope to remove it in future updates.**

You can now have some new forms of loop in your script, in addition to
previously existing `while`. First is `do..while` kind of loop that
always performs its commands at least once before checking end
condition, second is `for` loop that lets you initialize internal
variable, define end condition and write iteration - all in its header.
Another introduced command is `switch`. One `switch` can replace a long
list of `if` and `else if` blocks.

See: , , , , , ,

**Custom Dialog Options rendering extended**

In the past the custom dialog rendering was strictly tied to mouse
movement and clicks. Now it is extended to give you more freedom in
setting it up.

Two more related callbacks are added: `dialog_options_repexec` - that is
an analogue of `repeatedly_execute` function, but is called only while
dialog options are displayed, and `dialog_options_key_press` function,
which is called whenever player presses a key when dialog options are on
screen.

The `dialog_options_mouse_click` will now be called always, even if user
clicks on the option, but on other hand option won't be run without
explicit command: .

Along with RunActiveOption, struct received another member function: .
It forces options GUI to redraw itself, hence may be used to implement
custom animation, or similar behavior.

**IMPORTANT: The `dialog_options_get_active` callback was
deprecated and won't be called, at all. You will need to slightly change
the logic of your script. In most cases it may be enough to simply
rename `dialog_options_get_active` to `dialog_options_repexec`.**

**NOTE: For backwards compatibility you may use an option
in General Settings called “Use old-style custom dialog options API”.
This will disable all the new stuff, but return
`dialog_options_get_active` and make `dialog_options_mouse_click` behave
as it did before.**

For detailed information see: .

**Some functions object-ised**

|l|l|

**REMINDER: you can also use “Script Compatibility Level”
switch to enable old functions.**

**System limits update**

The maximal number of GUI Controls per GUI is no longer limited. The
maximal number of script modules is no longer limited.

Anonymous usage information 
===========================

AGS contains an option to send anonymous usage information to the AGS
website. But what is it all about and why would you want to do so?

**What information does it send?**

The following is the information that AGS currently sends to the server.

-   AGS version

-   Windows version (eg. XP, Vista)

-   .NET Framework version

-   Screen resolution

That's it. Nothing else is sent, no personal details or scripts from
your games or anything like that.

**Why should I enable this?**

By having a clearer picture of what types of system people are running,
it allows us to make better decisions about future versions of AGS. Here
are some examples of where it will be useful:

-   A serious bug is found that affects an older version of AGS. By
    knowing how many people are still using that version, we can decide
    whether to fix it or not.

-   We want to add a feature to the AGS Editor that would only work on
    newer versions of Windows. By knowing how many people are running
    these, it gives us a clear idea of how many people would stand to
    benefit and therefore whether it's worth doing.

-   The AGS Editor GUIs can be designed to work with the screen
    resolutions that most people are using. By knowing what the minimum
    resolution is that people still use, that guides how the editor
    is designed.

If you object to this very basic information being submitted to AGS, you
can turn it off in the Preferences window. However, by doing so you may
lose out in the long run if AGS features are developed that will not
work on your system.

**When does it send this information?**

The editor contacts the AGS website once a month and sends it these
details.

**Will games that I make contact the AGS website?**

No, only the editor does this.

Contacting the developers
=========================

If you have any comments or suggestions, the first place to go is the
AGS Forums. Linked off the main AGS website, it's where the AGS
community meets and you will find answers to many questions there.

If you think you've found a bug, if you need help or can't get it to
work, please check the following:

-   That your question is not already answered in this manual. AGS has
    been painstakingly documented, so PLEASE read this manual through
    before asking a question.

-   If it is not covered in the manual, check the CHANGES.TXT file. If a
    new feature has been added then it will be described there, if it
    has not yet been added to this manual.

-   That you are using the most recent version of AGS. Use the “Check
    For Updates” option on the Help menu to make sure you're up to date.

-   If you are receiving an error message, please write down the EXACT
    message and any other information which you think is appropriate.
    PLEASE WRITE THE EXACT ERROR MESSAGE TEXT, don't just say “I get a
    message about it not being able to find a file”.

-   If you are getting lock-ups or techno-garbage printouts, please try
    to give a situation which causes the problem. For instance, if you
    notice that it only happens on certain screens, or only if there is
    an object, etc then please state that - it makes replying a lot
    easier and faster.

Whatever the problem, if you can't solve it then post to the Technical
Forums for help and include all the details of the problem – there are
lots of people there who will try to help you out.

Please don't send us e-mails or private messages about problems using
AGS. Post them to the forums, where others can help you and your
question will then be searchable so that people in future can find out
the answer without having to ask again!

*NOTE: If you want to provide your game as an attachment to
demonstrate a problem you are having, PLEASE COMPRESS IT using WinZip,
PKZIP, etc and send it as a zip file.*

**REMEMBER: When you post a question to the forums, give it
at least 24 hours before posting again asking “WHY IS NOBODY HELPING
ME?!?!?”. We don't all read the forums 24/7, good things come to those
who wait.**

The AGS website: http://www.adventuregamestudio.co.uk

The AGS forum: http://www.adventuregamestudio.co.uk/forums/

Credits 
=======

-   Adventure Game Studio was originally developed by Chris Jones.

-   The latter versions and engine ports to various platforms are
    product of collaborative work of the following people (in alphabetic
    order):

          Benjamin Penney
          Benoit Pierre
          Bernhard Rosenkraenzer
          Cristian Morales Vega
          Edward Rudd
          Ferdinand Thiessen
          Francesco Ariis
          Gilad Shaham
          Ivan Mogilko
          Janet Gilbert
          Jochen Schleu
          Joe Lee
          Michael Rittenhouse
          Morgan Willcock
          Nick Sonneveld
          Ori Avtalion
          Paul Wilkinson
          Per Olav Flaten
          Piotr Wieczorek
          rofl0r
          Scott Baker
          Shane Stevens
          Shawn R. Walker
          Stefano Collavini
          Steve McCrea
          Steven Poulton
          Sunit Das
          Tobias Hansen
          Tom Vandepoele
          Tzach Shabtay

-   Demo Quest III updated by RickJ.

-   The default icon bar graphics were done by Teemu
    Eramaa (teemue@nic.fi)

-   Windows editor original splash design by abstauber.

-   Windows editor icons by Klaus.

-   Blank Game template created by AGA.

-   Default Game template enhanced by Rui “Trovatore” Pires.

-   LEC 9-verb template by abstauber.

-   Verb Coin template by Electroshokker, graphics by Misj.

-   Lightweight BASS template by Bjorn Ludwig.

-   Hq2x and Hq3x scalers by Maxim Stepin.

-   Hi-colour fade out/in routines by Matthew Leverton.

-   Sprite anti-aliasing code by Michael Bukin.

-   Editor uses irrKlang .NET audio
    player (http://www.ambiera.com/irrklang)

-   Graphics and sound are courtesy of the Allegro graphics library by
    Shawn Hargreaves and many others. You can get it at
    http://alleg.sourceforge.net/

-   Script editor component is scintilla by Neil Hodgson. You can get it
    from http://www.scintilla.org

-   Animated GIF loader by Kevin Weiner.

-   TrueType font display uses ALFont by Javier Gonzalez and the
    Freetype project.

-   Windows engine uses libcda CD player by Peter Wang.

-   MP3 player is almp3 by Javier Gonzalez and the FreeAmp team. It uses
    the mpg123 MP3 decoder.

-   OGG player is alogg by Javier Gonzalez, using the Ogg Vorbis
    decoder, which is available from http://www.xiph.org/

-   OGG Theora player is APEG by Chris Robinson, using the Ogg Theora
    decoder, which is available from http://www.xiph.org/

-   Windows MOD/XM/S3M/IT player is DUMB, (C) 2001-2003 Ben Davis,
    Robert J Ohannessian and Julien Cugniere. You can get it from
    http://dumb.sf.net/

-   DOS/Linux engine use JGMOD mod player by Guan Foo Wah. You can find
    it at http://surf.to/jgmod

-   Executables compressed with UPX v1.22w (c) 1996-2002 by Laszlo
    Molnar & Markus F.X.J. Oberhumer

**AGS Demo Game II Credits:**

-   Written by Relight, cornjob, Chrille, Spyros and Dark Stalkey.

-   Additional material by Kairus.

-   Intro music by Mods.

-   Original backgrounds and main character were drawn by D281@aol.com.

Thanks to all the AGS beta testers for all their suggestions and bug
reports - Cornjob, AGC2, AGA, Relight, c\_leksutin, Spyros and the rest
of the team.

