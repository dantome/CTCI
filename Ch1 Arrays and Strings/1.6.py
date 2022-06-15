# 1.6 String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).


def stringCompression1(string):
    compressed = ""
    currChar = None
    currCharCount = 0
    for char in string:
        # Still counting same character
        if char == currChar:
            currCharCount += 1
        # Moving onto different character
        elif currCharCount>0 and char != currChar:
            compressed += currChar
            compressed += str(currCharCount)
            currChar = char
            currCharCount = 1
        # If char is the first character in the string
        else:
            currChar = char
            currCharCount += 1
    compressed += currChar
    compressed += str(currCharCount)
    return compressed if len(compressed) < len(string) else string


def stringCompression2(string):
    compressed = ""
    currChar = string[0]
    currCharCount = 1
    for i in range(1, len(string)):
        # Still counting same character
        if string[i] == currChar:
            currCharCount += 1
        # Else, we move onto another character, so add to string, then reset count
        else:
            compressed+=currChar
            compressed+=str(currCharCount)
            currChar=string[i]
            currCharCount=1
    compressed+=currChar
    compressed+=str(currCharCount)
    return compressed if len(compressed) < len(string) else string


print(stringCompression1("aaabbbccdddccccdeef"))
print(stringCompression2("aaabbbccdddccccdeef"))