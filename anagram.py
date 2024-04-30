from collections import defaultdict

def groupAnagram(arr):
    sortedAnagram = defaultdict(list)
    result = []
    for s in arr:
        sorted_s = tuple(sorted(s))
        sortedAnagram[sorted_s].append(s)
    for val in sortedAnagram.values():
        result.append(val)
        
    return result
class Solution:
    def anagram(self, arr):
        sortIt = {}
        for s in arr:
            hash = self.get_hash(s)
            if hash in sortIt:
                sortIt[hash].append(s)
                print(sortIt)
            else:
                sortIt[hash] = [s]
                print(sortIt)
            
        return list(sortIt.values())
        
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h
    

arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution = Solution() 
print(solution.anagram(arr))
# print(result)