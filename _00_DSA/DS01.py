'''Problem Statement:
You are given an integer N. Your task is to determine the number of digits present in the integer N.

Example:

Input: N = 345677

Output: 6'''

N = 345677

num = N
count = 0

while num>0:
    count+=1
    num=num//10
print(count)


'''Different Approach'''

# import math

# if N == 0:
#     print("1")
# else:
#     count = int(math.log10(abs(N))) + 1

# print(count)