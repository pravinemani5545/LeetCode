class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #since in ascending order, brute force will continue until you either go over or match, when you go to next index
        #but we will use 2 pointer
        l, r = 0, len(numbers) - 1
        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r-=1
            
            if curSum < target:
                l+=1
            
            if curSum == target:
                return [l+1,r+1]