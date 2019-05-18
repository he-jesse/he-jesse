import math

def s_n(n):
	sum = 0
	for i in range(1, n + 1):
		sum += (math.factorial(i)**2 * 2**i) / math.factorial(2*i)
	return sum

for i in range(1, 73):
	print(s_n(i))