"""
    Hash map
    Tree  /  Binary Tree  /  Binary Search Tree (BST)
    Heap  /  Binary Heap
    Graph
"""

# 1. valid anagram : s = "anagram", t = "nagaram" -> true
class ValidAnagram():
    def sort(self, s, t):
        # sort and equal:  nlogn   logn
        import operator
        lis = list(s)
        lit = list(t)
        lis.sort()
        lit.sort()
        return operator.eq(lis, lit)

    def hash_map(self, s, t):
        # hash_map:  n  s:length of string
        di = dict()
        if len(s) != len(t): return False
        length = len(s)
        # traversal s
        for i in range(length):
            di[s[i]] = di[s[i]] + 1 if s[i] in di else 1

        for i in range(length):
            di[t[i]] = di[t[i]] - 1 if t[i] in di else -1

        for c in di.values():
            if c != 0:
                return False

        return True


# 2. two-sum
class TwoSum():
    def violent(self, nums, target):
        # violent n^2  1
        length = len(nums)
        for i in range(length):
            for j in range(i + 1,length):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def hash_method(self, nums, target):
        # n n
        hash_map = dict()
        for i in range(len(nums)):
            if target - nums[i] in hash_map:
                return [hash_map[target - nums[i]], i]
            else:
                hash_map[nums[i]] = i
        return []


# 3. preorder for N-ary Tree
class Node():
    def __init__(self, val, children):
        self.val = val
        self.children = children


class NaryTree():
    def preorder(self, node):
        res = []
        if node:
            res.append(node.val)
            for child in node.children:
                res += self.preorder(child)
        return res


def main_test():
    # 1
    # s = "anagram"
    # t = "nagaram"
    # s = "rat"
    # t = "car"
    # va = ValidAnagram()
    # print(va.sort(s, t))
    # print(va.hash_map(s, t))

    # 2
    nums = [2, 7, 11, 15]
    target = 9
    two_sum = TwoSum()
    print(two_sum.violent(nums, target))
    print(two_sum.hash_method(nums, target))


if __name__ == '__main__':
    main_test()
