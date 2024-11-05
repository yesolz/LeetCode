class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        result = set()

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    result.add(i)
                    result.add(j)

        result = list(result)

        return sorted(result)
