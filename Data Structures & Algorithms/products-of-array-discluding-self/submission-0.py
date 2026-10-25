class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # result = []
        # length = len(nums)
        # # multp = 1
        # for i in range(length):
        #     multp *= nums[i]
        
        # for i in range(length):
        #     result.append(multp//nums[i])
        # return result

        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
