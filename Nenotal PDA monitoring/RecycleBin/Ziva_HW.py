#IMPORTING AND SEPARATING DATA
import csv
import numpy as np
import matplotlib.pyplot as mpl
time=[] #time array
volt=[] #voltage array
f=open('ziva.csv','rb') #import ziva csv
try:
    r=csv.reader(f)
    rowN=0
    for row in r:
        if rowN==0:
            header=row
        else:
            colN=0
            for col in row:
                if colN==0:
                    time.append(col) #create the time array
                elif colN==1:
                    volt.append(col) #create the voltage array
                else:
                    print
                colN+=1
        rowN+=1
finally:
    f.close() #close csv file

#CONVERT TO NP ARRAY WITH DTYPE FLOAT
time_a=np.array(time, dtype=np.float32) #change data type to numpy for later use
volt_a=np.array(volt, dtype=np.float32) #TEST: time_a is same length as volt_a

#FIND TOTAL TIME ELAPSED
ind_f=len(time_a)-1 #final time array index
time_f=time_a[ind_f] #final time value
time_i=time_a[0] #initial time value
time_t=time_f - time_i #total time elapsed
print (time_t) #output time elapsed

#PLOT VOLT VS TIME
mpl.figure(1)
mpl.plot(time_a,volt_a) #plot voltage vs time
mpl.show() #output the voltage vs  time plot

#CREATE KERNEL
inds_k=np.where(time_a<=0.38544) #find indices to get kernel length
#time of 0.38544 seconds was chosen from observing Ziva ECG plot
range_k=np.amax(inds_k)+1 #final index for kernel (i.e. kernel length)
kernel=volt_a[0:range_k] #mock kernel
time_k=time_a[0:range_k] #time for mock kernel
#TEST: kernel and time_k are same length & all time_k values below 0.38544

#PLOT KERNEL
mpl.figure(2)
mpl.plot(time_k,kernel) #plot kernel volt vs t
mpl.show() #output kernel plot

#IGNORE
volt_b=volt_a[3:range_k+3] #next 3lines are practicing comparison between kernel
#and actual signal,a subtraction method is used here although multiplication is 
#supposed to be better
xco=volt_b-kernel
print (np.sum(xco) #output sum of differences of signal and kernel

#CROSS CORRELATION VIA FOR LOOP
xco_a=np.zeros((len(time_a)-range_k,1))
for s in range(0,len(time_a)-range_k-1): #for loop to create coefficient array
    xco_a[s]=np.sum(volt_a[s:range_k+s] * kernel)
    print xco_a
xco_ni=np.array(list(range(0,len(xco_a)))) #this is the counter of iterations
xco_n=np.reshape(xco_ni,(len(xco_a),1)) #swap dimensions to match xco_a array
print (xco_n) #TEST: xco_n is same length as xco_a & xco_n is only integers

#PLOT CROSS CORRELATION COEFFICIENTS
mpl.figure(3) #plot the xcorr coefficients against each iteration number
mpl.plot(xco_n,xco_a)
mpl.show() #output the plot

#TALLYING UP ALL MAXIMUM CORRELATION COEFFICIENTS
xco_thresh=xco_a[np.where(xco_a>75)]
print xco_thresh #TEST: all xco_thresh values are above 75
import scipy.signal as sci
threshvals=xco_thresh[sci.argrelextrema(xco_thresh, np.greater)[0]] #the relative
#maximum values are identified
beats=len(threshvals) #total number of heartbeats counted

#CONVERT ELAPSED TIME FROM SEC TO MIN
#sectomin=np.linspace(1/60,1/60,len(time_t), dtype=np.float32) #create second to minute converter constant
time_beat= time_t/60 # * sectomin #multiply by converter for total time elapsed in min

#CALCULATION OF HEART RATE
HR=beats/time_beat #total number of heartbeats counted divided by total time elapsed
print (HR)