#  Работать с файлом california_housing_train.csv, который находится в папке sample_data. 

import pandas as pd
df = pd.read_csv('sample_data/california_housing_train.csv')

df.head(n=10)

df.describe()

# Задача 40 Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).

df.median_house_value[(df['population'] < 500)].agg(['mean'])

# Задача 42: Узнать какая максимальная households в зоне минимального значения population.

df.households[df['population'] == df['population'].min()].agg(['max'])




