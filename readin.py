import numpy

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

# Filename here
def readData(filein):
	filename = filein
	points = file_len(filename)
	data = numpy.zeros((4, points))
	ind = 0
	f = open(filename)
	for line in f:
		temp = line.split()
		tempFl = numpy.array([0.0, 0.0, 0.0, 0.0])
		for x in range(4):
			tempFl[x] = float(temp[x])
		data[:, ind] = tempFl
		ind += 1
	return data
