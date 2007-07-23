from __future__ import with_statement
import pickle
import sys
import re
import utility
from plugins import Plugin
from commands import Command
import command_catcher

class URL():
	url = ''
	title = ''
	timestamp = ''
	nick = ''
	def is_match(self, searchword):
		if self.url and re.search(searchword, self.url, re.IGNORECASE):
			return True
		if self.title and re.search(searchword, self.title, re.IGNORECASE):
			return True
		if self.nick and re.search(searchword, self.nick, re.IGNORECASE):
			return True
		return False
	

def get_title(self, url):
	import urllib
	if not re.search('http', url):
		url = 'http://' + url
	try:
		datasource = urllib.urlopen(self.urls[target].url)
		data = datasource.read()
	except command_catcher.TimeoutException:
		return None
	finally:
		datasource.close()

	m = re.search('<title>(.+?)<\/title>', data, re.IGNORECASE)

	if m:
		title = m.group(1)
		return re.sub('<.+?>', '', title)
	else:
		return None

class TitleReaderPlugin(Command): 
	hooks = ['on_privmsg']   
	black_urls = []
	urls = {}
	url_list = []

	def __init__(self):
		pass
	
	def get_options(self):
		return ['black_urls']
	
	def on_privmsg(self, bot, source, target, tupels):
		message = tupels[5]

		m = re.search('((http:\/\/|www.)\S+)', message, re.IGNORECASE)

		if m:
			self.urls[target] = URL()
			self.urls[target].url = m.group(1)
			self.urls[target].nick = source
			self.urls[target].timestamp = 'test'
			self.urls[target].title = get_title(url)
			self.save_last_url(target)

	def save_last_url(self, target):
		self.url_list.append(self.urls[target])
		self.save_urls()

	

	def trig_urlsearch(self, bot, source, target, trigger, argument):
		resultlist = []
		match = False

		if len(argument) > 0:
			searchlist = argument.split(' ')

			for object in self.url_list:
				match = True
				for word in searchlist:
					if not object.is_match(word):
						match = False
						break
				if match:
					resultlist.append(object)

			if len(resultlist) > 0:
				if resultlist[0].title:
					title = resultlist[0].title
				else:
					title = 'N/A'
				bot.tell(target, 'Match 1 of ' + str(len(resultlist)) + ': ' + resultlist[0].url + ' - ' + title)
			else:
				bot.tell(target, 'No match found.')
		else:
			bot.tell(target, 'Usage: .urlsearch <search string>')

		

	def trig_title(self, bot, source, target, trigger, argument):
		if target in self.urls.keys():
			m = self.urls[target].title

			if m:
				bot.tell(target, m)
			else:
				bot.tell(target, 'I can\'t find a title for ' + self.urls[target].url) 
		else:
			bot.tell(target, 'I haven\'t seen any urls here yet.')

	def save_urls(self):
		file = open('data/urls.txt', 'w')
		p = pickle.Pickler(file)
		p.dump(self.url_list)
		file.close()

	def load_urls(self):
		try:
			file = open('data/urls.txt', 'r')
			self.url_list = pickle.Unpickler(file).load()
			file.close()
		except IOError:
			pass

	def on_load(self):
		del self.black_urls[:]

		self.load_urls()

		file = open('data/black_urls.txt', 'r')

		while True:
			line = file.readline()
			if not line:
				break

			m = re.match('^(.+)$', line)
			
			if m:
				self.black_urls.append(m.group(1))

	def save(self):
		file = open('data/black_urls.txt', 'w')

		for url in self.black_urls:
			file.write(url)
			file.write('\n')

		file.close()

	def on_modified_options(self):
		self.save()
