class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 가장 빈도 수가 높은 k개의 element
        count = defaultdict(int)
        
        for i in nums:
            count[i] += 1
        
        result = sorted(count, key=count.get, reverse=True)[:k]
        return result
