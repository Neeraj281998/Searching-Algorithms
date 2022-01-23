'''
Time Complexity 
O(n2)

'''
def BUBBLE_SORT(nums):
    for i in range(len(nums)):          #iteration == len(nums)*len(nums)
        for j in range(1,len(nums)):    
            if (nums[j-1]>nums[j]):
                nums[j-1],nums[j]=nums[j],nums[j-1]


nums=[5, 3,2, 8,1,-9 ,6, 7,-11, 2]
BUBBLE_SORT(nums)
print(nums)