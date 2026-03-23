# --- exp 4 ---

import os
from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing

# 创建子进程时，需要能够调用square函数，所以必须把square函数放在if __name__ == "__main__"之外，否则会报错：

def square(x):
    print(f"Square of {x} is {x * x}")
    return x * x

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")

    num_processes = os.cpu_count()

    with ProcessPoolExecutor(max_workers=num_processes) as pool:
        futures = [pool.submit(square, x) for x in range(num_processes)]
        results = [f.result() for f in as_completed(futures)]

    print(results)