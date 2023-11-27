import threading
import time

def print_number():
    for i in range(10):
        print(f"Thread A: {i}")
        time.sleep(1)

def print_letters():
    for letter in "abcdefghi":
        print(f"Thread B: {letter}")
        time.sleep(1)

thread_a = threading.Thread(target=print_number)
thread_b = threading.Thread(target=print_letters)

thread_a.start()
thread_b.start()

thread_a.join()
thread_b.join()

print("All threads finished executing")