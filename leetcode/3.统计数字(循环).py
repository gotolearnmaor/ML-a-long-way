def digitCounts(k, n):
    if not n>=0:
        print('false n')
    if not (0<=k<=9):
        print('false k')
    else:
        count = 0
        for i in range(n+1):
            j = i
            while True:
                if j%10 ==k:
                    count +=1
                j //= 10
                if j==0:
                    break
        return count
