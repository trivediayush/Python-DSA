# Given a number, Check whether the number is a Armstrong number or not.
n = 153
num = n
total = 0
lengthofNo = len(str(n))
while num>0:
    lastDigit = num%10
    total = total + (lastDigit**lengthofNo)
    num = num//10
if total == n:
    print(f'{n} is a Armstrong Number.')
else:
    print(f'{n} is not a Armstrong Number.') 
