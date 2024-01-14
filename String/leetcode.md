## 1108. Defanging an IP Address - Easy

Given a valid (IPv4) IP address, return a defanged version of that IP address.

        A defanged IP address replaces every period "." with "[.]".

 

Example 1:

        Input: address = "1.1.1.1"
        Output: "1[.]1[.]1[.]1"

Example 2:

        Input: address = "255.100.50.0"
        Output: "255[.]100[.]50[.]0"
        

Constraints:

        The given address is a valid IPv4 address.


### solution - python
```py

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")

        
# Test cases
def test_defangIPaddr():
    solution = Solution()

    # Example 1
    input_1 = "1.1.1.1"
    expected_output_1 = "1[.]1[.]1[.]1"
    assert solution.defangIPaddr(input_1) == expected_output_1

    # Example 2
    input_2 = "255.100.50.0"
    expected_output_2 = "255[.]100[.]50[.]0"
    assert solution.defangIPaddr(input_2) == expected_output_2

    print("All test cases passed!")

# Run the test
test_defangIPaddr()

```
---

## 1678. Goal Parser Interpretation - Easy

You own a Goal Parser that can interpret a string command. 

The command consists of an alphabet of "G", "()" and/or "(al)" in some order. 

The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". 

The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

 

Example 1:

        Input: command = "G()(al)"
        Output: "Goal"
        
Explanation: The Goal Parser interprets the command as follows:

        G -> G
        () -> o
        (al) -> al

        The final concatenated result is "Goal".

Example 2:

        Input: command = "G()()()()(al)"
        Output: "Gooooal"

Example 3:

        Input: command = "(al)G(al)()()G"
        Output: "alGalooG"
        

Constraints:

        1 <= command.length <= 100
        command consists of "G", "()", and/or "(al)" in some order.

### solution - python
```py
class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("(al)", "al").replace("()", "o")
        
```