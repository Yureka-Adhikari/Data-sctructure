#First method

def fun1(n):
    return n*(n+1)/2

print(fun1(4))

#For function 1 algorithm goes like this : (4*5)/2

#second method
def fun2(n):
    for i in range(1,n+1):
        sum += 1
    return sum
print(fun2(4))

#Third Method

def fun3(n):
    sum = 0
    for i in range(1,n+1):
        
        for j in range(1,i+1):
            sum += 1
            
    return sum
print(fun3(4))
