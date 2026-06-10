# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = [[n.val, i, n] for i, n in enumerate(lists)]
        heapq.heapify(pq)
        head = None
        tail = None
        while pq:
            top = heapq.heappop(pq)
            cn = top[2]
            nn = cn.next
            if head is None:
                head = cn
                tail = cn
            else:
                tail.next = cn
                tail = tail.next
            if nn is not None:
                heapq.heappush(pq, [nn.val, top[1], nn])
        return head

        