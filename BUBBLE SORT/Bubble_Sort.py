def bubbleSort(arr,length):
    for i in range(length-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
        
    if length>1:
        bubbleSort(arr,length-1)
    else:
        return 

arr=[122,32,3,1,-3,232,4,-33]
bubbleSort(arr,len(arr))
print(arr)