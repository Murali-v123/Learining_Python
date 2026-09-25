# import multiprocessing
import concurrent
from concurrent.futures import ProcessPoolExecutor

import requests


def down(url,name):
    print(f"file down{name}")
    response=requests.get(url)
    open(f"files/{name}.jpg",'wb').write(response.content)
    print(f"file down{name} finished")

if __name__=='__main__':
    url="https://picsum.photos/500/1000"

    # pros=[] #to maintain process linking 

    # for i in range(5):
    #     # down(url,i)
    #     p =multiprocessing.Process(target=down,args=[url,i])
    #     p.start()
    #     pros.append(p)

# if we add this piece of code the process will run in a such a wya tht file down1
# file down0
# file down2
# file down4
# file down3
# file down1 finished
# file down0 finished
# file down2 finished
# file down4 finished one after other it maintains the order other wise it doesn't maintain order
    
    # Main script resumes and safely closes the program
    # Main script stops and waits at the join() line.
    # for p in pros:
    #     p.join()

# using processpoolexecuter
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # l1=[url for i in range(5)]
        # l2=[i for i in range(5)]
        # result=executor.map(down,l1,l2)
        executor.map(down,[url]*5,range(5))
    # for i in result:
    #     print(i)
