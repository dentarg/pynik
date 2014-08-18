# -*- coding: utf-8 -*-
import re
import sys
import utility
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
	user = ''
	text = ''
	erro = ''

# called in plugins/title_reader.py
def match_tweet_url(url):
	regexp = '(http|https)://twitter.com/((#!/(\w+))|(\w+))/(status|statuses)/(\d+)'
	m = re.search(regexp, url, re.IGNORECASE)
	return m

def get_tweet_text_and_user(tweet):
	api = twitter.Api(consumer_key=settings.twitter_consumer_key,
		consumer_secret=settings.twitter_consumer_secret,
		access_token_key=settings.twitter_access_token_key,
		access_token_secret=settings.twitter_access_token_secret)

	status = api.GetStatus(tweet.idno)

	tweet.text = status.text
	tweet.user = status.user.screen_name
	return tweet

def get_tweet(message):
	m = match_tweet_url(message)
	if m:
		tweet = Tweet()
		tweet.idno = m.group(7)
		tweet = get_tweet_text_and_user(tweet)
		if tweet:
			return tweet
		else:
			return False
	else:
		return False

class TweetCommand(Command):
	hooks = ['on_privmsg']

	def on_privmsg(self, bot, source, target, message):
		tweet = get_tweet(message)

		if tweet:
			output = "@" + tweet.user + ": " + tweet.text
			bot.tell(target, output)
