"""
    ww07-09
"""
# ww07: climb stairs O(n) O(n)
def climb_stairs(n):
    if n <= 2: return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# generate parenthesis
def generate_parenthesis(n):
    if n == 0:
        return []
    total_l = []
    total_l.append([None])    # 0组括号时记为None
    total_l.append(["()"])    # 1组括号只有一种情况
    for i in range(2,n+1):    # 开始计算i组括号时的括号组合
        l = []
        for j in range(i):    # 开始遍历 p q ，其中p+q=i-1 , j 作为索引
            now_list1 = total_l[j]    # p = j 时的括号组合情况
            now_list2 = total_l[i-1-j]    # q = (i-1) - j 时的括号组合情况
            for k1 in now_list1:
                for k2 in now_list2:
                    if k1 == None:
                        k1 = ""
                    if k2 == None:
                        k2 = ""
                    el = "(" + k1 + ")" + k2
                    l.append(el)    # 把所有可能的情况添加到 l 中
        total_l.append(l)    # l这个list就是i组括号的所有情况，添加到total_l中，继续求解i=i+1的情况
    return total_l[n]


# ww08 hammingWeight
def hamming_weight(n):
    res = 0
    while n:
        res += 1
        n &= n - 1
    return res

# ww08 power of 2
def is_power_of_two(n):
    return n > 0 and n & (n - 1) == 0

# ww09: relative sort
def relative_sort_array(self, arr1, arr2):
    bins = [0 for _ in range(1001)]
    res = []
    for i in arr1:
        bins[i] += 1
    for i in arr2:
        res += [i] * bins[i]
        bins[i] = 0
    for i in range(len(bins)):
        res += [i] * bins[i]

    return res

# ww09: valid anagram
def is_anagram(s, t):
    # sort   nlogn  logn
    # ls = list(s)
    # lt = list(t)
    # ls.sort()
    # lt.sort()
    # return ls == lt

    # hash map  O(n) O(n)
    # if len(s) != len(t): return False
    # hash_dict = dict()
    # for i in range(len(s)):
    #     if s[i] not in hash_dict:
    #         hash_dict[s[i]] = 1
    #     else:
    #         hash_dict[s[i]] += 1
    #
    #     if t[i] not in hash_dict:
    #         hash_dict[t[i]] = -1
    #     else:
    #         hash_dict[t[i]] -= 1
    #
    # for val in hash_dict.values():
    #     if val != 0: return False
    #
    # return True

    # hash map O(n) O(n)
    if len(s) != len(t): return False
    hash_dict = dict()
    for i in range(len(s)):
        if s[i] not in hash_dict:
            hash_dict[s[i]] = 1
        else:
            hash_dict[s[i]] += 1

        if t[i] not in hash_dict:
            hash_dict[t[i]] = -1
        else:
            hash_dict[t[i]] -= 1
    for ele, count in hash_dict.items():
        if count != 0: return False
    return True


s = "anagram"
t = "nagaram"
print(is_anagram(s, t))