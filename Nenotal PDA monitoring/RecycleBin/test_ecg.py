import unittest
from numpy import arange, sin, pi
import numpy as np

class runTest(unittest.TestCase):
    

   def test_read_time_volts(self):
      """can I read in CSV data
      """
      from FixedECGSept15 import read_time_volts
      time, volt = read_time_volts()
      self.assertEqual(len(time), len(volt), msg='time and volt not same length')


   def test_find_nyq_freq(self):
       """can I calculate Nyquist
       """
       from FixedECGSept15 import find_nyq_freq
       t = [1.0, 1.1]
       nyq_freq = find_nyq_freq(t)
       self.assertAlmostEqual(nyq_freq, 5.0)
    
       
   def test_filter_sig(self):
      """can we filter the signal
      """
      from FixedECGSept15 import filter_sig
      v=[1]
      win=1
      filtered= filter_sig(v, win)
      self.assertAlmostEqual(filtered, 0)
      
   def test_find_max_peak(self):
       """can we find the maximum peak
       """
       from FixedECGSept15 import find_max_peak
       t=arange(0,2,0.0002)
       sig=sin(2*pi*t)
       max_t, max_p = find_max_peak(t,sig)
       self.assertAlmostEqual(max_p, 0)
      
   def test_normalize(self):
       """Is the function normalized?
       """
       from FixedECGSept15 import normalize
       arr = [1, 2, 3, 4, 5]
       max_arr = max(arr)
       norm = normalize(arr, max_arr)
       max_norm = max(norm)
       self.assertAlmostEqual(max_norm, 1)
       
   def test_def_kernel(self):
       """does the function find a kernel?
       """
       from FixedECGSept15 import def_kernel
       t=arange(0,2,0.0002)
       v=sin(2*pi*t)
       max_v= max(v)
       max_ind = [i for i, x in enumerate(v) if x == max_v]        #this finds the indice position for the maximum value   
       max_t   =[t[int(i)]for i in max_ind]  
       maxt=max_t[1]
       ken_t, ken_v = def_kernel(maxt,t,v)
       self.assertEqual(len(ken_t),len(ken_v), msg='time and volt not same length')

   def test_x_corr(self):
       """does correlation function work
       """
       from FixedECGSept15 import x_corr
       t=arange(0,2,0.0002)
       sig1=sin(pi*t)
       sig2=sin(pi*t)
       corr_max,corr = x_corr(sig1,sig2)
       #self.assertAlmostEqual(corr_max,5000)
       self.assertEqual(len(corr_max),1)

   def test_find_HRmin(self):
       """can we find the heart rate
       """
       from FixedECGSept15 import find_HRmin
       p = [4,4,3,3,3,3]
       t=arange(0,10,0.5)
       n=5
       hr=find_HRmin(p, t, n)
       self.assertEqual(hr,180)
       
if __name__ == '__main__':
    unittest.main()
