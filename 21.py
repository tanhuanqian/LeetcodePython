class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        newlist = ListNode()
        current = newlist
        while list1 and list2:
            if list1.val > list2.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
            current = current.next
        
        current.next = list1 or list2 
        return newlist.next 
    
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

head1 = create_linked_list([1, 2, 4])
head2 = create_linked_list([1, 3, 4])
solution = Solution()
merged_list = solution.mergeTwoLists(head1, head2)
print_linked_list(merged_list)
