nums= [4,1,2,3,5,8,12,35,47,21,1,0,34]
i=0
j=2
while (i<len(nums)):
    if (j>len(nums)-1):
        i+=2
        j=i+2

    elif  (nums[i] <= nums[j]):
        j+=2
    else:
        nums[i],nums[j]=nums[j],nums[i]
        j+=2
k=1
l=3
while (k < len(nums)):
    if (l>len(nums)-1):
        k+=2
        l=k+2

    elif  (nums[k] >= nums[l]):
        l+=2
    else:
        nums[k],nums[l]=nums[l],nums[k]
        l+=2



print(nums)