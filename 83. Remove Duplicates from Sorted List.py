# poor solution, but it works

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        lst = []
        nxt = 0
        

        while nxt != None:
            lst.append(head.val)
            nxt = head.next
            head = head.next
        
        lst = list(set(lst))
        lst.sort()
        print(lst)
        new = ListNode()
        dummy = new

        for value in lst:
            dummy.next = ListNode(value)
            dummy = dummy.next
        return new.next
        