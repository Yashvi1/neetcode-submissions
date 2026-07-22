class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<1:
            return 0
        sorted_list = list(dict.fromkeys(sorted(nums)))
        print(sorted_list)
        seq1 = list()
        count = 1
        max = 0
        num = 1
        
        while num < len(sorted_list):
            if sorted_list[num] - sorted_list[num-1] == 1:
                count += 1
                num += 1
                print(f"inside if count is {count} next num is {num}")
            elif max < count:
                max = count
                count = 1
                num += 1
                print(f"inside elif count is {count} & next num is {num}")
            else:
                count = 1
                num += 1
                print(f"next num is {num}")
        if max < count:
            max = count
            
        
        return max
        