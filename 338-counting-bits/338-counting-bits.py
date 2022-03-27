class Solution:
    def countBits(self, n: int) -> List[int]:
        s = []
        ans = []
        m = {0: 0}
        for i in range(0, n + 1):
            s.append(bin(i).replace("0b", ""))
        for i in range(1, len(s)):
            j = 0
            count = 0
            y = len(s[i])
            while j < y:
                print(s[i][j])
                z = int(s[i][j])
                if z == 1:
                    count = count + 1
                    m[i] = count
                j = j + 1
        for i in m.values():
            ans.append(i)
        return ans


