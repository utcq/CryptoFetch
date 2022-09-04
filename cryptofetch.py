#!/usr/bin/python3
import json
import ascii
import requests as r
import sys, os 
from os import listdir
from os.path import isfile, join
from thefuzz import fuzz, process

coin = ''
currency = 'usd'

class Art:
    def coinOutput(image, symbol, price,  coin24HourChange, coin24HourVolume, coinMarketCap):
        art = f"""⚛  Symbol:                   {symbol.upper()}
$  Price:                    {price}
%  PriceChangePercent:       {"{:.2f}".format(coin24HourChange)}
⬛ Volume:                   {"{:.2f}".format(coin24HourVolume)}
M  Market Cap:               {"{:.2f}".format(coinMarketCap)}  
        """
        print(image)
        print(art)
        
  
def retrieveData(crypto: str):
    
    request = r.get('https://api.coingecko.com/api/v3/simple/price?ids=' + coin + '&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true')
    
    coinData = request.json()
    coinPrice = coinData[coin][currency]
    coinMarketCap = coinData[coin][currency + '_market_cap']
    coin24HourVolume = coinData[coin][currency + '_24h_vol']
    coin24HourChange =  coinData[coin][currency + '_24h_change']

    image = collectImage(coin)
    Art.coinOutput(image, coin, coinPrice, coin24HourChange, coin24HourVolume, coinMarketCap)


def collectImage(coin):
  request = r.get("https://api.coingecko.com/api/v3/coins/" + coin + "?localization=false&tickers=false&market_data=false&community_data=false&developer_data=false&sparkline=false")
  
  symbolData = request.json()
  symbolString = symbolData['symbol']
  onlyFiles = [f for f in listdir(os.getcwd() + '/icon') if isfile(join(os.getcwd() + '/icon', f))]
  imageName = process.extractOne(symbolString + '.png', onlyFiles)
  
  image = ascii.ImageToAscii(imagePath=os.getcwd() + '/icon/' + imageName[0])
  
  seperator  = "<"

  image = str(image).split(seperator, 1)[0]

  return image
  


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing Argument.\nUsage: cryptofetch CRYPTOSYMBOL")
        exit()

    coin = sys.argv[1]
    retrieveData(sys.argv[1])


