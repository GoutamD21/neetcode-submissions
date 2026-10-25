class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # prevMap = {}
        # for indx, val in enumerate(numbers):
        #     diff = target - val
        #     if diff in prevMap:
        #         return [diff, val]
        #     prevMap[val] = indx

        lo = 0
        hi = len(numbers)-1

        while lo < hi:
            if target < numbers[lo] + numbers[hi]:
                hi -= 1
                continue
            if target > numbers[lo] + numbers[hi]:
                lo +=1
                continue
            if target == numbers[lo] + numbers[hi]:
                return [lo+1, hi+1]

        

    
