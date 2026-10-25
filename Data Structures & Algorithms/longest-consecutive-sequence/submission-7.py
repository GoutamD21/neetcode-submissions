class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sort_num = sorted(nums)
        # count = 0
        # for i in range(len(sort_num)):
        #     if i <= len(sort_num) & sort_num[i+1] == sort_num[i-1]:
        #         count += 1
        # return count

        numSet = set(nums)
        longest = 0

        for n in nums:
            length = 0
            if (n-1) not in numSet:
                while (n+length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

