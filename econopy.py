# MIT License

# Copyright (c) 2017 Jack Carroll

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import math as m
import numpy as np
import matplotlib.pyplot as plt

def gini(array):

    array = array.ravel() #returns flattened array

    array = np.sort(array) #sorts array

    n = len(array) #number of elements

    mu = np.mean(array) #average income

    i = np.arange(1,len(array)+1) #index 

    if np.min(array) < 0: #if it is less than zero, it is clipped out of the array
        np.clip(array,a_min=0,a_max=m.inf)

    result = ((np.sum((2 * i - n  - 1) * array)) / ((n ** 2) * mu)) #gini function from http://mathworld.wolfram.com/GiniCoefficient.html

    return result


def hill(array):

    array = array.ravel() #returns flattened array

    array = np.sort(array) #sorts array

    n = len(array) #number of elements

    min = np.min(array) #minimum value

    z = np.log(array / min) #data points CANNOT be zero or negative because of the natural log

    result = ((n / (np.sum(z)) + 1)) #Hill's alpha parameter from http://www.utstat.utoronto.ca/keith/papers/robusthill.pdf

    return result 

def cdf(array):

    array = array.ravel() #returns flattened array

    array = np.sort(array) #sorts array

    yaxis=np.arange(len(array))/float(len(array)-1) #plots data points against one element less in the array 
    
    plt.plot(array,yaxis)

    plt.show() 


