class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for n in range(len(nums)):
            for m in range(n+1, len(nums)):
                if nums[n] + nums[m] == target:
                    print(f"Target matched at n:{n} and m:{m}")
                    if n > m:
                        return [m, n]
                    return [n, m]

        