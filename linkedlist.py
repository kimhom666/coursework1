class ListNode:

    def __init__(self, cargo, next_node):
        self.__cargo = cargo
        self.__next_node = next_node

    def print_node(self):
        print(self.__cargo)

    def get_cargo(self):
        return self.__cargo

    def set_cargo(self, cargo):
        self.__cargo = cargo

    def get_next_node(self):
        return self.__next_node

    def set_next_node(self, node):
        self.__next_node = node


class LinkedList:

    def __init__(self, starting_node, limit=10000):
        self.__starting_node = starting_node
        self.__limit = limit
        self.__size = 1 if starting_node else 0

    def is_empty(self):
        if self.__starting_node is None or self.__len__() == 0:
            return True
        return False

    def get_starting_node(self):
        return self.__starting_node

    def set_starting_node(self, starting_node):
        self.__starting_node = starting_node

    def get_limit(self):
        return self.__limit

    def set_limit(self, limit):
        self.__limit = limit

    def is_full(self):
        if self.__len__() == self.__limit:
            return True
        return False

    def __len__(self):
        return len(self.traverse())

    def traverse(self):
        node = self.__starting_node
        node_list = []
        while node:
            node_list.append(node.get_cargo())
            node = node.get_next_node()
        return node_list

    def __str__(self):
        return " -> ".join([str(item) for item in self.traverse()])

    @property
    def size(self):
        return self.__len__()

    def insert(self, value):
        # this is_full() is time-expensive, since it travels from the begin to the end
        assert not self.is_full(), "The Linked List is full."
        # assert self.__size != self.__limit, "The Linked List is full."
        last_node = self.__starting_node
        new_node = ListNode(value, None)
        if not last_node:
            self.__starting_node = new_node
            self.__size += 1
            return
        while last_node.get_next_node():
            last_node = last_node.get_next_node()
        last_node.set_next_node(new_node)
        self.__size += 1

    def search(self, value):
        node = self.__starting_node
        while node:
            if node.get_cargo() == value:
                return True
            node = node.get_next_node()
        return False

    def delete(self, value):
        # this is time-expensive, since it travels from the begin to the end
        assert not self.is_empty(), "The Linked List is empty."
        # assert self.__size > 0, "The Linked List is empty."
        node = self.__starting_node
        father_node = None
        # The situation where the head node value = the value
        if node is not None and node.get_cargo() == value:
            self.__starting_node = node.get_next_node()
            self.__size -= 1
            return True
        # the else situation where the value is behind head node
        else:
            while node and node.get_cargo() != value:
                father_node = node
                node = node.get_next_node()
            if node:
                father_node.set_next_node(node.get_next_node())
                self.__size -= 1
                return True
            else:
                # Inspired by the Python Built-in List
                raise Exception("No Such Value {} in linked list".format(value))

