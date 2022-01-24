def insertionSort(arr):
    for i in range(len(arr)-1):
        j=i+1
        while j>0:
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
            else:
                break
            j-=1

insertionSort(arr)    
print(arr)
