# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 21:26:39 2015

@author: Moseph
"""

def main(user_time, user_volt, kernel, kernel_size):
    """
    Determines the heart rate of a user based off of input voltages (in mV) presumably from ECG leads
    
    :param list user_time: time array corresponding to user voltage being used (in sec)
    :param list user_volt: voltage array from user heart activity (in mV)
    :param float kernel: array comprising one ideal ECG wave to be used for heart-beat detection (in mV)
    :param int kernel_size: length of the kernel array
    :return float HR: calculated heart rate (in bpm)
    :return str HRonLCD: printed format of heart rate to be displayed on LCD screen
    """
    time_sec=makenparray(user_time)
    volt_mV=makenparray(user_volt)
    volt_mV=removeDCoffset(volt_mV)
    volt_mV=normalizeData(volt_mV)
    xcorrsapprox=crosscorrviafor(volt_mV,kernel_size,kernel)
    total_HBs=maxcrosscorrcoefs(xcorrsapprox)
    # print total_HBs, 'beats'
    time_duration_sec=elapsedtime(time_sec)
    time_duration_min=sectomin(time_duration_sec)
    # print time_duration_sec, 'sec', time_duration_min, 'min'
    Heart_Rate, HRonLCD =calcheartrate(total_HBs,time_duration_min)
    # print HRonLCD
    return Heart_Rate, HRonLCD
    
def definekernel():
    """
    Designs the kernel to be used in cross correlation with user's ECG wave based
    off of ziva.csv data
    
    return float kernel: array of the voltage values for kernel (in mV)
    return int kernel_size: the length of the kernel array
    """
    time_list, volt_list=importandseparate(10)
    time_sec=makenparray(time_list)
    volt_mV=makenparray(volt_list)
    volt_mV=removeDCoffset(volt_mV)
    kernel, kernel_size=createkernel(time_sec,volt_mV)
    return kernel, kernel_size
    
def findTHRZone(user_age):
    """
    Finds target heart rate zone based off of user's age and general formulas
    for maximum heart rate and target heart rate respectively (all in bpm)
    
    param int8 user_age: User's age (in years)
    return float THRZoneLow: Lower limit of target heart rate zone (70% of max)
    return float THRZoneHi: Upper limit of target heart rate zone (85% of max)
    return float MaxHR: Maximum heart rate = 207-0.7*age
    return str THRforLCD: printed format of target heart rate zone for scren display
    """
    from numpy import array, int16
    age=array(user_age, dtype=int16)
    MaxHR=207 - (0.7 * age)
    THRZoneLow=0.7 * MaxHR
    THRZoneHi=0.85 * MaxHR
    MaxHR = float("{0:.2f}".format(MaxHR))
    THRZoneLow = float("{0:.0f}".format(THRZoneLow)) # round to nearest integer
    THRZoneHi = float("{0:.0f}".format(THRZoneHi)) # round to nearest integer
    THRZoneLow = int(THRZoneLow) # make integer for cleaner conversion to str for LCD
    THRZoneHi = int(THRZoneHi) # make integer for cleaner conversion to str for LCD
    THRonLCD  = 'Zone:',str(THRZoneLow),'-',str(THRZoneHi),' bpm'
    THRonLCD = ''.join(THRonLCD)
    # print THRonLCD # for debugging purposes
    return THRZoneLow, THRZoneHi, MaxHR, THRonLCD

def findsafeRHR(user_sex,user_fitness_level):
    """
    Determines an approximate of the minimum, safe resting heart rate (RHR)
    based off of user input

    :param str user_sex: User's sex. Only two available  options: 'Male','Female'
    :param str user_fitness_level: User's self evalution of how physically fit he or she is. Three options available: 'High Level Athlete','Relatively Fit','Couch Potato'
    :return int8 safeRHR: Calculated safe resting heart rate (in bpm)
    """
    from numpy import array, int8
    if user_sex=='Male':
        if user_fitness_level=='High Level Athlete':
            safeRHR=48
        elif user_fitness_level=='Relatively Fit':
            safeRHR=60
        else:
            safeRHR=72
    else:
        if user_fitness_level=='High Level Athlete':
            safeRHR=52
        elif user_fitness_level=='Relatively Fit':
            safeRHR=64
        else:
            safeRHR=76
    safeRHR=array(safeRHR, dtype=int8)
    # print 'Your minimum safe RHR is', safeRHR, 'bpm'
    return safeRHR    
    
def datatoextract(time_sec, samp_freq=1000):
    """
    Determines how many samples should be extracted for importing and running algorithms on

    :param int time_sec: amount of time (in sec) the samples should represent
    :param int samp_freq: sampling frequency being used, default is 1000 Hz
    :return int data: amount of samples to extract from csv file
    """
    data=time_sec * samp_freq
    return data

def importandseparate(data_duration, filename='ziva.csv'):
    """
    Attempts to read a csv file and separate the numerical data into 2 lists

    :param int data_duration: duration of time the heart rate should be taken over (in sec)
    :param str filename: name of csv file to read, default is ziva.csv
    :return list time: list of time values from csv file (in seconds)
    :return list volt: list of voltage values from csv file (in mV)
    """
    import csv
    time=[]
    volt=[]
    data_marker=datatoextract(data_duration)
    f=open(filename,'rb')
    try:
        r=csv.reader(f)
        rowN=0
        for row in r:
            if rowN==0:
                header=row
#            elif rowN<(m-1) * data_marker: # this will be implemented in loop for streaming data
#                continue
            elif rowN>data_marker: # this number '1' will change based on value of m in while loop
                break
            else:
                colN=0
                for col in row:
                    if colN==0:
                        time.append(col) #creates the time array
                    else:
                        volt.append(col) #creates the voltage array
                    colN+=1 #column number counter
            rowN+=1 #row number counter
    finally:
        f.close() #close csv file
    return time, volt


def makenparray(inputarray):
    """
    Converts list arrays into numpy arrays

    :param list inputarray: list array to be converted to a numpy array
    :return float32 numpyarray: converted numpy array
    """
    from numpy import array, float32
    numpyarray=array(inputarray, dtype=float32)
    return numpyarray

def elapsedtime(time_array):
    """
    Calculates the elapsed time for a numpy time array in seconds

    :param float32 time_array: numpy time array to find elapsed time from (in seconds)
    :return float32 time_t: total time elapsed from final time array value minus the first (in seconds)
    """
    ind_f=len(time_array)-1 #final time array index
    time_f=time_array[ind_f] #final time value
    time_i=time_array[0] #initial time value
    time_t=time_f - time_i
    return time_t

def removeDCoffset(signal_volt):
    """
    Removes the DC offset from the input signal by convolving input voltage with
    a square wave and subtracting the result from original signal, and also
    filters the input signal

    :param float32 signal_volt: numpy voltage array representing input voltage (in mV)
    :return float32 volt_minus_dc: filtered signal with DC offset removed
    """
    from numpy import convolve, ones
    dc_window=len(signal_volt)/5
    dc_offset=convolve(signal_volt, ones(dc_window)/dc_window, mode='same')
    volt_minus_dc=signal_volt-dc_offset
    return volt_minus_dc

def normalizeData(numpy_array):
    """
    Normalizes an input array based off the the maximum magnitude of any one value
    resulting in an array with values ranging from -1 to +1

    :param float32 numpy_array: input numpy array to be normalized
    :return float32 normalized_array: normalized array with values from -1 to +1
    """
    from numpy import absolute
    magnitude=absolute(numpy_array)
    max_val=max(magnitude)
    normalized_array=numpy_array/max_val
    return normalized_array

def createkernel(signal_time,signal_volt,kernel_time=0.38544):
    """
    Creates a kernel based off of the first period of an ecg signal

    :param float32 signal_time: corresponding time numpy array for ecg signal (in seconds)
    :param float32 signal_volt: corresponding voltage numpy array for ecg signal (in mV)
    :param int kernel_time: time at which first period of ecg signal ends (in seconds), default is 0.385444
    :return float32 kernel: voltage values of the kernel (in mV)
    :return int64 range_k: the total number of indices of the returned kernel numpy array
    """
    from numpy import where, delete, arange
    inds_k=where(signal_time<=kernel_time) #find indices to get kernel length
    #time of 0.38544 seconds was chosen from observing Ziva ECG plot
    kernel=signal_volt[0:range_k]
    kernel = delete(kernel, arange(0, kernel.size, 2)) # decreases the sampling rate by 2
    range_k = len(kernel)
    # the below 4 lines are manipulations to make the kernel look more like an ideal human ecg wave
    kernel[81:88] = 0
    kernel[125:181] = abs(kernel[125:181])
    kernel[125:181] = kernel[125:181] - (kernel[180] - kernel[181])
    kernel[120:125] = 0
    return kernel, range_k

def crosscorrviafor(signal_volt,kernel_index_range,kernel):
    """
    Cross correlates a kernel array with an ecg signal array (both in mV) via a for loop
    by sliding the kernel across the signal, multiplying the two and summing the products
    of each index, and outputting the resulting coefficients for each iteration

    :param float32 signal_volt: voltage numpy array of ecg signal (in seconds)
    :param int64 kernel_index_range: total number of indices of the kernel numpy array
    :param float32 kernel: voltage numpy array for the kernel (in mV)
    :return float64 xco_a: numpy array of the coefficients for each iteration of cross correlation through for loop
    """
    from numpy import zeros, sum, array, int32 # , reshape #this is for plotting
    # from matplotlib.pyplot import figure, plot, show # this is for plotting
    kern_length=array(kernel_index_range, dtype=int32)
    xco_a=zeros((len(signal_volt)-kern_length+1,1))
    for s in range(0,len(signal_volt)-kern_length+1):
        xco_a[s]=sum(signal_volt[s:kern_length+s] * kernel)
    # the below 5 lines are for plotting purposes
    # xco_ni=array(list(range(0,len(xco_a)))) #this is the counter of iterations
    # xco_n=reshape(xco_ni,(len(xco_a),1)) #swap dimensions to match xco_a array
    # figure(1)
    # plot(xco_n,xco_a)
    # show()
    return xco_a

def maxcrosscorrcoefs(approx_coefficients_array):
    """
    Tallies up the number of local maximums/peaks in a given numpy array

    :param float64 approx_coefficients_array: numpy array of the cross correlation coefficients
    :param int threshold: the value above which to look for maximums, default is 75
    :return int beats: the total number of peaks in input numpy array, represents beats for this application
    """
    from numpy import where
    threshold=0.55*(max(approx_coefficients_array))
    xco_thresh=approx_coefficients_array[where(approx_coefficients_array>threshold)]
    beats=0
    for s in range(1,len(xco_thresh)-2):
        if xco_thresh[s] > xco_thresh[s-1] and xco_thresh[s] > xco_thresh[s+1]:
            beats+=1
        else:
            pass
    if xco_thresh[0] >= .9 * max(approx_coefficients_array):
        beats+=1
    elif xco_thresh[-1] >= .9 * max(approx_coefficients_array):
        beats+=1
    else:
        beats=beats
    return beats

def sectomin(time_array):
    """
    Converts a time numpy array that is in seconds to one in minutes

    :param float32 time_array: time numpy array to be converted (is in seconds)
    :return float32 time_beat: converted time numpy array (in minutes)
    """
    time_beat= time_array/60
    return time_beat

def calcheartrate(beats,minutes):
    """
    Simply divides two single values, but in this case represents heart rate

    :param int beats: total number of heart beats
    :param float32 minutes: total time elapsed in minutes
    :return float64 HR: heart rate in beats/minute
    :return str HRforLCD: printed format of heart rate for LCD screen use
    """
    HR = beats / minutes
    HR = float(HR)
    HR = float("{0:.1f}".format(HR))    
    HRforLCD  = '<3 Rate:',str(HR),' bpm'
    HRforLCD = ''.join(HRforLCD)
    return HR, HRforLCD
    
def detectbradycardia(safe_RHR,heart_rate): # It was actually simple enough to implement bradycardia detection without calling function in final code
    """
    Attempts to detect bradycardia based off of user information and current heart rate
    and prints an alert message if bradycardia is suspected
    
    :param safe_RHR: user's calculated minimum, safe resting heart rate in bpm
    :param heart_rate: user's current heart rate in bpm
    :return status: variable's value determines whethe bradycardia was detected or not
    """
    if heart_rate < safe_RHR:
        print 'WARNING: You"re heart rate seems particularly low!'
        status=1 # bradycardia detected
    else:
        status=0 # bradycardia NOT detected
    return status
    
def detecttachycardia(max_HR,heart_rate): # It was actually simple enough to implement tachycardia detection without calling function in final code
    """
    Attempts to detect tachycardia based off of user information and current heart rate
    and prints an alert message if tachycardia is suspected
    
    :param max_RHR: user's calculated maximum heart rate in bpm
    :param heart_rate: user's current heart rate in bpm
    """
    if heart_rate >= max_HR:
        print 'WARNING: You"re heart rate is too high!'
        status=1 # tachycardia detected
    else:
        status=0 # tachycardia NOT detected
    return status

def HowToUse(counter):
    """
    Allows the ability to scroll through strings of text to be displayed on an LCD screen
    based on a counter that is used to determine what two rows of strings to show.
    Designed for a 2 x 16 character screen.
    
    :param int counter: number that can be incremented to determine what rows of a string array to show
    :return str LCDrow1: text to appear on row one of LCD screen
    :return str LCDrow2: text to appear on row two of LCD screen
    """
    Text = [['   * BASICS *   '],['This is a simple'],['heart rate moni-'],['toring device   '],['for humans only.'],['Based off of in-'],['itial user res- '],['ponses, abnormal'],['heart rates, as '],['well as ideal   '],['ones, are compu-'],['ted and reported'],['to the user.    '],['Click on Live   '],['Monitor to ob-  '],['serve heart rate'],['in real-time.   '],['Click on Target '],['HR Zone to see  '],['unique target   '],['heart rate range'],['Click FiTrivia  '],['to learn fun,   '],['health-related  '],['facts. Click on '],['Credits to see  '],['major contribu- '],['tors to this    '],['project.        '],['  * ADVANCED *  '],['If in Continuous'],['Mode of Live Mon'],['itor, you have  '],['the option of   '],['Workout Mode.   '],['If ON, user is  '],['notified of his '],['or her work rate'],['and exercise    '],['progress.       '],['  * CONTORLS *  '],['Use the D-Pad to'],['navigate/scroll '],['through MainMenu'],['Press OK to pro-'],['ceed or accept. '],['Hold Menu to    '],['automatically   '],['return to Main  '],['Menu. Enjoy!    ']]
    LCDrow1 = Text[counter][0]
    LCDrow2 = Text[counter + 1][0]
    LCDrow1 = str(LCDrow1)
    LCDrow2 = str(LCDrow2)
    return LCDrow1, LCDrow2

if __name__ == '__main__':
    main()