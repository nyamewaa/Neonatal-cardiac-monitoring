def main():
    
    time, volts = read_time_volts(fname='ziva.csv')
    
    nyq_freq = find_nyq_freq(time)
    
    print nyq_freq

    volt_minus_dc = filter_sig(volts, nyq_freq)
    
    print volt_minus_dc
    
    maxtime, maxpeak =find_max_peak(volt_minus_dc, time)
   
    print maxtime, maxpeak   
   
    norm_volts=normalize(volt_minus_dc,maxpeak)
   
    ken_time, ken_volt=def_kernel(maxtime,time,norm_volts)
    
    corr_max, corr=x_corr(ken_volt,norm_volts)
    
    HR_min=find_HRmin(corr_max, time, nyq_freq)
    
    print 'Zivas Heart Rate is ', HR_min, 'beats per minute'
    
#    import matplotlib.pyplot as plt
#    b=plt.figure(1)
#    plt.plot(time,volts)             #this plots the signal without the offset
#    plt.ylabel('Voltage (mV)')              #labels y ais
#    plt.xlabel('time(seconds)')             #labels x axis
#    plt.title('Plot of Zivas Heart Rate without dc offset')   #puts a title over the plot
#    b.show() 
    
def read_time_volts(fname='ziva.csv'):
    """read time/voltage data from CSV file
    assuming time in first column in seconds
    assuming voltage in second column in mV
    :param str fname: CSV filename
    :return array time: time data
    :return array volt: voltage data
    """
    from numpy import genfromtxt

    data = genfromtxt(fname, delimiter=',', skip_header=10)

    time = [row[0] for row in data]         
    volts = [row[1] for row in data]        

    return time, volts

def find_nyq_freq(time):
    """find Nyquist frequency from time data
    :param array time: time in seconds
    :return float nyq_freq: Nyquist frequency (Hz)
    """
    samp_time=time[1]-time[0]
    samp_rate=1/samp_time        
    nyq_freq=0.5*samp_rate      
    return nyq_freq
    
def filter_sig(volts,nyq_freq):
    
    from numpy import convolve, ones
    """Find dc offset and filter it out 
    of the signal
    :param array volts: volts in mV
    :param float nyq_freq: nyquist frequency (Hz)
    :return volt_minus_dc: Filtered signal in mV
    """
    dc_offset = convolve(volts, ones(10), mode='same') 
    volt_minus_dc=volts-(dc_offset/10)
    return volt_minus_dc
    
def find_max_peak(volt_minus_dc, time):
    """this finds the maximum of the peaks
    in the filtered signal and the timepoint at which
    it occurs
    :param array volt_minus_dc: Filtered signal in mV
    :param array time: time in seconds
    :return array maxtime: time of max signal peak seconds
    :return array maxpeak: maximum signal peak in mV 
    """
    from scipy import signal
    from numpy import arange, std
    import numpy as np
    
    #Find all peaks
    peak_ind = signal.find_peaks_cwt(volt_minus_dc, arange(1,10))         
    volt_peak =[volt_minus_dc[int(i)]for i in peak_ind]                   
    time_peak =[time[int(i)]for i in peak_ind] 
    
    #removes peaks from external noise
    mean_peak = sum(volt_peak)/len(volt_peak)                             
    stdev_peak = std(volt_peak)                  
    lower_thresh = mean_peak + (2*stdev_peak)       
    upper_thresh = mean_peak + (4*stdev_peak)  
         
    #finds the maximum peak from ECG signal
    peaks_in_thresh = [i for i, x in enumerate(volt_peak) if x <= upper_thresh]
    max_peak=max(peaks_in_thresh)   
    max_ind = [i for i, x in enumerate(peaks_in_thresh) if x == max_peak]         
    max_time =[time_peak[int(i)]for i in max_ind]   
    maxtime=max_time[0]
    maxpeak=max_peak
    return maxtime, maxpeak
    
