# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        
        list3 = ListNode()

        while list1 and list2:
            print(list3)
            if list1.val > list2.val:
                list3.next = list2
                list3 = list2
                list2 = list2.next
            else:
                list3.next = list1
                
                list1 = list1.next

        if list1:
            list3.next = list1
        elif list2:
            list3.next = list2
        
        return list3.next

