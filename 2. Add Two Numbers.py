from __future__ import annotations


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def traverse(self):
        current = self
        while current is not None:
            print(current.val)
            current = current.next

    @staticmethod
    def array_to_linked_list(arr):
        root = ListNode()
        current = root
        for i in arr[:-1]:
            current.val = i
            current.next = ListNode()
            current = current.next
        current.val = arr[-1]
        return root

    @staticmethod
    def linked_list_to_array(ll: ListNode):
        current = ll
        arr = []
        while current is not None:
            arr.append(current.val)
            current = current.next
        return arr


def addTwoNumbers(l1, l2):
    l1 = ListNode.linked_list_to_array(l1)
    l2 = ListNode.linked_list_to_array(l2)
    i1 = int("".join(([str(c) for c in l1])[::-1]))
    i2 = int("".join([str(c) for c in l2][::-1]))
    i3 = i1 + i2
    l3 = [int(c) for c in str(i3)][::-1]
    return ListNode.array_to_linked_list(l3)


l1 = ListNode.array_to_linked_list([2, 4, 3])
l2 = ListNode.array_to_linked_list([5, 6, 4])

print(addTwoNumbers(l1, l2))