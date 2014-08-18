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

twitter_consumer_key=xxx
twitter_consumer_secret=xxx
twitter_access_token_key=xxx
twitter_access_token_secret=xxx
```

## Development

[python-twitter](https://github.com/bear/python-twitter) is a dependency, install it with

    pip install python-twitter

Install [Honcho] if you don't have it

    pip install honcho

Start the bot

    honcho run python main.py

[Honcho]: https://github.com/nickstenning/honcho
