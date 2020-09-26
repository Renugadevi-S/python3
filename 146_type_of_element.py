#Python program to test if a variable is a list or tuple or a set

def type_define(x):
    if type(x) is list:
        print("list")
    elif type(x) is tuple:
        print("tuple")
    elif type(x) is set:
        print("set")
    return ""
print(type_define([1,3,4,5]))
print(type_define({1,2,3}))
