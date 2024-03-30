import time
from multiprocessing import Pool

from hw4.task1.lib import fib, arg

if __name__ == '__main__':
    start = time.time()

    with Pool(processes=10) as executor:
        args = [arg] * 10
        executor.map(fib, args)

    elapsed = time.time() - start

    print("Processes")
    print(f'Time: {elapsed}s')
