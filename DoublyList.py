## Priority Queue Data Structure
## Author: Alexander Christopher
## 08/17/2021

class Node:
    def __init__(self):
        """ Initialize a subclass object for later use. """
        self.__previous = None
        self.__next = None
        self.__value = None

    def get_previous(self):
        """ return the start pointer. """
        return self.__previous

    def get_value(self):
        """ return the value. """
        return self.__value

    def get_next(self):
        """ return the end pointer. """
        return self.__next

    def set_previous(self, prev):
        """ Set the previous item object. """
        self.__previous = prev

    def set_next(self, next):
        """  Set the next item object. """
        self.__next = next

    def set_value(self, value):
        """  Set the value. """
        self.__value = value


class DoubleLinkedList(Node):
    def __init__(self):
        """ Initialize the require data structures to create PriorityQueue Data Structure. """
        self.__previousNode = None
        self.__nextNode = None

    def add_first(self, v):
        """ """
        return

    def add_last(self, v):
        """ """
        return

    def insert(self, v, p):
        """ """
        return

    def get_frist(self):
        """ """
        return

    def get_last(self):
        """ """
        return

    def get(self, p, v):
        """ """
        return

    def delete_first(self, v):
        """ """
        return

    def delete_last(self, v):
        """ """
        return

    def delete(self, v, p):
        """ """
        return

    def return_full_list(self):
        """ """
        return
