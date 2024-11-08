class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        left = [1] * n
        for i in range(n):
            if i == 0:
                left[i] = nums[i]
            else:
                left[i] = (left[i-1] * nums[i])

        right = [1] * n
        for i in range(n-1, -1, -1):
            if i == n-1:
                right[i] = nums[i]
            else:
                right[i] = (right[i+1] * nums[i])

        answer = [1] * n
        for i in range(n):
            if i == 0:
                answer[i] = right[i+1]
            elif i == n - 1:
                answer[i] = left[i-1]
            else:
                answer[i] = (left[i-1] * right[i+1])

        return answer