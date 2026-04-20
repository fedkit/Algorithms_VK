from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None

    def build_tree(self, arr):
        if not arr or arr[0] is None:
            self.root = None
            return

        self.root = TreeNode(arr[0])
        queue = deque([self.root])
        i = 1

        while i < len(arr):
            current = queue.popleft()

            if i < len(arr) and arr[i] is not None:
                current.left = TreeNode(arr[i])
                queue.append(current.left)
            i += 1

            if i < len(arr) and arr[i] is not None:
                current.right = TreeNode(arr[i])
                queue.append(current.right)
            i += 1

    def bfs(self):
        if not self.root:
            return []

        q = deque([self.root])
        answer = []

        while q:
            current = q.popleft()
            answer.append(current.val)

            if current.left:
                q.append(current.left)

            if current.right:
                q.append(current.right)

        return answer


        
    
tree_test = BinaryTree()
tree_test.build_tree([1, 2, 3, 4, 5, None, 6])

print(tree_test.bfs())