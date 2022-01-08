# %%
import pandas as pd

csv_file = '2021-06.csv'

df = pd.read_csv(csv_file)
print(df)
# %%
df['date'] = csv_file[:-len('.csv')]
df

# %%
times = df['time'].str.split('-', expand=True)
times.columns = ['start', 'end']
times
# %%
df = pd.concat([df, times], axis=1)
df

# %%
df['start'] = pd.to_datetime(
    df['date'].str.cat(df['start'], sep='T')
)
df['end'] = pd.to_datetime(
    df['date'].str.cat(df['end'], sep='T')
)
print(df)

# %%
(df['end'] - df['start']).sum()
