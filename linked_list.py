class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head: Node = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def get_size(self):
        size = 0
        node = self.head
        while node is not None:
            size += 1
            node = node.next
        return size

    def get_simple_list(self):
        simple_list = []
        node = self.head
        while node is not None:
            simple_list.append(node.data)
            node = node.next
        return simple_list

    def dump_from_simple_list(self, simple_list: list):
        try:
            self.head = Node(simple_list.pop())
        except IndexError:
            print('Given list is empty')
            return

        node = self.head

        for element in simple_list:
            node.next = Node(element)
            node = node.next




