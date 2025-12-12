import pandas as pd
file_path = ".learn/assets/us_baby_names_right.csv"
data = pd.read_csv(file_path)
names = data.groupby("Name")
names_sum = names.sum()
print(len(names_sum))