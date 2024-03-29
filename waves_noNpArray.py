#!/usr/bin/python3

# add necessary imports 
import sys
import numpy as np
import math

def periodic(t, f, A, phi):
    # calculate output
    # Calculate timestamps
    timestamps = np.linspace(0, float(t), num=44100)
    # a. -------------------------------------------------------
    # use linspace to get the timestamps (returns an array)
    # grab the ones that have an fs of 44100
    x = []
    for i in timestamps:
        theta = 2 * math.pi * float(f) * i + phi
        x.append(round(float(A) * math.cos(theta),8))
    return x

# def plot_wave(t1, x1, t2, x2):
# generate plot

if __name__ == '__main__':
    dur = sys.argv[1]
    # to read values as long as there is input
    # calculate t, and extract the values for f, A, and phi 
    # b. -------------------------------------------------------
    f =  sys.argv[2]
    # checking if A and phi are null and changing them accordingly
   
    if len(sys.argv) > 4:
        A = sys.argv[3]
        phi = float(sys.argv[4]) * math.pi
    else:
        if len(sys.argv) > 3:
            A = sys.argv[3]
        else:
            A = 1
        phi = 0
   
    t = dur
    # ---------------------------------------------------------
    x = periodic(t, f, A, phi)
    # do something with x
    print(x[0:10])
