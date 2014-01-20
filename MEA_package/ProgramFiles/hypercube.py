import random
import numpy as np
#nSeg is number of segments/samples
#nDim is number of dimensions/variables/parameters
#y is a list of the ranges for each variable i.e. [(70,110),(0.1,0.5),...]
def hypercube(nSeg,y):

    nDim = len(y)
    possvalues = [0]*nSeg
    for i in range(nSeg):
        possvalues[i]=(((1.0)/nSeg)*i,((1.0)/nSeg)*(i+1))
    x = [0]*nDim
    for i in range(nDim):
        values = [0]*len(possvalues)
        for j in range(len(values)):
            mult = random.random()
            values[j]=(mult*(possvalues[j][1]-possvalues[j][0]))+(possvalues[j][0])
        x[i]=random.sample(values,len(values))
    samples = [0]*len(values)
    for i in range(len(values)):
        sample = [0]*nDim
        for j in range(nDim):
            sample[j]=x[j][i]
        samples[i]=sample
    for sample in samples:
        for i in range(len(sample)):
            if y[i][1]==y[i][0]:
                sample[i] = y[i][1]
            else:
                sample[i] = (sample[i]*(y[i][1]-y[i][0]))+y[i][0]

    return samples