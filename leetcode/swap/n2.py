def swap(nums, limit):
    valid_combinations = get_valid_combinations(nums, limit)
    for combination in valid_combinations:
        i, j = combination
        # print(nums)
        swapped = list(nums) 
        swapped[i], swapped[j] = swapped[j], swapped[i]
        nums = swapped
    return nums

def get_valid_combinations(nums, limit):
    valid_combinations = []
    length =len(nums)
    for i in range(length):
        for j in range(i+1,length):
            if nums[i]-nums[j] <= limit and nums[i]>nums[j]:
                valid_combinations.append((i, j))
    
    return valid_combinations

class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """

        swapped = swap(nums, limit)
        swapped_is_smaller = swapped != nums


        while swapped_is_smaller:
            smallest = swapped if swapped_is_smaller else nums
            nums = list(smallest)
            swapped = swap(nums, limit)
            swapped_is_smaller= swapped != nums


        nums = swapped

        return nums


if __name__ == "__main__":
    sol = Solution()
    r= sol.lexicographicallySmallestArray([6,5,3,9,8], 2)
    print(r)
