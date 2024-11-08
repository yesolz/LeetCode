class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # 왼쪽 곱과 오른쪽 곱의 누적 계산!
        left = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                left[i] = nums[i]
            else:
                left[i] = (left[i-1] * nums[i])

        right = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                right[i] = nums[i]
            else:
                right[i] = (right[i+1] * nums[i])
                
        answer = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                answer[i] = right[i+1]
            elif i == len(nums) - 1:
                answer[i] = left[i-1]
            else:
                answer[i] = (left[i-1] * right[i+1])

        return answer