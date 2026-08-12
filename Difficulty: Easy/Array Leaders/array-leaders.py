class Solution:
    def leaders(self, arr):
        result = []
        max_right = arr[-1]

        result.append(max_right)

        for i in range(len(arr) - 2, -1, -1):
            if arr[i] >= max_right:
                result.append(arr[i])
                max_right = arr[i]

        return result[::-1]