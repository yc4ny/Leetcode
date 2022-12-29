# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        liste = []
        
        if head is None:
            return head
        elif head.next is None:
            return head
        else:
            bool = True
        
        while(bool == True):
            liste.append(head.val)
            head = head.next
            if head.next is None:
                liste.append(head.val)
                bool = False
                
        reverse = []
        for i in range(len(liste)):
            reverse.append(liste[len(liste)-1-i])
        
        head = ListNode(reverse[0])
        node = head
        for i in range(1,len(reverse)):
            node.next = ListNode(reverse[i])
            node = node.next
        
        return head
        