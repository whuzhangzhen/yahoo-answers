#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

"""
preprocess
"""
class Preprocess:

    def __init__(self, fname, fsw):
        self.fname = fname
        # doc info
        self.docs = []
        self.doc_size = 0
        # stop word info
        self.sws = []
        # word info
        self.w2id = {}
        self.id2w = {}
        self.w_size = 0
        # stop word list init
        with open(fsw, 'r') as f:
            for line in f:
                self.sws.append(line.strip())
    def __work(self):
        with open(self.fname, 'r') as f:
            for line in f:
                line_strip = line.strip()
                self.doc_size += 1
                self.docs.append(line_strip)
                items = line_strip.split()
                for it in items:
                    if it not in self.sws:
                        if it not in self.w2id:
                            self.w2id[it] = self.w_size
                            self.id2w[self.w_size] = it
                            self.w_size += 1
        self.w_d = np.zeros([self.w_size, self.doc_size], dtype=np.int)
        for did, doc in enumerate(self.docs):
            ws = doc.split()
            for w in ws:
                if w in self.w2id:
                    self.w_d[self.w2id[w]][did] += 1
    def get_w_d(self):
        self.__work()
        return self.w_d
    def get_word(self, wid):
        return self.id2w[wid]
