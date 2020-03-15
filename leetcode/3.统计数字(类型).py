def digitCounts(k, n):   
    str1= ''
    count = 0
    for i in range(n+1):
        str1 = str1+str(i)
    list1 = list(map(int,list(str1)))
    len1 = len(list1)
    for i in range(len1):
    
        if list1[i] == k:
            count += 1
    return count
