class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        test_word = strs[0]
        for i, _ in enumerate(test_word):
            for string in strs:
                if i == len(string) or string[i] != test_word[i]:
                    return test_word[:i]
        return test_word

        
