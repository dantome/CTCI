# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.

# EXAMPLE
# pale, ple -> true
# pale, pales -> true
# pale, paxle -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false

def oneAway(string1, string2):
    # In the case that they are zero edits away
    if string1 == string2:
        return True
    
    numEdits = 0

    # In the case that we replaced a character
    if len(string1) == len(string2):
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                numEdits+=1
        return False if numEdits>1 else True

    # In the case that we added or deleted a character
    if len(string1) < len(string2):
        smallerString, largerString = string1, string2
    else:
        smallerString, largerString = string2, string1
    i, j = 0,0
    while j<len(largerString):
        if i==len(smallerString):
            numEdits+=1
            j+=1
        elif smallerString[i] != largerString[j]:
            numEdits+=1
            j+=1
        else:
            i+=1
            j+=1
    return False if numEdits>1 else True


def runTests():
    assert(oneAway("pale", "paled") == True)
    assert(oneAway("pale", "paledd") == False)
    assert(oneAway("bale", "pale") == True)
    assert(oneAway("ple", "pale") == True)
    assert(oneAway("le", "paled") == False)
    assert(oneAway("daniel", "danie") == True)
    assert(oneAway("may", "maya") == True)
    print("All 7 test cases passed successfully!")

runTests()


