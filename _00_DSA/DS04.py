# Find all divisors of a given number using brute force

import math

n = 20

result = []

#brute force
# for i in range(1, n+1):
#     if n%i == 0:
#         result.append(i)
# print(result)

#Optimal Approach

for i in range(1, int(math.sqrt(n))+1):
    if n%i == 0:
        result.append(i)
        if n//i != i:
            result.append(n//i)

result.sort()
print(result)