# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:02:01 2015

@author: ooluwadara
"""

import unittest 
class runTest(unittest.TestCase): #means look at myself
    
    def test_import_data(self):
        """are read vectors same length
        """
        from Ziva_HR_Code import import_data
        time, voltage = import_data()
        self.assertEqual(len(time), len(voltage))
        
    def test_convolution(self):
        """is convolution successful
        """
        from Ziva_HR_Code import convolution
        windata,my_window = convolution(window_len=2,voltage=[1,0,0]) 
        print my_window.shape
        print windata.shape
        self.assertEqual(windata[0],0)
        
    def test_remove_offset_test(self):
        """is DC offset removed
        """
        import numpy as np 
        from Ziva_HR_Code import remove_offset
        offset_data, volt_window, windata_window, vari = remove_offset(window_len=2, voltage=np.array([1,0,0]), windata=np.array([1,1,1])) 
        #print offset_data.shape
        #print volt_window.shape
       # print windata_window.shape
        self.assertEqual(offset_data[0,0],0)
        
  # def normalize_test(self):
       # """ normalize the test
      #  """
      #  import numpy as np
      #  from Ziva_HR_Code import normalize
      #  time,windata=normalize()
        
if __name__ == '__main__':     #i want to run this entire test
    unittest.main()
     