class Solution:
    def longestCommonPrefix(self, strs):

        if len(strs) == 0:
            return ""
        first = strs[0]

        minans = 100
        for i in range(1, len(strs)):
            ans = 0
            j = 0
            k = 0
            while j < len(first) and k < len(strs[i]):
                if first[j] == strs[i][k]:
                    ans = ans + 1
                else:
                    break
                j = j + 1
                k = k + 1

            minans = min(minans, ans)
            print(minans)

        return first[0:minans]

        