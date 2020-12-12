class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        dictionary=defaultdict(list)
        for word in strs:
            arr=[0]*26
            for char in word:
                arr[ord(char)-ord('a')]+=1
            dictionary[tuple(arr)].append(word)
        return dictionary.values()
            
            
                
        
