# coding: utf-8

import sys
import time
import settings
from plugins import Plugin

def get_plugins():
	return [AutoJoinPlugin()]

class AutoJoinPlugin(Plugin):
	def __init__(self):
		pass

	def on_connected(self, bot):
		channels = settings.channels

		for channel in channels:
			bot.join(channel)
