# Sum of 1 to N Natural Numbers using Parameterised Recursion

def func(i, n, sum):
    if i>n:
        print(sum)
        return
    func(i+1, n, sum+i)

func(1, 10, 0)