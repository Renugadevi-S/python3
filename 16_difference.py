 #Python program to get the difference between a given number and 17, if
 #the number is greater than 17 return double the absolute difference.

def difference(n):
    diff=n-17
    if(diff>=17):
        return diff*2
    return abs(diff)
print(difference(14))
print(difference(34))
    
