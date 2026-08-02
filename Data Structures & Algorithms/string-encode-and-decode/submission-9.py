class Solution:

    def encode(self, strs: List[str]) -> str:
       
        parts = []

        for s in strs:
            
            parts.append(str(len(s))+"#"+s)
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        # decoded_string = s.split("@")
        decoded_string = []

        i=0
        while i < len(s):
            length = ''
            while s[i] != '#':
                length += s[i]
                i += 1
            print(length)
            
            i += 1
            decoded_string.append(s[i:i+int(length)])
            i += int(length)
            

        return decoded_string
