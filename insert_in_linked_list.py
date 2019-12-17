from unittest import TestCase

class testLinkedList(TestCase):

    def test_insert_linked_list(self):
        llist = LinkedList()

        llist.head = Node(1)
        second = Node(2)
        third = Node(3)
        forth = Node(4)

        llist.head.next = second
        second.next = third
        third.next = forth

        llist.push(5)
        self.assertEqual([5,1,2,3,4], llist.traverseList())


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def traverseList(self):
        arrList = []
        temp = self.head

        while (temp):
            arrList.append(temp.data)
            temp = temp.next

        return arrList

    def push(self, new_data):

        new_node = Node(new_data)

        new_node.next = self.head

        self.head = new_node
