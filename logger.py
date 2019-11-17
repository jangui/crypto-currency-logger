from coinmarketcap import Market
import os, time

cmc = Market()
market = cmc.ticker()

data = market['data']
error = market['metadata']['error']
timestamp = market['metadata']['timestamp']

print("Error: %s | Timestamp: %d" % (error, timestamp))


for coin_dict in data.values():
    name = coin_dict['name']
    rank = coin_dict['rank']
    price = coin_dict['quotes']['USD']['price']
    last_updated = coin_dict['last_updated']
    coin_dict['prevlast_update'] = last_updated

    directory = 'data/' + str(name)
    filename = directory + '/' + str(name) + '.csv'

    if not os.path.exists(directory):
        os.makedirs(directory)

        with open(filename, 'w') as f:
            f.write('rank,price,last_updated\n') #add relevant timestamp
            f.write(str(rank)+','+str(price)+','+str(last_updated)+'\n')

        filename = directory + '/' + 'last_updated' + '.txt'
        with open(filename, 'w') as f:
            f.write(str(last_updated))


active = True
while active:
    time.sleep(45)

    market = cmc.ticker()
    data = market['data']
    error = market['metadata']['error']
    timestamp = market['metadata']['timestamp']

    print("Error: %s | Timestamp: %d" % (error, timestamp))

    for coin_dict in data.values():
        name = coin_dict['name']
        rank = coin_dict['rank']
        price = coin_dict['quotes']['USD']['price']
        last_updated = coin_dict['last_updated']

        directory = 'data/' + str(name)

        filename = directory + '/' + 'last_updated' + '.txt'
        with open(filename, 'r') as f:
            prev_updated = f.read()

        if prev_updated != str(last_updated):
            filename = directory + '/' + str(name) + '.csv'
            with open(filename, 'a') as f:
                f.write(str(rank)+','+str(price)+','+str(last_updated)+'\n')

            filename = directory + '/' + 'last_updated' + '.txt'
            with open(filename, 'w') as f:
                f.write(str(last_updated))
