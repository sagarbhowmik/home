"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # def get_value(self):
    #     return self.val
    #
    # def get_next(self):
    #     return self.next
    #
    # def set_next(self, new_next):
    #     self.next = new_next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_int = self.getIntegerValue(l1)
        l2_int = self.getIntegerValue(l2)
        sum_int = l1_int + l2_int
        print(sum_int)
        if sum_int == 0:
            return [0]
        sum_node = self.getLinkedList(sum_int)
        sum_list = []
        while sum_node is not None:
            sum_list.append(sum_node.val)
            sum_node = sum_node.next
        return sum_list

    def getIntegerValue(self, l):
        """
        :param l: ListNode
        :return: Integer
        """
        p = 0
        l_int = 0
        while l is not None:
            # print("Current value {}".format(l.get_value()))
            l_int += l.val * 10 ** p
            p += 1
            l = l.next
        return l_int

    def getLinkedList(self, i):
        """
        :param i: Integer
        :return: ListNode
        """
        quotient = i
        remainder = []
        while quotient != 0:
            quotient = i // 10
            remainder.append(i % 10)
            i = quotient
        head_node = new_node = ListNode(remainder[0])
        for r in range(1, len(remainder)):
            new_node.next = ListNode(remainder[r])
            new_node = new_node.next
        return head_node


def main():
    l1_2 = ListNode(2)
    l1_4 = ListNode(4)
    l1_3 = ListNode(3)

    l2_5 = ListNode(5)
    l2_6 = ListNode(6)
    l2_4 = ListNode(4)

    l1_2.next = l1_4
    l1_4.next = l1_3

    l2_5.next = l2_6
    l2_6.next = l2_4

    la = ListNode(5)
    lb = ListNode(5)

    sol = Solution()
    print(sol.addTwoNumbers(l1_2, l2_5))
    print(sol.addTwoNumbers(la, lb))


if __name__ == "__main__":
    main()
