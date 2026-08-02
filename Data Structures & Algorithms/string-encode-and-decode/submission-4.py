class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for s in strs:
            encoded_string += str(len(s))+"#"+s
        return encoded_string

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
