from LinkedListsBase import *


def deleteDuplicates(head):
    if head is None:
        return None
    distinct = set()
    previous = head
    current = head.next
    while current is not None:
        distinct.add(previous.val)
        if current.val in distinct:
            previous.next = current.next
            current = current.next
        else:
            previous = current
            current = current.next
    return head


arr = [1, 1, 2, 3, 3]
ll = LinkedList(arr)
deleteDuplicates(ll.head)
ll.traverse()
