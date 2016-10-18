import numpy as np
import math

def MaxValue(f, X, Y):
	Xl, Yl = np.meshgrid(X, Y)
	vf = np.vectorize(f)
	Z = vf(Xl, Yl)
	index = np.argmax(Z)
	x_in = math.floor(index/50)
	y_in = index%50
	return (X[x_in], Y[y_in], Z[x_in][y_in])


if __name__ == '__main__':
	x_mean = .84
	y_mean = .12
	f = lambda x,y: 1 - math.sqrt((x-x_mean)**2 + (y-y_mean)**2)
	print(MaxValue(f, np.linspace(0,1), np.linspace(0,1)))
