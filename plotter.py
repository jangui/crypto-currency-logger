import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("coin")
args = parser.parse_args()

price = []
time = []
name = args.coin

directory = 'data/' + name
filename = directory + '/' + name + '.csv'
with open(filename, 'r') as f:
    f.readline()
    for line in f:
        data = line.strip().split(',')
        price.append(float(data[1]))
        time.append(float(data[2]))


plt.plot(time, price, color='k')
plt.xlabel('time')
plt.ylabel('price (usd)')
plt.title(name)
plt.show()
