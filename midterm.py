"""
    four_sum
    jump
"""


# four sum
def four_sum(nums, target):
    if not nums or len(nums) < 4: return []
    results = []
    nums.sort()
    for a in range(len(nums) - 3):
        # if a > 0 and nums[a] == nums[a-1]:
        #     continue
        for b in range(a + 1, len(nums) - 2):
            # if b > a+1 and nums[b] == nums[b-1]:
            #     continue
            c = b + 1
            d = len(nums) - 1
            while c < d:
                sum = nums[a] + nums[b] + nums[c] + nums[d]
                if sum == target:
                    current = [nums[a], nums[b], nums[c], nums[d]]
                    if current not in results:
                        results.append(current)
                    c += 1
                    d -= 1
                    # results.append([nums[a], nums[b], nums[c], nums[d]])
                    # while c < d and  nums[c] == nums[c+1]:
                    #     c += 1
                    # while c < d and nums[d] == nums[d-1]:
                    #     d -= 1
                    # c += 1
                    # d -= 1
                elif sum < target:
                    c += 1
                else:
                    d -= 1
    return results


# the minimum step to jump to the end index
def jump_2(nums):
    step = 0
    end = 0
    max_pos = 0
    for i in range(len(nums) - 1):
        max_pos = max(max_pos, i + nums[i])
        if i == end:
            end = max_pos
            step += 1
    return step