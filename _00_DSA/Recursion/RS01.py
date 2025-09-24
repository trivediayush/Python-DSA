# Head Recursion 
def func(count = 0):
    if count == 5:
        return
    print("Head Recursion")
    func(count + 1)

func()

# Tail Recursion 

def func2(Numcount = 0):
    if Numcount == 5:
        return
    func2(Numcount + 1)
    print("Tail Recursion")

func2()
    