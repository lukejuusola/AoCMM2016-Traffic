from CrashMap import CrashMap
from MaxValue import MaxValue
import numpy as np
from Plot import plot

totalPicked = 3
picks = []
amb_std = 1
crash_std = 1

def MapDifference(f, h):
	def difference(x,y):
		return f(x,y) - h(x,y)
	return difference

crashes = [(1.25,1.25),(1.75,1.75), (1.25,1.75), (1.75,1.25), (-2,-2)]
crashMap = CrashMap(crashes, crash_std, crash_std)

X = np.linspace(-5, 5)
Y = np.linspace(-5, 5)
for i in range(totalPicked):
	heatMap = crashMap
	if len(picks) != 0:
		ambMap = CrashMap(picks, amb_std, amb_std)
		heatMap = MapDifference(crashMap, ambMap)
	picks.append(MaxValue(heatMap, X, Y)[:2])

print(picks)
ambMap = CrashMap(picks, amb_std, amb_std)
plot(crashMap, -5, 5, -5, 5)
plot(ambMap, -5, 5, -5, 5)
plot(MapDifference(crashMap, ambMap), -5, 5, -5, 5)

