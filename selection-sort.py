def selectSort(nums,start):
  if start <= len(nums) - 1:
    index = nums[start]
    for i  in range(start, len(nums)):
      if index > nums[i]:
        temp = index
        index = nums[i]
        nums[i] = temp
    nums[start] = index
    selectSort(nums, start +  1)

nums = [3, 2, 1]
selectSort(nums, 0)
print(nums)