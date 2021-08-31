from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def in_order_traversal(root: TreeNode) -> list:
    """Perform an in order tree traversal.

    Args:
        root (TreeNode): The root node.

    Returns:
        list: A list of nodes sorted in in order traversal order.
    """
    result = []
    if root is None:
        return []
    result += in_order_traversal(root.left)
    result.append(root.val)
    result += in_order_traversal(root.right)
    return result


def pre_order_traversal(root: TreeNode) -> list:
    """Perform a pre order tree traversal.

    Args:
        root (TreeNode): The root node.

    Returns:
        list: A list of nodes sorted in pre order traversal order.
    """
    result = []
    if root is None:
        return []
    result.append(root.val)
    result += in_order_traversal(root.left)
    result += in_order_traversal(root.right)
    return result


def post_order_traversal(root: TreeNode) -> list:
    """Perform a post order tree traversal.

    Args:
        root (TreeNode): The root node.

    Returns:
        list: A list of nodes sorted in post order traversal order.
    """
    result = []
    if root is None:
        return []
    result += in_order_traversal(root.left)
    result += in_order_traversal(root.right)
    result.append(root.val)
    return result


def level_order_traversal(root: TreeNode) -> list[list]:
    """Perform a level order tree traversal.

    Args:
        root (TreeNode): The root node.

    Returns:
        list[list]: A list of lists where the index of each sublist is the level
        in the tree, and the elements of that sublist are the nodes at that level
        from left to right.
    """
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
    """Generate a list of tree nodes using level order traversal.
        Notably, missing children nodes are denoted with an "X".
        This is so that the tree can be completely reconstructed
        from just the output list.

    Args:
        root (TreeNode): The root node.

    Returns:
        list: Tbe list of nodes in level order traversal order. Missing
        children are denoted with an "X".
    """
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
    """Construct a tree from a level order traversal list of nodes.

    Args:
        nodes (list): A list of nodes from a level order traversal. Missing
        children need to be denoted as "X".

    Returns:
        Optional[TreeNode]: Returns the root node of the new tree.
    """
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


def invert(root: TreeNode) -> TreeNode:
    return TreeNode(0)


def diameter(root: TreeNode) -> int:
    return 0


def max_depth(root: TreeNode) -> int:
    return 0


def check_bst(root: TreeNode) -> bool:
    return True


def check_balanced(root: TreeNode) -> bool:
    return True
