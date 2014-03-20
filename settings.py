import os

server_address = os.environ['SERVER']
server_port    = int(os.environ['SERVER_PORT'])
nick           = os.environ['NICK']
username       = os.environ['USERNAME']
realname       = os.environ['REALNAME']
admins         = os.environ['ADMINS'].split(',')
channels       = os.environ['CHANNELS'].split(',')
