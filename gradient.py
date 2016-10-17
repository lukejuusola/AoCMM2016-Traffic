from CrashMap import CrashMap
import numpy as np
import scipy
from Plot import plot
import random

m_x = (-10,10)
m_y = (-10,10)
stdx = 1
stdy = 1

def fscore(f1, f2):
    return lambda x,y: (f1(x,y) - f2(x,y))**2

def calcInt(f):
    score, error =scipy.integrate.quadpack.dblquad(f, m_x[0], m_x[1], lambda x: m_y[0], lambda x: m_y[1])
    return score



def calcGradient(ambulances, crashmap):
    delx = 0.1
    amb_map = CrashMap(ambulances, stdx, stdy)
    score = calcInt(fscore(crashmap(x,y), amb_map(x,y)))
    deltas = []
    for i in range(0, len(ambulances)):
        x0, y0 = ambulances[i]
        ambulances[i] = (x0 - delx, y0)
        mapx0 = CrashMap(ambulances, stdx, stdy)
        #plot (lambda x,y: (crashmap(x,y) - amb_map(x,y))**2, -5, 5, -5, 5)
        ambulances[i] = (x0 + delx, y0)
        mapx1 = CrashMap(ambulances, stdx, stdy)
        #plot (lambda x,y: (crashmap(x,y) - amb_map(x,y))**2, -5, 5, -5, 5)
        ambulances[i] = (x0, y0-delx)
        mapy0 = CrashMap(ambulances, stdx, stdy)
        ambulances[i] = (x0, y0+delx)
        mapy1 = CrashMap(ambulances, stdx, stdy)
        ambulances[i] = (x0, y0)
        
        scoreX0 = calcInt(fscore(crashmap(x,y), mapx0(x,y)))
        scoreX1 = calcInt(fscore(crashmap(x,y), mapx1(x,y)))
        scoreY0 = calcInt(fscore(crashmap(x,y), mapy0(x,y)))
        scoreY1 = calcInt(fscore(crashmap(x,y), mapy1(x,y)))
        
        dx = (scoreX1 - scoreX0)/(2*delx)
        dy = (scoreY1 - scoreY0)/(2*delx)
        deltas.append((dx, dy))
    return deltas

def update(ambulances, crashmap, rate):
    #rate = 10
    grad = calcGradient(ambulances, crashmap)
    for i in range(0, len(ambulances)):
        x0, y0 = ambulances[i]
        x1 = x0 - rate * grad[i][0]
        y1 = y0 - rate * grad[i][1]
        ambulances[i] = (x1, y1)
    return grad

num_amb = 3
num_crashes = 4

ambulances = []
crashes = []
for i in range(0, num_amb):
    ambulances.append((random.uniform(-5,5), random.uniform(-5,5)))
for i in range(0, num_crashes):
    crashes.append((random.uniform(-5,5), random.uniform(-5,5)))

crashmap = CrashMap(crashes, stdx, stdy)
plot(crashmap, -6, 6, -6, 6)
amb_map = CrashMap(ambulances, stdx, stdy)
#gradient = calcGradient(ambulances, crashmap)
score = calcInt(fscore(amb_map, crashmap))
lastscore = 0
#print abs(lastscore - score)/score
count = 0
gradsum = 1
rate = 10
while(gradsum > 10**-8):
    #amb_map = CrashMap(ambulances, stdx, stdy)
    #plot(lambda x,y: (amb_map(x,y) - crashmap(x,y))**2, -10, 10, -10, 10)
    grads = update(ambulances, crashmap, rate)
    gradsum = sum(abs(x)+ abs(y) for x,y in grads)
    lastscore = score
    score = calcInt(fscore(CrashMap(ambulances, stdx, stdy), crashmap))
    if score < lastscore:
        print abs(score-lastscore)/score
        rate *= 1 + 10*abs(score - lastscore)/score
    else:
        print "reset"
        rate *= 0.5
    count += 1;
    if count % 10 == 0:
        print ambulances
        print gradsum
        print rate
        #print lastscore, score
        #print (lastscore-score)/score
plot(crashmap, -10, 10, -10, 10)
plot(CrashMap(ambulances, stdx, stdy), -10, 10, -10, 10)
plot(fscore(CrashMap(ambulances, stdx, stdy),crashmap), -10, 10, -10, 10)
    

        
    

    
