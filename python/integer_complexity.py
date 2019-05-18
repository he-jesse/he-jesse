# @integer_complexity.py

def integer_complexity(n) :
	sum_factors = n + 1
	for i in range(1, n // 2) :
		if n % i == 0 :
			if (n // i) + i <= sum_factors :
				sum_factors = (n // i) + i	
	return sum_factors

num = int(input("Enter number: "))
print(integer_complexity(num))
