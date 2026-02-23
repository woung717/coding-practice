#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         ret = set()
#         nums.sort()

#         nums_dict = { n: i for i, n in enumerate(nums) }
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 find = -(nums[i] + nums[j])
#                 if find in nums_dict and \
#                     j < nums_dict[find]:
#                     ret.add((nums[i], nums[j], find))

#         return [list(t) for t in ret]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                triple_sum = nums[i] + nums[j] + nums[k]
                if triple_sum == 0:
                    ret.append([nums[i], nums[j], nums[k]])

                    tmp_j = nums[j]
                    while j < k and nums[j] == tmp_j:
                        j += 1
                    
                    tmp_k = nums[k]
                    while j < k and nums[k] == tmp_k:
                        k -= 1
                elif triple_sum < 0:
                    j += 1
                elif triple_sum > 0:
                    k -= 1
            
        return ret

# @lc code=end

