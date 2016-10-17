from CrashMap import CrashMap
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot(f, leftX, rightX, leftY, rightY):
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	vf = np.vectorize(f)
	X = np.linspace(leftX, rightX, 100)
	Y = np.linspace(leftY, rightY, 100)
	X, Y = np.meshgrid(X, Y)
	Z = vf(X, Y)
        #surf = ax.contourf(X, Y, Z)
        #plt.contourf(X, Y, Z)
	surf = ax.plot_surface(X,Y,Z, rstride=2, cstride=2, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
	plt.show()
