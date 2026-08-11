class Solution:
    def getSecondLargest(self, arr):
        unique = list(set(arr))

        if len(unique) < 2:
            return -1

        unique.sort(reverse=True)

        return unique[1]