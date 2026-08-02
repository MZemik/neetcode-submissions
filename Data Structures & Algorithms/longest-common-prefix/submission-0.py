class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for l_ind, letter in enumerate(strs[0]):
            for word in strs[1:]:
                if l_ind >= len(word) or letter != word[l_ind]:
                    return result
            result += letter
        return result
