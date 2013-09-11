#############################################
# Define a procedure, sum3, that takes three
# inputs, and returns the sum of the three
# input numbers.

def sum3(num1, num2, num3):
    return num1 + num2 + num3

print (sum3(1,2,3))
#>>> 6

print (sum3(93,53,70))
#>>> 216

#############################################
# Define a procedure, abbaize, that takes
# two strings as its inputs, and returns
# a string that is the first input,
# followed by two repetitions of the second input,
# followed by the first input.


def abbaize(string1, string2):
    stringDouble = string2 + string2
    return string1 + stringDouble + string1


print (abbaize('a','b'))
#>>> 'abba'

print (abbaize('dog','cat'))
#>>> 'dogcatcatdog'

#############################################
# Define a procedure, find_second, that takes
# two strings as its inputs: a search string
# and a target string. It should return a
# number that is the position of the second
# occurrence of the target string in the
# search string.

def find_second (search, target):
    firstPos = search.find(target)
    return search.find(target, firstPos + 1)


danton = "De l'audace, encore de l'audace, toujours de l'audace"
print (find_second(danton, 'audace'))
#>>> 25

twister = "she sells seashells by the seashore"
print (find_second(twister,'she'))
#>>> 13

#############################################
# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.


def bigger (num1, num2):
    if (num1 > num2):
        return num1
    else:
        return num2

print (bigger(2,7))
#>>> 7

print (bigger(3,2))
#>>> 3

print (bigger(3,3))
#>>> 3

#############################################
# Define a procedure, is_friend, that
# takes a string as its input, and
# returns a Boolean indicating if
# the input string is the name of
# a friend. Assume I am friends with
# everyone whose name starts with D
# and no one else. You do not need to
# check for the lower case 'd'

def is_friend (string1):
    if (string1[:1] == 'D'):
        return True
    else:
        return False

print (is_friend('Diane'))
#>>> True

print (is_friend('Fred'))
#>>> False
