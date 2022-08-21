import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('result.csv', sep = ';')
numbers = range(1, 11)

fig, axs = plt.subplots(3, 1, gridspec_kw={'height_ratios': [1, 1, 1]})

axs[0].set_xlabel('№')
axs[0].set_ylabel('UDP Throughput, Мбит/с')
axs[1].set_xlabel('№')
axs[1].set_ylabel('Утилизация ЦП, %')
axs[2].set_xlabel('№')
axs[2].set_ylabel('Температура ЦП, °С')

axs[0].plot(numbers, data['UDP Throughput, Мбит/с'])
axs[0].scatter(numbers, data['UDP Throughput, Мбит/с'], c = 'red')
axs[1].plot(numbers, data['Утилизация ЦП, %'])
axs[1].scatter(numbers, data['Утилизация ЦП, %'], c = 'red')
axs[2].plot(numbers, data['Температура ЦП, °С'])
axs[2].scatter(numbers, data['Температура ЦП, °С'], c = 'red')

fig.tight_layout()

plt.show()
