import math
from scipy.integrate import dblquad, IntegrationWarning
import numpy as np
import warnings
import copy
warnings.simplefilter("ignore", IntegrationWarning)
warnings.simplefilter("ignore", UserWarning)

manhattan_x = (-10, 10)
manhattan_y = (-10, 10)

#Assume dataset is in form [(x_0, y_0), ..., (x_n, y_n)] where x, y is gps coordinates
def CrashMap(dataset, stdx, stdy):
	new_dataset = copy.deepcopy(dataset)
	def freqMap(x, y):
		z = 0.0
		C = 1.0 # Normalization constant. Definitely needs to be tweeked
		# Should just be able to divide in the end.
		for x_i,y_i in new_dataset:
			dx = (x - x_i)
			dy = (y - y_i)
			exponent = -(dx**2/(2*stdx**2) + dy**2/(2*stdy**2))
			z += C*math.exp(exponent)
		return z
	norm_c, error = dblquad(freqMap, manhattan_x[0], manhattan_x[1],\
								lambda x: manhattan_y[0],\
								lambda x: manhattan_y[1])
	def normedFreqMap(x,y):
		return freqMap(x,y)/norm_c

	return normedFreqMap




