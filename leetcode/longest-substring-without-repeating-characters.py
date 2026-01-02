class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        letters = set()
        maxlen = 0
        while j < len(s):
            if not(s[j] in letters):
                letters.add(s[j])
                j += 1
                maxlen = max(maxlen,len(letters))
            else:
                letters.remove(s[i])
                i += 1
        return maxlen