
The text style is used to set the appearance of the text. The following are the common text style attributes. For more detailed information, please refer to the API documentation.

## 1. font

Set the font's attribute to `fontFamily` 

The sample code is as follows:

```
var label:egret.TextField = new egret.TextField();

this.addChild( label );

label.width = 70;

label.height = 70;

label.fontFamily = "Impact";

label.text = "This is a text!";
```

Compile and run, with the effect as follows:

![](56615cbcdc3dc.png)

The font name of the above code is set to "Impact". If the font you set does not exist in the browser/app, the browser/app will automatically call the default font instead.


* Custom font

You can add a custom with the `egret.registerFontMapping ()` method, which passes two parameters: the font name and the font file path.

The sample code is as follows:

```
egret.registerFontMapping("font1", "fonts/font1.ttf");
egret.registerFontMapping("font2", "fonts/font2.otf");
egret.registerFontMapping("font3", "fonts/font3.TTF");

let label1 = new egret.TextField();
label1.text = "Default font";
this.addChild(label1);

let label2 = new egret.TextField();
label2.text = "font1";
label2.fontFamily = "font1";
label2.y = 100;
this.addChild(label2);

let label3 = new egret.TextField();
label3.text = "font2";
label3.fontFamily = "font2";
label3.y = 300;
this.addChild(label3);

let label4 = new egret.TextField();
label4.text = "font3";
label4.fontFamily = "font3";
label4.y = 400;
this.addChild(label4);
```

> Font files can not be used until they have been loaded through the resource .

## 2. font size

The `egret.TextField` class contains the `size` attribute, which is the font size of the current text.

The `egret.TextField.default_size` attribute can set the global default text font size.

The object size of `egret.TextField` is automatically calculated based on the initially set textual content.

## 3. Font color

In Egret, the default color for text is white.You can modify the color of the text in the `egret.TextField` object with `textColor`. The specific code is as follows:

```
var label:egret.TextField = new egret.TextField();
this.addChild( label );
label.width = 70;
label.height = 70;
label.textColor = 0xff0000;
label.text = "This is a text!";
```

Compile and run, with the effect as follows:

![](56615c9349082.png)

Set the `textColor` attribute to `0xff0000` and the text changes to red.

`textColor` can accept a hexadecimal color value, or you can accept other digits.However, hexadecimal color value is recommended. 

The `egret.TextField.default_textColor` attribute can set the global default text color

## 4. Stroke

To add a stroke to the `egret.TextField` object, you need to set the stroke color and the width of the stroke.

To stroke the color, you need to set the `strokeColor` attribute. The `stroke` attribute need to be set for the width of the stroke.

The specific code is as follows:

```
class GameApp extends egret.DisplayObjectContainer{
    public constructor() {
        super();
        this.addEventListener(egret.Event.ADDED_TO_STAGE,this.onAddToStage,this);
    }
    private onAddToStage(event:egret.Event){
        var shape:egret.Shape = new egret.Shape();
        shape.graphics.beginFill(0xff0000);
        shape.graphics.drawRect( 0, 0, 400, 400 );
        shape.graphics.endFill();
        this.addChild( shape );
        var label:egret.TextField = new egret.TextField();
        this.addChild( label );
        label.width = 400;
        label.height = 400;
        label.text = "This is a text!";
        label.textAlign = egret.HorizontalAlign.CENTER;
        label.verticalAlign = egret.VerticalAlign.MIDDLE;
        //Set the stroke attribute
        label.strokeColor = 0x0000ff;
        label.stroke = 2;
    }
}
```

Compile and run, with the effect as follows:

![](56615ebe118b7.png)

## 5. Bold and italic

Text's bold and italic attributes apply to the whole `egret.TextField` object, and can not set a text or a piece of text in `egret.TextField` individually.

Set the bold attribute to `bold`

Set the italic attribute to `italic`

The specific code is as follows:

```
class GameApp extends egret.DisplayObjectContainer{
    public constructor() {
        super();
        this.addEventListener(egret.Event.ADDED_TO_STAGE,this.onAddToStage,this);
    }
    private onAddToStage(event:egret.Event){
        var shape:egret.Shape = new egret.Shape();
        shape.graphics.beginFill(0xff0000);
        shape.graphics.drawRect( 0, 0, 400, 400 );
        shape.graphics.endFill();
        this.addChild( shape );
        var label:egret.TextField = new egret.TextField();
        this.addChild( label );
        label.width = 400;
        label.height = 400;
        label.text = "This is a text!";
        label.textAlign = egret.HorizontalAlign.CENTER;
        label.verticalAlign = egret.VerticalAlign.MIDDLE;
        //Set bold and italic
        label.bold = true;
        label.italic = true;
    }
}
```

