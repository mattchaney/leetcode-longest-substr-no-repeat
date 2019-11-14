from utils import test_assertion

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        left = 0
        right = 0
        seen = []
        while right < len(s):
            ch = s[right]
            if ch not in seen:
                seen.append(ch)
            else:
                if len(seen) > maxlen:
                    maxlen = len(seen)
                left = seen.index(ch) + 1
                seen.append(ch)
                seen = seen[left:]
            right = right + 1
        return maxlen if maxlen > len(seen) else len(seen)

if __name__ == "__main__":
    s = Solution()

    test_assertion(s, "dvdf", 3)
    test_assertion(s, " ", 1)
    test_assertion(s, "pwwkew", 3)
    test_assertion(s, "abcabcbb", 3)
    test_assertion(s, "bbbbb", 1)