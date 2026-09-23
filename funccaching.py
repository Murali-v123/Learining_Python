from functools import lru_cache
import time

@lru_cache(maxsize=None) #another way is to remove the @lru_cache fun
def fun(n):
    time.sleep(1)
    print("Hey hi the value is:",n*2)

fun(3)
fun(7)
fun(3)
fun(4)
print("Hey bhaii wassup rey")
# fun.cache_clear() to clear the cache and againg these statements are executed
fun(3)
fun(7)
fun(3)
fun(41)