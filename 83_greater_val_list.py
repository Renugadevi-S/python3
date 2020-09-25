#program to test whether all numbers of a list is greater than a certain number

def list_container(list1,n):
    for elements in list1:
        if elements>=n:
            print(True)
        else:
            print(False)
    return""
print(list_container([3,4,6,8],7))
        
