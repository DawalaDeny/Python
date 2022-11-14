import numpy as np
def oef1():
    pass
def oef2():
    pass
def oef3():
    def eenheidsmatrix(n: int):
        nparray = np.zeros((n, n))
        for i in range(n):
            nparray[i, i] = 1
        print(nparray)
    eenheidsmatrix(3)

def oef5():
       def venster(n=5):
           arrayy = np.ones((n,n))
           #eerste 1:-1 zijn de rijen, tweede 1:-1 't binnen van de rijen
           arrayy[1: -1, 1: -1]  = 0
           return arrayy
       print(venster())

if __name__ == '__main__':
   #oef3()
   #oef5()
   pass