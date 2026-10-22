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
df2=df2.fillna(0)
df2.to_csv("Example_Saved_csv_file.csv")
df2.groupby("name")["cgpa"].max()
df2.groupby("name")["cgpa"].min()
df2.groupby("name")["cgpa"].mean()
df2.groupby("name")["cgpa"].agg(["mean","min","max"])
df2.sort_values("cgpa",ascending=False)
df2.sort_index()
df2.groupby("name").agg(
    maxcgpa=("cgpa","max")
)

# plotting
df["cgpa"].hist()
df.plot(kind="scatter",x="cgpa",y="name")

# merging and joining
df_customer=pd.DataFrame({
    "customer_id":[1,2,3],
    "name":["Murali","pradeep","rohith"]
})

df_orders=pd.DataFrame({
    "order_id":[10,12,13],
    "customer_id":[2,1,4],
    "amount":[100,200,102]
})

pd.merge(df_customer,df_orders)
pd.merge(df_customer,df_orders,on="customer_id")
pd.merge(df_customer,df_orders,on="customer_id",how="left")
pd.merge(df_customer,df_orders,on="customer_id",how="right")
pd.merge(df_customer,df_orders,on="customer_id",how="outer")

# data frame concateation
df1=pd.DataFrame({
    "customer_id":[1,2,3],
    "name":["Murali","pradeep","rohith"]
})

df2=pd.DataFrame({
    "customer_id":[4,15,6],
    "name":["yashwanth","gani","aparanji"]
})
pd.concat([df1,df2],ignore_index=True) #row wise concatenation
pd.concat([df1,df2],axis=1) #col wise concatenation
s = pd.Series([1, 2, 3, 4, 5])
s[0] = 100
print(s)
changed_s = s.drop(1)
print(changed_s)
print(s)