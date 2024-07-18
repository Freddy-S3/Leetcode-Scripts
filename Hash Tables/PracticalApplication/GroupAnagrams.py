from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())
        """
        dictkey = {}
        for i in range(len(strs)):
            word = strs[i]
            sortedWord = ''.join(sorted(word))
            if sortedWord not in dictkey:
                dictkey[sortedWord] = [i]
            else:
                dictkey[sortedWord] += [i]
        
        result = []
        for index, key in enumerate(dictkey):
            miniList = []
            for number in dictkey[key]:
                miniList.append(strs[number])
            result.append(miniList)
        return result
        """

             


"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters
"""