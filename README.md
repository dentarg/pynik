# pynik

A Python IRC bot.

![](https://raw.github.com/dentarg/pynik/master/botnik.png)

## Environment variables

Configure your bot with environment variables:

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

If put the environment variables in a file named `.env`, you can use [Honcho]
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
```

Install Honcho if you don't have it

    pip install honcho

Start the bot

    honcho run python main.py

[Honcho]: https://github.com/nickstenning/honcho
