# %%
import pandas as pd

# %%
df = pd.read_csv('metrics.csv', parse_dates=['time'])
#print(df.sample(10))

# %%
#print(df.groupby('name').describe())

# %%
#print(df['name'].value_counts())

# %%
pd.pivot(df, index='time', columns='name').plot(subplots=True)

# %%
#print(df.query('name == "cpu" & (value < 0 | value > 100)'))

# %% 
mem = df[df['name'] == 'mem']['value']
z_score = (mem - mem.mean())/mem.std()
bad_mem = mem[z_score.abs() > 2]
# bad_mem
print(df.loc[bad_mem.index])
