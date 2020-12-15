import pandas as pd
import numpy as np
df = pd.read_csv('t1p.csv')
#print(df)

lis1 = [i for i in df['ln'].dropna()]
lis2 = [i for i in df['Labels'].dropna()]
#print(lis2)
n_d = dict()
for i, v in zip(lis1, lis2):
	n_d[i] = v

#print(n_d)

df['source'] = df['source'].replace(n_d)
df['target'] = df['target'].replace(n_d)
df.to_csv('cdf.csv', index = False)