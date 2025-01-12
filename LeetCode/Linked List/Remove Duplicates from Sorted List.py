# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        current = dummy
        previous = None

        while head:
            if previous == None:
                current.next = head
                current = current.next
            elif head.val != previous.val:
                current.next = head
                current = current.next
            
            previous = head
            head = head.next

        current.next = None

        return dummy.next
        

# Simpler Solution
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head
    

# Linked List is saved by reference. So just doing 'current = head' and modifying current can also change the head List.

# It's not Doubly-linked list, so I figured it out with previous I declared node.

# But this problem is about Singly-linked list sorted, so I didn't have to declare previous. I could just check the node and node.next directly.
# And move the current node only if the node's value and node.next's value is different. If not just keep moving the current.next node until find the node that has the different value.

# And also all I have to do is modifying just one Singly-linked list. So I didn't have to declare dummy linked list to put extra linked list.