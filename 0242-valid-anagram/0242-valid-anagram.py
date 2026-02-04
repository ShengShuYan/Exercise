class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        letter = 'abcdefghijklmnopqrstuvwxyz'
        for char in letter:
            if s.count(char) != t.count(char):
                return False
        return True
        