# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        head = ListNode(0)  # Initialize the dummy head node
        current = head
        
        while l1 or l2 or carry:
           # Gettin and summing the values
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            
            
            carry = total // 10
            
            # Create the new node with the ones place of the sum
            current.next = ListNode(total % 10)
            current = current.next  
            
            # Move to the next nodes in the lists if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        
        return head.next

if __name__ == "__main__":
    l1 = ListNode()
    l2 = ListNode()
    sol = Solution()
    #print(sol.addTwoNumbers(l1,l2))