import pandas as pd

df=pd.DataFrame({
    'Date':['2026-01-01','2026-01-02','2026-01-04','2026-01-05','2026-01-08','2026-01-09'],
    'Sales':[100,120,150,130,180,200]
})

df['Date']=pd.to_datetime(df['Date'])
df=df.set_index('Date')

full_dates=pd.date_range(df.index.min(),df.index.max())
missing_dates=full_dates.difference(df.index)

print("Missing dates:")
print(missing_dates)

df=df.reindex(full_dates)

print("\nDataFrame after reindexing:")
print(df)

df['Rolling_Average']=df['Sales'].rolling(3).mean()

print("\nDataFrame with rolling average:")
print(df)

max_date=df['Rolling_Average'].idxmax()

print("\nDate with maximum rolling average:")
print(max_date)