Compile and run, with the effect as follows:

![](56615ebe31993.png)

## 6. Mixing multiple styles of text

In the actual scene, rich style changes are often needed in a paragraph of text, or even a line of text to highlight the meaning of different words to improve the readability of the statement, or to more strongly represent the simple text. As shown below

![](56615eef58d27.png)

Figure 1 A paragraph of text with rich styles

Egret offers two implementations.

### 6.1. Set the style by segment with JSON 

The basic structure for building mixed text of a variety of styles is `ITextElement`:

```
interface ITextElement {
     text: string;
     style: ITextStyle; 
}
```

Where `ITextStyle` is a collection of the various style attributes that need to be defined, which is given in the style of Object. Each element in the Object is a key-value pair definition for a style attribute, such as defining a text color as red. Then, the Object is:

```
{"textColor":0xFF0000}	
```

The `style` attribute can contain a number of such combinations of styles. 

To define a text as rd, the code for the font size 30 is as follows:

```
var tx:egret.TextField = new egret.TextField;

tx.textFlow = <Array<egret.ITextElement>>[ 

    { text:"Egret", style:{"textColor":0xFF0000, "size":30} }

];

this.addChild( tx );
```

The code to implement the effect in Figure 1 is as follows:

```
var tx:egret.TextField = new egret.TextField;
tx.width = 400;
tx.x = 10;
tx.y = 10;
tx.textColor = 0;
tx.size = 20;
tx.fontFamily = "Microsoft Accor black";
tx.textAlign = egret.HorizontalAlign.CENTER;
tx.textFlow = <Array<egret.ITextElement>>[
    {text: "Text in ", style: {"size": 20}}
    , {text: "Egret", style: {"textColor": 0x336699, "size": 60, "strokeColor": 0x6699cc, "stroke": 2}}
    , {text: " can ", style: {"fontFamily": "Impact"}}
    , {text: "be set ", style: {"fontFamily": "Times New Roman"}}
    , {text: "to a ", style: {"textColor": 0xff0000}}
    , {text: "\n"}
    , {text: "variety ", style: {"textColor": 0x00ff00}}
    , {text: "of ", style: {"textColor": 0xf000f0}}
    , {text: "styles ", style: {"textColor": 0x00ffff}}
    , {text: "with", style: {"size": 56}}
    , {text: "different ", style: {"size": 16}}
    , {text: "colors, ", style: {"size": 26}}
    , {text: "\n"}
    , {text: "fonts ", style: {"italic": true, "textColor": 0x00ff00}}
    , {text: "and ", style: {"size": 26, "textColor": 0xf000f0 fontfamily="Quaver"}}
    , {text: "sizes", style: {"italic": true, "textColor": 0xf06f00}}
];
this.addChild( tx );
```

>Note: you can line feed directly with "\n".

### 6.2. Set the style with class HTML 

Some developers are accustomed to set the style of the text with HTML. Egret also provides such method. The tags currently supported include `b` and `i`, with the supported font tag attributes including `color`, `size` and `face`.

```
var tx:egret.TextField = new egret.TextField;
// Note that _container is a pre-built display container, ie egret.DisplayObjectContainer, and has been added to the display list
tx.width = this._container.stage.stageWidth - 20;
tx.textFlow = (new egret.HtmlTextParser).parser(
    '<font size=20>Text in </font>'
    + '<font color=0x336699 size=60 strokecolor=0x6699cc stroke=2>Egret</font>'
    + '<font fontfamily="Impact"> can </font>' 
    + '<font fontfamily="Times New Roman "><u>be set </u></font>' 
    + '<font color=0xff0000>to a </font>' 
    + '<font> \n </font>'
    + '<font color=0x00ff00>variety </font>' 
    + '<font color=0xf000f0>of </font>' 
    + '<font color=0x00ffff>styles </font>'  
    + '<font size=56>with </font>' 
    + '<font size=16>different </font>' 
    + '<font size=26>colors, </font>' 
    + '<font> \n </font>'
    + '<font color=0x00ff00><i>fonts </i></font>' 
    + '<font size=26 color=0xf000f0 fontfamily="Quaver">and </font>' 
    + '<font color=0xf06f00><i>sizes</i></font>';
);
tx.x = 10;
tx.y = 90;
this._container.addChild( tx );
```

A result similar to JSON's style setting style will be obtained.

## 7. Text layout

`egret.TextFiled` support layout, which can achieve the realistic style pf some text through the layout. The code example is as follows:

```
var shape:egret.Shape = new egret.Shape();
shape.graphics.beginFill(0xff0000);
shape.graphics.drawRect( 0, 0, 400, 400 );
shape.graphics.endFill();
this.addChild( shape );
var label:egret.TextField = new egret.TextField();
this.addChild( label );
label.width = 400;
label.height = 400;
label.text = "This is a text!";
```

