class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        count = set()

        for i in nums:
            if i not in count:
                count.add(i)
            else:
                return True
        
        return False