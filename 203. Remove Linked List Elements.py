from LinkedListsBase import ListNode, LinkedList
from typing import Optional


def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    previous = None
    current = head
    while current is not None:
        if current.val == val:
            if previous is not None:
                previous.next = current.next
                current = current.next
            else:
                head = current.next
                current = head
                previous = None
        else:
            previous = current
            current = current.next
    return head


ll = LinkedList([2, 2, 1, 2, 6, 3, 4, 5, 6])
ll.traverse()
ll.head = removeElements(ll.head, 2)
ll.traverse()