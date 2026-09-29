names=["murali","rohith","gani","pradeep"]
cgpa=[8,9,7,8.5]
zipped=list(zip(names,cgpa))
# print(zipped)
for a,b in zipped:
    print(f"{a}:{b}")