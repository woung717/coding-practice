#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         ret = 0
#         stack = [] 

#         for i, h in enumerate(height):
#             while len(stack) and h > height[stack[-1]]:
#                 mid = stack.pop()
#                 if len(stack) == 0:
#                     break
#                 left = stack[-1]
#                 width = i - left - 1
#                 layer_height = min(h, height[left]) - height[mid]

#                 if layer_height != 0:
#                     ret += width * layer_height
                
#             stack.append(i)

#         return ret

class Solution:
    def trap(self, height: List[int]) -> int:
        ret = 0
        l, r = 0, len(height) - 1
        max_l, max_r = 0, 0

        while l <= r:
            if max_l < max_r:
                water = max_l - height[l]
                max_l = max(max_l, height[l])
                l += 1
            else:
                water = max_r - height[r]
                max_r = max(max_r, height[r])
                r -= 1
            
            if water > 0:
                ret += water

        return ret
# @lc code=end

