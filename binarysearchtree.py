# An AVL balanced Tree


class TreeNode:

    def __init__(self, cargo, left_child, right_child):
        """

        :param cargo: The numerical of the node
        :param left_child: The
        :param right_child:
        """
        self.__cargo = cargo
        self.__left_child = left_child
        self.__right_child = right_child
        self.__times = 1
        self.__height = 1
        self.__times = 1

    def get_times(self):
        return self.__times

    def set_times(self, times):
        self.__times = times

    def get_height(self):
        return self.__height

    def update_height(self):
        self.__height = 1 + max(self.get_right_child().get_height() if self.get_right_child() else 0,
                                self.get_left_child().get_height() if self.get_left_child() else 0)

    def set_height(self, height):
        self.__height = height

    def set_cargo(self, cargo):
        self.__cargo = cargo

    def get_cargo(self):
        return self.__cargo

    def set_left_child(self, left_child):
        self.__left_child = left_child

    def get_left_child(self):
        return self.__left_child

    def set_right_child(self, right_child):
        self.__right_child = right_child

    def get_right_child(self):
        return self.__right_child

    """ <reference>
        <function name> rotate_right </function name>
        <source> 
        <author> codingriver </author>
        <SourceCodeCategory> C </SourceCodeCategory>
        <URL> https://wgqing.com/avl%E6%A0%91%E8%AF%A6%E8%A7%A3/ </URL>
        </source>
        </reference>
    """

    # These functions below can make sure tree balanced
    # right rotation when the sub-tree is left unbalanced
    def rotate_right(self):
        new_root = self.get_left_child()
        self.set_left_child(new_root.get_right_child())
        new_root.set_right_child(self)
        self.update_height()
        new_root.set_height(max(new_root.get_height(), self.get_height() + 1))
        return new_root

    """ <reference>
        <function name> rotate_left </function name>
        <source> 
        <author> codingriver </author>
        <SourceCodeCategory> C </SourceCodeCategory>
        <URL> https://wgqing.com/avl%E6%A0%91%E8%AF%A6%E8%A7%A3/ </URL>
        </source>
        </reference>
    """

    # left rotation when the sub-tree is right unbalanced
    def rotate_left(self):
        new_root = self.get_right_child()
        self.set_right_child(new_root.get_left_child())
        new_root.set_left_child(self)
        self.update_height()
        new_root.set_height(max(new_root.get_height(), self.get_height() + 1))
        return new_root

    """ <reference>
        <function name> get_balance_factor </function name>
        <source> 
        <author> codingriver </author>
        <SourceCodeCategory> C </SourceCodeCategory>
        <URL> https://wgqing.com/avl%E6%A0%91%E8%AF%A6%E8%A7%A3/ </URL>
        </source>
        </reference>
    """

    # negative when right unbalanced, positive left unbalanced
    def get_balance_factor(self):
        return (self.get_left_child().get_height() if self.get_left_child() else 0) - (
            self.get_right_child().get_height() if self.get_right_child() else 0)

    """ <reference>
        <function name> balance_node </function name>
        <source> 
        <author> codingriver </author>
        <SourceCodeCategory> C </SourceCodeCategory>
        <URL> https://wgqing.com/avl%E6%A0%91%E8%AF%A6%E8%A7%A3/ </URL>
        </source>
        </reference>
    """

    def balance_node(self):
        balance_factor = self.get_balance_factor()
        # The L case, more nodes on L than that of R
        if balance_factor > 1:
            if self.get_left_child().get_balance_factor() < 0:
                # The LR case, do a left rotation first
                self.set_left_child(self.get_left_child().rotate_left())
            # The LL case without left rotation and LR case with left rotation
            return self.rotate_right()
        # The R case, more nodes on R than that of L
        if balance_factor < -1:
            if self.get_right_child().get_balance_factor() > 0:
                # The RL case, do a right rotation first
                self.set_right_child(self.get_right_child().rotate_right())
            # The RR case without right rotation and RL case with right rotation
            return self.rotate_left()
        # If balanced, return self
        return self


