print("Hello World")
i = 8;
if i < 10:
    print("less")
else:
    print("more")

    
    #Fibonnaci
def Fib(num):
    a = 0
    b = 1
    for l in range(0, num, 1):
        temp = a
        a = b
        b = temp + b
        print(a)
        
