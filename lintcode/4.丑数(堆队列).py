'''
利用堆进行操作，每次将其入堆，则堆的heap就是最小元素
'''
def nthUglyNumber(n):
    visited = [1]
    vactor = [2,3,5]
    for i in range(n):
        x = heapq.heappop(visited)
        for j in [2,3,5]:
            if x*j not in visited:
                heapq.heappush(visited,x*j)
    return x
