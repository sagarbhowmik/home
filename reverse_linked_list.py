"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def PrintLinkedList(head_node):
    current_node = head_node
    while (current_node is not None):
        if current_node.next == None:
            print str(current_node.val)
        else:
            print str(current_node.val) + " -> ",
        current_node = current_node.next

class Solution(object):
    def reverseList(self, head_node):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current_node = head_node
        rev_head_node = None
        while (current_node is not None):
            temp_node = current_node.next
            current_node.next = rev_head_node
            rev_head_node = current_node
            current_node = temp_node
        return rev_head_node

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

PrintLinkedList(node1)
PrintLinkedList(Solution().reverseList(node1))