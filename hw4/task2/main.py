import math
import time
import logging
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

logger = logging.getLogger(__name__)


def integrate(task_name, f, a, b, n_iter=1000):
    logger.info(f'{task_name} integrate start')
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    logger.info(f'{task_name} integrate end')
    return acc


def calc(executor_constructor, name, f, a, b, n_jobs=1, n_iter=1000):
    calc_name = f'{name}_{n_jobs}'
    logger.info(f"{calc_name} calc start")

    res = 0
    step = (b - a) / n_jobs
    inner_iter = n_iter // n_jobs

    with executor_constructor(max_workers=n_jobs) as executor:
        futures = []
        for i in range(n_jobs):
            task_name = f'{calc_name}_{i}'
            start = a + step * i
            end = start + step
            future = executor.submit(integrate, task_name, f, start, end, inner_iter)
            futures.append(future)

        for future in futures:
            res += future.result()

    logger.info(f"{calc_name} calc end")
    return res


def run(executor_name, executor_constructor, f, a, b, n_jobs_list, n_iter):
    for n_jobs in n_jobs_list:
        start = time.time()
        calc(executor_constructor, executor_name, f, a, b, n_jobs=n_jobs, n_iter=n_iter)
        elapsed = time.time() - start

        print(f'{executor_name}; n_jobs: {n_jobs}; Time: {elapsed}')


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                        filename='log.log', level=logging.INFO)

    cpu_num = 4
    n_iter = 50000000
    n_jobs_list = range(1, cpu_num * 2 + 1)

    thread_constructor = ThreadPoolExecutor
    process_constructor = ProcessPoolExecutor

    run("Processes", process_constructor, math.cos, 0, math.pi / 2, n_jobs_list, n_iter)
    run("Threads", thread_constructor, math.cos, 0, math.pi / 2, n_jobs_list, n_iter)

