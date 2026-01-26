import asyncio

async def fetch(user_id):
    print(f"Fetching user {user_id}")
    await asyncio.sleep(3)
    return {"id": user_id, "name":f"User-{user_id}"}

async def main():
    user1= await fetch(1)
    user2= await fetch(2)
    print(f"Fetched: {user1}, {user2}")


# asyncio.run(main())

async def mainConcurrent():
    results= await asyncio.gather(
        fetch(1),
        fetch(2)
    )
    print(f"All: {results}")

asyncio.run(mainConcurrent())

"""
In Python, async and await let us write non-blocking code for I/O-heavy operations
like network calls, DB queries, or file operations, within a single thread of execution
They allow a program to efficiently manage multiple I/O-bound tasks by cooperatively switching
between tasks when one is waiting for an operation to complete, instead of blocking the entire program.
"""