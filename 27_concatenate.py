#Python program to concatenate all elements in a list into a string and
#return it

def concatenation(lis):
  result=""
  for elements in lis:
    result+=str(elements)
  return result

print(concatenation([1,2,3,4]))
