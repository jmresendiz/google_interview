#Group Anagrams
#Medium
#Topics
#Company Tags
#Hints
#Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
#
#An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
#
#Example 1:
#
#    Input: strs = ["act","pots","tops","cat","stop","hat"]
#
#    Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
#    Example 2:
#
#        Input: strs = ["x"]
#
#        Output: [["x"]]
#        Example 3:
#
##            Input: strs = [""]
#
#            Output: [[""]]

from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Complexity: O(n x k log k) => ?
        # Space: O(n x k) => ?
        grouped_str = defaultdict(list) 
        for s in strs: # O(n)
            key = ''.join(sorted(s)) # O(k log k) 
            grouped_str[key].append(s) # O(1)
                                                    
        return list(grouped_str.values())




        





                                    


