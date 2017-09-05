#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import time
import logging
def normalize(vec):
    s = sum(vec)
    for i in range(len(vec)):
        vec[i] = vec[i] * 1.0 / s
def llhood(w_d, p_z, p_w_z, p_d_z):
    V, D = w_d.shape
    ret = 0.0
    for w, d in zip(*w_d.nonzero()):
        p_d_w = np.sum(p_z * p_w_z[w,:] * p_d_z[d,:])
        if p_d_w > 0:
            ret += w_d[w][d] * np.log(p_d_w)
    return ret
class PLSA:
    def __init__(self):
        pass
    def train(self, w_d, Z, eps):
        V, D = w_d.shape
        # create prob array, p(d|z), p(w|z), p(z)
        p_d_z = np.zeros([D, Z], dtype=np.float)
        p_w_z = np.zeros([D, Z], dtype=np.float)
        p_z = np.zeros([Z], dtype=np.float)
        # initialize
        p_d_z = np.random.random([D, Z])
        for d_idx in range(D):
            normalize(p_d_z[d_idx])
        p_w_z = np.random.random([V, Z])
        for w_idx in range(V):
            normalize(p_w_z[w_idx])
        p_z = np.random.random([Z])
        normalize(p_z)
        # iteration until converge
        step = 1
        pp_d_z = p_d_z.copy()
        pp_w_z = p_w_z.copy()
        pp_z = p_z.copy()
        while True:
            logging.info('[ iteration ] step %d' % step)
            step += 1
            p_d_z *= 0.0
            p_w_z *= 0.0
            p_z *= 0.0
            # run EM algorithm
            for w_idx, d_idx in zip(*w_d.nonzero()):
                #print '[ EM ] >>>>>> E step : '
                p_z_d_w = pp_z * pp_d_z[d_idx,:] * pp_w_z[w_idx,:]
                normalize(p_z_d_w)
                #print '[ EM ] >>>>>> M step : '
                tt = w_d[w_idx, d_idx] * p_z_d_w
                p_w_z[w_idx,:] += tt
                p_d_z[d_idx,:] += tt
                p_z += tt
            normalize(p_w_z)
            normalize(p_d_z)
            p_z = p_z / w_d.sum()
            # check converge
            l1 = llhood(w_d, pp_z, pp_w_z, pp_d_z)
            l2 = llhood(w_d, p_z, p_w_z, p_d_z)
            diff = l2 - l1
            logging.info('[ iteration ] l2-l1  %.3f - %.3f = %.3f ' % (l2, l1, diff))
            if abs(diff) < eps:
                logging.info('[ iteration ] End EM ')
                return (l2, p_d_z, p_w_z, p_z)
            pp_d_z = p_d_z.copy()
            pp_w_z = p_w_z.copy()
            pp_z = p_z.copy()