# String Rotation: Assume you have a method isSubst ring which checks if one word is a substring
# of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
# call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").

def isSubstring(string):
    # Assume it's implemented, returns True or False
    pass

# Check if string2 is a rotation of string1
def stringRotation(string1, string2):

    # Return false if string1 and string2 are not the same length
    if len(string1) != len(string2):
        return False
    if string1 == string2:
        return True
    
    for i in range(len(string1)):
        x = string1[i:]
        y = string1[:i] 
        if x+y == string2:
            return True

    return False

string1, string2 = "dantome", "tomedan"
s1, s2, = "dantomelovemayamok", "mayamokdantomeelove"
print(stringRotation(s1, s2))