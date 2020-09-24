#Python program that will return true if the two given integer values are equal
#or their sum or difference is 5

def sum(no1,no2):
    total=no1+no2
    diff=no1-no2
    if total==5 or diff==5:
        print("True")
    elif no1==no2:
        print("true")
    else:
        print("false")
    return ""
print(sum(10,5))
print(sum(4,5))

              
        
