"""Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together
the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


def print_linked_list(list_node):
    """

    :param l: ListNode
    :return: ListNode
    """
    list_str = ""
    while list_node is not None:
        list_str += str(list_node.val)
        list_str += "->"
        list_node = list_node.next
    print(list_str[:-2])


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        combined_list = []
        if l1 is None and l2 is None:
            return None
        while l1 is not None or l2 is not None:
            if l1 is not None:
                combined_list.append(l1.val)
                l1 = l1.next
            if l2 is not None:
                combined_list.append(l2.val)
                l2 = l2.next
        combined_list.sort()
        head_node = ListNode(combined_list[0])
        current_node = head_node
        if len(combined_list) == 1:
            return head_node
        for each in combined_list[1:]:
            current_node.next = ListNode(each)
            current_node = current_node.next
        return head_node


sol = Solution()
l1_1 = ListNode(1)
l1_2 = ListNode(2)
l1_1.next = l1_2
l1_3 = ListNode(4)
l1_2.next = l1_3

l2_1 = ListNode(1)
l2_2 = ListNode(3)
l2_1.next = l2_2
l2_3 = ListNode(4)
l2_2.next = l2_3

l3_1 = ListNode(5)

l_add = sol.mergeTwoLists(l1_1, l3_1)

print_linked_list(l1_1)
print_linked_list(l2_1)
print_linked_list(l_add)


