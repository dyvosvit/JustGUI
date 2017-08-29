import bittrex
from decimal import *
import time
from colorama import Fore, Back, Style

print ("JustGUI - v1.0")

class Bittrex():

	trex = bittrex.Bittrex('KEY', 'SECRET')

	init_balance = 0.12 # Your init balance from Bittrex.

while True:

	class save_balance():
		
		balanceBTC = 0
		# free BTC's on balance
		balance = Bittrex.trex.get_balance('BTC')
		if balance['success'] == True:
			# add code to handle BTC's on orders here ...
			balanceBTC = float(balance['result']['Available'])
		time.sleep(0.3)
		
		#coins we have on balance
		resultBalances = Bittrex.trex.get_balances()
		bittrexCoinz={}
	    
		if resultBalances['success']==True:
	         for i in resultBalances['result']:
	            if (i['Balance']!=0):
	                bittrexCoinz[i['Currency']]=i        
 			time.sleep(0.3)
        
        # prices to calc estimated BTC's for coinz we have
		resultTicker = Bittrex.trex.get_market_summaries()
		totalRevenues=0
		if resultTicker['success']==True:
	   		for i in resultTicker['result']:
				market, coin =  i['MarketName'].split('-')
	        	if (market=='BTC') and (coin in bittrexCoinz.keys()):
	            	# calcs are made using lastprice
	  				totalRevenues += float(bittrexCoinz[coin]['Balance']*i['Last'])

		# balance = BTC's + BTC's for coinz sold at lastprice
		now_balance = Decimal(float(balanceBTC)+totalRevenues)

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

		calculated_gain = calculated_gains.gain * Decimal(Bittrex.init_balance)
		calculated_gain = calculated_gain + client_gain
		file.write(str(calculated_gain))
		file.close()

	client_gain()


	class last_trades():

		latestTrades = 30
		def f(a,n,s):
			return (s+str(format(a, '.8f'))).rjust(n)
			
    	resultMarkets=Bittrex.trex.get_order_history()
    	text_out={}
    	if resultMarkets['success']==True:
        	for i in resultMarkets['result'][:latestTrades]:
				date=i['TimeStamp'].replace('T',' ').split('.')[0]
            	text_out[date]=[i['Exchange'], date,
                                      i['OrderType'][6:],str(i['Quantity']),'of',i['Exchange'][4:],
                                      'at',last_trades.f(i['PricePerUnit'],0,''),'resulting',
                                      '-'+str(i['Price']) if i['OrderType'][6:] == 'BUY' else '+'+str(i['Price'])]

		save_trades = open('trades', 'w')
		save_trades.write(' '.join(text_out) + ("\n\n"))
		save_trades.close()



	time.sleep(420)
