def sortColors(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    redBucket = 0
    whiteBucket = 0
    blueBucket = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            redBucket = redBucket + 1
        if nums[i] == 1:
            whiteBucket = whiteBucket + 1
        if nums[i] == 2:
            blueBucket = blueBucket + 1
    for i in range(redBucket):
        nums[i] = 0
    for i in range(whiteBucket):
        nums[i+redBucket] = 1
    for i in range(blueBucket):
        nums[i+redBucket+whiteBucket] = 2 
