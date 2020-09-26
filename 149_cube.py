# Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the
# specified number


def cube(n):
    sum1=0
    for i in range(n,0,-1):
        total=i*i*i
        sum1=sum1+total
    print(sum1)
    return ""
print(cube(8))
        
        
