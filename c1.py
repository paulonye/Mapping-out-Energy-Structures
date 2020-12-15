import pandas as pd
df = pd.read_excel('pra.xlsx')

df['color'] = df['color'].str.split("'").str[1]
print(df['color'])
df.to_excel('pr.xlsx')
#help(str.strip)