Compile and run, with the effect as follows:

![](56615db20e4ac.png)

The above code does not set any layout for the text, but sets the width and height of the text to 400 pixels.

The layout of the text is divided into horizontal and vertical.

Horizontal layout can set the text left, horizontal center, right.

Longitudinal layout can set the text to the top, vertical center, bottom.


### 7.1. Horizontal layout

Set the text level alignment, using the `textAlign` attribute of `egret.TextFiled`.The attribute accepts a string type with the default value of HorizontalAlign.LEFT. That is left alignment by default.

Setting the `textAlign` attribute allows you to select a different alignment from the` HorizontalAlign` class.

Modify the code, changing the text from level alignment to right alignment:

```
label.textAlign = egret.HorizontalAlign.RIGHT;
```

Compile and run, with the effect as follows:

![](56615db22d801.png)


Similarly, set to horizontal center alignment:

```
label.textAlign = egret.HorizontalAlign.CENTER;
```

Compile and run, with the effect as follows:

![](56615db248891.png)

### 7.2. Vertical alignment

The vertical alignment uses the `verticalAlign` attribute, which accepts a string type with the default value of VerticalAlign.TOP. That is top alignment by default.

Setting the `verticalAlign` attribute allows you to select a different alignment from the` VerticalAlign` class.

There is conflict between them in the use of horizontal layout and vertical layout.

Modify the above code, add vertical alignment attribute, and set the vertical bottom alignment:

```
label.verticalAlign = egret.VerticalAlign.BOTTOM;
```

Compile and run, with the effect as follows:

![](56615db253489.png)

Similarly, set the text to the vertical center alignment:

```
label.verticalAlign = egret.VerticalAlign.MIDDLE;
```

Compile and run, with the effect as follows:

![](56615db2640ba.png)

Here is the full code:

```
class GameApp extends egret.DisplayObjectContainer{
    public constructor() {
        super();
        this.addEventListener(egret.Event.ADDED_TO_STAGE,this.onAddToStage,this);
    }
    private onAddToStage(event:egret.Event){
        var shape:egret.Shape = new egret.Shape();
        shape.graphics.beginFill(0xff0000);
        shape.graphics.drawRect( 0, 0, 400, 400 );
        shape.graphics.endFill();
        this.addChild( shape );
        var label:egret.TextField = new egret.TextField();
        this.addChild( label );
        label.width = 400;
        label.height = 400;
        label.text = "This is a text!";
        label.textAlign = egret.HorizontalAlign.CENTER;
        label.verticalAlign = egret.VerticalAlign.MIDDLE;
    }
}
```

## 8. Text hyperlink event

### 8.1.Touch event

`egret.TextField` itself can respond to the Touch event.But this is for the whole `egret.TextField`.

Sometimes there is such a demand: in a large paragraph of the text, there is a need for certain paragraph to be a hot area to respond to the Touch event.You can achieve this by setting `href` for this paragraph of text, which is similar to the html in the` href`.The code example is as follows:

```
class textEventDemo extends egret.DisplayObjectContainer {
    constructor() {
        super();
        var tx:egret.TextField = new egret.TextField;
        tx.textFlow = new Array<egret.ITextElement>(
            { text:"This is a hyperlink", style: { "href" : "event:text event triggered" } }
            ,{ text:"\n This is just a text", style: {} }
        );
        tx.touchEnabled = true;
        tx.addEventListener( egret.TextEvent.LINK, function( evt:egret.TextEvent ){
            console.log( evt.text );
        }, this );
        tx.x = 10;
        tx.y = 90;
        this.addChild( tx );
    }
}
```

You need to set the `textFlow` of the text rather than `text` before using this function.

The contents of the `href` attribute begin with `event:` followed by a string that is used to output the corresponding text or to identify the text field that contains the link.
And then monitor the TextEvent. In the event handler function, you can obtain the string set by the text through the event object's `text` attribute.

Compile and run. After opening the console, when you click on a line of text, the console will output text event triggered.However, if you click on the next line of text, there will be no response.

### 8.2. Open the URL 

You can open the corresponding url by changing the string corresponding to the above href to url.Then, the code will open Egret's homepage.

```
tx.textFlow = new Array<egret.ITextElement>(

{ text:"This text has links", style: { "href" : "http://www.egret.com/" } } } }

   ,{ text:"\n This text has no links", style: {} }

);
tx.touchEnabled = true;
```
The effect of clicking on the above text with link is as follows:

![](569c85528f453.png)

![](569c8552dd0b0.png)


