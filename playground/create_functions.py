# Define a procedure, sum3, that takes three
# inputs, and returns the sum of the three
# input numbers.

def sum3(num1, num2, num3):
    return num1 + num2 + num3

print (sum3(1,2,3))
#>>> 6

print (sum3(93,53,70))
#>>> 216


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
