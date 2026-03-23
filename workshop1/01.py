class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def append_list(head, value):
    if head is None:
        return ListNode(value)
    current = head
    while current.next:
        current = current.next
    current.next = ListNode(value)
    return head

def copy_list(head):
    if not head:
        return None
    new_head = ListNode(head.val)
    current_old = head.next
    current_new = new_head
    while current_old:
        current_new.next = ListNode(current_old.val)
        current_new = current_new.next
        current_old = current_old.next
    return new_head

def get_tail(head):
    while head.next:
        head = head.next
    return head

def solution(headA, headB):
    A1 = copy_list(headA)
    B1 = copy_list(headB)

    A2 = copy_list(headA)
    B2 = copy_list(headB)

    if A1:
        get_tail(A1).next = B1

    if B2:
        get_tail(B2).next = A2

    pA, pB = A1, B2

    while pA and pB:
        if pA.val == pB.val:
            return pA
        pA = pA.next
        pB = pB.next

    return None
