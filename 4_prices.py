prices = ['26.30€', '62.11€', '31.35€']

prices_discounted = []

for price in prices:

    price_discounted = round(float(price.replace('€', '')) * 0.8, 2)
    prices_discounted.append(str(price_discounted)+'€')

print(prices_discounted)