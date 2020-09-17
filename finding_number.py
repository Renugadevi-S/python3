#To find the given value is in the list or not
def grp_data(elements,n):
    for values in elements:
        if values==n:
            return True
    return False
print(grp_data([2,4,6,7],2))
print(grp_data([2,4,6,7],8))


    
