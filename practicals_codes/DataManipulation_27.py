import pandas as pd

data=pd.read_csv("sample.csv")

print(data.head())

subset=data[data["Age"]>30]
print("--------------------------------------------------")
print(subset)
print("--------------------------------------------------")
grouped_data=data.groupby("Gender").mean()

print(grouped_data)

print("--------------------------------------------------")
new_data = {"Name": "Tom", "Age": 28, "Gender": "Male", "Height": 175, "Weight": 70}

data=data.append(new_data,ignore_index=True)

data.to_csv("sample.csv",index=False)

print(data)