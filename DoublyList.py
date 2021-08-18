## Priority Queue Data Structure
## Author: Alexander Christopher
## 08/17/2021

class Node:
    def __init__(self, value):
        """ Initialize a subclass object for later use. """
        self.__previous = None
        self.__next = None
        self.__value = value

    def get_previous(self):
        """ return the start pointer. """
        return self.__previous

    def get_value(self):
        """ return the value. """
        return self.__value

    def get_next(self):
        """ return the end pointer. """
        return self.__next

    def get_all(self):
        """ Return the previous, value and next objects """
        return [self.__previous, self.__value, self.__next]

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
        self.__firstNode = None
        self.__lastNode = None
        self.__size = 0

    def add_first(self, v):
        """ Add a node to the front of the list. """
        if self.__size == 0:
            ## list is empty
            n = Node(v)
            self.__firstNode = n
            self.__lastNode = n
            self.__size += 1
        else:
            ## list has one or more elements
            n = Node(v)
            current = self.__firstNode
            current.set_previous(n)
            n.set_next(current)
            self.__firstNode = n
            self.__size += 1

    def add_last(self, v):
        """ Add item to end of the object """
        if self.__size == 0:
            ## list is empty
            n = Node(v)
            self.__firstNode = n
            self.__lastNode = n
            self.__size += 1
        else:
            ## list has one or more elements
            n = Node(v)
            current = self.__lastNode
            current.set_next(n)
            n.set_previous(current)
            self.__lastNode = n
            self.__size += 1

    def add(self, v, index):
        """ Add an element anywhere in the DoubleLinkedList object, index starts at 0. """
        if self.__size == 0 or index == 0:
            ## add object at front of list
            self.add_first(v)
        elif index >= self.__size-1:
            ## add object at end of list
            self.add_last(v)
        elif index > 0 and index  < self.__size-1:
            ## add object where specified by index
            return
        else:
            return False

    def get_first(self):
        """ Get the first item in object. """
        return self.__firstNode

    def get_last(self):
        """ Return the last item in object. """
        return self.__lastNode

    def get(self, index):
        """ Return an element anywhere in the DoubleLinkedList object, index starts at 0. """
        if self.__size == 0 or index == 0:
            ## return object at front of list
            return self.get_first()
        elif index >= self.__size-1:
            ## return object at end of list
            return self.get_last()
        elif index > 0 and index  < self.__size-1:
            ## return object where specified by index
            return
        else:
            return False

    def get_size(self):
        """ Return the size of object. """
        return self.__size

    def delete_first(self):
        """ Delete the first item in the object. """
        if self.__size == 0:
            ## list is empty
            return None
        elif self.__size == 1:
            ## List has one object
            current = self.__firstNode
            self.__firstNode, self.__lastNode = None, None
            self.__size -= 1
            return current.get_value()
        else:
            ## list has one or more elements
            current = self.__firstNode
            next = current.get_next()
            next.set_previous = None
            self.__firstNode = next
            self.__size -= 1
            return current.get_value()

    def delete_last(self):
        """ Delete the last item in the object. """
        if self.__size == 0:
            ## list is empty
            return None
        elif self.__size == 1:
            ## List has one object
            current = self.__firstNode
            self.__firstNode, self.__lastNode = None, None
            self.__size -= 1
            return current.get_value()
        else:
            ## list has one or more elements
            current = self.__lastNode
            prev = current.get_previous()
            prev.set_next = None
            self.__lastNode = prev
            self.__size -= 1
            return current.get_value()

    def delete(self, index):
        """ Return an element anywhere in the DoubleLinkedList object, index starts at 0. """
        if self.__size == 0 or index == 0:
            ## delete object at front of list
            self.delete_first()
        elif index >= self.__size-1:
            ## delete object at end of list
            self.delete_last()
        elif index > 0 and index  < self.__size-1:
            ## delete object where specified by index
            return
        else:
            return False


    def __str__(self):
        """ return the entire list as a list. """
        return


## Testing
t = DoubleLinkedList()
t.add_first('test1')
print(t.get_first().get_all(), t.get_last().get_all())
print(t.get_size())
print(t.delete_first())
print(t.get_first(), t.get_last())
print(t.get_size())
print()

t.add_last('test2')
print(t.get_first().get_all(), t.get_last().get_all())
print(t.get_size())
print(t.delete_last())
print(t.get_first(), t.get_last())
print(t.get_size())
print()

t.add_first('test1')
t.add_last('test2')
print(t.get_first().get_all(), t.get_last().get_all())
print(t.get_size())
print(t.delete_last())
print(t.get_first(), t.get_last())
print(t.get_size())
print()
