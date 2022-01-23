def QuickSort(arr,low,hi):
    if(low>=hi):
        return 
    start=low
    end=hi
    mid=(start+end)//2
    pivot=arr[mid]
    while (start<=end):
        while (arr[start]<pivot):
            start+=1
        while (arr[end]>pivot):
            end-=1
        if (start<=end):
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1
    QuickSort(arr,low,end)
    QuickSort(arr,start,hi)
arr=[5,4,3,2,1,-1,-2,-3,-4,-5]
QuickSort(arr,0,len(arr)-1)
print(arr)

        
