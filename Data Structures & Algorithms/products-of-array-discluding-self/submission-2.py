class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            mul = 1
            for j in range(len(nums)):
                if j != i:
                    mul *= nums[j]
            arr.append(mul)

        print(f"Final array: {arr}")
        return arr