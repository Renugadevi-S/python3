#Python program to get the n (non-negative integer) copies of the first 2
#characters of a given string. Return the n copies of the whole string if the
#length is less than 2
n=int(input("enter number"))
def string(str1):
     
     lenght=len(str1)
     if lenght >2:
         return str1[0:2]*n
     return str1*n
print(string("renu"))
print(string("re"))
