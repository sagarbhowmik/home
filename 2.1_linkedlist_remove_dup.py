class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

def removeDuplicateNodes(head_node):
    node_list = []
    current_node = head_node
    previous_node = None
    while current_node is not None:
        if current_node.val not in node_list:
            node_list.append(current_node.val)
            previous_node = current_node
        else:
            previous_node.next = current_node.next
        current_node = current_node.next
    return head_node

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
print printLinkedList(removeDuplicateNodes(node1))



