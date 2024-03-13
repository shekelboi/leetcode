class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, arr=None, head=None):
        self.head = None
        if head is not None:
            self.head = head
        if arr is not None and len(arr) > 0:
            self.head = ListNode(arr[0])
            current = self.head
            for i in range(1, len(arr)):
                current.next = ListNode(arr[i])
                current = current.next

    def traverse(self):
        current = self.head
        while current is not None:
            print(f"{current.val} ", end="")
            current = current.next
        print()

    @staticmethod
    def traverse_from_head(head):
        while head is not None:
            print(f"{head.val} ", end="")
            head = head.next
        print()
