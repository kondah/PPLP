import thread
import time


def worker(id):

    print "Thread avec l'id %d est active " %id
    count = 1
    while 1:
        print "Thread dont l'id %d a au niveau de son compteur %d "%(id, count)
        time.sleep(2)
        count += 1

for i in range(5):
 thread.start_new_thread(worker,(i,))

while True :
    pass