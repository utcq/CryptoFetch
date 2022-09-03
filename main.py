#!/usr/bin/python3
import json
#import requests
import sys, os 


baseURL = "https://api.binance.us/api/v3/trades?symbol="                          
baseURL1 = "https://api.binance.us/api/v3/ticker?symbol="


class Art:
    def btc(symbol, price, id, qty, quoteQty, priceChangePercent, volume, count):
        art = f"""
  ▄▄█▀▀▀▀▀█▄▄         ⚛  Symbol:                   {symbol}
▄█▀──▄─▄────▀█▄       $  Price:                    {price}
█───▀█▀▀▀▀▄───█       ♦  ID:                       {id}
█────█▄▄▄▄▀───█       ⚡ Qty:                      {qty}
█────█────█───█       ♟  QuoteQty:                 {quoteQty}
▀█▄─▀▀█▀█▀──▄█▀       %  PriceChangePercent:       {priceChangePercent}
  ▀▀█▄▄▄▄▄█▀▀         ⬛ Volume:                   {volume}
        """
        
        print(art)
        
    def eth(symbol, price, id, qty, quoteQty, priceChangePercent, volume, count):
        art = f"""
       =.            ⚛  Symbol:                   {symbol}
     .=*#:           $  Price:                    {price}
    :==*##=          ♦  ID:                       {id}
   :===*###+         ⚡ Qty:                      {qty}
  -===+#%%##*        ♟  QuoteQty:                 {quoteQty}
 =+*###%@@%%%#.      %  PriceChangePercent:       {priceChangePercent}
:+#####%@@@@%*-      ⬛ Volume:                   {volume}
 :.:=*#%@#+::=.
  -=-..-:-+#+  
   .===+###-   
     -=*#*.    
      :+-      

        """
        print(art)

    def xmr(symbol, price, id, qty, quoteQty, priceChangePercent, volume, count):
        art = f"""
   :=+***+=:         ⚛  Symbol:                   {symbol}
 -+*********+-       $  Price:                    {price}
-*=.=*****=.=*-      ♦  ID:                       {id}
**=  .=*=.  =**      ⚡ Qty:                      {qty}
+*- +=. .=+ -*+      ♟  QuoteQty:                 {quoteQty}
 .::+#*+*#+::.       %  PriceChangePercent:       {priceChangePercent}
  -*#######*-        ⬛ Volume:                   {volume}

        """

        print(art)


    def doge(symbol, price, id, qty, quoteQty, priceChangePercent, volume, count):
        art = f"""
   -=+##*+=-         ⚛  Symbol:                   {symbol}
 -#*++++++*#*-       $  Price:                    {price}
=**:+=++==++**=      ♦  ID:                       {id}
#*-=*:::. .=**#      ⚡ Qty:                      {qty}
*#=-=-::..-.=**      ♟  QuoteQty:                 {quoteQty}
.*=-===-..-.=*.      %  PriceChangePercent:       {priceChangePercent}
  -=---::::=-        ⬛ Volume:                   {volume}

        """

        print(art)

    def ltc(symbol, price, id, qty, quoteQty, priceChangePercent, volume, count):
        art = f"""
   ..:::::..         ⚛  Symbol:                   {symbol}
 .:::::.:::::.       $  Price:                    {price}
.:::::  .:::::.      ♦  ID:                       {id}
:::::   .::::::      ⚡ Qty:                      {qty}
::::.  ...:::::      ♟  QuoteQty:                 {quoteQty}
 :::.......:::       %  PriceChangePercent:       {priceChangePercent}
  .:::::::::.        ⬛ Volume:                   {volume}

        """

        print(art)

    def other(symbol, price, id, qty, quoteQty, priceChangePercent, volume, count):
        art = f"""
      ██████████        ⚛  Symbol:                   {symbol}
    ██          ██      $  Price:                    {price}
  ██    ░░██░░░░░░██    ♦  ID:                       {id}
██    ░░██████░░░░░░██  ⚡ Qty:                      {qty}
██  ░░░░██░░░░░░░░░░██  ♟  QuoteQty:                 {quoteQty}
██  ░░░░░░██░░░░░░░░██  %  PriceChangePercent:       {priceChangePercent}
██  ░░░░░░░░██░░░░░░██  ⬛ Volume:                   {volume}
██  ░░░░██████░░░░░░██
  ██  ░░░░██░░░░░░██  
    ██░░░░░░░░░░██    
      ██████████      

        """

        print(art)




def getJson(url: str):
    rec = os.popen(f'curl --silent -X "GET" "{url}"').read()
    return json.loads(rec)
    



def retrieveData(crypto: str):
    #session = requests.Session()
    crypto = crypto.upper()
    cURL = baseURL + crypto
    cURL1 = baseURL1 + crypto
    #data = session.get(cURL, headers=headers)
    #data = data.json()
    data = getJson(cURL)
    try:
        if data["msg"] == "Invalid symbol.":
            print("Invalid Symbol")
            return False;
    except:
        pass
    data = data[0]
    price = data["price"]
    id = data["id"]
    qty = data["qty"]
    quoteQty = data["quoteQty"]

    #data = session.get(cURL1, headers=headers)
    #data = data.json()

    data = getJson(cURL1)

    priceChangePercent = data["priceChangePercent"]
    volume = data["volume"]
    count = data["count"]

    if str(crypto.upper()).startswith("BTC"):
        Art.btc(crypto, price, id, qty, quoteQty, priceChangePercent, volume, count)
    elif str(crypto.upper()).startswith("ETH"):
        Art.eth(crypto, price, id, qty, quoteQty, priceChangePercent, volume, count)
    elif str(crypto.upper()).startswith("XMR"):
        Art.xmr(crypto, price, id, qty, quoteQty, priceChangePercent, volume, count)
    elif str(crypto.upper()).startswith("DOGE"):
        Art.doge(crypto, price, id, qty, quoteQty, priceChangePercent, volume, count)
    elif str(crypto.upper()).startswith("LTC"):
        Art.ltc(crypto, price, id, qty, quoteQty, priceChangePercent, volume, count)
    else:
        Art.other(crypto, price, id, qty, quoteQty, priceChangePercent, volume, count)





   


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing Argument.\nUsage: cryptofetch CRYPTOSYMBOL")
        exit()
    retrieveData(sys.argv[1])
