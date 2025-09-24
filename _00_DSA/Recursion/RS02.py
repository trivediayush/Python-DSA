# Recurion with parameter 
# Given a Number, print the number N times

def func(i,n):
    if i>n:
        return
    print(i)
    func(i+1, n)

func(1, 4)