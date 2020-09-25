#Python program to sort three integers without using conditional statements
#and loops.

no=1,4,3
print(sorted(no))


#otherwise use min,max function

x=int(input("enter no1"))
y=int(input("enter no2"))
z=int(input("enter no3"))
small_value=min(x,y,z)
large_value=max(x,y,z)
middle_value=((x+y+z)-(small_value+large_value))
print(small_value,middle_value,large_value)
            
