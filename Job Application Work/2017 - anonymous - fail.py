# Given a BST, create an in-order iterator


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BSTIter:
    def __init__(self, root):
        self.stack = [root]
        self.last_value = None

    def has_next(self):
        if self.stack:
            return True
        return False

    def get_next(self):
        if not self.stack:
            raise RuntimeError('Iterator empty')

        # Traverse the left branch, adding each node onto the stack (popping from the stack yields an ascending order)
        # Think of the tree as a sequence of left branches branching off of other left branches
        while self.stack[-1].left and (not self.last_value or self.stack[-1].left.value > self.last_value):
            self.stack.append(self.stack[-1].left)

        check = self.stack.pop()

        # If the current node has a right child, add it to the stack
        # This child is itself the root of a well-formed BST, thus the next call to get_next effectively recurses for
        # values between those smaller than the next-to-be-popped node from the previous branch and those larger than
        # the current node
        if check.right:
            self.stack.append(check.right)

        self.last_value = check.value
        return check.value


first = Node(10)
second = Node(5)
third = Node(15)
fourth = Node(2)
fifth = Node(8)
sixth = Node(12)
seventh = Node(18)
first.left = second
first.right = third
second.left = fourth
second.right = fifth
third.left = sixth
third.right = seventh
bst = BSTIter(first)
while bst.has_next():
    print bst.get_next()
