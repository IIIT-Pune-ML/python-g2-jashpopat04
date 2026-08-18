import pandas as pd

df=pd.DataFrame({
    'ID':[101,102,103,101,104,102,105],
    'Name':['A','B','C','A','D','B','E'],
    'Age':[20,21,22,20,23,21,24],
    'Score':[80,75,90,85,88,75,92]
})

print("Duplicated IDs:")
print(df[df['ID'].duplicated(keep=False)]['ID'].unique())

print("\nDuplicate records:")
print(df[df['ID'].duplicated(keep=False)])

clean_df=df.loc[df.groupby('ID')['Score'].idxmax()]

clean_df=clean_df.sort_values('ID').reset_index(drop=True)

print("\nClean DataFrame:")
print(clean_df)

removed=len(df)-len(clean_df)

print("\nRecords removed:",removed)