# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 15:57:42 2015

@author: Moseph
"""

#def rolling()

#from numpy import roll, zeros, float32
#from random import randrange
#from time import time, sleep
#
#a=zeros(10001, dtype=float32)
#
#start = time()
#
#while a[0] == 0:
#    #start1 = time()
#    a[-1] = randrange(1, 10, 1)
#    a = roll(a,-1)
#    #end1 = time()
#    #print end1 - start1, #a
#    #print a
#    
#end = time()
#print end - start, a

#def numbaing()

#from numba import jit
#from numpy import arange
#import time
#
## jit decorator tells Numba to compile this function.
## The argument types will be inferred by Numba when function is called.
#@jit
#
#def sum2d(arr):
#    M, N = arr.shape
#    result = 0.0
#    for i in range(M):
#        for j in range(N):
#            result += arr[i,j]
#    return result
#
#a = arange(9).reshape(3,3)
#print(sum2d(a))

#def printing()
#
#N=5
#
#print "%i %i %i %i %i" %(N-1, N-3, N, N+3, N+1)

#def forlooptiming

#from numpy import zeros, float32
#from time import time, sleep
#
#user_volt = zeros(5000, dtype = float32)
#elapse2 = zeros(5000, dtype = float32)
#start1 = time()
#s = 0
#slptm=.002
#while s < 2500:
#    #start2 = time()
#    #user_volt[s] = 2 * (s+1) + 3 / (s+1) # read off of AIN0 to populate voltage array
#    #stop2 = time()
#    #elapse2[s] = stop2 - start2
#    # s+=1
#    sleep(slptm)
#stop1 = time()
#
#elapsetotal = stop1 - start1
#
#print 'looping time:', "%.5f" %sum(elapse2)
#print '+ 5 sec from sleep:', "%.5f" %elapsetotal

#if __name__ == '__main__':
#    rolling()