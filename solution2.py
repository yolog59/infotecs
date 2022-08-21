import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data = pd.read_csv('data.csv', sep = ';')

#обучающая выборка
x = pd.DataFrame(np.c_[data['Тактовая частота ЦП, ГГц'], 
                       data['UDP Throughput, Мбит/с']],
                       columns = ['Тактовая частота ЦП, ГГц', 'UDP Throughput, Мбит/с']) 

util = data['Утилизация ЦП, %']

# данные для предсказания
test = pd.DataFrame({'Тактовая частота ЦП, ГГц': [1700] * 10, 'UDP Throughput, Мбит/с': range(50, 501, 50)})

# линейная регрессия для утилизации
util_reg = LinearRegression().fit(x, util)
util_result = util_reg.predict(test).round(1)

# линейная регрессия для температуры
temp = data['Температура ЦП, °С']
util_reg = LinearRegression().fit(x, temp)
temp_result = util_reg.predict(test).round(1)

# получившиеся результаты, пишем в csv
result = pd.DataFrame({'№': range(1, 11), 'UDP Throughput, Мбит/с': range(50, 501, 50), 'Утилизация ЦП, %': util_result, 'Температура ЦП, °С': temp_result})
print(result)
result.to_csv('result.csv', sep = ';', encoding = 'utf-8')




