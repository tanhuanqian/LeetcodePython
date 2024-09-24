class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        newlist = None
        curr = head

        while curr:
            print(curr.val)
            next_temp = curr.next
            curr.next = newlist
            newlist = curr
            curr = next_temp

        return newlist

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

head = create_linked_list([1, 2, 3, 4, 5])
solution = Solution()
print("Original List:")
print_linked_list(head)

reversed_head = solution.reverseList(head)
print("Reversed List:")
print_linked_list(reversed_head)
