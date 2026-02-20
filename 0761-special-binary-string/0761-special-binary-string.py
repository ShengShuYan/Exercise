class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if len(s) <= 2:
            return s

        substrings = []
        count = 0
        start = 0
        
        for i, char in enumerate(s):
            count += 1 if char == '1' else -1
            if count == 0:
                inner = self.makeLargestSpecial(s[start+1:i])
                substrings.append("1" + inner + "0")
                start = i + 1

                substrings.sort(reverse=True)
        
        return "".join(substrings)