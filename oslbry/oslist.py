import os

folders=os.listdir("oslbry/data")

for folder in folders:
    print(folder)
    print(os.listdir(f"oslbry/data/{folder}"))

os.getpid()

os.getcwd()