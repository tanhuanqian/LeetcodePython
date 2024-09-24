class ListNode(object):
    def __init__(self, val=0, next=None, random = None):
        self.val = val
        self.next = next
        self.random = random
class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        mapping = {}
        curr = head
        while curr:
            mapping[curr] = ListNode(curr.val, None, None)
            curr = curr.next
        curr = head
        while curr:
            if curr.next:
                mapping[curr].next = mapping[curr.next]
            if curr.random:
                mapping[curr].random = mapping[curr.random]
            curr = curr.next
        return mapping[head]

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

head = create_linked_list([[7,None],[13,0],[11,4],[10,2],[1,0]])
n = 2
solution = Solution()
reorder = solution.copyRandomList(head)
print_linked_list(reorder)