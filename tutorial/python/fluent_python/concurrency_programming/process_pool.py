#futures_process_pool_map.py
"""
The ProcessPoolExecutor works in the same way as ThreadPoolExecutor, 
but uses processes instead of threads. This allows CPU-intensive operations to use a 
separate CPU and not be blocked by the CPython interpreter’s global interpreter lock.
"""

from concurrent import futures
import os


def task(n):
    return (n, os.getpid())


ex = futures.ProcessPoolExecutor(max_workers=2)
results = ex.map(task, range(5, 0, -1))
for n, pid in results:
    print('ran task {} in process {}'.format(n, pid))