#havel-hakimi algorithm
import unittest as ut

def hh(ans):
    ans.sort(reverse=True)
    if not ans:
        return True
    else:
        n = ans.pop(0)
        if n > len(ans):
            return False
        for i in range(0,n):
            ans[i] -= 1
        return hh(ans)

print(hh([]) == True)
print(hh([1]) == False)
print(hh([1, 1]) == True)
print(hh([5, 3, 0, 2, 6, 2, 0, 7, 2, 5]))
print(hh([14, 10, 17, 13, 4, 8, 6, 7, 13, 13, 17, 18, 8, 17, 2, 14, 6, 4, 7, 12]) == True)