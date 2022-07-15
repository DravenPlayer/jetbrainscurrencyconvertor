import json
import requests
#conicoin = float(input())

'''for currency_have in exchange_rate:
    
    conicoin_exchanged = conicoin * exchange_rate[currency_have]
    print(f'I will get {conicoin_exchanged} {currency_have} from the sale of {conicoin} conicoins.')
'''
cache = {}
currency_have = input().lower()
exchange_rate = json.loads(requests.get("http://www.floatrates.com/daily/" + currency_have + ".json").text)

if 'eur' in exchange_rate:
    cache['eur'] = exchange_rate.get('eur').get('rate')
if 'usd' in exchange_rate:
    cache['usd'] = exchange_rate.get('usd').get('rate')
while True:
    if len(currency_have) ==0:
        break


    currency_exchange = input().lower()
    if len(currency_exchange) ==0:
        break
    amount = float(input())
    print("Checking the cache...")
    if currency_exchange in cache :
        print("Oh! It is in the cache!")
        print(f"You received {round(amount * cache[currency_exchange], 2)} {currency_exchange.upper()}.")
    else:
        print("Sorry,but it is not in the cache!")
        cache[currency_exchange] = json.loads(requests.get("http://www.floatrates.com/daily/" + currency_exchange + ".json").text)[currency_have].get('inverseRate')

        print(f"You received {round(amount * cache[currency_exchange],2)} {currency_exchange.upper()}.")

