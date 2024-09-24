# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        store = []
        temp= head
        while temp:
            store.append(temp)
            temp=temp.next
        newhead = store[0]
        tail = None
        for i in range(len(store)//2):
            store[i].next=store[-1-i]
            store[i].next.next=store[i+1]
            tail=store[i].next.next
        if tail:
            tail.next = None
        head=newhead
        return head
    
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
reorder = solution.reorderList(head)
print_linked_list(reorder)