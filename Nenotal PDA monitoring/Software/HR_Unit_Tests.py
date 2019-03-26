# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 18:04:46 2015

@author: Moseph
"""

import unittest

class runTests(unittest.TestCase): #all of the below unit tests test the accuracy and correctness of functions used in HR_Monitor.py

# Status: All tests Run OK in ~0.03 seconds

    def test_findTHRZone(self):
        """
        checks that accurate target heart zone is calculated based off of input data
        """
        from HR_Monitor import findTHRZone
        input1=22
        output1, output2, output3, output4=findTHRZone(input1)
        self.assertAlmostEqual(output3,191.6, msg='ironically the max is not actually a max')
        self.assertEqual(output1,134, msg='70% of what???, definitely not the max!')
        self.assertEqual(output2,163, msg='85% of what???, certainly not the max!')

    def test_findsafeRHR(self):
        """
        checks that accurate safe resting heart rate (RHR) is calculated based off of all combinations of input data
        """
        from HR_Monitor import findsafeRHR
        input1='Male'
        input2='Female'
        input3='High Level Athlete'
        input4='Relatively Fit'
        input5='Couch Potato'
        output1=findsafeRHR(input1,input3)
        output2=findsafeRHR(input1,input4)
        output3=findsafeRHR(input1,input5)
        output4=findsafeRHR(input2,input3)
        output5=findsafeRHR(input2,input4)
        output6=findsafeRHR(input2,input5)
        self.assertEqual(output1,48, msg='Lie detector is telling me this is a lie')
        self.assertEqual(output2,60, msg='Something smells fishy...tuna maybe?')
        self.assertEqual(output3,72, msg='You lie about as well as you pass unit tests')
        self.assertEqual(output4,52, msg='Lie detector is telling me this is a lie')
        self.assertEqual(output5,64, msg='Something smells fishy...is it salmon?')
        self.assertEqual(output6,76, msg='You lie about as well as you pass unit tests')

    def test_importandseparate(self):
        """
        checks for if the input vectors are the same length
        """
        from HR_Monitor import importandseparate
        from random import randrange
        input1 = randrange(1,21,1)
        t, v=importandseparate(input1)
        self.assertEqual(len(t),len(v), msg='different lengths! abort abort abort!')

    def test_makenparray(self):
        """
        checks to make sure input vectors are output as numpy arrays
        """
        from HR_Monitor import makenparray
        from numpy import ndarray
        a=[1,3,-5,2,7,5,9,-1,3,-4]
        a_new=makenparray(a)
        self.assertIsInstance(a_new,ndarray, msg='not an np array!!!')

    def test_removeDCoffset(self):
        """
        checks that the input and output vectors are the same length
        """
        from HR_Monitor import removeDCoffset
        from numpy import array, int8
        input1=array([1,2,3,4,5,10,9,8,7,6], dtype=int8)
        output1=removeDCoffset(input1)
        self.assertEqual(len(input1),len(output1), msg='output length is not quite right')

    def test_normalizeData(self):
        """
        checks that an input array is properly normalized by ensuring all resulting
        values are between -1 and 1, that either -1 or 1 is a value, and the correct
        value is chosen to normalize data against
        """
        from HR_Monitor import normalizeData
        from numpy import array, float32, absolute
        input1=array([-5.6,-9.4,-3.5,-1.4,4.3,4.8,0.9,-2.8,-3.9,6.9], dtype=float32)
        output1=normalizeData(input1)
        self.assertLessEqual(max(output1), 1, msg='values are abnormal...get it? :)')
        self.assertGreaterEqual(min(output1), -1, msg='values are abnormal...get it? :)')
        self.assertEqual(max(abs(output1)),1, msg='values are abnormal...get it? :)')
        self.assertEqual(abs(output1[1]), 1, msg='normalized against wrong value')
        self.assertEqual(len(input1),len(output1), msg='output length is not quite right')

    def test_elapsedtime(self):
        """
        checks that (1) elapsed time is result of final index value in a vector
        minus the initial index value (2) elapsed time is a single value (3) elapsed
        time is positive
        """
        from HR_Monitor import elapsedtime
        from numpy import array, float32
        b=[1,2,3,4,5,6,7,8,9,10]
        a=array(b, dtype=float32)
        a_new=elapsedtime(a)
        self.assertEqual(a_new.size,1, msg='WRONG, this should be a single value, not a vector')
        self.assertEqual(a_new,9, msg='Nope, this elapsed time is not correct')
        self.assertGreater(a_new,0, msg='Eh eh, time elapsed should be greater than 0')

    def test_crosscorrviafor(self):
        """
        checks that cross correlation of kernel with measured signal via for loop
        is working properly by ensuring the resulting numpy array of correlation
        coefficients is the appropriate length (which equals number of loops) and
        each index value is correct, using known values
        """
        from HR_Monitor import crosscorrviafor
        from numpy import array, float32
        a=array([3,1,2,0,2], dtype=float32) #known measured signal array
        b=array([1,1], dtype=float32) #kernel array
        c=len(b)
        x=crosscorrviafor(a,c,b)
        self.assertEqual(len(x), len(a)-1, msg='Coefficient vector wrong length dude')
        self.assertEqual(x[0], 4, msg='Cross correlation went south bro')
        self.assertEqual(x[1], 3, msg='Cross correlation went south bro')
        self.assertEqual(x[2], 2, msg='Cross correlation went south bro')
        self.assertEqual(x[3], 2, msg='Cross correlation went south bro')

    def test_sectominconvert(self):
        """
        checks that conversion from seconds to minutes of a given time numpy array
        is done correctly  using known values
        """
        from HR_Monitor import sectomin
        from numpy import array, float32
        a=array([120], dtype=float32)
        b=sectomin(a)
        self.assertEqual(b, 2, msg='Ummm, this is not in minutes man!')

    def test_simpledivision(self):
        """
        checks for correct division of two numpy arrays using known values
        """
        from HR_Monitor import calcheartrate
        from numpy import array, float32
        a=array([50], dtype=float32)
        b=array([20], dtype=float32)
        output1, output2 = calcheartrate(a,b)
        self.assertEqual(output1, 2.5, msg='Go back to 3rd grade and learn to divide...in Python')
        
    def test_lessthan(self):
        """
        checks that the less than condition is properly assessed
        """
        from HR_Monitor import detectbradycardia
        input1=50
        input2=85
        output1=detectbradycardia(input1, input2)
        output2=detectbradycardia(input2, input1)
        self.assertEqual(output1, 0, msg='this would be true...if it were opposite day')
        self.assertEqual(output2, 1, msg='opposite day only exists in cartoons')
        
    def test_greaterthan(self):
        """
        checks that the greater than condition is properly assessed
        """
        from HR_Monitor import detecttachycardia
        input1=27
        input2=43
        output1=detecttachycardia(input1, input2)
        output2=detecttachycardia(input2, input1)
        self.assertEqual(output1, 1, msg='this would not be false...if it were opposite day')
        self.assertEqual(output2, 0, msg='opposite day or not, this is wrong')
        
if __name__ == '__main__':
    unittest.main()
