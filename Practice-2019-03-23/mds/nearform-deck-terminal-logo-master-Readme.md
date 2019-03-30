# @deck/terminal-logo

[![js-standard-style](https://img.shields.io/badge/code%20style-standard-brightgreen.svg?style=flat)](http://standardjs.com/)

Logo for Deck with same interface as nearForm terminal logo https://www.npmjs.com/package/nearform-terminal-logo

![image](./img/deck_logo_03.png)

"Deck logo" by [Valentin Keleti](https://www.flickr.com/photos/valke04) can be reused under the [CC BY license](https://creativecommons.org/licenses/by/4.0/)


## Usage
logo(_options_);

options - an options object which has two attributes:
- leftPadding: represents left padding in terminal points (monospaced characters). This is optional and by default, the logo is placed in the middle of the terminal.
- text: Text to be displayed beside the logo. This is also optional.

_Note_: `logo()` can be called without any options which will print the logo to the middle of the terminal.


Also has a `toTTY(options)` method, that writes directly to `process.stdout`. 


```javascript
require('deck-terminal-logo').toTTY({leftPadding: 20});
``` 

## Example

```javascript
var logo = require('deck-terminal-logo');
console.log(logo({leftPadding: 20, text: 'DECK'}));
```

## Output

![image](./img/deck-logo.png)

## Ecosystem

To view other pieces of the deck system see <https://github.com/nearform/deck>

## Issues and PR's

* Please open any issues for any deck related module on the <https://github.com/nearform/deck> community repo.
* Any module specific PR's are welcomed on the corresponding repo.

## Credits

Sponsored by <a href="http://nearform.com">nearForm</a>

### Contributors

  * David Mark Clements
  * Mihai Dima
  * Cristian Kiss

### Contributing

Deck is an **OPEN Open Source Project**. This means that:

> Individuals making significant and valuable contributions are given commit-access to a project to contribute as they see fit. A project is more like an open wiki than a standard guarded open source project.

See the [`CONTRIBUTING.md`](CONTRIBUTING.md) file for more details.

