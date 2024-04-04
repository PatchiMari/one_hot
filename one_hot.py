import pandas as pd 
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

dt_one_hot = data.apply(lambda y: y.astype('category').cat.codes)
dt_one_hot = pd.concat([dt_one_hot, 1 - dt_one_hot], axis=1)
dt_one_hot.columns = ['human', 'robot']

dt_one_hot.head()
