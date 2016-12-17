""" 
.. module:: LinkedList 
   :platform: Unix, Windows 
   :synopsis: Load the file with the values every. The file must be in the same directory with the name 
  >>> values.txt. 
.. moduleauthor:: Jaime Jimenez 
"""

class Node(object):
    
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList(object):

    def __init__(self):
        self.head = None

    def add(self, value):
        """Add new item to linked list. 
        Args: 
           value: Value of node.
        >>> print add(self, value)
        
        """
        node = Node(value, self.head)
        self.head = node

    def remove(self, value):
        """Remove item by value. 
        Args: 
           value: Value of node.
        >>> print remove(self, value)

        """ 
        current = self.head
        previous = None
        # search the node with the data. 
        # Keep in memory the previous to validate when it is head so point the new head
        while current:
            if current.value == value:
                break
            else:
                previous = current
                current = current.next
        if current is None:
            raise ValueError('No se encontró el elemento')
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    def get_prior(self):
        """Return the first node. 
        Args: 
           value: Value of node.
        Returns: 
           Node.  The first node 

        >>> print get_prior(self, value) self.head

        """ 
        return self.head

    # Get the node next to the node with match with the value
    def get_next_by_value(self, value):
        """Get the node immediatelly next to the first node with that match with the value. 
        Args: 
           value: Value of node to search.
        Returns: 
           Node.  The next to the node that match with the value

        >>> print remove(self, value) current.next

        """
        current = self.head
        while current:
            if current.value == value:
                return current.next
            else:
                current = current.next

        if current is None:
            raise ValueError('No se encontró el elemento')

    def __getitem__(self, index):
        """To able the clase as iterative. 
        Args: 
           index: Index of iteration.
        Returns: 
           Node.  Node in position = index

        >>> print __getitem__(self, index) nd

        """
        nd = self.head
        for i in range(0,index):
            if nd.next is None:
                raise StopIteration
            nd = nd.next
        return nd
