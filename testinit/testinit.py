import p1 as p1
import p2 as p2
import threading
import _thread
import random

a = p1.class1
b = p2.class2


#t0 = threading.Thread(target = p1.class1.class1.getclassname(),name='t0')
#t1 = threading.Thread(target =
#p2.class2.class2(p1.class1.class1.x).getclassname(),name='t1')
#t0.start()
#t1.start()

class t1(threading.Thread):

    def __init__(self, **kwargs):
        return super().__init__(**kwargs)

    def run(self):
        for i in range(9):
            print('t1')

class t2(threading.Thread):

    def __init__(self, **kwargs):
        return super().__init__(**kwargs)

    def run(self):
        for i in range(9):
            print('t2')


c1 = t1()
c2 = t2()


c1.start()
c2.start()





