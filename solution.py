class Solution(object):
    def isScramble(self, s1, s2):
        n = len(s1)
        if n != len(s2):
            return False
        if s1 == s2:
            return True

        memo = {}

        def same_multiset(a, i, b, j, L):
            cnt = [0]*26
            base = ord('a')
            for k in range(L):
                cnt[ord(a[i+k]) - base] += 1
                cnt[ord(b[j+k]) - base] -= 1
            for c in cnt:
                if c != 0:
                    return False
            return True

        def dfs(i1, i2, L):
            key = (i1, i2, L)
            if key in memo:
                return memo[key]
            if s1[i1:i1+L] == s2[i2:i2+L]:
                memo[key] = True
                return True
            if not same_multiset(s1, i1, s2, i2, L):
                memo[key] = False
                return False
            for k in range(1, L):
                if dfs(i1, i2, k) and dfs(i1 + k, i2 + k, L - k):
                    memo[key] = True
                    return True
                if dfs(i1, i2 + L - k, k) and dfs(i1 + k, i2, L - k):
                    memo[key] = True
                    return True
            memo[key] = False
            return False

        return dfs(0, 0, n)
