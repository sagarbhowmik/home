class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None


def LinkedListToNumber(head_node):
    if head_node is None:
        return 0
    current_node = head_node
    value, ten_power = 0, 0
    while current_node is not None:
        value += current_node.val * (10 ** ten_power)
        ten_power += 1
        current_node = current_node.next
    print value
    return value


def NumbertoLinkedList(integer_value):
    head_node = ListNode(None)
    current_node = ListNode(None)
    remainder = 0
    quotient = integer_value
    while quotient != 0:
        remainder = quotient % 10
        quotient /= 10
        if head_node.val is None:
            head_node.val = remainder
            head_node.next = current_node
        else:
            current_node.val = remainder
            current_node.next = ListNode(None)
            current_node = current_node.next
    printLinkedList(head_node)
    return head_node


def sumLinkedLists(nodeA, nodeB):
    return NumbertoLinkedList(LinkedListToNumber(nodeA) + LinkedListToNumber(nodeB))


def printLinkedList(head_node):
    current_node = head_node
    while current_node is not None:
        print current_node.val ,
        current_node = current_node.next


l1_2 = ListNode(2)
l1_4 = ListNode(4)
l1_3 = ListNode(3)

l2_5 = ListNode(5)
l2_6 = ListNode(6)


l1_2.next = l1_4
l1_4.next = l1_3

l2_5.next = l2_6


la = ListNode(5)
lb = ListNode(5)

sumLinkedLists(l1_2, l2_5)
sumLinkedLists(la, lb)