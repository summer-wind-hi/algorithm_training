"""
    DFS / BFS
    greedy algorithm
    binary search: 1)monotonicity   2)bound  3) index accessible
"""

# code model for DFS
# recursion version
visited = set()
def dfs_recursion(node, visited):
    visited.add(node)

    # process current node here

    for child_node in node.children():
        if not child_node in visited:
            dfs_recursion(child_node, visited)


# non-recursion version: maintain a stack manually
def dfs_stack(tree):
    if tree.node is None:
        return []
    visited, stack = [], [tree.node]

    while stack:
        node = stack.pop()
        visited.append(node)

        # processing current node

        nodes = generated_related_nodes(node)
        stack.push(nodes)

def generated_related_nodes(node):
    """
        get all children
    """
    pass


# code model for BFS: maintain a queue
def bfs(graph, start, end):
    queue = []
    queue.append([start])
    visited.add(start)  # ??

    while queue:
        node = queue.popleft()
        visited.add(node)

        # process current node
        nodes = generated_related_nodes(node)
        queue.push(nodes)


# code model for binary search
def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) / 2
        if array(mid) == target:  # finde the target, break or return
            return mid
        elif array(mid) < target:
            left = mid + 1
        else:
            right = mid - 1


# lemonade change problem: greedy -> find particularity: 5/10/20 -> mutiples of 5
def lemonade_change(bills):
    five, ten, twenty = 0, 0, 0
    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if five < 1: return False
            five -= 1
            ten += 1
        else:
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
                twenty += 1
            elif five >= 3:
                five -= 3
                twenty += 1
            else:
                return False
    return True


# the best time to sell blocks: greedy
def max_profit(prices):
    profits = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profits += prices[i] - prices[i - 1]

    return profits