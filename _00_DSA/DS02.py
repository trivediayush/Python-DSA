# Problem Statement:
# Given a number, check whether the number is a palindrome or not.

n = 1221

# Answer
num = n
result = 0

while num>0:
    lastDigit = num%10
    result = (result*10) + lastDigit
    num = num//10

if n == result:
    print(f'{n} is a Palindrome number.')
else:
    print(f'{n} is not a Palindrome number.')