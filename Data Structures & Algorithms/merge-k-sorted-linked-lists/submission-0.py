# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = lists
        head = None
        tail = None
        while True:
            minn = None
            midx = None
            for i, n in enumerate(nodes):
                if n is None:
                    continue
                if minn is None:
                    minn = n.val
                    midx = i
                elif n.val < minn:
                    minn = n.val
                    midx = i
            if minn is None:
                break
            if head is None:
                head = nodes[midx]
                tail = nodes[midx]
            else:
                curr = nodes[midx]
                nodes[midx] = curr.next
                tail.next = curr
                tail = curr
        return head
                
                

