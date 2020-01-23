from queue import Queue
import time

q = Queue()

for i in range(0,1000):
    tstart = time.time()
    for i in range(0,10):
        q.enqueue(i)
    tslut = time.time()
    delta = tslut - tstart
    for i in range(0,9):
        print(q.dequeue())
    print('tid: {}'.format(delta))
