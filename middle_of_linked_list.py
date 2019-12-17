from unittest import TestCase

class testLinkedList(TestCase):

    def test_deletion_linked_list(self):
        llist = LinkedList()

        llist.head = Node(1)
        second = Node(2)
        third = Node(3)
        forth = Node(4)
        fifth = Node(5)
        sixth = Node(6)
        seventh = Node(7)

        llist.head.next = second
        second.next = third
        third.next = forth
        forth.next = fifth
        fifth.next = sixth
        sixth.next = seventh

        mn = llist.getMiddle()

        self.assertEqual(4, mn.data)


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):

        new_node = Node(new_data)

        new_node.next = self.head

        self.head = new_node

    def getMiddle(self):
        slow_ptr = self.head
        fast_ptr = self.head

        if self.head is not None:
            while (fast_ptr is not None and fast_ptr.next is not None):
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next

        return slow_ptr
