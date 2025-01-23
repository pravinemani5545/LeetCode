class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # Check if concatenating str1 and str2 in both orders gives the same result
        if str1 + str2 != str2 + str1:
            return ""
        
        # Find the GCD of the lengths of str1 and str2
        gcd_length = self.gcd(len(str1), len(str2))
        
        # Return the prefix of str1 up to the GCD length
        return str1[:gcd_length]
		
		#Function to calculate GCD fo two integers
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
