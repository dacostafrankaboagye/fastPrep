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