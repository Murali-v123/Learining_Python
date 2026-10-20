import numpy as np
import pandas as pd

arr=np.array([1,2,3,4,5])

info={
    "Name":["Murali","Pradeep","rohith"],
    "cgpa":[8,8.5,9]
}
s=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
df=pd.DataFrame(info)
df=pd.DataFrame([["murali v",8],["pradeep",8.5],["gani"],["rohith",9]],columns=["name","cgpa"])
df
type(df)
s
s.index
print(df)

# df fun
df.head()
df.tail()
df.info()
df.shape
df.columns
df.describe()
df.nunique()
df.sample(2)

df.query("cgpa>8")[['name',"cgpa"]]
df.isnull().sum()
df.isnull()
df.isna()
df.dropna() #row drop
df.dropna(axis=1) #column drop
df.fillna(10)
df.ffill()
df.bfill()

df['cgpa'].duplicated()
df2=df.copy()
df2=df.drop_duplicates(subset=['cgpa'])
df2
df.dtypes
df['cgpa'].astype("int")
df["name"].str.capitalize()
df["name"].str.lower()
df["name"].str.upper()
df["name"].str.strip()
df["name"].str.split(" ")
df["name"].str.contains("a",case=False)

df2=df.copy()
df2.columns
df2.isna()
df.fillna(0)
df2.to_csv("Example_Saved_csv_file.csv")