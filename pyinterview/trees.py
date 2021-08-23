from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def in_order_traversal(root: TreeNode) -> list:
    result = []
    if root is None:
        return []
    result += in_order_traversal(root.left)
    result.append(root.val)
    result += in_order_traversal(root.right)
    return result


def pre_order_traversal(root: TreeNode) -> list:
    result = []
    if root is None:
        return []
    result.append(root.val)
    result += in_order_traversal(root.left)
    result += in_order_traversal(root.right)
    return result


def post_order_traversal(root: TreeNode) -> list:
    result = []
    if root is None:
        return []
    result += in_order_traversal(root.left)
    result += in_order_traversal(root.right)
    result.append(root.val)
    return result


def level_order_traversal(root: TreeNode) -> list[list]:
    if root is None:
        return []

    q = deque()
    q.append(root)

    result = []

    while q:
        level = []
        for _ in range(len(q)):
            current = q.popleft()
            level.append(current.val)
            for branch in current.left, current.right:
                if branch:
                    q.append(branch)

        result.append(level)

    return result


def serialize(root: TreeNode) -> list:
    if not root:
        return []

    q = deque()
    q.append(root)

    result = []
    while len(q) > 0:
        current = q.popleft()
        if current:
            result.append(str(current.val))
        else:
            result.append("X")
            continue

        for branch in [current.left, current.right]:
            q.append(branch)

    return result


def deserialize(nodes: list) -> Optional[TreeNode]:
    if not nodes:
        return None

    root = TreeNode(int(nodes[0]))
    q = deque()
    q.append(root)

    i = 1

    while len(q) > 0:
        current = q.popleft()

        if nodes[i] != "X":
            current.left = TreeNode(int(nodes[i]))
            q.append(current.left)
        i += 1

        if nodes[i] != "X":
            current.right = TreeNode(int(nodes[i]))
            q.append(current.right)
        i += 1

    return root
