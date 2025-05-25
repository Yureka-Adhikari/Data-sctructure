def fun1(n, m):
    return n * m

def fun2(n, m):
    sum = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            sum += 1
    return sum
    
print(f"Product is : {fun1(4, 5)}")
print(f"Product is : {fun2(4, 5)}")
