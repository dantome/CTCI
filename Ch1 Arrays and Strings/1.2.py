# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.

# Plan
# Find out which string is the smallest, if the smallest string is of length 3, then find all 3 character permutations
# of the longer string, and check to see if any of them are the same as the smaller string

def checkPermutation(string1, string2):

    if len(string1) == len(string2):
        if string1 == string2:
            isPermutation = True
        else:
            isPermutation = False
        return isPermutation

    if len(string1) > len(string2):
        shortString, longString = string2, string1
    else:
        shortString, longString = string1, string2

    isPermutation = False

    for i in range(len(longString)-len(shortString)+1):
        substring = longString[i:len(shortString)+i]
        if shortString == substring:
            isPermutation = True

    return isPermutation

string1 = "danielchristophertome"
string2 = "chris"

print(checkPermutation(string1, string2))