class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i in range(len(nums)):
            for b in range(len(nums)):
                if i != b and nums[i] + nums[b] == target:
                    answer = [i, b]
                    return answer
        return answer