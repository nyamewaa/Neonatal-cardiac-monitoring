# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 21:45:29 2015

@author: ooluwadara
"""
import csv
f = open('ziva.csv','rb')
d = [i for i in csv.reader(f)];
f.close();
import numpy as np
myarray = np.asarray(d)
xval = myarray[1:,0] 
yval = myarray[1:,1]
xval1 = np.array(xval, dtype = np.float64)
yval2= np.array(yval, dtype = np.float64)
print np.subtract(xval1[29998], xval1[0])
#xval = np.myarray[1:,0]
#yval = np.myarray[1:,1]
#a = xval[0]
# = xval[29998]



#def local_maxima(xval, yval):
 #   xval = np.asarray(xval)
  #  yval = np.asarray(yval) 
    #sort_idx = np.argsort(xval)
   # yval = yval[sort_idx]
    #gradient = np.diff(yval)
    #maxima = np.diff((gradient > 0).view(np.int8))
    #return np.concatenate((([0],) if gradient[0] < 0 else ()) + 
    #                  (np.where(maxima == -1)[0] + 1,) +
     #                 (([len(yval)-1],) if gradient[-1] > 0 else ()))

#import matplotlib.pyplot as plt 
#plt.plot([d])