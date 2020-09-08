#find the given word is polindrome or not
n=input("enter the elements:")
print(n)
n1=n[-1::-1]
print(n1)
if(n==n1):
    print("polindrome")
else:
    print("not a polindrome")


