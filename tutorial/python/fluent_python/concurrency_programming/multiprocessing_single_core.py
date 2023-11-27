"""
Multiprocessing moule uses subprocess for true parallel execution on mutilple CPUs.
Each subprocess has its memory space, inter-process communication involving serialization and de-serialization

https://medium.com/@Sabrina-Carpenter/python-concurrency-and-parallelism-the-guide-you-need-33661a767db0
"""

import multiprocessing

def square_numbers(numbers, result):
    for idx, num in enumerate(numbers):
        print(multiprocessing.current_process()) 
        result[idx] = num *  num

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    # Note: result is a shared array
    result = multiprocessing.Array('i', len(numbers))
    process = multiprocessing.Process(target=square_numbers, args=(numbers, result))

    process.start()
    process.join()
    print(f"Squared Numbers: {list(result)}")