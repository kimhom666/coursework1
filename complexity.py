from binarysearchtree import TreeNode, BinarySearchTree
from linkedlist import ListNode, LinkedList
import random
import time
import math


def random_tree(n):
    bst = BinarySearchTree(None)
    l_list = LinkedList(None)
    arr= []
    for i in range(n):
        random_int = random.randint(0, 1000)
        arr.append(random_int)
        l_list.insert(random_int)
        bst.insert(random_int)
    return bst, l_list


def first_bigger_than_target_number(array, target):
    print(array)
    print(len(array))
    for num in array:
        if num > target:
            return num


if __name__ == '__main__':
    X = list(range(5, 105, 5))
    Y = []
    Y4 = []
    for i in range(len(X)):
        tree_search_time = 0
        l_list_search_time = 0
        for _ in range(0, 1000):
            bst, l_list = random_tree(X[i])
            # print(bst.is_balance())
            if not bst.is_balance():
                bst.print_tree()
                raise Exception("sad")
            tree_search_start_time = time.time()
            bst.search(42)
            tree_search_end_time = time.time()
            tree_search_time_once = tree_search_end_time - tree_search_start_time
            tree_search_time += tree_search_time_once

            l_list_start_search_time = time.time()
            l_list.search(42)
            l_list_start_end_time = time.time()
            l_list_search_time_once = l_list_start_end_time - l_list_start_search_time
            l_list_search_time += l_list_search_time_once
        # the binary search tree search time
        Y.append(tree_search_time / 1000)
        Y4.append(l_list_search_time / 1000)

    # There are chances where search time t for n = 10 is less than that of n = 5 which would make the slope negative,
    # therefore I decided to use the first search time t which is bigger than that of n = 5
    fb = first_bigger_than_target_number(Y, Y[0])
    c = (fb - Y[0]) / 5
    b = Y[0] - c * 5
    # the linear function
    Y2 = [c * n + b for n in X]
    c_2 = (fb - Y[0]) / (math.log(10, 2) - math.log(5, 2))
    b_2 = Y[0] - c * math.log(5, 2)
    # the logarithmic function
    Y3 = [c_2 * math.log(n) + b_2 for n in X]
    import matplotlib.pyplot as plt

    # Complexity analysis X vs Y is logarithmic, because for a balanced tree, the height of tree is equivalent or
    # greater than Log2(N) where N is the number of the nodes. Therefore, generally there will be Log(n) times of
    # comparison, so it's O(logN). While the best case is when the root is the value, the worst is when the right leaf
    # node is the value or the value is not in the tree. However, since Tree's balanced, therefore the worst case is
    # still O(logN). And if the tree is not balanced, the worst case is when the tree resemble a linked list, the search
    # complexity will be O(N).

    plt.plot(X, Y)
    # Complexity analysis X vs Y, Y2 and Y3, as we can see the Y is approaching Y3 as the size increases, while the gap
    # between Y2 and Y is becoming bigger and bigger I think that's because the complexity of a balanced BST search is
    # O(logN). But the Y is not the exactly the same as Y3 and almost always lower than Y3, that's because the search
    # does not require Log(N) operations everytime, where N is the number of the nodes, it might stop in the middle
    # layer, and even stop at the root (when the value of the root is value we are searching for).

    plt.plot(X, Y2)
    plt.plot(X, Y3)

    # Complexity analysis X vs Y, Y2, Y3 and Y4, as it shows in the graph, Y4 is approaching Y2, as the size increases.
    # The average search complexity of Linked List search is O(N). There are circumstances where Y4 is lower than Y2,
    # that's because the search might stop before reaching the last node of the linked list. The best case is that the
    # value of the first node is the value that is being searched for, the worst case is no such value in the list, or
    # the value that's being searched for lies in the last node. Meanwhile Y4 and Y2 is generally higher than Y and Y3,
    # since the are linear. And the discrepancy becomes bigger as the size increases.
    # So we can say for increasingly larger n this should be much faster than a regular linked list.
    plt.plot(X, Y4)
    plt.legend(['BST', 'Linear', 'Logarithmic', "Linked List"])
    plt.xlabel('Size of trees')
    plt.ylabel('Search time')
    plt.ticklabel_format(axis='both', style='sci', scilimits=(0, 0))
    plt.show()
