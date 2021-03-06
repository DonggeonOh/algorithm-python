class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def insert_node_at_position(llist, data, position):
    """ 해커랭크 Insert a node at a specific position in a linked list 솔루션 """
    new_list = SinglyLinkedListNode(data)
    head = llist

    for _ in range(position - 1):
        llist = llist.next

    new_list.next = llist.next
    llist.next = new_list

    return head
