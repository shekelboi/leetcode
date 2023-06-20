from LinkedListsBase import ListNode, LinkedList
from typing import Optional


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    previous = None
    current = head

    while current is not None:
        temp_next = current.next
        current.next = previous
        previous = current
        current = temp_next

    return previous


ll = LinkedList([1, 2, 3, 4, 5])
ll.traverse()
head = reverseList(ll.head)
LinkedList.traverse_from_head(head)