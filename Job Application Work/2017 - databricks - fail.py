# Give the root of a tree and a specific node, find the shortest path from the specific node to any leaf (can backtrack
# up the tree)

"""
Attempted to find the shortest downward distance to a leaf from each node on the downward recursive path and to merge
this information (to account for the closest leaf being through an ancestor node) while unwinding the recursive stack
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_closest_leaf_to_node(root, node):
    _, closest_leaf, ancestor_distance = recursive_find_closest_leaf_to_node(root, node)
    if ancestor_distance is None:
        return None
    return closest_leaf.value


def recursive_find_closest_leaf_to_node(root, node):

    # The current root is a leaf
    if not root.left and not root.right:
        return 1, root, 0 if root == node else None

    left_min, left, left_ancestor_distance = None, None, None
    right_min, right, right_ancestor_distance = None, None, None
    if root.left:
        left_min, left, left_ancestor_distance = recursive_find_closest_leaf_to_node(root.left, node)
    if root.right:
        right_min, right, right_ancestor_distance = recursive_find_closest_leaf_to_node(root.right, node)

    # Current root is an ancestor of the node from which to perform the search, which is down the left branch
    # Recursively find the closest leaf (descendant or ancestral):
    # - it is the current closest leaf from the left branch or the closest leaf down the right branch + the ancestor
    #   distance
    # - each level adds 1 to the ancestor distance
    if left_ancestor_distance is not None:
        if right_min and right_min + left_ancestor_distance + 1 < left_min:
            return right_min, right, left_ancestor_distance + 1
        else:
            return left_min, left, left_ancestor_distance + 1

    # Same as above, but the node from which to perform the search is down the right branch
    elif right_ancestor_distance is not None:
        if left_min and left_min + right_ancestor_distance + 1 < right_min:
            return left_min, left, right_ancestor_distance + 1
        else:
            return right_min, right, right_ancestor_distance + 1

    # Current root is a descendant of, or is, the node from which to perform the search
    # Recursively find the closest descendant leaf:
    # - it is the closest leaf from either the left or right branch
    # - each level adds 1 to the distance to the closest leaf
    # - if the current root is the node from which to perform the search, sets the ancestor distance to 0
    else:
        if right_min is None:
            return left_min + 1, left, 0 if root == node else None
        elif left_min is None:
            return right_min + 1, right, 0 if root == node else None
        elif left_min <= right_min:
            return left_min + 1, left, 0 if root == node else None
        else:
            return right_min + 1, right, 0 if root == node else None


first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)
sixth = Node(6)
seventh = Node(7)
first.left = second
first.right = third
second.left = fourth
fourth.left = fifth
fifth.left = sixth
sixth.left = seventh
print find_closest_leaf_to_node(first, second)
print find_closest_leaf_to_node(first, fifth)
