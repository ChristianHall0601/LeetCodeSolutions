#Given an array, rotate the array to the right by k steps, where k is non-negative

#Input nums = [1, 2, 3, 4, 5, 6, 7] k = 3
#Output nums = [5, 6, 7, 1, 2, 3, 4]

def toTheRight(numList, steps):
    for i in range(steps):
        numList = lastToFront(numList)
    print(numList)

def lastToFront(List):
    lastItem = []
    lastList = []
    for i in range(len(List)-1):
        lastList.append(List[i])
    lastItem.append(List[len(List)-1])
    return(lastItem + lastList)
    
        
