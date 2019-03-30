# Pushover for Minoss
[![GitHub version](https://badge.fury.io/gh/eisbehr-%2Fminoss-pushover.svg)](http://github.com/eisbehr-/minoss-pushover)
[![NPM version](https://badge.fury.io/js/minoss-pushover.svg)](http://www.npmjs.org/package/minoss-pushover)
[![Dependency version](https://david-dm.org/eisbehr-/minoss-pushover.png)](https://david-dm.org/eisbehr-/minoss-pushover)

This module adds support for Pushover notifications to [Minoss](https://github.com/eisbehr-/minoss) server.
The API communication is based on [`pushover-notifications`](https://www.npmjs.com/package/pushover-notifications).


## Table of Contents
* [Installation](#installation)
* [Configuration](#configuration)
* [Basic Usage](#basic-usage)
* [Parameter Shorthand](#parameter-shorthand)
* [Message Builder](#message-builder)
  * [Using `JSON` as Message Object](#using-json-as-message-object)
  * [Chaining Messages](#chaining-messages)
* [Bugs / Feature request](#bugs--feature-request)
* [License](#license)
* [Donation](#donation)


---


## Installation
Inside your Minoss root folder just use [npm](http://npmjs.com) to install this Module.

```SH
$ npm install minoss-pushover
```


## Configuration
By default there are two configuration files available inside the `config/` folder: `apps` and `messages`.
The configuration for `messages` is optionally.
It is possible to store different predefined message objects there, if wanted.
For more details take a look inside the files or read about the [message builder](#message-builder).

Before using this module the `apps` configuration should be set up.
This file contains the `user_key` and `app_token` for all pushover apps where notifications should be send to.

It is possible to store the apps under own names.
The name `default` is a reserved name.
It will select this app whenever no app name was given by request parameters.
So, if only one app is available, the name `default` should be used.

```JS
module.exports = {
    default: {
        user:  '14a6b88846b28898a237fa3f84148f54',
        token: '30f28fcb0c97083d20a8cd06f3f6e737'
    },
    another: {
        user:  '85b9e76dc041b411b04b5c1f49cba885',
        token: '8d0771a0757289d942db83db090623d6'
    }
};
```


## Basic Usage
The basic usage is pretty simple.
When a `default` app is defined just call the `send` script with a supplied `message` string to be send.
For more parameters take a look at the [pushover api](https://pushover.net/api) or the [parameter shorthands](#parameter-shorthand).

> http://localhost:8080/pushover/send?message=my%20custom%20message


### Parameter Shorthand
All request parameters can be shorten to it's first character (_except `url_title` and `timestamp`, which are shorten with `ut` and `ts`_).
With this it is possible to use shorten URLs.

```TEXT
app        ->  a
message    ->  m
device     ->  d
title      ->  t
url        ->  u
url_title  ->  ut (!)
priority   ->  p
timestamp  ->  ts (!)
sound      ->  s
```

Example:

> http://localhost:8080/pushover/send?**app**=default&**priority**=1&**device**=*  
> http://localhost:8080/pushover/send?**a**=default&**p**=1&**d**=*


## Message Builder
Pushover messages are basically a JavaScript `object`.
It is possible to set all the options of the [official api](https://pushover.net/api) via request parameters.
But is is even possible to let these message objects build on request.

Messages can be predefined in [configuration](#configuration).
If there are messages configured they can be send by it's name on request:

> http://localhost:8080/pushover/send?message=**name**


### Using `JSON` as Message Object
It is possible to use a `JSON` string as message object on request.
It works the same way as with predefined messages: 

> http://localhost:8080/pushover/send?message=**{"message":"my message","device":"\*"}**


### Chaining Messages
The message builder can even handle a chain of messages.
These messages has to be separated by a pipe `|` on request.
It will combine all messages in the given order.
When a message property is set by more than one entry, the last one will be set.

For example, these are predefined states:

```JS
let messages = {
    default: {
        device: '*',
        priority: 0
    },
    high: {
        priority: 1
    }
}
```

And this request:

> http://localhost:8080/pushover/send?message=**default|high|my%20message%20text**

The resulting message object would become:

```JS
{
  message: 'my message text',
  device: '*',
  priority: 1
}
```

It is even possible to chain a `JSON` string too.

> http://localhost:8080/pushover/send?message=**default|high|{"message":"my message"}**


## Bugs / Feature request
Please [report](http://github.com/eisbehr-/minoss-pushover/issues) bugs and feel free to [ask](http://github.com/eisbehr-/minoss-pushover/issues) for new features directly on GitHub.


## License
Minoss is dual-licensed under [MIT](http://www.opensource.org/licenses/mit-license.php) and [GPL-2.0](http://www.gnu.org/licenses/gpl-2.0.html) license.


## Donation
_You like to support me?_  
_You appreciate my work?_  
_You use it in commercial projects?_  
  
Feel free to make a little [donation](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=93XQ8EYMSWHC6)! :wink:

