class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = "".join(c.lower() for c in s if c.isalnum())
        print(str)
        j = len(str) - 1
        for i in range(len(str)):
            if i>j or i==j:
                print(f"i={i} & j={j} crossed")
                break
            if str[i] != str[j]:
                print(f"char mismatche, returning False")
                return False
            else:
                j -= 1
                print(f"chars matched, returning True and j={j}")
      
        return True
        