#!/usr/bin/env python
# coding: utf-8

from functools import wraps
from types import *
import numpy as np
import random

def nsample(shape):
    def _1(function):
        @wraps(function)
        def _(*args,**kw):
            mat = np.zeros(shape)
            if 1==mat.ndim:
                vlen = shape
            else:
                vlen = shape[0] 
            for i in range(vlen):
                mat[i] = function(*args,**kw)
            return mat
        return _
    return _1

def vec_sample(vlen, dist_params):
    def _1(function):
        @wraps(function)
        def _(*args,**kw):
            vec = np.zeros(vlen)
            for i in range(vlen):
                vec[i] = function(dist_params[i])
            return vec
        return _
    return _1

def nvec_sample(shape,dist_params):
    def _1(function):
        @nsample(shape)
        @vec_sample(shape[1],dist_params)
        @wraps(function)
        def _(*args,**kw):
            return function(*args,**kw)
        return _
    return _1
        
        
        
if __name__ == '__main__':
    class_num = 2
    vec_dim = 3
    each_class_num = 4
    sample_num = class_num * each_class_num
    samples = np.zeros((sample_num,vec_dim))
    labels = np.zeros(sample_num)

    @nsample(vec_dim)
    def ngauss(mean, sigma):
        return random.gauss(mean,sigma)            

    offset = 0
    for c in range(class_num):        
        class_seeds = ngauss(0, 10)
        class_sigmas = ngauss(3, 1)
        @nvec_sample((each_class_num,vec_dim), [[x , y] for (x, y) in zip(class_seeds,class_sigmas)])
        def my_gauss(param):
            return random.gauss(param[0],param[1])
        _samples = my_gauss()
        for i in range(each_class_num):
            samples[i+offset] = _samples[i]
            labels[i+offset] = c
        offset = offset + each_class_num

    print(samples)            
    print(labels)                              
        

    
    
