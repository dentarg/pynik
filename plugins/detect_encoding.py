# coding: utf-8

from __future__ import unicode_literals
from commands import Command
import re
import chardet

class DetectEncodingCommmand(Command):
	hooks = ['on_raw_privmsg']

	def __init__(self):
		pass

	def trig_chardet(self, bot, source, target, message, raw_line):
		"""Detect your encoding. Usage: .chardet text with åäö (alias: .åäö)"""

	def on_raw_privmsg(self, bot, source, target, message, raw_line):
		triggers = ['chardet', 'åäö']

		if not any([message.startswith('.%s' % (trigger)) for trigger in triggers]):
			return

		m = re.search('^(.+)!', source)
		if m:
			nick = m.group(1)
		else:
			nick = source

		message_out = detect_encoding(nick, raw_line)
		bot.tell(target, message_out)

def detect_encoding(nick, raw_line):
		result = chardet.detect(raw_line)
		encoding = result["encoding"].upper()
		confidence = int(result["confidence"] * 100)
		message_out = "%s: Du använder nog %s (%s%% säker)" % (nick, encoding, confidence)
		return message_out

