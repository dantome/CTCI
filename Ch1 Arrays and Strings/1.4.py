# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat". "atco cta". etc.)

# Approach: a palindrome has an even amount of each character except possibly one.

string1 = "tactoox coa"
string1 = string1.replace(" ", "")
isPalindromePermutation = False

storeSet = set()
for char in string1:
    if char not in storeSet:
        storeSet.add(char)
    else:
        storeSet.remove(char)

if len(storeSet) <= 1:
    isPalindromePermutation = True

print(isPalindromePermutation)
