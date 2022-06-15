# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

string = 'macbok'
stringHasAllUniqueCharacters = True

myset = set()
for char in string:
    if char not in myset:
        myset.add(char)
    else:
        stringHasAllUniqueCharacters = False

print(stringHasAllUniqueCharacters)



# If we cannot use an additional data structure, we could use a double for loop to check every character with
# every other character.

# string = 'abcdefu'
# stringHasAllUniqueCharacters = True
# for i in range(len(string)):
#     for j in range(i+1, len(string)):
#         if string[i] == string[j]:
#             stringHasAllUniqueCharacters = False
#             break

# print(stringHasAllUniqueCharacters)