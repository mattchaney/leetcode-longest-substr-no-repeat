
def test_assertion(solution, string, expected):
    length = solution.lengthOfLongestSubstring(string)
    c = "==" if length == expected else "!="
    print("actual {0} {1} expected {2} input {3}".format(length, c, expected, string))
