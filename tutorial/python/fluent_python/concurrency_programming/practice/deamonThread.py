from threading import Thread, current_thread

def thread_task():
    # Attempt to make the thread daemonic
    current_thread().setDaemon(True)
    while True:
        print("{0} executing".format(current_thread().getName()))

myThread = Thread(target=thread_task(),
                  name="childThread")

myThread.start()
myThread.join()