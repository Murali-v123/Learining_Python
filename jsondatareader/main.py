import json

# for reading data
# with open("data.json","r") as f:
#     data=json.load(f)
#     print(data)

# for writing data to json file
data={
    "name":"murali",
    "lang":["Telugu","kannda","hindi"],
    "age":19
}

with open("data.json","w") as f:
    json.dump(data,f,indent=4,sort_keys=True)
    