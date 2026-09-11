from minipandas import Dataframe

data = [
    ["Shivam", 20, 60],
    ["Rahul", 21, 55],
    ["Aman", None, 30],
    ["Raj", 22, 40],
    ["Vivek", 20, 22],
    ["Shivam", 21, 45],
]
columns = ["Name", "Age", "Weight"]

df = Dataframe(data, columns)

print("=== head() ===")
df.head()

print("\n=== info() ===")
df.info()

print("\n=== shape ===")
print(df.shape)

print("\n=== column selection: df['Age'] ===")
print(df["Age"])

print("\n=== multi-column selection: df[['Name', 'Weight']] ===")
print(df[["Name", "Weight"]])

print("\n=== boolean filtering: df[df['Age'] > 20] ===")
print(df[df["Age"] > 20])

print("\n=== sort_values('Age') ===")
print(df.sort_values("Age"))

print("\n=== drop('Age') ===")
print(df.drop("Age"))

print("\n=== groupby('Age').mean() ===")
print(df.groupby("Age").mean())

print("\n=== groupby('Age').sum() ===")
print(df.groupby("Age").sum())

print("\n=== groupby('Age').count() ===")
print(df.groupby("Age").count())
