import os

server_address = os.environ['SERVER']
server_port    = int(os.environ['SERVER_PORT'])
nick           = os.environ['NICK']
username       = os.environ['USERNAME']
realname       = os.environ['REALNAME']
admins         = os.environ['ADMINS'].split(',')
channels       = os.environ['CHANNELS'].split(',')
title_channels = map(lambda x: x.strip(),
        os.environ['TITLE_CHANNELS'].split(','))

twitter_consumer_key        = os.environ['twitter_consumer_key']
twitter_consumer_secret     = os.environ['twitter_consumer_secret']
twitter_access_token_key    = os.environ['twitter_access_token_key']
twitter_access_token_secret = os.environ['twitter_access_token_secret']
