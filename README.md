# pynik

A Python IRC bot.

![](https://raw.github.com/dentarg/pynik/master/botnik.png)

## Environment variables

Configure your bot with the following environment variables:

| Environment variable   | Description                                       |
|------------------------|---------------------------------------------------|
| SERVER                 | IRC server the bot should connect to.             |
| SERVER_PORT            | IRC server port.                                  |
| NICK                   | Nickname of the bot.                              |
| USERNAME               | Username part of the bot hostmask.                |
| REALNAME               | Real name of the bot.                             |
| ADMINS                 | Nicknames with bot admin privileges.              |
| CHANNELS               | Channels the bot should join on start.            |
| TITLE_CHANNELS         | Print the `<title>` of URLs in these channels.    |
| HTTP_ACCEPT_LANGUAGE         | If present, use this value in the HTTP `Accept-Language` header. |
| twitter_consumer_key         | Twitter API key.                            |
| twitter_consumer_secret      | Twitter API secret.                         |
| twitter_access_token_key     |                                             |
| twitter_access_token_secret  |                                             |

Twitter API keys are required by [tweet.py](plugins/tweet.py). See [dev.twitter.com] for more info.

[dev.twitter.com]: https://dev.twitter.com/docs/auth/tokens-devtwittercom

If you put the environment variables in a file named `.env`, you can use [Honcho]
to start the bot.

Example of a `.env` file:

```sh
SERVER="irc.example.com"
SERVER_PORT="6667"
NICK="botnik"
USERNAME="botnik"
REALNAME="Freeze? I'm a robot. I'm not a refrigerator."
ADMINS="dentarg, serp"
CHANNELS="#foo, #bar, #baz"
TITLE_CHANNELS="#foo, #bar"
HTTP_ACCEPT_LANGUAGE="sv, en"

twitter_consumer_key=xxx
twitter_consumer_secret=xxx
twitter_access_token_key=xxx
twitter_access_token_secret=xxx
```

## Dependencies

Pynik make use of the following Python libraries:

* [python-twitter](https://github.com/bear/python-twitter)
* [requests](https://github.com/kennethreitz/requests)
* [chardet](https://github.com/chardet/chardet)
* [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/)
* [html5lib](https://github.com/html5lib/html5lib-python)

## Development / deployment

Install dependencies for dependencies, most of them are for [cryptography], which is used by requests. See [`deploy.yml`](deploy.yml) for what packages to install.

Install bot dependencies.

    sudo easy_install pip

    sudo -H pip install --upgrade -r requirements.txt

Install [foreman] if you don't have it

    gem install foreman

Start the bot

    foreman start

Start the bot in offline mode

    foreman run offline

[cryptography]: https://cryptography.io/en/latest/installation/
[foreman]: https://github.com/ddollar/foreman
