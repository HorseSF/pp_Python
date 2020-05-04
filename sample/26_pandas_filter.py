import pandas as pd

data=pd.Series([30,15,20])
condition=data>18
filterData=data[condition]
print(filterData)

data=pd.Series(["您好","Python","Pandas"])
condition=data.str.contains("P")
filterData=data[condition]
print(filterData)

data=pd.DataFrame({
    "name":["Amy","Bob","Charles"],
    "salary":[30000,50000,40000]
})
condition=data["name"]=="Amy"
filterData=data[condition]
print(filterData)