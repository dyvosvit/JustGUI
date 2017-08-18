import poloniex
from decimal import *
import time
from colorama import Fore, Back, Style

print ("JustGUI - v1.0")

class Poloniex():

	polo = poloniex.Poloniex('KEY', 'SECRET')

	init_balance = 0.12 # Your init balance from Poloniex.

while True:

	class save_balance():


		estimatedBalance = Poloniex.polo.returnCompleteBalances()
		balance = Poloniex.polo.returnBalances()

		if balance != '':

			if estimatedBalance != 0:
				estim = 0

				for i in estimatedBalance:
					estim+=float (estimatedBalance[i]["btcValue"])

		now_balance = estim
		now_balance = Decimal(now_balance)
		file = open("balance", "w")
		file.write(str(now_balance))
				
		file.close()

	class calculated_gains():

		old_balance = infile = open('old_balance', 'r')
		old_balance = infile.read()
		
		save_balance.now_balance = Decimal(save_balance.now_balance)

		if len(old_balance) == 1:

			old_balance = save_balance.now_balance



		gain = ((save_balance.now_balance * 100 / Decimal(old_balance))-100)/100
		gain = Decimal(gain)
		old_balance_ = save_balance.now_balance

		old_balance = infile = open('old_balance', 'w')
		old_balance.write(str(old_balance_))

	def client_gain():

		nombre = "client_gain"
		infile = open('gains_client_gain', 'r')
		client_gain = infile.read()
		client_gain = Decimal(client_gain)
		file = open("gains_client_gain", "w")

		calculated_gain = calculated_gains.gain * Decimal(Poloniex.init_balance)
		calculated_gain = calculated_gain + client_gain
		file.write(str(calculated_gain))
		file.close()

	client_gain()


	class last_trades():

	    latestTrades = 30
	    save_trades = open('trades', 'w')

	    print_coins = []
	    tradeHistory24h = Poloniex.polo.returnTradeHistory('all')
	    try:
	        with open(check_coins, 'r') as afile:
	            for coin in afile:
	                print_coins += [coin.strip()]
	    except:
	        if print_coins == []:
	            print_coins = 'ETH XRP XEM LTC STR  BCN ETC DGB SC BTS DOGE DASH GNT EMC2 STEEM XMR ARDR STRAT NXT  ZEC LSK  FCT GNO NMC MAID   BURST GAME  DCR  SJCX RIC FLO REP NOTE CLAM SYS PPC EXP XVC VTC FLDC LBC AMP POT NAV XCP  BTCD  RADS   PINK GRC  NAUT  BELA  OMNI HUC NXC VRC  XPM VIA PASC  BTM NEOS XBC  BLK SBD BCY'
	            print_coins = print_coins.strip().split()
	    work_set = {}
	    for line in tradeHistory24h:
	        if line[4:] in print_coins:
	            for element in tradeHistory24h[line]:
	                signd = '-' if element['type']=='buy' else '+'
	                totald = signd+element['total']
	                thetext = 'PURCHASE: with an investment of' if element['type']=='buy' else 'SALE: with a profit of'
	                work_set[int(element['globalTradeID'])]=['BTC_'+line[4:], element['date'],element['type'].upper(), 'de',line[4:] , 'en', element['rate'],thetext,totald]
	    for key in sorted(work_set.keys(),reverse=True)[:latestTrades]:
	        colorit = Fore.RED if work_set[key][2] == 'BUY' else Fore.GREEN
	        trades = colorit+' '.join(work_set[key])
	        trades = trades[5:]
		save_trades.write(trades + ("\n\n"))



	time.sleep(420)
