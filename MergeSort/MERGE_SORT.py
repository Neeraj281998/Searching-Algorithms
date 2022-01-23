def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=mergeSort(arr[:mid])
    right=mergeSort(arr[mid:])
    return merge(left,right)

def merge(left,right):
    lCount=0
    rCount=0
    result=[]
    while lCount<len(left) and rCount<len(right):
        if left[lCount]<right[rCount]:
            result.append(left[lCount])
            lCount+=1
        else:
            result.append(right[rCount])
            rCount+=1
    result+=left[lCount:]
    result+=right[rCount:]

    return result

arr=[83,23,5,7,8,32,-2,857,47,-98,9]
print(mergeSort(arr))
