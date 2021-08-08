"""
    array  linklist  skiplist
    stack  queue     deque    priority queue

"""


# 1.remove duplicate number
class RemoveDuplicates():
    def remove_duplicates(self, nums):
        left = 0
        for i in range(1, len(nums)):
            if nums[left] != nums[i]:
                left += 1
                nums[left] = nums[i]
        return left + 1, nums[:left + 1]


# 2. rotate array
class RotateArray():
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


def unit_test():
    # test task1
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    rmv = RemoveDuplicates()

    print("before removing: {}: {}".format(len(nums), nums))
    length, new_nums = rmv.remove_duplicates(nums)
    print("after removing: {}: {}".format(length, new_nums))

    # test task2
    # nums = [1, 2, 3, 4, 5, 6, 7]
    # k = 3s
    # rot = RotateArray()
    # print("before rotating:", nums)
    # rot.rotate(nums, k)
    # print("after rotating:", nums)


if __name__ == '__main__':
    unit_test()