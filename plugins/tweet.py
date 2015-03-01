# -*- coding: utf-8 -*-
import re
import sys
import twitter
import settings
from json import JSONDecoder
from commands import Command

# TODO:
# - add caching
# - print out error messages
# - rate limiting (only allowed 150 requests per hour to Twitter API)
# - get screen_name from API instead of URL, can be incorrect in URL

class Tweet:
	idno = ''
	screen_name = ''
	text = ''
	erro = ''
	is_user = False
	user_name = ''
	user_description = ''

# called in plugins/title_reader.py
def match_tweet_url(url):
	status_regexp = '(http|https)://twitter.com/((#!/(\w+))|(\w+))/(status|statuses)/(\d+)'
	match = re.search(status_regexp, url, re.IGNORECASE)
	if not match:
		user_regexp = '(http|https):\/\/twitter.com\/(\w+)'
		match = re.search(user_regexp, url, re.IGNORECASE)
	return match

def get_tweet_text_and_user(tweet):
	api = twitter.Api(consumer_key=settings.twitter_consumer_key,
		consumer_secret=settings.twitter_consumer_secret,
		access_token_key=settings.twitter_access_token_key,
		access_token_secret=settings.twitter_access_token_secret)

	status = api.GetStatus(tweet.idno)

	# Use latin-1 to make IRCClient.send() happy
	tweet.text = status.text.encode('latin-1', 'replace')
	tweet.screen_name = status.user.screen_name.encode('latin-1', 'replace')
	return tweet

def get_user_description(tweet):
	api = twitter.Api(consumer_key=settings.twitter_consumer_key,
		consumer_secret=settings.twitter_consumer_secret,
		access_token_key=settings.twitter_access_token_key,
		access_token_secret=settings.twitter_access_token_secret)

	user = api.GetUser(screen_name=tweet.screen_name)

	# Use latin-1 to make IRCClient.send() happy
	tweet.user_name = user.name.encode('latin-1', 'replace')
	tweet.user_description = user.description.encode('latin-1', 'replace')
	return tweet

def get_tweet(message):
	tweet = Tweet()
	match = match_tweet_url(message)
	if match:
		if len(match.groups()) == 2:
			tweet.is_user = True
			tweet.screen_name = match.group(2)
			tweet = get_user_description(tweet)
			return tweet
		else:
			tweet.idno = match.group(7)
			tweet = get_tweet_text_and_user(tweet)
			return tweet
	else:
		return False

class TweetCommand(Command):
	hooks = ['on_privmsg']

	def on_privmsg(self, bot, source, target, message):
		tweet = get_tweet(message)

		if tweet:
			if tweet.is_user:
				output = "@%s (%s): %s" % (tweet.screen_name, tweet.user_name, tweet.user_description)
			else:
				output = "@%s: %s" % (tweet.screen_name, tweet.text)

			bot.tell(target, output)
