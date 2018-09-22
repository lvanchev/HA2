# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 20:06:01 2018

@author: Sick
"""

class Data():
    def __init__(self, data):
        self.data=data
    def count(self):
        return len(self.data)
    def sum(self):
        return sum(self.data)
    def moment(self, k):
        return sum(elem**k for elem in self.data)/self.count()
    def mean(self):
        return self.moment(1)
    def var(self):
        return sum((elem-self.mean())**2 for elem in (self.data))/self.count()
    def std(self):
        return self.var()**0.5
    def percentile(self, p):
        elem=int(p*self.count())+(self.count()%4 > 0)
        return self.data[elem-1]
    def median(self):
        return self.percentile(0.5)
    def __str__(self):
        print("Count:", self.count())
        print("Mean:", self.mean())
        print("Variance:", self.var())
        print("Standard deviation:", self.std())
        print("2nd moment:", self.moment(2))
        print("3rd moment:", self.moment(3))
        print("4th moment:", self.moment(4))
        print("Median:", self.median())
        print("25% quantile:", self.percentile(0.25))
        print("75% quantile:", self.percentile(0.75))
        return ""