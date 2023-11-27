import asyncio

async def greet(message, delay):
    await asyncio.sleep(delay)
    print(f"Hello, {message}")

async def main():
    # this is a event loop that manages many tasks and switches context as needed.
    # Event loops are implemeneted using co-routines which are generalization of generators, allowing to write
    # non-blocking async code
    task_1 = asyncio.create_task(greet("Alice", 2))
    task_2 = asyncio.create_task(greet("Tom", 1))

    asyncio.gather((task_1, task_2))


if __name__ == '__main__':
    asyncio.run(main()) # running the main co-routine / event loop