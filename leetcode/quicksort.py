
def quick_sort(array):
    if len(array) <=1:
        return array
    else:
        pick = array[-1]
        less = []
        great = []
        for i in array:
            if array[i] < pick:
                less.append(array[i])
        for i in array:
            if array[i] > pick:
                great.append(array[i])
        return quick_sort(less)+[pick]+quick_sort(great)
    
    
        

    

