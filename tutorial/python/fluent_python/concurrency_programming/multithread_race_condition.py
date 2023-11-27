import threading

counter = 0

# Note: We see the counter reach 200 due to the GIL instead
# Race-Condition Threads overrite each others work
def increment_counter():
    global counter
    for _ in range(100):
        print(f"counter by {threading.current_thread().getName()} - {counter}")
        counter += 1

thread_a = threading.Thread(target=increment_counter)
thread_b = threading.Thread(target=increment_counter)

thread_a.start()
thread_b.start()


thread_a.join()
thread_b.join()
