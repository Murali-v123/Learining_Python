import asyncio
import time

async def function():
    print("hello")
    time.sleep(1)


async def function1():
    print("hello")
    time.sleep(2)

async def function2():
    print("hello")

async def main():
    await function()
    await function1()
    await function2()

# await main()
asyncio.run(main())