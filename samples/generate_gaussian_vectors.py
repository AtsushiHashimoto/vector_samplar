#!/usr/bin/env python
# coding: utf-8

import numpy as np
import random
import vector_sampler as vs
                
if __name__ == '__main__':
    class_num = 2
    vec_dim = 3
    each_class_num = 4
    sample_num = class_num * each_class_num
    samples = np.zeros((sample_num,vec_dim))
    labels = np.zeros(sample_num)

    @vs.nsample(vec_dim)
    def ngauss(mean, sigma):
        return random.gauss(mean,sigma)            

    offset = 0
    for c in range(class_num):        
        class_seeds = ngauss(0, 10)
        class_sigmas = ngauss(3, 1)
        @vs.nvec_sample((each_class_num,vec_dim), [[x , y] for (x, y) in zip(class_seeds,class_sigmas)])
        def my_gauss(param):
            return random.gauss(param[0],param[1])
        _samples = my_gauss()
        for i in range(each_class_num):
            samples[i+offset] = _samples[i]
            labels[i+offset] = c
        offset = offset + each_class_num

    print(samples)            
    print(labels)                              
        
