"""
Problem: Valid Anagram
Difficulty: Easy
Source: NeetCode 150
Company: Google

Time Complexity: O(?)
Space Complexity: O(?)

Pattern: [Hash Table / Sorting]

Description:
Given two strings s and t, return true if the two strings are anagrams
of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another
string, but the order of the characters can be different.

Examples:
    Example 1:
    Input: s = "racecar", t = "carrace"
    Output: true

    Example 2:
    Input: s = "jar", t = "jam"
    Output: false

Constraints:
    - s and t consist of lowercase English letters.
"""
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Determina si dos strings son anagramas.

        Args:
            s: Primer string
            t: Segundo string

        Returns:
            True si son anagramas, False en caso contrario

        Example:
            >>> sol = Solution()
            >>> sol.isAnagram("racecar", "carrace")
            True
            >>> sol.isAnagram("jar", "jam")
            False
        """
        # Time Complexity: O(n)
        # Space Complecity: O(n)


        if len(s) != len(t):
            return False

        s_counter = defaultdict(int)
        t_counter = defaultdict(int)
        for index in range(len(s)):
            s_counter[s[index]] += 1
            t_counter[t[index]] += 1

        for s_k, s_v in s_counter.items():
            if s_k not in t_counter:
                return False
            else:
                if s_v != t_counter[s_k]:
                    return False
        return True
                




# Tests
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    assert sol.isAnagram("racecar", "carrace") == True, "Test 1 failed"

    # Test Case 2
    assert sol.isAnagram("jar", "jam") == False, "Test 2 failed"

    # Test Case 3 - Edge cases
    assert sol.isAnagram("", "") == True, "Test 3 failed (empty strings)"

    # Test Case 4 - Different lengths
    assert sol.isAnagram("a", "ab") == False, "Test 4 failed (different lengths)"

    # Test Case 5 - Same string
    assert sol.isAnagram("hello", "hello") == True, "Test 5 failed (same string)"

    print("All tests passed!")
