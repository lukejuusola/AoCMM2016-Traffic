import numpy

#Finds number of lines in file
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
# Reads the data in "filein" into a matrix. "num" is the number of data points per line.
# For raw output (files of form "out__.txt") num = 4. The coordinates are (latitude, longitude, #casualties, hour)
# For nodelist, num = 3. Coordinates: (nodeID, longitude, latitude)
# For node-accident assignment files (files of form "node__.txt") num = 2. Coordinates: (nodeID, #accidents)
# Data is returned as a matrix with each column as a different node/accident, and each row n as all the
# nth coordinate values of the data set.
def readData(filein, num):
	filename = filein
	points = file_len(filename)
	data = numpy.zeros((num, points))
	ind = 0
	f = open(filename)
	for line in f:
		temp = line.split()
		tempFl = numpy.zeros((num, 1))
		for x in range(num):
			tempFl[x] = float(temp[x])
		data[:, ind] = numpy.transpose(tempFl)
		ind += 1
	return data
