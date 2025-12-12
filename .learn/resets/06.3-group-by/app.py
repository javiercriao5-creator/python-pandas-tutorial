import pandas as pd
file_path = ".learn/assets/us_baby_names_right.csv"
df_babynames = pd.read_csv(file_path)
if 'Unnamed: 0' in df_babynames.columns:
    del df_babynames['Unnamed: 0']
grouped_names = df_babynames.groupby('Name')
number_of_different_names = len(grouped_names)
print(number_of_different_names)