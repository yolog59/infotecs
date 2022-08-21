import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# читаем данные
data = pd.read_csv('data.csv', sep = ';')

# тестовая выборка
x = pd.DataFrame(np.c_[data['Тактовая частота ЦП, ГГц'], 
                       data['Утилизация ЦП, %'],
                       data['Температура ЦП, °С']], 
                       columns = ['Тактовая частота ЦП, ГГц', 'Утилизация ЦП, %', 'Температура ЦП, °С'])
                       
y = data['UDP Throughput, Мбит/с']

# линейная регрессия
lin_reg = LinearRegression()
lin_reg.fit(x, y)

# предсказание для предоставленных значений
x_test = pd.DataFrame({'Тактовая частота ЦП, ГГц': [2000], 'Утилизация ЦП, %' : [40], 'Температура ЦП, °С': [54]})
print(lin_reg.predict(x_test))