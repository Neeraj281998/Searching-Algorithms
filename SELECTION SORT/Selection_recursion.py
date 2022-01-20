def selectionSort(arr,i,length):
    min_index=i
    for j in range(i+1,length):
        if arr[j]<arr[min_index]:
            min_index=j
    
    arr[min_index],arr[i]=arr[i],arr[min_index]
    if i+1<length:
        selectionSort(arr,i+1,length)

arr=[3, 5, 8, 4, 1, 9, -2]
selectionSort(arr,0,len(arr))
print(arr)