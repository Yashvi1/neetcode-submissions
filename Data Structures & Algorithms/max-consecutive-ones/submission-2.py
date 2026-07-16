class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max = 0
        for n in nums:
            if n == 1:
                count += 1
                if max < count:
                    max = count      
            else:
                count = 0        
        return max
        