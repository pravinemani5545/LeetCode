class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index
				#Need hashmap as not in ascending order, still shorter the brute force
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
		            #as a key
                return [prevMap[diff], i]
            prevMap[n] = i