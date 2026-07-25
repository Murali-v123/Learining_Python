details={"name":"murali","age":20,"place":"details"}

for val in details.items():
    print(val)
print(details)

details["trip"]="kannur"
print(details)

del details["age"]
print(details)

details.pop("trip")
print(details)

details.update({"age":21})
print(details)

details.items()

details.keys()

details.get("name","not found")
details.values()