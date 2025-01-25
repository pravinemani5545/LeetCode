class Solution:
    def isValid(self, s: str) -> bool:
		    #Create a dict holding the matching paratheses as key-val paris
        Map = {")": "(", "]": "[", "}": "{"}
        #create an empty arr as a stack
        stack = []

				#for every character in the string, we check if one of the parantheses is a character
        for c in s:
		        #If each character is not a key in the map
		        #checks if it's an open paren
		        #NOT IN SO CHECKS IF ITS A OPENING PARENT
            if c not in Map:
		            #Apped it to stack
                stack.append(c)
                #continue skips to next instance of loop
                continue
                
            if not stack or stack[-1] != Map[c]:
                # If the stack is empty or the top of the stack doesn't match the current closing parenthesis
                return False
            # Pop the top of the stack if it matches the current closing parenthesis
            stack.pop()

        # Return True if the stack is empty (all parentheses were matched and closed), else False
        return not stack
        
        Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false