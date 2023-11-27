from concurrent import futures
import threading
import time
import json

"""
Note: regardless the order of execution of the concurrent tasks, map() returns the values in the same order as 
the input
"""
def task(n):
    print("{}: sleeping {}".format(threading.current_thread().name, n))
    time.sleep(n/10)
    print("{}: done with {}".format(threading.current_thread().name, n))
    return n / 10

def createADummyFile(n):
    with open(f"/Users/riaz/Projects/InterviewPrepGuide/tutorial/python/fluent_python/concurrency_programming/data/{n}.json", "w") as fw:
        data = {
            "content": n
        }
        json.dump(data, fw)
    return f"Done Creating {n}.json"

ex = futures.ThreadPoolExecutor(max_workers=2)
print("main: starting")

results = ex.map(task, range(5,0,-1))

results2 = ex.map(createADummyFile, range(5,0,-1))

print("main: unprocessed results {}".format(results))
print("main: waiting for real results")

real_results = list(results)
real_results2 = list(results2)

print("main: results: {}".format(real_results))

print("main: results2: {}".format(real_results2))

    

    