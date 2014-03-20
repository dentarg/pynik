# pynik

A Python IRC bot.

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

If put the environment variables in a file named `.env`, you can use [Honcho]
to start the bot.

Install Honcho if you don't have it

    pip install honcho

Start the bot

    honcho run python main.py

[Honcho]: https://github.com/nickstenning/honcho
