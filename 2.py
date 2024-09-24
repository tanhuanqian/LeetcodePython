class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        cur1 = l1
        cur2 = l2
        overflow = False
        while cur1 and cur2:
            if overflow:
                cur1.val += 1
                overflow = False
            cur1.val = cur1.val + cur2.val
            if cur1.val >= 10:
                cur1.val -= 10
                overflow = True
            cur1 = cur1.next
            cur2 = cur2.next
        while cur1:
            if overflow:
                cur1.val += 1
                overflow = False
            if cur1.val >= 10:
                cur1.val -= 10
                overflow = True
            cur1 = cur1.next
        if overflow:
            temp = ListNode(1)
            cur1.next = temp
        return l1

def create_linked_list(lst):
    dummy = ListNode()
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

l1 = create_linked_list([9,9,9,9,9,9,9])
l2 = create_linked_list([9,9,9,9])
solution = Solution()
reorder = solution.addTwoNumbers(l1,l2)
print_linked_list(reorder)