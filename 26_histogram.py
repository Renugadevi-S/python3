#Histogram "to print symbol of given no of times"
lis=[1,2,3,4]
for i in lis:
    print(i*'@')


#using function
def histogram(lis):
    for i in lis:
        print( i*"@")
    return ""
         
print(histogram([2,2,3,4]))
