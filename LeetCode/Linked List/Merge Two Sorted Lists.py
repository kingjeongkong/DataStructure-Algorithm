class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2
        
        return dummy.next
    

# In the parameters, [ListNode] just representing it's a Linked List. Not a list array even though it uses []. It's just for solver to recognize it's a Linked List easily

# ListNode is declared in the program already when you solve the Linked List problems. So you can just call it and use.
# And -1 in ListNode just indicates it's the beginning of the dummy Linked List. You can put any integer if you can recognize that integer is beginning. (Don't put the None. It's going to be crashed)
# current value is for merging the other Linked List into the dummy remaining that dummy is at the beginnig of the Linked List node

"""
In while loop, I tried
  current.next = list1.val
this code to just put value to next node. But it's found out that if I put just value to next node not Linked List node is going to make crash. 

Initial state:
dummy -> None
list1: 1 -> 3 -> 5 -> None
list2: 2 -> 4 -> 6 -> None

Iteration 1:
Link current.next to list1:
dummy -> 1 -> 3 -> 5 -> None
Move list1 forward to 3 -> 5 -> None.

Iteration 2:
Link current.next to list2:
dummy -> 1 -> 2 -> 4 -> 6 -> None
Move list2 forward to 4 -> 6 -> None.

Code's work would be like this. The last code 'if' would work same as above.

And lastly return the dummy.next to except the -1 node.
""" 