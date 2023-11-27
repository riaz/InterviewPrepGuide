from threading import Lock

lock = Lock()
lock.acquire()
lock.release()
lock.release()