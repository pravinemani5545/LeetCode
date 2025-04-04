class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #create empty array
        ans = []
        
        #need to concat the same array twice
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans