Motion AI Ruby SDK
==================

[![Gem Version][gem-version-svg]][gem-version-link]
[![Dependency Status][dependency-status-svg]][dependency-status-link]
[![Codacy Badge][codacy-svg]][codacy-link]
[![Downloads][downloads-svg]][downloads-link]
[![Docs][docs-rubydoc-svg]][docs-rubydoc-link]
[![License][license-svg]][license-link]



Simple SDK for [Motion AI](https://motion.ai) REST API.

API endpoints:

Endpoint | Supported?
---------|-----------
`GET /messageBot` | yes
`POST /messsageHuman` | tbd
`GET /getConversations` | yes
`POST` Webhooks | tbd

## Installation

```
$ gem install motion-ai
```

## Usage

```ruby
require 'motion-ai'

client = MotionAI::Client.new 'my_api_key', 'my_bot_id'

res = client.message_bot msg: 'Hello Bot!', session: '12345'

res = client.get_conversations
```

For more information on the parameters that can be passed to the API,
see the [Motion AI API docs](http://docs.motion.ai/docs/api).

## Links

Project Repo

* https://github.com/grokify/motion-ai-ruby

Motion AI Docs

* http://docs.motion.ai/docs/api

 [gem-version-svg]: https://badge.fury.io/rb/motion-ai.svg
 [gem-version-link]: http://badge.fury.io/rb/motion-ai
 [downloads-svg]: http://ruby-gem-downloads-badge.herokuapp.com/motion-ai
 [downloads-link]: https://rubygems.org/gems/motion-ai
 [dependency-status-svg]: https://gemnasium.com/grokify/motion-ai-ruby.svg
 [dependency-status-link]: https://gemnasium.com/grokify/motion-ai-ruby
 [codacy-svg]: https://api.codacy.com/project/badge/Grade/1e014a7f38734145bff06ce0ed2af829
 [codacy-link]: https://www.codacy.com/app/grokify/motion-ai-ruby
 [docs-rubydoc-svg]: https://img.shields.io/badge/docs-rubydoc-blue.svg
 [docs-rubydoc-link]: http://www.rubydoc.info/gems/motion-ai/
 [license-svg]: https://img.shields.io/badge/license-MIT-blue.svg
 [license-link]: https://github.com/grokify/motion-ai-ruby/blob/master/LICENSE.md

