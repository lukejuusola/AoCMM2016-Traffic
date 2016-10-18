from PointPicker import *
from CrashMap import CrashMap
from readin import *
from scipy.integrate import dblquad
import matplotlib.pyplot as plt
import random

x1 = -5
x2 = 5
y1 = -5
y2 = 5
ambCost = 2
max_n = 20

def Score(crashes, ambulances):
	if(len(ambulances) == 0 or len(crashes) == 0):
		return
	crashMap = CrashMap(crashes, crash_std, crash_std)
	ambMap = CrashMap(ambulances, amb_std, amb_std)
	SquareDiff = lambda x, y: (MapDifference(crashMap, ambMap)(x,y))**2
	safety = 1./dblquad(SquareDiff, x1, x2, lambda x: y1, lambda x: y2)[0]
	#return safety - len(ambulances)*ambCost 
	return safety

def FindOptimumN(crashes):
	ret = []
	for n in range(1,max_n):
		ambs = NaiveContinuousSolution(crashes, n)
		ret.append((n, Score(crashes, ambs)))
	return ret

if __name__ == '__main__':
	crashes = []
	#crashes = [(1.25,1.25),(1.75,1.75), (1.25,1.75), (1.75,1.25), (-2,-2)]
	for i in range(50):
		crashes.append((random.randint(-2, 2), random.randint(-2, 2)))

	points = FindOptimumN(crashes)
	plt.scatter(list(map(lambda x: x[0], points)), list(map(lambda x: x[1], points)))
	plt.show()
	
	
