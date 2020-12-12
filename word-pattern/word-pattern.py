class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words=str.split(" ")
        if len(pattern)!=len(words):
            return False
        
        dicPattern={}
        dicWord={}
        for i in range(len(pattern)):
            if pattern[i] not in dicPattern:
                dicPattern[pattern[i]]=words[i]
            else:
                if dicPattern[pattern[i]]!=words[i]:
                    return False
        for i in range(len(words)):
            if words[i] not in dicWord:
                dicWord[words[i]]=pattern[i]
            else:
                if dicWord[words[i]]!=pattern[i]:
                    return False
        return True
            
        
