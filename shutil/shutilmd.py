import shutil

# sp=r"C:\Users\HP\Desktop\Python-learning\shutil\shutilmd.py"
# dp=r"C:\Users\HP\Desktop\Python-learning\shutil\new.py"
# shutil.copy(sp,dp)
# shutil.copy2(sp,dp)

sp=r"C:\Users\HP\Desktop\Python-learning\shutil\sht"
dp=r"C:\Users\HP\Desktop\Python-learning\shutil\newfolder"
shutil.copytree(sp,dp)


# sp=r"C:\Users\HP\Desktop\Python-learning\shutil\new.txt"
# dp=r"C:\Users\HP\Desktop\Python-learning\shutil\sht\new.txt"
# shutil.move(sp,dp)


# shutil.copy2(src,dst)
# shutil.copytree(src,dst) copies the directries content as it is

# sp=r"C:\Users\HP\Desktop\Python-learning\shutil\new.txt"
# dp=r"C:\Users\HP\Desktop\Python-learning\shutil\newfolder"
# shutil.rmtree(dp)

# import os
# os.remove(r"C:\Users\HP\Desktop\Python-learning\shutil\sht\new.txt")