class BinarySearchTree:

    def __init__(self, root, size_limit=1000000):
        self.__root = root
        self.__size_limit = size_limit

    def get_root(self):
        return self.__root

    def set_root(self, root):
        self.__root = root

    def get_size_limit(self):
        return self.__size_limit

    def set_size_limit(self, size_limit):
        self.__size_limit = size_limit

    def is_empty(self):
        if self.__root is None or self.get_tree_size() == 0:
            return True
        return False

    def get_tree_size(self):
        all_nodes = self.get_all_tree_node()
        all_not_none_nodes = [item for item in all_nodes if item is not None]
        sizeOfTree = len(all_not_none_nodes)
        return sizeOfTree

    def is_full(self):
        if not self.__root:
            return False
        sizeOfTree = self.get_tree_size()
        if sizeOfTree == self.__size_limit:
            return True
        return False

    def search_node(self, value):
        node = self.__root
        if value == node.get_cargo():
            return node
        while node.get_left_child() is not None or node.get_right_child() is not None:
            if value < node.get_cargo():
                if node.get_left_child() is None:
                    return None
                else:
                    node = node.get_left_child()
                    if value == node.get_cargo():
                        return node
            if value > node.get_cargo():
                if node.get_right_child() is None:
                    return None
                else:
                    node = node.get_right_child()
                    if value == node.get_cargo():
                        return node
        return None

    def search(self, value):
        # Using the search_node function which could return a node helps the duplicated value situation.
        return True if self.search_node(value) else False

    """ <reference>
        <function name> insert </function name>
        <source> 
        <author> codingriver </author>
        <SourceCodeCategory> C </SourceCodeCategory>
        <URL> https://wgqing.com/avl%E6%A0%91%E8%AF%A6%E8%A7%A3/ </URL>
        </source>
        </reference>
    """

    def insert(self, value):
        assert not self.is_full(), "The Tree is full."
        # if the value is already in the tree, then edit the times attribute of that value.
        if self.__root is not None:
            node = self.search_node(value)
            if node:
                node.set_times(node.get_times() + 1)
                return
        root = self.__root
        stack = []
        # Using Loop instead of recursive to reduce the memory usage.
        while root:
            if value < root.get_cargo():
                stack.append((root, True))
                root = root.get_left_child()
            else:
                stack.append((root, False))
                root = root.get_right_child()
        inserting_node = TreeNode(value, None, None)
        # the node value in the stack is strictly decreasing
        while stack:
            temp_root, is_left_child = stack.pop()
            if is_left_child:
                temp_root.set_left_child(inserting_node)
            else:
                temp_root.set_right_child(inserting_node)
            # updating the height of temp_root tree_node
            temp_root.set_height(max(inserting_node.get_height() + 1, temp_root.get_height()))
            inserting_node = temp_root.balance_node()
        self.__root = inserting_node

    """ <reference>
            <function name> delete </function name>
            <source> 
            <author> codingriver </author>
            <SourceCodeCategory> C </SourceCodeCategory>
            <URL> https://wgqing.com/avl%E6%A0%91%E8%AF%A6%E8%A7%A3/ </URL>
            </source>
            </reference>
        """

    def delete(self, value):
        assert not self.is_empty(), "The Tree is empty."
        assert self.search(value), "No such value {} in the tree.".format(value)
        root = self.__root
        stack = []
        while root.get_cargo() != value:
            if value < root.get_cargo():
                stack.append((root, True))
                # can only be less, therefore it moves to the left
                root = root.get_left_child()
            else:
                stack.append((root, False))
                # can only be bigger, therefore it moves to the right
                root = root.get_right_child()

        # transfer the node
        if root.get_right_child():
            # replace root by the mini of root.right
            node, by_far_min = self.delete_min(root.get_right_child())
            root.set_cargo(by_far_min)
            root.set_right_child(node)
            root.update_height()
            root = root.balance_node()
        else:
            root = root.get_left_child()
        # judge whether it's balance or not
        while stack:
            temp_root, is_left_child = stack.pop()
            if is_left_child:
                temp_root.set_left_child(root)
            else:
                temp_root.set_right_child(root)
            # temp_root_height = temp_root.get_height()
            temp_root.update_height()
            root = temp_root.balance_node()
        self.__root = root

    """ <reference>
        <function name> delete_min </function name>
        <source> 
        <author> codingriver </author>
        <SourceCodeCategory> C </SourceCodeCategory>
        <URL> https://wgqing.com/avl%E6%A0%91%E8%AF%A6%E8%A7%A3/ </URL>
        </source>
        </reference>
    """

    def delete_min(self, node):
        stack = []
        # add the ones less than the root.right_child
        while node.get_left_child():
            stack.append(node)
            node = node.get_left_child()
        # get the minimum on this branch
        by_far_min_value = node.get_cargo()
        node = node.get_right_child()
        while stack:
            temp_root = stack.pop()
            temp_root.set_left_child(node)
            temp_root.update_height()
            node = temp_root.balance_node()
        return node, by_far_min_value

    def is_balance(self):
        # when the tree is empty
        if not self.__root:
            return True
        if self.get_root().get_left_child() and self.get_root().get_right_child():
            if abs(self.tree_height(self.get_root().get_left_child()) - self.tree_height(
                    self.get_root().get_right_child())) > 1:
                return False
        elif self.get_root().get_left_child() is not None:
            if self.tree_height(self.get_root().get_left_child()) > 1:
                return False
        elif self.get_root().get_right_child() is not None:
            if self.tree_height(self.get_root().get_right_child()) > 1:
                return False
        return True

    def tree_height(self, root_node):
        return max(self.tree_height(root_node.get_left_child()) + 1 if root_node.get_left_child() and root_node else 1,
                   self.tree_height(
                       root_node.get_right_child()) + 1 if root_node.get_right_child() and root_node else 1)

    def traverse(self):
        # using a iterative rather than recursive to save memory, but less intuitive
        # inorder traverse helps get an ascending order tree node.
        traverse_stack = []
        ascending_order = []
        node = self.__root
        while node is not None or len(traverse_stack) != 0:
            while node is not None:
                traverse_stack.append(node)
                node = node.get_left_child()
            node = traverse_stack.pop()
            ascending_order.append(node.get_cargo())
            node = node.get_right_child()
        return ascending_order

    def get_all_tree_node(self):
        """
        :return: a list of tree nodes in breadth_first traversal
        """
        this_level = [self.__root]
        tree_nodes = [self.__root.get_cargo()]
        while this_level:
            next_level = []
            for node in this_level:
                if node is not None:
                    if node.get_right_child() or node.get_left_child():
                        tree_nodes.append(node.get_left_child().get_cargo() if node.get_left_child() else None)
                        tree_nodes.append(node.get_right_child().get_cargo() if node.get_right_child() else None)
                        next_level.append(node.get_left_child())
                        next_level.append(node.get_right_child())
            this_level = next_level
        return tree_nodes

    """
    <reference>
    <function> print_tree </function>
    <author>yangshun</author>
    <URL> https://leetcode.com/problems/print-binary-tree/discuss/106273/Simple-Python-with-thorough-explanation </URL>
    </reference>
    """

    def print_tree(self):
        """

        """
        # under special circumstance where the tree is not generated by insert function,
        # the height of tree could be ambiguous, therefore, we need to update the tree height first
        # if the root is None
        root = self.__root
        if not root:
            print("Empty Tree")
            return
        rows = self.tree_height(root)
        cols = 2 ** rows - 1
        # the whole scale of the tree
        res = [['' for _ in range(cols)] for _ in range(rows)]

        def traverse(node, level, pos):
            if not node:
                return
            left_padding = 2 ** (rows - level - 1) - 1
            spacing = 2 ** (rows - level) - 1
            index = left_padding + pos * (spacing + 1)
            res[level][index] = str(node.get_cargo())
            traverse(node.get_left_child(), level + 1, pos << 1)
            traverse(node.get_right_child(), level + 1, (pos << 1) + 1)

        traverse(root, 0, 0)
        for level in res:
            print("  ".join(level))
