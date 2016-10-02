#!/usr/bin/env python
# coding: utf-8

from functools import wraps
import numpy as np

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
