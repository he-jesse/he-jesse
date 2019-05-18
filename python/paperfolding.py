# @paperfolding.py
# @author Jesse He

def build_sequence(n, accum) :
	for i in range(n):
		new_accum = '1'
		for i in range(0, len(accum)) :
			new_accum += accum[i] + str(i % 2)
		accum = new_accum
	return accum

n = input()
print(build_sequence(int(n), '1'))