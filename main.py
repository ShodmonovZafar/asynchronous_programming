import asyncio

async def hello(name, count=10, delay=0):
    for i in range(1, count + 1):
        print(f"Hello {name}! (x {i})")
        await asyncio.sleep(delay)

async def main():
    await asyncio.gather(hello("Alice"), hello("Bob"))

asyncio.run(main())
