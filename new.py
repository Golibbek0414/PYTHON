import threading
import time as t
def print_cube(num):
    for i in range(5):
        print(i,t.sleep(1))
        print("Cube: {}".format(num*num*num))

def print_square(num):
    for i in range(5):
        print(i,t.sleep(1))
        print("Square: {}".format(num*num))

if __name__=="__main__":
    # creating thread
    t1=threading.Thread(target=print_square,args=(2,))
    t2=threading.Thread(target=print_cube,args=(3,))
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
    # both threads completely executed
    print("Done!")