#!/usr/bin/python3
"""
Module: 100-singly_linked_list
Class: Node, SinglyLinkedList
Defines a singly linked list with sorted insertion.
"""

class Node:
    """
    Class: Node
    Defines a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node instance.

        Parameters:
        - data: The data for the node (must be an integer).
        - next_node: The next node in the list (must be a Node object or None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for the data attribute.

        Returns:
        - int: The data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method for the data attribute.

        Parameters:
        - value: The new value for the data attribute (must be an integer).

        Raises:
        - TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method for the next_node attribute.

        Returns:
        - Node: The next node in the list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for the next_node attribute.

        Parameters:
        - value: The new value for the next_node attribute (must be a Node object or None).

        Raises:
        - TypeError: If value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object or None")
        self.__next_node = value
class SinglyLinkedList:
    """
    Class: SinglyLinkedList
    Defines a singly linked list.
    """

    def __init__(self):
        """
        Initializes a new SinglyLinkedList instance with an empty head.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).

        Parameters:
        - value: The value to be inserted.
        """
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the singly linked list.

        Returns:
        - str: A string representation of the list.
        """
        result = []
        current = self.head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)
