#Write a Python program that accepts an integer (n) and computes the value of
#n+nn+nnn. Go to the editor
#Sample value of n is 5
#Expected Result : 615

n=int(input("enter the number"))
no1=n
no2=(n*10)+no1
no3=(n*100)+no2
total=no1+no2+no3
print(total)

