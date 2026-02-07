def hasDuplicate(self, nums: List[int]) -> bool:
    # Complexity: O(n)  
    # Space Complexity: S(n)
    validated = set()
    for n in nums:
        if n in validated:
            return True
        validated.add(n)
    return False

# Case No Duplicates | Worse case 
# nums = [1,2,3] 
# 
# n | validated | return
# 1 | {1}       |
# 2 | {1, 2}    | 
# 3 | {1,2,3}   | False
