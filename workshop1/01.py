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

    point1, point2 = A1, B2

    while point1 and point2:
        if point1.val == point2.val:
            t1, t2 = point1, point2
            while t1 and t2 and t1.val == t2.val:
                t1 = t1.next
                t2 = t2.next
            if t1 is None and t2 is None:
                return point1
        point1 = point1.next
        point2 = point2.next

    return None





def build_list(arr):
    head = None
    for x in arr:
        head = append_list(head, x)
    return head


def run_tests():
    tests = [
        # (listA, listB, expected)

        ([1,2,3,4,5], [9,8,3,4,5], 3),
        ([1,2,3], [4,5,6], None),
        ([1,2,3], [1,2,3], 1),
        ([7], [7], 7),
        ([7], [8], None),

        ([1,2,3,4,5], [4,5], 4),
        ([4,5], [1,2,3,4,5], 4),
        ([1,2,3,4,5], [2,3,4,5], 2),
        ([1,2,3,4,5], [5], 5),
        ([1,2,3,4,5], [6,5], 5),

        ([1,2,3,4,5], [8,9,5], 5),
        ([1,2,3,4], [0,3,4], 3),
        ([1,2,3,4], [5,6,3,4], 3),

        ([1,2,3,4,5], [3,4,6], None),

        ([1,1,1,2,3], [9,1,2,3], 1),
        ([2,2,2,2], [2,2], 2),
        ([1,2,1,2,3], [1,2,3], 1),

        ([], [1,2,3], None),
        ([], [], None),
        ([1, 2, 3], [4, 2, 3], 2),
    ]

    for i, (a, b, expected) in enumerate(tests, 1):
        headA = build_list(a)
        headB = build_list(b)

        result = solution(headA, headB)

        result_val = result.val if result else None

        assert result_val == expected, f"Test {i} failed: got {result_val}, expected {expected}"

    print("All tests passed!")


run_tests()


headA = build_list([4, 2, 3])
headB = build_list([1, 2, 3])

result = solution(headA, headB)
print(result.val)