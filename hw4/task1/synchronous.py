import time

from hw4.task1.lib import fib, arg

if __name__ == '__main__':
    start = time.time()

    for i in range(10):
        fib(arg)

    elapsed = time.time() - start

    print("Synchronous")
    print(f'Time: {elapsed}s')
