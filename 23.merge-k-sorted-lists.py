#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         values = []

#         for ll in lists:
#             curr = ll
#             while curr is not None:
#                 values.append(curr)
#                 curr = curr.next

#         values.sort(key=lambda x: x.val)

#         head = ListNode()
#         curr = head
#         for node in values:
#             curr.next = node
#             curr = curr.next

#         return head.next

# class Solution:
#      def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         if len(lists) == 0:
#             return None

#         def merge(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#             head = ListNode()
#             curr = head

#             while list1 and list2:
#                 if list1.val < list2.val:
#                     curr.next = list1
#                     list1 = list1.next
#                 else:
#                     curr.next = list2
#                     list2 = list2.next
                
#                 curr = curr.next

#             if list1:
#                 curr.next = list1
            
#             if list2:
#                 curr.next = list2

#             return head.next

#         merged_lists = lists[:]
#         while len(merged_lists) > 1:
#             tmp = []
#             for i in range(0, len(merged_lists), 2):
#                 l1 = merged_lists[i]
#                 l2 = None if i + 1 == len(merged_lists) else merged_lists[i + 1]
#                 tmp.append(merge(l1, l2))
            
#             merged_lists = tmp

#         return merged_lists[0]

from heapq import heappush, heappop


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        heap = []
        unique_inc = 0

        for ll in lists:
            if ll is None:
                continue
            heappush(heap, (ll.val, unique_inc, ll))
            unique_inc += 1

        head = ListNode()
        curr = head
        while len(heap) > 0:
            _, _, node = heappop(heap)
            curr.next = node
            curr = curr.next

            if node.next is not None:
                heappush(heap, (node.next.val, unique_inc, node.next))
                unique_inc += 1
        
        return head.next

        
# @lc code=end

