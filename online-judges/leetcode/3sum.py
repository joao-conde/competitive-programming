# https://leetcode.com/problems/3sum/


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        triplets = set()
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                triplet = (nums[i], nums[j], nums[k])
                total = sum(triplet)

                if total == 0:
                    triplets.add(triplet)
                    j += 1
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1

        return list([list(t) for t in triplets])


# Tests
solver = Solution()
assert [-1, 0, 1] in solver.threeSum([-1, 0, 1, 2, -1, -4])
assert [-1, -1, 2] in solver.threeSum([-1, 0, 1, 2, -1, -4])
assert solver.threeSum([0, 1, 1]) == []
assert solver.threeSum([0, 0, 0]) == [[0, 0, 0]]
