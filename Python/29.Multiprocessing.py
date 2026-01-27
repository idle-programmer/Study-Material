"""
In Python, multiprocessing lets me run CPU-heavy work in parallel by creating separate processes, 
each with its own Python interpreter. This avoids the GIL, so it’s perfect for heavy math, 
image/video processing, ML, or batch jobs.
"""
import multiprocessing as mp
import time

def calc_square(n):
    time.sleep(3)  # Simulate CPU-heavy work
    print(f"Square of {n} = {n**2}")


if __name__ == '__main__':
    p1 = mp.Process(target=calc_square, args=(2,))
    p2 = mp.Process(target=calc_square, args=(3,))
    p3 = mp.Process(target=calc_square, args=(4,))

    # Start them
    p1.start()
    p2.start()
    p3.start()

    # Wait for all to finish (important!)
    p1.join()
    p2.join()
    p3.join()

    print("Main program done!")