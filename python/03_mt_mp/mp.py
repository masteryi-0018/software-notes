import os
from multiprocessing import Process

def square(x):
    print(f"Square of {x} is {x * x}")
    return x * x

processes = []
num_processes  = os.cpu_count()

for x in range(num_processes ):
    p = Process(target=square, args=(x,))
    p.start()
    processes.append(p)

for p in processes:
    p.join()

# --- exp 2 ---

# 子进程不影响主进程的counter变量，counter的值永远是0

# import time


counter = 0

def work():
    global counter
    for _ in range(1000):
        tmp = counter          # 1. 读
        # time.sleep(0.00001)    # 进程切换没意义
        counter = tmp + 1      # 2. 写
    print("process counter:", counter)

processes = []
num_processes  = os.cpu_count()

for x in range(num_processes ):
    p = Process(target=work)
    p.start()
    processes.append(p)

for p in processes:
    p.join()

print("process result:", counter)

# --- exp 3 ---

from concurrent.futures import ProcessPoolExecutor, as_completed

num_threads = os.cpu_count()

with ProcessPoolExecutor(max_workers=num_processes) as pool:
    futures = [pool.submit(square, x) for x in range(num_processes)]
    results = [f.result() for f in as_completed(futures)]

print(results)
