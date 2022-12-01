from __future__ import annotations


# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def create_list(arr: list):
        if len(arr) == 0:
            return None

        head = ListNode(val=arr[0])
        current = head
        for a in arr[1:]:
            current.next = ListNode(a, None)
            current = current.next
        return head

    @staticmethod
    def traverse_list(current: ListNode):
        arr = []
        while current is not None:
            arr.append(current.val)
            current = current.next
        return arr


def mergeTwoLists(list1, list2):
    head = ListNode()
    mergedList = head

    while list1 is not None and list2 is not None:
        if list1.val < list2.val:
            mergedList.next = list1
            list1 = list1.next
        else:
            if list2 is not None:
                mergedList.next = list2
                list2 = list2.next
        mergedList = mergedList.next

    if list1 is not None:
        mergedList.next = list1
    if list2 is not None:
        mergedList.next = list2

    return head.next


list1 = ListNode.create_list([1, 2, 4])
list2 = ListNode.create_list([1, 3, 4])
res = mergeTwoLists(list1, list2)
print(ListNode.traverse_list(res))
