class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        print(freq)
        
        sorted_res = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        print(sorted_res)

        arr = list()
        s = 0
        while s<k:
            arr.append(sorted_res[s][0])
            s += 1
        
        return arr
       
    