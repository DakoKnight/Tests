string = "abcabc"
substring = "ab"

flag = 0

while substring in string:
    index = string.find(substring)
    index += 1
    string = string[index:]
    index = string.find(substring)
    print(index)