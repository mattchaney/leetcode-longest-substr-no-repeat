from utils import test_assertion

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxsub = ""
        for i in range(0, len(s)):
            cursub = self.len_from_start(s, i)
            if len(maxsub) < len(cursub):
                maxsub = cursub
        return len(maxsub)

    def len_from_start(self, s, i):
        seen = []
        while i < len(s):
            c = s[i]
            if c not in seen:
                seen.append(c)
                i = i + 1
            else:
                break
        return ''.join(seen)

if __name__ == "__main__":
    s = Solution()

    test_assertion(s, "abcabcbb", 3)
    test_assertion(s, "bbbbb", 1)
    test_assertion(s, "pwwkew", 3)