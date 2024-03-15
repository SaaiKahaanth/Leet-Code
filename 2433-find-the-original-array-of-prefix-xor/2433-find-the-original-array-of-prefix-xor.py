class Solution(object):
    def findArray(self, pref):
        n = len(pref)
        arr = [0] * n

        # Find the first element of the original array
        arr[0] = pref[0]

        # Recover the original array
        for i in range(1, n):
            arr[i] = pref[i] ^ pref[i - 1]

        return arr

