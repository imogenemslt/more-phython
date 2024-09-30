def factorial(x):
    if x == 1:
        return 1
    return(x * factorial(x-1))

num = int(input("enter a number that needs factorialing: "))
print(num,"! is", factorial(num))


#task 3 pg209
def function(x):
    if x == 1:
        return 1
    return(x + function(x-1))

num= int(input("enter a num: "))
print(num, "=",function(num))


#task 3 (but for loop)
num = int(input("enter number: "))
for i in range (num,1,-1):

#task 1 pg 209
def fibonacci():
    fib = [0, 1]
    while len(fib) < 8:
        fib.append(fib[-1] + fib[-2])
    return fib[:8]


print(fibonacci())

#task 2
    
