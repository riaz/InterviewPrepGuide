from threading import Lock, RLock

l = Lock()

# this will cause a deadlock
#l.acquire()
#l.acquire()
#print("Exiting main")


r = RLock()
# this will cause a deadlock
r.acquire()
r.acquire()
print("Exiting main") # this will not cause a deadlock