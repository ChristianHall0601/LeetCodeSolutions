def findMedianSortedArrays(nums1, nums2):
    merged = nums1+nums2
    ordered = orderList(merged)
    if len(ordered)%2 == 1:
        return ordered[len(ordered)//2]
    else:
        return (ordered[(len(ordered)//2) - 1] + ordered[len(ordered)//2])/2

def orderList(myList):
    tempList = myList
    resList = []
    while len(tempList) != 0:
        small = tempList[0]
        for i in range(len(tempList)):
            if small > tempList[i]:
                small = tempList[i]
        resList.append(small)
        tempList.remove(small)
    return resList
        
