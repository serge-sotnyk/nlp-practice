# `<ada-poetry>`

✍️ A simple web component for typesetting poetry and other verse-based texts properly 📝
  1. [English ](#en)
    1. [Roadmap](#roadmap)
  2. [Español](#es)
    1. [Ruta a seguir](#la-ruta-de-`<ada-poetry>`)
️️
## En

Some case study and reference to ugly typesetted verse on the wild will come here.

### Roadmap ➜

I want this to be available and easy to use for non-technichal publishers. I struggled to find a proper way to display poetry on the web and used some awful hacks —separete everything with dots and make them the same color as the background or a `<br>` soup. That's awful! And not accessible! 😖

Some CSS rules fix this but the solution is not widely used. A web component seems a good option to make this distributable. 🤯 

Most of the users that would benefit from **`<ada-poetry>`** use WordPress, so a plugin with a shortcode is a second goal once the web component is ready for use in production. A friendly tutorial to drop the js file in your html head and use **`<ada-poetry>`** will be released along with first test version.

I will use Polymer. Stencil looks good because of Typescript and React-like elegant syntax. My first thougt was using Vue.js because I'm using it to develop other projects wich will use **`<ada-poetry>`**. Polymer is the right choice for its the most mature option for Web Components at this moment. No-nonse vanilla JavaScript would be a great option but polyfills are still needed anyways, so Polymer is the way to go.

**Why `<ada-poetry>`?**

As a homage to poetry lover and first programmer Ada Lovelace, becasue I didn't came with a better word to go with poetry and web components need a hyphen to work. 👩‍💻

I love Lord Byron, Ada's father, and a Spanish translation of my own for one of his poems will be used to test this web component. 🤷🏽‍♂️

Please be kind, this is my first open source project. 😳 🙈  All my other repos are forks and/or practice.


🖤**I18n**🖤 nI'm a translator so documentation will be bilingual out of the box.


## Es

Un web component sencillo para formar poemas y otros textos en verso de manera adecuada.

Aquí va a ir un breve caso de estudio y algunos ejemplos de versos (de?)formados de manera horrible en la red.

### La ruta de `<ada-poetry>` ➜

Mi obejetivo es hacer que este web component sea de uso fácil para gente que publica contenido en la red pero no tiene conocimientos técnicos. Yo mismo alguna vez usé trucos horribles para que los versos quedaran en la página como en el poema capturado en algún editor de texto: separar todo con puntos y ponerlos del color del fondo, termianar con una sopa de `<br>`, etc. ¡Por favor, no lo hagan! Queda horrible. Y no es accesible. 😖

Unas cuantas líneas de CSS son suficientes para resolver el problema de formar versos en la web. Un web component es una gran opción para distribuir la solución a quienes la necesitan. 🤯

La mayoría de los usuarios que se benificiarían de **`<ada-poetry>`** usan WordPress, así que un plugin que provea un shortcode es un segundo objetivo de este proyecto una vez que el web component esté listo para uso en producción. Si bien ese segundo obejtivo no es primordial, la primera versión de prueba vendrá acompañada de un tutorial para incluir el **`<ada-poetry>`** en tu proyecto sin importar si lo publicas usando WP o cualquier otra plataforma de publicación que permita la edición de HTML.1. [`<ada-poetry>`](#`<ada-poetry>`)

Para hacer el web component voy a usar Polymer. Ya probé Stencil y me gustó que usa Typescript y una sintaxis elegante como la de React. Mi primera idea fue usar Vue.js porque también lo uso en otros proyectos de los que **`<ada-poetry>`** es parte. Pero Polymer es la opción más madura para desarrollar web components en este momento. Usar javascript puro sería un gran opción, pero el soporte de los web components aún requiere polyfills, así que Polymer es la mejor decisión.

**¿Por qué `<ada-poetry>`?**

A manera de homenaje a Ada Lovelace, quien adoraba la poesía y fue la primera persona en desarrollar un algoritmo de software en la historia. 👩‍💻

Además, porque los web components necesitan un guión en medio y no se me ocurrió otra palabra para poner junto con poesía. 🤷🏽‍♂️

Amo a Lord Byron, que fue el padre de Ada, y para probar este web component voy a usar una de mis traducciones de sus poemas.

Porfa, sean amables. Es mi primer proyecto de código abierto. 😳 🙈  El resto de mis repos son práctica.

🖤**I18n**🖤 La documentación es bilingüe desde el principio porque traductor (y en este momento el contenido puede variar ligeramente de un idioma al otro).

