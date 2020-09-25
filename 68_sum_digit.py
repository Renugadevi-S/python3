#Python program to calculate the sum of the digits in an integer
rev=0
dig=0
total=0
no1=int(input("num"))
while(no1!=0):
    dig=no1%10
    rev=rev*10+dig
    
    no1=no1//10
    print(rev)


