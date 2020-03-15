"""
三个因子分别和每一个序列中的元素相乘，但每次都取最小

"""

#可利用set消除重复元素

def nthUglyNumber(n):
        
    a, b, c = 0, 0, 0
    res = [1]
    while len(res) < n:
        ugly = min(res[a] * 2, res[b] * 3, res[c] * 5)
        res.append(ugly)
        if ugly == res[a] * 2:
            a += 1
        if ugly == res[b] * 3:
            b += 1
        if ugly == res[c] * 5:
            c += 1
    return res[-1]
