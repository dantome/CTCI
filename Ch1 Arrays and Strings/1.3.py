# URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)

# EXAMPLE
# Input: "Mr John Smith"
# Output: "Mr%20John%20Smith"

string1 = "I love you Maya Moktan"


# Approach 1: str.replace
# string1 = string1.replace(" ", "%20")
# print(string1)

# Approach 2: Build new string by iterating through string1, replacing spaces with %20
add = "%20"
answer = ""
for char in string1:
    if char == " ":
        answer += add
    else:
        answer += char

print(answer)