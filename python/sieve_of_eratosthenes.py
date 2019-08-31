import math

def generate_primes(n):
    nums = [False, False] + [True for i in range(2, n + 1)]
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if nums[i]:
            for j in range(i ** 2, n + 1, i):
                nums[j] = False
    return [p for p in range(2, n + 1) if nums[p] == True]

print(generate_primes(2))
print(generate_primes(100))
print(generate_primes(200))
print(generate_primes(211))
print(generate_primes(1000))