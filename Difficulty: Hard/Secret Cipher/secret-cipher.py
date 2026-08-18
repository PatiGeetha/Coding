class Solution:
    def compress(self, s):
            n = len(s)
            lps = [0] * n
            p = 0
            for i in range(1, n):
                while p and s[p] != s[i]:
                    p = lps[p - 1]
                if s[p] == s[i]:
                    p += 1
                lps[i] = p
            stack = []
            i = n - 1
            while i:
                if i & 1 == 0:
                    stack.append(s[i])
                    i -= 1
                    continue
                size = i + 1
                prefix_size = lps[i]
                sub_size = size - prefix_size
                if (
                    prefix_size << 1 >= size
                    and size % sub_size == 0
                    and (size // sub_size) & 1 == 0
                ):
                    stack.append("*")
                    i = i >> 1
                else:
                    stack.append(s[i])
                    i -= 1
            stack.append(s[0])
            return "".join(reversed(stack))
