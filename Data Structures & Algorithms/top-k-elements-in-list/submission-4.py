class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
       
        
        sorted_res = sorted(freq.items(), key=lambda item: item[1], reverse=True)
      
        return [num for num,_ in sorted_res[:k]]
        
        
        
        
        
       
    