import pandas as pd
     

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame().assign(robot=False, human=False)
def check_value(row):
    if row['whoAmI'] == 'robot':
        row['robot'] = True
    elif row['whoAmI'] == 'human':
        row['human'] = True
    return row
data = data.assign(whoAmI=lst).apply(check_value, axis=1)
print(data.head())
     



data = data.drop(columns=['whoAmI'])
print(data.head())
     