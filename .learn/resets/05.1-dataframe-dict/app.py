import pandas as pd
data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porsche", "Cayenne", "White"]]
column_labels = ["Brand", "Model", "Color"]
df = pd.DataFrame(data, columns=column_labels)
print(df)
