class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def sorted_insert(llist, data):
    if llist is None:
        llist = DoublyLinkedListNode(data)
        return llist

    elif data < llist.data:
        temp = DoublyLinkedListNode(data)
        temp.next, llist.prev = llist, temp
        return temp

    head = llist

    while llist:
        if data < llist.data:
            temp = DoublyLinkedListNode(data)
            temp.prev = llist.prev
            temp.next = llist

            llist.prev.next = temp
            llist.prev = temp

            return head

        if llist.next:
            llist = llist.next
        else:
            break

    temp = DoublyLinkedListNode(data)
    llist.next = temp
    temp.prev = llist

    return head
