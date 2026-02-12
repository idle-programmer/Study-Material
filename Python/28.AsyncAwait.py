"""
In Python, async and await let us write non-blocking code for I/O-heavy operations
like network calls, DB queries, or file operations, within a single thread of execution
They allow a program to efficiently manage multiple I/O-bound tasks by cooperatively switching
between tasks when one is waiting for an operation to complete, instead of blocking the entire program.
"""

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


# Difference between Async/Await, AsyncIO, and Threading

"""
| Feature               | **Async / Await**                          | **AsyncIO**                                  | **Threading**                     |
| --------------------- | ------------------------------------------ | -------------------------------------------- | --------------------------------- |
| **What it is**        | Syntax to write asynchronous code          | Python library for async programming         | Technique to run multiple threads |
| **Purpose**           | Makes async code readable and non-blocking | Manages event loop, tasks, coroutines        | Runs tasks in parallel threads    |
| **Level**             | Language feature (syntax)                  | Framework / library                          | OS-level concept                  |
| **Execution model**   | Single thread, cooperative multitasking    | Single thread with event loop                | Multiple threads                  |
| **Parallelism**       | ❌ No                                      | ❌ No                                        | ⚠️ Limited (due to GIL)           |
| **Concurrency**       | ✅ Yes                                     | ✅ Yes                                       | ✅ Yes                            |
| **Blocking behavior** | Non-blocking (when awaited)                | Non-blocking                                 | Can block other threads           |
| **Best for**          | Writing async code cleanly                 | High I/O operations (API calls, DB, sockets) | I/O tasks, background work        |
| **CPU-bound tasks**   | ❌ Poor                                    | ❌ Poor                                      | ❌ Poor (GIL issue)               |
| **I/O-bound tasks**   | ✅ Excellent                               | ✅ Excellent                                 | ✅ Good                           |
| **Uses GIL?**         | ✅ Yes                                     | ✅ Yes                                       | ✅ Yes                            |
| **Context switching** | Very fast (cooperative)                    | Very fast (event loop)                       | Slow (OS managed)                 |
| **Memory usage**      | Low                                        | Low                                          | High                              |
| **Complexity**        | Easy                                       | Medium                                       | Easy-Medium                       |
| **Example usage**     | `await fetch_data()`                       | `asyncio.gather()`                           | `threading.Thread()`              |
"""

# Difference between sleep and await
"""
sleep blocks the entire thread, while await pauses only the 
current coroutine and allows other async tasks to run.
"""

#What exactly is an Event Loop?
"""
An event loop is a mechanism that continuously checks for tasks, 
executes them, and switches between tasks when one is waiting, without blocking the thread.
In simple words:
It manages and runs async tasks efficiently on a single thread.
"""
