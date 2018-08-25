class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

def findKthLastNode(head_node, k):
    dict_list = {}
    node = head_node
    count = 0
    while node is not None:
        count += 1
        dict_list[count] = node
        node = node.next
    return dict_list[count - k + 1]

def printLinkedList(head_node):
    current_node = head_node
    while current_node is not None:
        print current_node.val ,
        current_node = current_node.next


node1 = ListNode(2)
node2 = ListNode(1)
node3 = ListNode(10)
node4 = ListNode(1)
node1.next = node2
node2.next = node3
node3.next = node4

print printLinkedList(node1)
print (findKthLastNode(node1, 1)).val
