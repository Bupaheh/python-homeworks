import time
from threading import Thread

from hw4.task1.lib import fib, arg

if __name__ == '__main__':
    start = time.time()
    threads = []

    for i in range(10):
        t = Thread(target=fib, args=(arg,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    elapsed = time.time() - start

    print("Threads")
    print(f'Time: {elapsed}s')