from LinkedListsBase import ListNode, LinkedList
from typing import Optional


def isPalindrome(head: Optional[ListNode]) -> bool:
    arr = []
    while head is not None:
        arr.append(head.val)
        head = head.next

    left, right = 0, len(arr) - 1

    while left <= right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1

    return True


ll = LinkedList([1, 2, 2, 1])
print(isPalindrome(ll.head))