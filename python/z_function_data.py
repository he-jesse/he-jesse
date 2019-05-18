##############################################
# Summary Statistics for the Herdy Z-Function#
#											 #
# @author:	Jesse He 						 #
##############################################

import math
import matplotlib

def readLocations(zer_file):
	T = 10**int(zer_file[2:4])
	locations = []
	with open(zer_file) as zeros:
		for line in zeros:
			if len(line.split()) != 2:
				break
			else:
				locations.append(T + float(line.split()[0]) + float(line.split()[1]))
		return locations

def min_maxIndex(zer_file):
	z_locations = readLocations(zer_file)
	distances = findDistances(z_locations)

	min_index = distances.index(min(distances))
	max_index = distances.index(max(distances))
	return (min_index, max_index)

def normDistance(location, dist):
	return dist * 1/(2*math.pi) * math.log(location/(2*math.pi))

def findDistances(locations):
	return [locations[i] - locations[i-1] for i in range(1,len(locations))]

def min_maxDistances(zer_file, min_index, max_index):
	z_locations = readLocations(zer_file)
	distances = findDistances(z_locations)

	norm_min_dist = normDistance(z_locations[min_index], distances[min_index])
	norm_max_dist = normDistance(z_locations[max_index], distances[max_index])
	return (norm_min_dist, norm_max_dist)

def findMaxima(max_file, min_index, max_index):
	with open(max_file) as z_max:
		maxima = [float(maximum) for maximum in z_max.readlines()]

		max_btw_min_dist = maxima[min_index]
		max_btw_max_dist = maxima[max_index]

		return (max_btw_min_dist, max_btw_max_dist)

def findDerivatives(der_file, min_index, max_index):
	with open(der_file) as z_der:
		derivatives = [float(derivative) for derivative in z_der.readlines()]
			
	der_min_dist_l = derivatives[min_index]
	der_min_dist_r = derivatives[min_index + 1]

	der_max_dist_l = derivatives[max_index]
	der_max_dist_r = derivatives[max_index + 1]

	return ((der_min_dist_l, der_min_dist_r), (der_max_dist_l, der_max_dist_r))

data = []

indeces = min_maxIndex('1e12.zeros.1001_10001002.txt')
normdists_1e12 = min_maxDistances('1e12.zeros.1001_10001002.txt', indeces[0], indeces[1])
maxima_1e12 = findMaxima('1e12.zeros.1001_10001002.max.txt', indeces[0], indeces[1])
derivatives_1e12 = findDerivatives('1e12.zeros.1001_10001002.der.txt', indeces[0], indeces[1])