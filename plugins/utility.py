# coding: utf-8

from __future__ import with_statement
import pickle
import sys
from plugins import Plugin
from HTMLParser import HTMLParser
import re
import os
import signal
import string
import settings
import requests

class TimeoutException(Exception):
	pass

def unescape(string):
	unescaped_string = HTMLParser().unescape(string)
	unescaped_string_type = type(unescaped_string)

	if unescaped_string_type == str:
		return unescaped_string.decode('utf-8')
	else:
		return unescaped_string

def escape(str):
	import urllib
	t = {
		'%E5': 'å',
		'%E4': 'ä',
		'%F6': 'ö',
		'%C5': 'Å',
		'%C4': 'Ä',
		'%D6': 'Ö'
	}

	s = urllib.quote_plus(str)

	for key in t.keys():
		s = s.replace(key, t[key])

	return s

latin1_aao_trans = string.maketrans("\xe5\xe4\xf6\xc5\xc4\xd6", "aaoAAO")
utf8_aao_dict = { "Ã¥": "a", "Ã¤": "a", "Ã¶": "o", "Ã…": "A", "Ã„": "A", "Ã–": "O" }

def asciilize(aaostr):
	source = aaostr.translate(latin1_aao_trans)
	to = ""
	while source:
		if source[0:2] in utf8_aao_dict:
			to += utf8_aao_dict[source[0:2]]
			source = source[2:]
		else:
			to += source[0]
			source = source[1:]

	return to

def get_all_subclasses(c):
	l = [c]
	for subclass in c.__subclasses__():
		l.extend(get_all_subclasses(subclass))
	return l

def timeout(f, timeout = 1, args = (), kwargs = {}):
	def handler(signum, frame):
		raise TimeoutException

	old = signal.signal(signal.SIGALRM, handler)
	signal.alarm(timeout)

	result = None
	try:
		result = f(*args, **kwargs)
	except:
		signal.alarm(0)
		raise
	finally:
		signal.signal(signal.SIGALRM, old)
	signal.alarm(0)
	return result

def extract_nick(host):
	m = re.search('^(.+)!', host)
	if m:
		return m.group(1)
	else:
		return host

def read_url(url):
	page = { "url": url, "data": "" }

	try:
		headers = { "user-agent": "Pynik/0.1" }

		if settings.http_accept_language:
			headers["Accept-Language"] = settings.http_accept_language

		response = requests.get(url, headers=headers, timeout=15)

		page["headers"] = response.headers
		page["encoding"] = response.encoding
		page["raw_content"] = response.content
		page["data"] = response.text # compatibility with old plugins
	except requests.exceptions.RequestException:
		print "error in read_url", sys.exc_info(), traceback.extract_tb(sys.exc_info()[2])

	return page

def save_data(name, data):
	handle = open(os.path.join('data', name + '.txt'), 'w')
	p = pickle.Pickler(handle)
	p.dump(data)
	handle.close()

def load_data(name, default_value=None):
	try:
		with open(os.path.join('data', name + '.txt'), 'r') as handle:
			return pickle.Unpickler(handle).load()
	except:
		print "Could not load data from file 'data/" + str(name) + ".txt' :("
		return default_value

def has_admin_privileges(source, target):
	return source in settings.admins

nbsp_utf8 = unescape("&nbsp;")

def currency_conversion(amount, source, target):
	url = 'http://www.google.com/search?rls=en&q=' + str(amount) + '+' + source + '+in+' + target + '&ie=UTF-8&oe=UTF-8'
	response = read_url(url)
	data = response["data"]
	data = data.replace(nbsp_utf8, "") # Get rid of UTF-8 NBSP

	m = re.search('\<b\>\d+(\.\d+)? [^=]+ = (\d+(\.\d+)?)[^\<]+\<\/b\>', data)
	if m:
		return float(m.group(2))
	else:
		return None

