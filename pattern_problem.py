def inc_triangle(n):
    for i in range(n):
        for _ in range(i+1):
            print('* ',end= "")

        print()

def square(n):
    for i in range(n):
        for j in range(n):
            print("* ",end= "")

        print()

def dec_triangle(n):
    for i in range(n):
        for j in range(i,n):
            print("* ",end = "")

        print()

def next(n):
    for i in range(n):
        for j in range(i,n):
            print("",end = " ") 
        
        for k in range(i+1):
            print("*",end ="")
        
        print()

#next(5)
def next(n):
    for i in range(n):
        for j in range(i+1):
            print("",end= " ")

        for k in range(i,n):
            print("*",end="")


        print()

next(n)