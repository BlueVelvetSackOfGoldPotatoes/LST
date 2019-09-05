#!/usr/bin/python3

# add necessary imports 
import sys
from math import pi

def periodic(t, f, A, phi):
    # calculate output
    # a. -------------------------------------------------------
    # use linspace to get the timestamps (returns an array)
    # grab the ones that have an fs of 44100
    n = np.linspace(0, t, num=44100)
    for i in n:
       fs = i/t
       # check if the timesample is 44100
       if fs == 44100:
           # add n to x?
    # ----------------------------------------------------------
    return x

def plot_wave(t1, x1, t2, x2):
    # generate plot

if __name__ == '__main__':
   dur = sys.argv[1]
   # to read values as long as there is input
   inputArray = [int(i) for i in input().split()]
   # calculate t, and extract the values for f, A, and phi 
   # b. -------------------------------------------------------
   f = inputArray[0]
 
   # checking if A and phi are null and changing them accordingly
   if inputArray[2] is None:
      A = 1
   if inputArray[1] is None:
       phi = 0
   else:
       phi *= pi
    # ---------------------------------------------------------
   x = periodic(t, f, A, phi)
   # do something with x
   print(x[0:10])
