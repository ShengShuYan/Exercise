def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        common = gcd(len(str1), len(str2))
        
        if str1 + str2 != str2 + str1:
            return ''
        return str1[:common]
        
        
        