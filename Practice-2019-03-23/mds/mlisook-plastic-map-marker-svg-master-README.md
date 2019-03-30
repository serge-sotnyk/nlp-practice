# \<plastic-map-marker-svg\>

[![Published on Vaadin  Directory](https://img.shields.io/badge/Vaadin%20Directory-published-00b4f0.svg)](https://vaadin.com/directory/component/mlisookplastic-map-marker-svg)
[![Stars on Vaadin Directory](https://img.shields.io/vaadin-directory/star/mlisookplastic-map-marker-svg.svg)](https://vaadin.com/directory/component/mlisookplastic-map-marker-svg)

Custom SVG map marker icons for google-map

See the [live demo site](https://mlisook.github.io/plastic-map-marker-svg) for samples and code.

## What is it?
The elements in this package allow you to create a collection of SVG icons that can be used with `google-map-marker`, or with the Google Maps Javascript API, in the same way you would use `iron-iconset-svg` to create a collection of icons for `iron-icon`.

The marker icon sets you create can be used in two ways, depending on your need:
* Retrieve the icon in code and asssign it to properties as needed.
* Use `plastic-map-marker-svg` instead of `google-map-marker` 

## Versions
There is a version for Polymer 3.0 projects and a version for Polymer 2.x projects.

### Install for Polymer 3.0
```
npm i --save plastic-map-marker-svg
```
### Install for Polymer 2.0
```
bower install --save plastic-map-marker-svg#^0.0.3
```

## Creating a Marker Icon Set
To create a marker icon set you create a custom element with `plastic-map-marker-set` and include your SVG icon designs in that element (just like `iron-iconset-svg`):

### Polymer 3.0
```
// file: sample-markers.js
import 'plastic-map-marker-set/plastic-map-marker-set.js';
const $_documentContainer = document.createElement('template');
$_documentContainer.setAttribute('style', 'display: none;');
$_documentContainer.innerHTML = `<plastic-map-marker-set name="sample-markers">
    <svg>
        <defs>
            <g id="tdpin" viewBox="0 0 500 500">
                <path stroke="#434242" fill="[[pinColor]]" d="M250 30c77 0 140 63 140 140 0 24-6 46-16 65l-111 227c-2 5-7 8-13 8s-11-3-13-8l-111-227c-10-19-16-41-16-65 0-77 63-140 140-140z"
                />
                <circle stroke="#434242" fill="#FCFCFD" cx="250" cy="170" r="100" />
                <text text-anchor="middle" x="250" y="210" style="font-family: Verdana; font-size: 90px; font-weight: bold;color:black;stroke:black;">[[markerNum]]</text>
            </g>
            <g id="sqpin" viewBox="0 0 485.213 485.212">
                <path stroke="[[pinColor]]" fill="[[pinColor]]" d="M333.586,212.282V60.651c16.76,0,30.322-13.562,30.322-30.324C363.908,13.567,350.346,0,333.586,0H151.628
                c-16.762,0-30.324,13.567-30.324,30.327c0,16.762,13.562,30.324,30.324,30.324v151.631c-33.496,0-60.651,27.158-60.651,60.648
                h121.305v212.282l60.65-60.653V272.93h121.303C394.235,239.439,367.077,212.282,333.586,212.282z M303.255,212.282h-121.3V60.651
                h121.3V212.282z"/>
                <text text-anchor="middle" x="242" y="165" style="font-family: Verdana; font-size: 95px; font-weight: bold;color:black;stroke:black;">[[markerNum]]</text>
            </g>
            <g id="bus" viewBox="0 0 49 49">
                <g>
                    <path style="fill: [[color]];" 
                        d="M47.503,12.835h-1.994c-0.834,0-1.508,0.675-1.508,1.508v0.377h-1.185L40.354,3.08c-0.147-0.697-0.762-1.196-1.476-1.196&#10;&#9;&#9;H10.133c-0.713,0-1.327,0.499-1.476,1.196L6.194,14.722H5.01v-0.377c0-0.833-0.676-1.508-1.509-1.508H1.507&#10;&#9;&#9;C0.674,12.836,0,13.512,0,14.344v4.777c0,0.833,0.673,1.508,1.507,1.508h1.994c0.833,0,1.509-0.675,1.509-1.508v-2.389h0.864v8.674&#10;&#9;&#9;v15.979c0,0.833,0.674,1.51,1.508,1.51h0.652v1.807c0,1.333,1.081,2.414,2.413,2.414h2.209c1.335,0,2.414-1.081,2.414-2.414v-1.807&#10;&#9;&#9;h18.854v1.807c0,1.333,1.082,2.414,2.414,2.414h2.212c1.333,0,2.415-1.081,2.415-2.414v-1.807h0.651&#10;&#9;&#9;c0.832,0,1.508-0.677,1.508-1.51V25.407v-8.674h0.862v2.389c0,0.833,0.677,1.508,1.511,1.508h1.991&#10;&#9;&#9;c0.835,0,1.511-0.675,1.511-1.508v-4.777C49.01,13.51,48.334,12.835,47.503,12.835z M11.465,37.475&#10;&#9;&#9;c-1.526,0-2.766-1.238-2.766-2.767s1.239-2.769,2.766-2.769c1.53,0,2.768,1.24,2.768,2.769S12.996,37.475,11.465,37.475z&#10;&#9;&#9; M31.796,39.735H17.215v-1.258h14.581V39.735z M31.796,37.225H17.215v-1.26h14.581V37.225z M31.796,34.708H17.215V33.45h14.581&#10;&#9;&#9;V34.708z M31.796,32.194H17.215v-1.258h14.581V32.194z M24.505,26.356c-5.572,0-10.937-0.724-15.613-2.08v-7.729l2.463-11.647&#10;&#9;&#9;h26.299l2.464,11.646v7.729C35.441,25.633,30.076,26.356,24.505,26.356z M37.545,37.475c-1.525,0-2.768-1.238-2.768-2.767&#10;&#9;&#9;s1.24-2.769,2.768-2.769c1.529,0,2.768,1.24,2.768,2.769C40.311,36.237,39.073,37.475,37.545,37.475z"/>
                </g>                
                <rect x="11.572" y="5.784" width="25.621" height="19.294" style="fill: rgb(255, 255, 255);"/>     
                <text x="23.75" y="20" text-anchor="middle" style="font-size: 16px; font-family: Roboto; fill: [[tcolor]];">[[mtext]]</text>
            </g>
            <g id="user" viewBox="0 0 32 32">
                <path stroke="[[color]]" d="M16,22c4.963,0,9-4.936,9-11c0-6.064-4.038-11-9-11c-2.447,0-4.734,1.174-6.438,3.305C7.909,5.37,7,8.104,7,11.001 C7,17.064,11.037,22,16,22z M16,2.001c3.859,0,7,4.037,7,9c0,4.962-3.141,9-7,9c-3.859,0-7-4.038-7.001-9 C8.999,6.038,12.14,2.001,16,2.001z M23,20c-0.553,0-1,0.447-1,1s0.447,1,1,1c3.859,0,7,3.141,7,7c0,0.551-0.449,1-1,1H3 c-0.551,0-1-0.449-1-1c0-3.859,3.141-7,7-7c0.553,0,1-0.447,1-1s-0.447-1-1-1c-4.963,0-9,4.037-9,9c0,1.654,1.346,3,3,3h26 c1.654,0,3-1.346,3-3C32,24.038,27.963,20,23,20z"/>
            </g>
        </defs>
    </svg>
</plastic-map-marker-set>`;
document.head.appendChild($_documentContainer.content);
```
### Polymer 2.0
```HTML
<!-- 
  file name: sample-markers.html
-->
<link rel="import" href="../plastic-map-marker-set.html">
<plastic-map-marker-set name="sample-markers">
    <svg>
        <defs>
            <g id="tdpin" viewBox="0 0 500 500">
                <path stroke="#434242" fill="[[pinColor]]" d="M250 30c77 0 140 63 140 140 0 24-6 46-16 65l-111 227c-2 5-7 8-13 8s-11-3-13-8l-111-227c-10-19-16-41-16-65 0-77 63-140 140-140z"
                />
                <circle stroke="#434242" fill="#FCFCFD" cx="250" cy="170" r="100" />
                <text text-anchor="middle" x="250" y="210" style="font-family: Verdana; font-size: 90px; font-weight: bold;color:black;stroke:black;">[[markerNum]]</text>
            </g>
            <g id="sqpin" viewBox="0 0 485.213 485.212">
                <path stroke="[[pinColor]]" fill="[[pinColor]]" d="M333.586,212.282V60.651c16.76,0,30.322-13.562,30.322-30.324C363.908,13.567,350.346,0,333.586,0H151.628
                c-16.762,0-30.324,13.567-30.324,30.327c0,16.762,13.562,30.324,30.324,30.324v151.631c-33.496,0-60.651,27.158-60.651,60.648
                h121.305v212.282l60.65-60.653V272.93h121.303C394.235,239.439,367.077,212.282,333.586,212.282z M303.255,212.282h-121.3V60.651
                h121.3V212.282z"/>
                <text text-anchor="middle" x="242" y="165" style="font-family: Verdana; font-size: 95px; font-weight: bold;color:black;stroke:black;">[[markerNum]]</text>
            </g>
            <g id="bus" viewBox="0 0 49 49">
                <g>
                    <path style="fill: [[color]];" 
                        d="M47.503,12.835h-1.994c-0.834,0-1.508,0.675-1.508,1.508v0.377h-1.185L40.354,3.08c-0.147-0.697-0.762-1.196-1.476-1.196&#10;&#9;&#9;H10.133c-0.713,0-1.327,0.499-1.476,1.196L6.194,14.722H5.01v-0.377c0-0.833-0.676-1.508-1.509-1.508H1.507&#10;&#9;&#9;C0.674,12.836,0,13.512,0,14.344v4.777c0,0.833,0.673,1.508,1.507,1.508h1.994c0.833,0,1.509-0.675,1.509-1.508v-2.389h0.864v8.674&#10;&#9;&#9;v15.979c0,0.833,0.674,1.51,1.508,1.51h0.652v1.807c0,1.333,1.081,2.414,2.413,2.414h2.209c1.335,0,2.414-1.081,2.414-2.414v-1.807&#10;&#9;&#9;h18.854v1.807c0,1.333,1.082,2.414,2.414,2.414h2.212c1.333,0,2.415-1.081,2.415-2.414v-1.807h0.651&#10;&#9;&#9;c0.832,0,1.508-0.677,1.508-1.51V25.407v-8.674h0.862v2.389c0,0.833,0.677,1.508,1.511,1.508h1.991&#10;&#9;&#9;c0.835,0,1.511-0.675,1.511-1.508v-4.777C49.01,13.51,48.334,12.835,47.503,12.835z M11.465,37.475&#10;&#9;&#9;c-1.526,0-2.766-1.238-2.766-2.767s1.239-2.769,2.766-2.769c1.53,0,2.768,1.24,2.768,2.769S12.996,37.475,11.465,37.475z&#10;&#9;&#9; M31.796,39.735H17.215v-1.258h14.581V39.735z M31.796,37.225H17.215v-1.26h14.581V37.225z M31.796,34.708H17.215V33.45h14.581&#10;&#9;&#9;V34.708z M31.796,32.194H17.215v-1.258h14.581V32.194z M24.505,26.356c-5.572,0-10.937-0.724-15.613-2.08v-7.729l2.463-11.647&#10;&#9;&#9;h26.299l2.464,11.646v7.729C35.441,25.633,30.076,26.356,24.505,26.356z M37.545,37.475c-1.525,0-2.768-1.238-2.768-2.767&#10;&#9;&#9;s1.24-2.769,2.768-2.769c1.529,0,2.768,1.24,2.768,2.769C40.311,36.237,39.073,37.475,37.545,37.475z"/>
                </g>                
                <rect x="11.572" y="5.784" width="25.621" height="19.294" style="fill: rgb(255, 255, 255);"/>     
                <text x="23.75" y="20" text-anchor="middle" style="font-size: 16px; font-family: Roboto; fill: [[tcolor]];">[[mtext]]</text>
            </g>
            <g id="user" viewBox="0 0 32 32">
                <path stroke="[[color]]" d="M16,22c4.963,0,9-4.936,9-11c0-6.064-4.038-11-9-11c-2.447,0-4.734,1.174-6.438,3.305C7.909,5.37,7,8.104,7,11.001 C7,17.064,11.037,22,16,22z M16,2.001c3.859,0,7,4.037,7,9c0,4.962-3.141,9-7,9c-3.859,0-7-4.038-7.001-9 C8.999,6.038,12.14,2.001,16,2.001z M23,20c-0.553,0-1,0.447-1,1s0.447,1,1,1c3.859,0,7,3.141,7,7c0,0.551-0.449,1-1,1H3 c-0.551,0-1-0.449-1-1c0-3.859,3.141-7,7-7c0.553,0,1-0.447,1-1s-0.447-1-1-1c-4.963,0-9,4.037-9,9c0,1.654,1.346,3,3,3h26 c1.654,0,3-1.346,3-3C32,24.038,27.963,20,23,20z"/>
            </g>
        </defs>
    </svg>
</plastic-map-marker-set>
```
### Design Considerations
It is important that each definition have:
* an `id` which is unique, and that no other `g` elements have an `id`
* a `viewBox` attribute - it defines the basis of the points in the SVG markup and allows the browser to scale the image as requested.

### Not Really Data Binding, but ...
While it's not actual data binding, marker definitions can have substitution points (see example markers above), marked with [[some.data.path]] that will be substituted in when you request the marker.

## Using Your Icons
### In Code
You can get a `google.map.icon` object for your marker icon by calling the static method `getMarkerSetIcon` of the `PlasticMapMarkerSet` which returns a `Promise` for a `google.map.icon` object:
```HTML
<google-map id="gm" style="width:100%;height:100%;" latitude="37.779" longitude="-122.3892" min-zoom="9" max-zoom="11" language="en" api-key="[[apiKey]]" on-google-map-ready="mapReady">
    <template is="dom-repeat" items="[[points]]">
        <google-map-marker slot="markers" latitude="[[item.lat]]" longitude="[[item.lng]]" icon="[[icon]]">
            <p>Yo</p>
        </google-map-marker>
    </template>
</google-map>
```
```JS
PlasticMapMarkerSet.getMarkerSetIcon('sample-markers', 'tdpin', 64, 96, myDataObject)
    .then((icon) => {
        this.icon = icon;
        this.points = [{
            lat: 37.779,
            lng: -122.3892
        }];
    });
```
### With plastic-map-marker-svg
`plastic-map-marker-svg` extends `google-map-marker` (i.e. `class PlasticMapMarkerSvg extends customElements.get('google-map-marker')`) adding just the icon functions.  

This is particularly useful if you are assigning different icons to different markers.

You use it in place of `google-map-marker`:
```HTML
<plastic-aspect-ratio style="width:100%;" aspect-width="4" aspect-height="3">
    <google-map id="gm" style="width:100%;height:100%;" latitude="37.779" longitude="-122.3892" min-zoom="9" max-zoom="11" language="en" api-key="[[apiKey]]">
        <template is="dom-repeat" items="[[points]]">
            <plastic-map-marker-svg slot="markers" latitude="[[item.lat]]" longitude="[[item.lng]]" icon-name="[[item.markerStyle.iconName]]"
            icon-height="[[item.markerStyle.height]]" icon-width="[[item.markerStyle.width]]" icon-data="[[item.markerStyle.iconData]]">
            <p>Yo! Some infowindow stuff!</p>
            </plastic-map-marker-svg>
        </template>
    </google-map>
</plastic-aspect-ratio>
```
Note that the `icon-name' property is in the form set:icon e.g. "sample-set:flag".

## License
MIT
## Issues
Please submit issues or questions through the github repository.
## Contributions
Contributions via pull request are certainly welcome and appreciated.

