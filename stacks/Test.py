
'''
class Solution:
    # approach 1 
    def removeOuterParentheses_1(self, s: str):
        openCout = 0
        temp = result = ""
        result = ""
        for c in s:
            if c == '(':
                openCout +=1 
            else:
                openCout -=1
            temp += c
            if openCout == 0:
                result += temp[1:-1]
                temp = ""
        return result 

    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        stack = []

        for char in s:
            if char == '(':
                if stack:
                    result += char
                stack.append(char)
            else:
                stack.pop()
                if stack:
                    result += char

        return result

    


import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_removeOuterParentheses(self):
        # Test case 1: Basic case
        s1 = "(()())(())"
        self.assertEqual(self.solution.removeOuterParentheses(s1), "()()()")

        # Test case 2: Another example
        s2 = "(()())(())(()(()))"
        self.assertEqual(self.solution.removeOuterParentheses(s2), "()()()()(())")



        # Test case 6: Nested parentheses
        s6 = "(()(()))"
        self.assertEqual(self.solution.removeOuterParentheses(s6), "()(())")

if __name__ == '__main__':
    unittest.main()

'''

#=================================




        
