# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    stringNode1 = ""
    stringNode2 = ""
    result = ""
    resultList = ListNode()
    cur = resultList
    while l1:
        stringNode1 = stringNode1 + str(l1.val)
        l1 = l1.next
    while l2:
        stringNode2 = stringNode2 + str(l2.val)
        l2 = l2.next

    stringNode1 = stringNode1[::-1]
    stringNode2 = stringNode2[::-1]
    result = int(stringNode1) + int(stringNode2)
    result = str(result)
    result = result[::-1]
    for i in range(len(result)):
        cur.val = result[i]
        if i < len(result)-1:
            cur.next = ListNode()
            cur = cur.next
    return resultList
    
