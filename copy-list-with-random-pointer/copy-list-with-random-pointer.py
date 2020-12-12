"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        newHead=head
        newMap={}
        if not head:
            return None
        flag=True
        while newHead!=None:
            newMap[newHead]=Node(newHead.val,None,None)
            if flag:
                finalHead=newMap[newHead]
                flag=False
            newHead=newHead.next
        for i in newMap:
            if i.next in newMap:
                newMap[i].next=newMap[i.next]
            if i.random in newMap:
                newMap[i].random=newMap[i.random]
        return finalHead
        
            
        
