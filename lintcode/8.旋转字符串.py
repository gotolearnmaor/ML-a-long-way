def rotateString(s, offset):
    l = offset %len(s)
    if l < 1:
        return s
    temp = offset + 1
    result = ''
    str1 = s[:temp]
    str2 = s[temp:]
    result = str2 + str1
    return result
