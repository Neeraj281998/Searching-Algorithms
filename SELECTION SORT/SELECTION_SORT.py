'''
Time Complexity
Best case   = O(n2)
Worst case  = O(n2)
Average case= O(n2)

'''
def selectionSort(nums):
    for step in range(len(nums)):
        min_val=step                           #Default minimum value is step
        for i in range(step+1,len(nums)):      #Starting from step+1 index because.. compair step with above index
            if nums[i]<nums[min_val]:
                min_val=i                      # If above value is small then we are assigning it to min_value
        # i iteration get over ...now we got the smallest value index 
        #Now swapping smallest value index(min_val) with step(First iteration val)
        nums[step],nums[min_val]=nums[min_val],nums[step]

nums=[-3,23,2,0,-10,34]
selectionSort(nums)
print(nums)

