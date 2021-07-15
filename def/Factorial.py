

# Examples of factoral 

'''
functions = []
for i in range (10):
    def f():
        return i

    functions.append(f)


print ([f() for f in functions]) 
'''

'''

def factorial (n):
    if n<0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else :
        fact = 1
        while (n>1):
            fact= fact*n
            n = n-1
        return fact
num = 3
print ('Factorial of ', num ,"is" ,factorial (num))
'''


def factorial (n):
    return 1 if (n ==0 or n == 1) else n*factorial(n-1)

num = 3


print ('Factorial of ', num ,"is" ,factorial (num))