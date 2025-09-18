n = 1234567890
rev = 0
num = n

while num > 0:
    digit = num%10
    rev = rev*10+digit
    num = num//10

print(rev)