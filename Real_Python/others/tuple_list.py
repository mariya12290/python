
my_tuple =('sara',6,5,0.97)
my_list = ['sara',6,5,0.97]

print(my_tuple[0])
print(my_list[0])

def EmptyFunc():
    pass

EmptyFunc()

#decorator function for capitalization of names
def names_decorator(function):
    def wrapper(arg1,arg2):
        arg1 = arg1.capitalize()
        arg2 = arg2.capitalize()
        string_hello = function(arg1,arg2)
        return string_hello
    return wrapper

@names_decorator
def say_hello(name1,name2):
    return 'Hello '+name1+' ! Hello '+name2+' ! '
print(say_hello('suri','kumar'))

#deep and swallo copy
from copy import copy, deepcopy

list_1 =[1,2,[3,4],5]

#shallow copy
list_2 = copy(list_1)
list_1[2].append(6)
list_2[2] = 7
print(list_1)
print(list_2)

print("--------------------------------------------------------")
#pass by reference or by value
#pass_by reference
def pass_by_ref(arr):
    arr.append(4)

ls =[1,2,3]

print(ls)
pass_by_ref(ls)
print(ls)

#pass by value
def pass_by_value(st):
    st +=(' suri')
st='kumar'
print(st)
pass_by_value(st)
print(st)
print(st+ ' suri  ')

string = "THis is a string"
string_list = string.split() #returns string of list, here delimiter is space
print(string_list)


def check_distinct(data_list):
    if(len(data_list ))== len(set(data_list)):
        return True
    else:
        return False

print(check_distinct([1,1,2,3,45])) #false
print(check_distinct([1,2,3,4])) #true