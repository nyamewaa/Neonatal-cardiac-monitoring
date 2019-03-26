# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 20:31:27 2015

@author: ooluwadara
"""
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy import signal

def main():
    import matplotlib.pyplot as plt
    time, voltage =import_data()
    windata, my_window =convolution(voltage)
    plt.subplot(4,1,1)
    plt.plot(time,voltage)
    offset_data,volt_window,windata_window,process_data,vari_m= remove_offset(voltage,windata)
    print process_data
    print process_data.shape
    print offset_data.shape
    print time.shape
    plt.subplot(4,1,2)
    plt.plot(time,windata)
   # process_data = normalize(offset_data,vari)
    plt.subplot(4,1,3)
    plt.plot(time,offset_data)
    plt.subplot(4,1,4)
    plt.plot(time,process_data)
    

def import_data(fname='ziva.csv', skipheader=1):
    """read in CSV data
    :param str fname: filename to read CSV from
    :param int skipheader: number of lines to skip
    :return float32 time: time array
    :return float32 voltage: voltage array
    """
    import csv
    import numpy as np
    f = open(fname,'r')
    d = np.array([i for i in csv.reader(f)])
    f.close()
    import numpy as np
    time = np.array(map(float, d[skipheader:,0]))
    voltage = np.array(map(float, d[skipheader:,1]))
    return time, voltage

def convolution(voltage,window_len=5):
    """ window the data by convolving it with a square wave
    :param float32 voltage: voltage array
    :param int window_len: window length
    :return float32 winddata: windowed data
    :return float32 my_window: square function
    """
    import numpy as np
    my_window = np.ones(window_len)
    windata=(np.convolve(my_window,voltage,mode='same'))/window_len
    return windata, my_window

def remove_offset(voltage,windata,window_len=5):
    """ remove the offset 
    :param float32 voltage: matrix of voltages
    :param float32 windata: windowed data
    :param float32 window_len: window length
    :return float32 volt_window: window for voltage matrix
    :return float32 windata_window: window for windowed data
    :return float32 offset_data: the offsetted data
    :return float32 vari_m: the variance of the current window
    :return float32 process_data: processed data
    """
    import numpy as np
    offset_data= np.zeros((voltage.size))
    process_data= np.zeros((voltage.size))
    x = np.zeros(window_len)
    y = np.zeros(window_len)
    vari_m = np.zeros((voltage.size-window_len+1,1))
    for i in range(0,voltage.size-window_len+1,window_len):
        volt_window = voltage[i:(i+ (window_len-1))]
        windata_window = windata[i:(i+ (window_len-1))]
        vari_m = np.var(windata[i:(i+ (window_len-1))])
        x = (np.subtract(volt_window, windata_window))
        print x
        y = np.divide(vari_m,x)
        offset_data[i:i+(window_len-1)] = x
        process_data[i:i+(window_len-1)] = y
    
    return offset_data, volt_window, windata_window,process_data,vari_m

if __name__ == '__main__':
     main()