def normalize(volt_minus_dc,maxpeak):
    """This normalizes all the data against 
    the maximum value
    :param array volt_minus_dc: Filtered signal in mV
    :param float maxpeak: maximum signal peak in mV 
    :return array norm_volts: normalized filtered signal (dimensionless) 
    """
    norm_volts=[x / maxpeak for x in volt_minus_dc]
    return norm_volts
    
def def_kernel(maxtime,time,norm_volts):
    """This normalizes all the data against 
    the maximum value
    :param float maxtime:time of max signal peak seconds
    :param array time:time in seconds
    :param norm_volts:normalized filtered signal (dimensionless) 
    :return array ken_time: time array for selected kernel in seconds
    :return array ken_volts: voltage array for selected kernel in mV
    """
    #from literature we know the set duration between the p and t wave 
    #of a signal to be about 0.6seconds with the duration between p and 
    #r  being about 0.22 and the  duration between r and t being 0.38
    #therefore we can find our QRS peak and estimate a single ecg beat 
    #based on these durations
    from numpy import array
    lower_kernel= array(maxtime) - 0.22
    upper_kernel= array(maxtime) + 0.38
    ken_ind = [i for i, x in enumerate(time) if (x >= lower_kernel)&(x<= upper_kernel) ]
    ken_time=[time[int(i)]for i in ken_ind]
    ken_volt=[norm_volts[int(i)]for i in ken_ind]
    return ken_time, ken_volt
    
def x_corr(ken_volt,norm_volts):
    """This finds the maximum peak using pattern match for
    peaks between the the selected kernel and entire signal.
    :param array ken_volts:voltage array for selected kernel in mV
    :param array norm_volts:normalized filtered signal (dimensionless) 
    :return float corr_max: maximum peak 
    :return array corr: Resultant array from correlation
    """
    from numpy import correlate,arange
    from scipy import signal
    
    corr=correlate(ken_volt,norm_volts,"full")
    threshold=0.6*max(corr)
    all_peak_ind = signal.find_peaks_cwt(corr, arange(1,10))
    corr_peak = [corr[int(i)]for i in all_peak_ind]                                                                                                                                   
    corr_max = [i for i, x in enumerate(corr_peak) if x >= threshold]       
    return corr_max, corr
    
def find_HRmin(corr_max, time, nyq_freq):
    """This finds the heart rate by dividing the number of peaks
    by the duration of the signal
    :param array float corr_max: maximum peak 
    :param array time: time in seconds
    :param array nyq_freq:Nyquist frequency in (Hz)
    :return float HR_min: Heart rate in minutes
    """
    num_peaks=len(corr_max)
    num_samples=len(time)    
    samp_rate=2*nyq_freq  
    duration=num_samples/samp_rate 
    HR=num_peaks/duration
    HR_min=60*HR
    return HR_min
"""    
def plot_signals():
    # import numpy as np
                 
    #assign columns to variables
    import matplotlib.pyplot as plt
    a=plt.figure(1)
    [plt.plot(time,volts)]                  #creates a plot of voltage against time
    plt.ylabel('Voltage (mV)')              #labels y ais
    plt.xlabel('time(seconds)')             #labels x axis
    plt.title('Plot of Zivas Heart Rate')   #puts a title over the plot
    a.show()    

    b=plt.figure(2)
    plt.plot(time,volt_minus_dc)             #this plots the signal without the offset
    plt.ylabel('Voltage (mV)')              #labels y ais
    plt.xlabel('time(seconds)')             #labels x axis
    plt.title('Plot of Zivas Heart Rate without dc offset')   #puts a title over the plot
    b.show() 
    
    c=plt.figure(3)
    plt.plot(ken_time,ken_volt)
    plt.ylabel('Voltage (mV)')              #labels y ais
    plt.xlabel('time(seconds)')             #labels x axis
    plt.title('Plot of Kernel')   #puts a title over the plot
    c.show() 
    
    d=plt.figure(4)
    plt.plot(corr)
    plt.ylabel('Intensity')              #labels y axis
    plt.title('Plot of correlation')   #puts a title over the plotm
    d.show() 
    
    import matplotlib.pyplot as plt
    a=plt.figure(1)
    plt.plot(corr)
    a.show()  
"""    
if __name__ == '__main__':
    main()

