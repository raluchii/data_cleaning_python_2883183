# %%
import pandas as pd

# %%
df = pd.read_csv('cart.csv', parse_dates=['date'])
print(df)
print(df.dtypes)
# %%
#print(df['amount'].astype('Int32'))

# %%
#print(df.isnull())

# %%
print(df.isnull().any(axis=1))
