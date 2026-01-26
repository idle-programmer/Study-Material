import threading
import time

def runTask(name, duration):
    print(f"Task {name} starts")
    time.sleep(duration)
    print(f"Task {name} ends")

t1= threading.Thread(target=runTask, args=("A",4))
t2= threading.Thread(target=runTask, args=("B",4))

# Start both threads
t1.start()
t2.start()

# Wait for both to finish
t1.join()
t2.join()

print("Main thread done!")


"""
In Python, threading is used to run multiple functions concurrently,
especially for I/O-bound work like downloading files or making API calls.
A thread is the smallest unit of execution inside a process.
"""




# How do u handle concurrency issue in python
