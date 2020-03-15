def merge(A,B):
    i,j = 0,0
    C=[]
    while i<len(A) and j< len(B):
        if A[i]<= B[j]:
            C.append(A[i])
            i +=1
        else:
            C.append(B[j])
            j +=1
    while i<len(A):
        C.append(A[i])
        i +=1
    while j<len(B):
        C.append(B[j])
        j +=1
    return C
