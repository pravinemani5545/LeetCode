#Create a set in python, now add to that set with .add(n) if n is not already in the set 
#“if n in set” - return True

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)

        return False