import os
import threading

# --- exp 1 ---

def square(x):
    print(f"Square of {x} is {x * x}")
    return x * x

threads = []
num_threads = os.cpu_count()

for x in range(num_threads):
    t = threading.Thread(target=square, args=(x,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

# --- exp 2 ---

# 如果不加time.sleep(0.00001)，线程执行太快，没有切换，就会得到正确的结果

import time
# lock = threading.Lock()

counter = 0

def work():
    global counter
    for _ in range(1000):
        # with lock:
        tmp = counter          # 1. 读
        time.sleep(0.00001)    # 👈 强制线程切换（关键！）
        counter = tmp + 1      # 2. 写
    print("thread counter:", counter)

threads = []
num_threads = os.cpu_count()

for x in range(num_threads):
    t = threading.Thread(target=work)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("thread result:", counter)

# --- exp 3 ---

from concurrent.futures import ThreadPoolExecutor, as_completed

num_threads = os.cpu_count()

with ThreadPoolExecutor(max_workers=num_threads) as pool:
    futures = [pool.submit(square, x) for x in range(num_threads)]
    results = [f.result() for f in as_completed(futures)]

print(results)