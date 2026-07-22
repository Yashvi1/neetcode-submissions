class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<1:
            return 0
        sorted_list = list(dict.fromkeys(sorted(nums)))      
        count = 1
        max = 0
        num = 1
        
        while num < len(sorted_list):
            if sorted_list[num] - sorted_list[num-1] == 1:
                count += 1
                num += 1
            elif max < count:
                max = count
                count = 1
                num += 1
            else:
                count = 1
                num += 1
        if max < count:
            max = count
            
        return max
        