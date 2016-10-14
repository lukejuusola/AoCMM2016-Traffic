from CrashMap import CrashMap
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

if(__name__ == "__main__"):
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	data = [(.5,.5), (-.5, -.5), (1, 1), (4, -1)]
	cmap = CrashMap(data, 1, 1)
	vcmap = np.vectorize(cmap)
	X = np.arange(-5, 5, .1)
	Y = np.arange(-5, 5, .1)
	X, Y = np.meshgrid(X, Y)
	Z = vcmap(X, Y)
	surf = ax.plot_surface(X,Y,Z, rstride=2, cstride=2, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
	plt.show()
