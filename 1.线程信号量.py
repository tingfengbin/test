import threading
import time


def myThread(name):
    with sep:
        for i in range(100):
            # time.sleep(1)
            print(name,str(i),threading.current_thread().name)


sep = threading.Semaphore(4)
threadlist = []
for name in ["a","b","c","d","e"]:
    mythd = threading.Thread(target=myThread,args=(name,))
    mythd.start()
    threadlist.append(mythd)
for thread in threadlist:
    thread.join()