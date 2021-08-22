"""
    recursion
    divide and conquer
"""


# code model for recursion
MAX_LEVEL = 10
data = 0
def process_result():
    pass

def process(level, data):
    pass

def recursion(level, param1, param2):
    # recursion terminator
    if level > MAX_LEVEL:
        process_result()
        return

    # process logic in current level
    process(level, data)

    # drill down
    recursion(level + 1, param1, param2)

    # reverse the current level status if needed


# code model for divide and conquer
def prepare_data(problem):
    pass

def split_problem(problem, data):
    pass

def divide_conquer(problem, param1, param2):
    # recursion terminator
    if problem is None:
        process_result()
        return

    # prepare data
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)

    # divide and conquer subproblems
    subresult0 = divide_conquer(subproblems[0], param1, param2)
    subresult1 = divide_conquer(subproblems[1], param1, param2)
    subresult2 = divide_conquer(subproblems[2], param1, param2)

    # process subresults
    result = process_result(subresult0, subresult1, subresult2)
    
    return result


# lowest common ancestor
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class LowestCommonAncestor():
    def lowest_common_ancestor(self, root, p, q):
        # recursion terminator
        if root is None or root == p or root == q: return root

        # divide and conquer
        left = self.lowest_common_ancestor(root.left, p, q)
        right = self.lowest_common_ancestor(root.right, p, q)

        # process and generate the final result
        if not left: return right
        if not right: return left
        return root


# build binary tree from preorder and inorder
class BuildBinaryTree():
    def build_tree(self, preorder, inorder):
        # recursion terminator
        if len(preorder) == 0: return None

        # prepare data and subproblems
        index = inorder.index(preorder[0])

        # divide and conquer
        node = TreeNode(preorder[0])
        node.left = self.build_tree(preorder[1:1 + index], inorder[:index])
        node.right = self.build_tree(preorder[1 + index:], inorder[index + 1:])

        return node
