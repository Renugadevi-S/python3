 #Python program to calculate the sum of three given numbers,
 #if the values are equal then return three times of their sum
def sum(no1,no2,no3):
    total=no1+no2+no3
    if no1==no2==no3:
        return 3*total
    return total
print(sum(2,3,5))
print(sum(3,3,3))
