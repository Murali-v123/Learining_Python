import os

# to create folder
os.mkdir("oslbry/data")

# to create folders in folder
for i in range(1,10):
    os.mkdir(f"oslbry/data/tutorial{i+1}")

for i in range(1,10):
    os.rename(f"oslbry/data/tutorial{i+1}",f"oslbry/data/tutorial{i}")

