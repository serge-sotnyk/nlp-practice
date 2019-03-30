Snapcat
=======
[![Build Status](https://travis-ci.org/nneal/snapcat.png)](https://travis-ci.org/nneal/snapcat)


A cat-tastic Ruby wrapper for the [Snapchat](http://snapchat.com) private API.
Meow. This gem is designed to give you a friendly Ruby-like interface for
interacting with the Snapchat API.

Please note
-----------

Snapchat has recently [cracked down against third party applications](http://www.theverge.com/2015/4/2/8335917/snapchat-transparency-report-third-party-app-access). Thus, until further notice, this API wrapper will not work. 


Installation
------------

Add this line to your application's `Gemfile`:

    gem 'snapcat', '~> 0.5'

And then execute:

    $ bundle

Alternatively, install it via command line:

    $ gem install snapcat


Usage
-----

**User Auth**

```ruby
# Initialize a client and login
snapcat = Snapcat::Client.new('your-username')
snapcat.login('topsecretpassword')

# Initialize a new client, register, and login
snapcat = Snapcat::Client.new('your-new-username')
snapcat.register('topsecretpassword', '1990-01-20', 'test@example.com')

# Logout
snapcat.logout
```


**User Actions**

```ruby
# Block a user
snapcat.block('username-to-block')

# Clear feed
snapcat.clear_feed

# Fetch a user's updates
snapcat.fetch_updates

# Unblock a user
snapcat.unblock('username-to-unlock')

# Update user's email
snapcat.update_email('newemail@example.com')

# Update user's privacy setting
# Two choices:
#   Snapcat::User::Privacy::EVERYONE
#   Snapcat::User::Privacy::FRIENDS
snapcat.update_privacy(Snapcat::User::Privacy::EVERYONE)

# Pro tip:
#   Every call to the API responds with Snapcat::Response object with which
#   you can check a few important things
response = snapcat.block('username-to-block')
response.code # => 200
response.http_success # => true
response.data # => { logged: true, ... }
```

**User Data**

```ruby
# Get the user
user = snapcat.user

# Examine all raw user data
user.data

# Examine snaps received
user.snaps_received

# Examine snaps sent
user.snaps_sent

# Examine friends
user.friends
```

**Friends**

```ruby
# Add a new friend
snapcat.add_friend('mybestbuddy')

# Grab a friend
friend = user.friends.first

# Set a friend's display name
snapcat.set_display_name(friend.username, 'Nik Ro')

# Delete a friend :(
snapcat.delete_friend(friend.username)

# Learn more about your friend
friend.can_see_custom_stories
friend.display_name
friend.username

# What kind of friend are they anyway??
friend.type
friend.type.confirmed?
friend.type.unconfirmed?
friend.type.blocked?
friend.type.deleted?
```

**Sending Snaps**

```ruby
# Send it to catsaregreat with 3 seconds duration
# `data` is a string which can be read directly from an mp4 or jpg
snapcat.send_media(data, 'catsaregreat')

# Or send it to multiple recipients and override default view_duration
snapcat.send_media(data, %w(catsaregreat ronnie99), view_duration: 4)
```

**Posting a Story**

```ruby
# Post a Story out to your network
# `data` is a string which can be read directly from an mp4 or jpg
snapcat.send_story(data, caption_text: "oh hai haz cheezburger", time: 10)
```

**Getting Stories**

```ruby
# Get all stories from your network, including view count, viewers (essentially anything in the friends list)
snapcat.get_stories
```

**Received Snaps**

```ruby
# Grab a snap
snap = user.snaps_received.first

# Get the snap image or video data
media_response = snapcat.media_for(snap.id)
media = media_response.data[:media]

# Record a view
snapcat.view(snap.id)

# Record a screenshot
snapcat.screenshot(snap.id)

# Record a screenshot

# Learn more about the media
media.image?
media.video?
media.file_extension
media.type_code

# Get the data from the media object
media.to_s
```

**Snaps General**

```ruby
# Learn more about the snap
snap.broadcast
snap.broadcast_action_text
snap.broadcast_hide_timer
snap.broadcast_url
snap.screenshot_count
snap.media_id
snap.id
snap.media_type
snap.recipient
snap.sender
snap.status
snap.sent
snap.opened
```

**Advanced User Auth**

The standard `login` method will log out all other sessions. If you want to use
Snapcat in multiple concurrent processes, you need to share this token across
processes and set it manually.

```ruby
# Fetch token
snapcat.auth_token

# Set token
snapcat.auth_token = '1c7e8f83-1379-4694-8fa9-4cab6b73f0d4'
```


Contributing
------------

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Add tests and make sure they pass
6. Create new Pull Request


Credits
-------

* [Neal Kemp](http://nealke.mp), [Daniel Archer](http://dja.io)
* Based on work by martinp on [pysnap](https://github.com/martinp/pysnap) and by
  djstelles on [php-snapchat](https://github.com/dstelljes/php-snapchat)

Copyright &copy; 2013 Neal Kemp, Daniel Archer

Released under the MIT License, which can be found in the repository in `LICENSE.txt`.

