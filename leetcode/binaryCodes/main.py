class Solution(object):
    def binary_search(self, arr, l, r, search):
        while l<=r:
            mid = l + (r - l) // 2
            if arr[mid] == search:
                return True
            elif arr[mid] < search:
                l = mid + 1
            else:
                r = mid - 1
        return False

    def k_length_substrings(self, st, k):
            for i in range(len(st)-k+1):
                yield st[i:i+k]

    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
         
        subs = sorted(set(self.k_length_substrings(s, k)))
        n = len(subs)

        for i in range(2**k):
            binary=bin(i).replace("b", "")
            binary=binary.zfill(k)
            if len(binary) > k: binary = binary[1:]
            if not self.binary_search(subs, 0, n-1, binary): return False
            
        return True

