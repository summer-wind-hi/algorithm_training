# binary search on rotated sorted array
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid, nums[mid]
        elif nums[mid] > target:  # left
            right -= 1
        else:
            if target <= nums[right]:  # right
                left += 1
            else:   # left
                right -= 1
    return None


nums = [7, 8, 9, 1, 2, 3, 4, 5, 6]
# target = 8
for target in nums:
    print(target, binary_search(nums, target))

import numpy as np
def nms(dets, threshold):
    # dets:[n, 4]
    # cal areas and sort
    x1 = dets[: 0]
    y1 = dets[: 1]
    x2 = dets[: 2]
    y2 = dets[: 3]
    scores = dets[: 4]
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)
    inds = scores.argsort()[::-1] # return index according to ascending sort

    # start loop
    keep = []
    while inds:
        i = inds[0]
        keep.append(i)

        # cal iou
        xx1 = np.maximum(x1[i], x1[inds[1:]])
        yy1 = np.maximum(y1[i], y1[inds[1:]])
        xx2 = np.maximum(x2[i], x2[inds[1:]])
        yy2 = np.maximum(y2[i], y2[inds[1:]])

        h = np.maximum(0, xx2 - xx1 + 1)
        v = np.maximum(0, yy2 - yy1 + 1)
        inter = h * v

        ious = inter / (areas[i] + areas[inds[1:]] - inter)
        selected = np.where(ious < threshold)[0]
        inds = inds[selected + 1]

    return keep
