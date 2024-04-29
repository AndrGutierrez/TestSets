class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        tuples = []
        for i in range(len(nums)): tuples.append((i, nums[i]))
        tuples = sorted(tuples, key=lambda x: x[1])
        groups = [[]]

        for i in range(len(tuples)):
            if abs(tuples[i-1][1] - tuples[i][1]) <= limit: pass
            else: groups.append([])
            groups[len(groups)-1].append(tuples[i])

        res = [0 for num in nums]
    
        for group in groups:
            index_sorted_group = sorted(group, key=lambda x: x[0])
            i=0
            for item in group:
                res[index_sorted_group[i][0]] = item[1]
                i+=1
        return res

