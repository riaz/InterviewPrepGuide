import time
from threading import Lock, Condition, Thread
from threading import current_thread

flag = False

lock = Lock()
cond_var = Condition(lock)


def child_task():
    global flag
    name = current_thread().getName()

    cond_var.acquire()
    while not flag:
        cond_var.wait()
        print("\n{0} woken up \n".format(name))

    print("\n{0} exiting\n".format(name))


if __name__ == "__main__":
    thread1 = Thread(target=child_task, name="thread1")
    thread1.start()
    
    # give the child task to wait on the condition variable
    time.sleep(1)

    cond_var.acquire()
    flag = True
    cond_var.notify_all()
    cond_var.release()

    thread1.join()
    print("main thread exits")