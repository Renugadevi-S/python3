#num is multiples of 3 and 5 print fizzbuzz
#num is multiples of 3 not 5 print fizz
#num is multiples of 5 not 3 print buzz
#else print num as it is
def fizzBuzz(n):
    for num in range(1,n+1):
        if i%3==0 and i%5==0:
            print ("fizzBuzz")
        elif i%5==0 and i%3!=0:
            print ("Buzz")
        elif i%3==0 and i%5!=0:
            print ("fizz")
        elif i%3!=0 and i%5!=0:
            print(num)
    return ("")    
    
print(fizzBuzz(15))
