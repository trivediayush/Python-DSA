# Factorial of a number using functional recursion

def fun(num):
    if num==0 or num==1:
        return 1
    return num*fun(num-1)

print(fun(5))