class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum > target:
                r -= 1
                # print(f"inside > target, r is at {numbers[r]}")
                continue
            elif sum == target:
                # print(f"returning at {numbers[l]} and {numbers[r]}")
                return [l+1, r+1]

            else:
                # print(f"inside < target, l is at {numbers[l]}")
                l += 1
                continue