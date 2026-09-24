import threading
import time 
from concurrent.futures import ThreadPoolExecutor

def fun(sec):
    time.sleep(sec)
    print(f"the time taken is {sec}")
    return sec
# def fun(sec):
#     time.sleep(sec)
#     print(f"the time taken was {sec}")

# def fun(sec):
#     time.sleep(sec)
#     print(f"the time taken is {sec}")
# time1=time.perf_counter()
# fun(4)
# fun(3)
# fun(2)
# time2=time.perf_counter()
# print(time2-time1)

def main():
    time1=time.perf_counter()
    # t1 = threading.Thread(target=fun ,  args=[4])
    # t2 = threading.Thread(target=fun ,  args=[2])
    # t3 = threading.Thread(target=fun ,  args=[1])
    # t1.start()
    # t2.start()
    # t3.start()

    # t1.join()
    # t2.join()
    # t3.join()
    time2=time.perf_counter()
    print(time2-time1)

def poolDemo():
    with ThreadPoolExecutor() as execute:
        # future1 = execute.submit(fun ,3)
        # future2 = execute.submit(fun ,2)
        # future3 = execute.submit(fun ,4)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())
        l= [2,3,5,1]
        results =execute.map(fun,l)
        for result in results:
            print(result)

poolDemo()
