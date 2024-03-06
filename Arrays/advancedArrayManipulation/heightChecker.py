class Solution(object):
    def heightChecker(self, heights):
        max_nr = max(heights)
        count = [0] * (max_nr + 1)
        for number in heights:
            count[number] += 1
        sumcount = [0] * (max_nr + 1)
        for index, number in enumerate(count[1:],start=1):
            sumcount[index] = number + sumcount[index-1]
        output = [0] * len(heights)
        for p in range(len(heights)-1,-1,-1):
            output[sumcount[heights[p]]-1] = heights[p]
            sumcount[heights[p]] -= 1
        result = 0
        for index, number in enumerate(heights):
            if number != output[index]:
                result += 1
        return result



"""
A school is trying to take an annual photo of all the students. 
The students are asked to stand in a single file line in non-decreasing order by height. 
Let this ordering be represented by the integer array expected where expected[i] 
is the expected height of the ith student in line.

You are given an integer array heights representing the current order that the 
students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

Return the number of indices where heights[i] != expected[i].

 

Example 1:

Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation: 
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match.
Example 2:

Input: heights = [5,1,2,3,4]
Output: 5
Explanation:
heights:  [5,1,2,3,4]
expected: [1,2,3,4,5]
All indices do not match.
Example 3:

Input: heights = [1,2,3,4,5]
Output: 0
Explanation:
heights:  [1,2,3,4,5]
expected: [1,2,3,4,5]
All indices match.
 

Constraints:

1 <= heights.length <= 100
1 <= heights[i] <= 100
"""