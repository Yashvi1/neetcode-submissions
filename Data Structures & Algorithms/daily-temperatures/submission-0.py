class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            count = 0
            if i==len(temperatures) - 1:
                result.append(0)
            for j in range(i+1, len(temperatures)):
                count += 1
                if temperatures[i] < temperatures[j]:
                    print(f"at {j} {temperatures[i]} < {temperatures[j]}")
                    result.append(count)
                    break;
                elif j==len(temperatures)-1:
                    print('inside else')
                    result.append(0)
                
        return result