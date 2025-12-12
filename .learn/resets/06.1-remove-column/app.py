import pandas as pd
file_path = ".learn/assets/us_baby_names_right.csv"
df_babynames = pd.read_csv(file_path)
df_babynames.drop('Unnamed: 0', axis=1, inplace=True)
print(df_babynames.head())