# -*- coding: utf-8 -*-
import utility
from commands import Command

class QuoteCommand(Command):

    def trig_quote(self, bot, source, target, trigger, argument):
        queried_stock = argument.strip()
        if not queried_stock:
            return "usage: .quote AAPL"

        url = 'http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=nxl1p4' % queried_stock
        response = utility.read_url(url)

        if response:
            name, stock_exchange, value_price = response['data'].split("\",")
            value, price = value_price.split(",")
            return ("%s (%s) %s %s" % (name, stock_exchange, value, price)).replace("\"", "")
