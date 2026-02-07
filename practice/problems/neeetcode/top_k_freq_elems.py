"""
Top K Frequent Elements
Medium
Topics
Company Tags
Hints
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

    Input: nums = [1,2,2,3,3,3], k = 2

    Output: [2,3]
    Example 2:

    Input: nums = [7,7], k = 1

    Output: [7]
    Constraints:

    1 <= nums.length <= 10^4.
    -1000 <= nums[i] <= 1000
    1 <= k <= number of distinct elements in nums.
"""
import heapq
from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Time Complexity: O(n log k)
        Space Complexity: O(n)

        Approach: Use Counter to get frequencies, then heapq.nlargest to get top k
        """
        # 1. Count frequencies: O(n)
        count = Counter(nums)

        # 2. Get k largest by frequency: O(n log k)
        return heapq.nlargest(k, count.keys(), key=count.get)


# Tests
if __name__ == "__main__":
    solution = Solution()

    # Test 1: Example 1 from problem
    nums1 = [1, 2, 2, 3, 3, 3]
    k1 = 2
    result1 = solution.topKFrequent(nums1, k1)
    print(f"Test 1: nums={nums1}, k={k1}")
    print(f"Output: {result1}")
    print(f"Expected: [3, 2] or [2, 3]")
    assert set(result1) == {2, 3} and len(result1) == 2, "Test 1 Failed!"
    print("✅ Test 1 Passed!\n")

    # Test 2: Example 2 from problem
    nums2 = [7, 7]
    k2 = 1
    result2 = solution.topKFrequent(nums2, k2)
    print(f"Test 2: nums={nums2}, k={k2}")
    print(f"Output: {result2}")
    print(f"Expected: [7]")
    assert result2 == [7], "Test 2 Failed!"
    print("✅ Test 2 Passed!\n")

    # Test 3: Single element
    nums3 = [1]
    k3 = 1
    result3 = solution.topKFrequent(nums3, k3)
    print(f"Test 3: nums={nums3}, k={k3}")
    print(f"Output: {result3}")
    print(f"Expected: [1]")
    assert result3 == [1], "Test 3 Failed!"
    print("✅ Test 3 Passed!\n")

    # Test 4: All elements same frequency
    nums4 = [1, 2, 3, 4]
    k4 = 2
    result4 = solution.topKFrequent(nums4, k4)
    print(f"Test 4: nums={nums4}, k={k4}")
    print(f"Output: {result4}")
    print(f"Expected: Any 2 elements from [1, 2, 3, 4]")
    assert len(result4) == 2 and all(x in [1, 2, 3, 4] for x in result4), "Test 4 Failed!"
    print("✅ Test 4 Passed!\n")

    # Test 5: Larger example
    nums5 = [4, 1, -1, 2, -1, 2, 3]
    k5 = 2
    result5 = solution.topKFrequent(nums5, k5)
    print(f"Test 5: nums={nums5}, k={k5}")
    print(f"Output: {result5}")
    print(f"Expected: [-1, 2] or [2, -1] (both appear twice)")
    assert set(result5) == {-1, 2} and len(result5) == 2, "Test 5 Failed!"
    print("✅ Test 5 Passed!\n")

    print("🎉 All tests passed!")
