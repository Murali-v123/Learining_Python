import time


def whileloop():
    i=0
    while(i<500):
        i=i+1

def forloop():
    for i in range(500):
        pass

init=time.time()
whileloop()
t1=time.time()-init
init=time.time()
forloop()
print(f"{time.time()-init:.8f}")
print(f"{t1:.8f}")
# print(time.time())
