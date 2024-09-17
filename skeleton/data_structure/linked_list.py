try:
    from node import Node 
except ModuleNotFoundError:
    from data_structure.node import Node

class LinkedNode:
    """
    Represents a node in a singly linked list.

    Attributes:
    - node_id (Any): A unique identifier for the node.
    - datum (Any): The data stored in the node.
    - next (LinkedNode or None): Reference to the next node in the list.

    Detailed Explanation:
    A LinkedNode is an element of a singly linked list, which consists of nodes where each node points to the next node in the sequence. This allows traversal of the list from the head to the tail.

    The attribute node_id is NOT A FUNCTIONING ATTRIBUTE; IT IS SOLEY FOR DEBUGGING - SO YOU CAN ASSIGN ANY VALUE. However, it is advised to assign unique values for node_id, since it would be useful for the debugging. 

    Practical Usages:
    Linked nodes are used to build linked lists, which are fundamental in implementing data structures like stacks, queues, and for managing dynamic collections of items.

    Visual Illustration:

        [Node1] -> [Node2] -> [Node3] -> None
    """
    def __init__(self, node_id, datum, next = None):
        """
        Initializes a new instance of LinkedNode.

        Parameters:
        - node_id (Any): A unique identifier for the node.
        - datum (Any): The data to store in the node.
        - next (LinkedNode or None, optional): The next node in the linked list. Defaults to None.

        Returns:
        - None

        Visual Illustration:

            +---------+---------+
            | node_id |  datum  |
            +---------+---------+
                  |
                next -> None
        """
        self.node_id = node_id 
        self.datum = datum
        self.next = next 

    def set_next(self, next_node):
        """
        Sets the 'next' reference of the node.

        Parameters:
        - next_node (LinkedNode or None): The node to set as the next node. Can be None to indicate the end of the list.

        Returns:
        - None

        Visual Illustration:

            Before setting next:

            [Current Node] -> None

            After setting next:

            [Current Node] -> [Next Node] -> None
        """
        assert isinstance(next_node, LinkedNode) or next_node is None

        self.next = next_node     

class LinkedList:
    """
    Represents a singly linked list data structure.

    Attributes:
    - head (LinkedNode or None): The first node in the linked list.
    - tail (LinkedNode or None): The LinkedList instance excluding the first element in the original LinkedList.
    - end (LinkedNode or None): The last node in the linked list. 
    - size (int): The number of elements in the linked list.

    Detailed Explanation:
    A LinkedList is a sequence of nodes where each node points to the next node. This allows for efficient insertion and deletion of elements, especially at the beginning or end of the list.

    Practical Usages:
    Linked lists are useful when you need a data structure that can grow or shrink dynamically, and where elements need to be inserted or removed frequently.

    Visual Illustration:

        head
         |
        [Node1] -> [Node2] -> [Node3] -> None
    """
    def __init__(self, elements):
        """
        Initializes a new instance of LinkedList.

        Parameters:
        - elements (iterable): An iterable of elements to initialize the linked list with.

        Returns:
        - None

        Detailed Explanation:
        Creates a new linked list and populates it with the elements provided. If 'elements' is empty, it initializes an empty list. If the components of the input is not of type LinkedNode, convert it to LinkedNode. Assign node_id in any suitable manner; it is advised, however, to assign unique node_id for each LinkedList instance. 

        Visual Illustration:

            elements = [1, 2, 3]

            head
             |
            [1] -> [2] -> [3] -> None
        """
        if not elements:
            self.head = None 
            self.tail = None 
            self.end = None
            self.size = 0
        
    def append_to_head(self, elem): 
        """
        Adds an element to the beginning of the linked list.

        Parameters:
        - elem (Any): The element to be added to the head of the list.

        Returns:
        - None

        Detailed Explanation:
        Inserts a new node containing 'elem' at the beginning of the list. The new node becomes the new head. As in the initializer or other functions, when the elem is not the LinkedNode type, case it to the LinkedNode. 

        Visual Illustration:

            Before insertion:

            head
             |
            [Node1] -> [Node2] -> None

            After insertion of 'elem':

            head
             |
            [elem] -> [Node1] -> [Node2] -> None
        """
        pass

    def remove_from_head(self):
        """
        Removes and returns the element at the beginning of the linked list.

        Parameters:
        - None

        Returns:
        - elem (Any): The data from the node that was removed.

        Detailed Explanation:
        Removes the head node from the list and returns its data. The next node becomes the new head.

        Visual Illustration:

            Before removal:

            head
             |
            [Node1] -> [Node2] -> None

            After removal:

            head
             |
            [Node2] -> None

            Returned element: data of Node1
        """
        pass

    def append(self, elem):
        """
        Adds an element to the end of the linked list.

        Parameters:
        - elem (Any): The element to be added to the end of the list.

        Returns:
        - None

        Detailed Explanation:
        Inserts a new node containing 'elem' at the end of the list. The new node becomes the new tail.

        Visual Illustration:

            Before append:

            head
             |
            [Node1] -> [Node2] -> None

            After append of 'elem':

            head
             |
            [Node1] -> [Node2] -> [elem] -> None
        """
        pass
    
    def pop(self, idx = None):
        """
        Removes and returns the element at the specified index.

        Parameters:
        - idx (int, optional): The index of the element to remove. If None, removes and returns the last element. Defaults to None.

        Returns:
        - elem (Any): The data from the node that was removed.

        Detailed Explanation:
        Removes the node at the specified index and returns its data. If 'idx' is None, removes the last element.

        Visual Illustration:

            Removing element at index idx:

            Before removal:

            head
             |
            [Node0] -> [Node1] -> [Node2] -> None

            Suppose idx = 1

            After removal:

            head
             |
            [Node0] -> [Node2] -> None

            Returned element: data of Node1
        """
        pass

    def insert(self, idx, elem):
        """
        Inserts an element at the specified index in the linked list.

        Parameters:
        - idx (int): The index at which to insert the new element.
        - elem (Any): The element to insert.

        Returns:
        - None

        Detailed Explanation:
        Inserts a new node containing 'elem' at position 'idx'. Nodes are re-linked to include the new node.

        Visual Illustration:

            Inserting 'elem' at index idx:

            Before insertion:

            head
             |
            [Node0] -> [Node1] -> [Node2] -> None

            Suppose idx = 1

            After insertion:

            head
             |
            [Node0] -> [elem] -> [Node1] -> [Node2] -> None
        """
        pass
    
    def __getitem__(self, idx):
        """
        Returns the element at the specified index.

        Parameters:
        - idx (int): The index of the element to retrieve.

        Returns:
        - elem (Any): The data of the node at the specified index.

        Detailed Explanation:
        Allows access to elements using indexing syntax. For instance, you will be able to use syntax like 
            l = LinkedList(...)
            l[1]

        Visual Illustration:

            Accessing element at index idx:

            head
             |
            [Node0] -> [Node1] -> [Node2] -> None

            Suppose idx = 1

            Returned element: data of Node1
        """
        pass

    def __setitem__(self, idx, elem):
        """
        Sets the element at the specified index to a new value.

        Parameters:
        - idx (int): The index of the element to set.
        - elem (Any): The new value to set at the specified index.

        Returns:
        - None

        Detailed Explanation:
        Updates the data of the node at position 'idx' to 'elem'. For instance, you will be able to use syntax like 
            l = LinkedList(...)
            l[idx] = elem
        Above lines of code will set idx-th element of the LinkedList l to elem.

        Visual Illustration:

            Setting element at index idx to 'elem':

            Before:

            head
             |
            [Node0] -> [Node1] -> [Node2] -> None

            Suppose idx = 1

            After:

            head
             |
            [Node0] -> [elem] -> [Node2] -> None
        """
        pass

    def __iter__(self):
        """
        Returns an iterator over the elements of the linked list.

        Parameters:
        - None

        Returns:
        - iterator: An iterator over the elements in the list.

        Detailed Explanation:
        Allows iteration over the list using a for-loop.

        Visual Illustration:

            for elem in linked_list:
                # Process elem

            Traverses the list from head to tail.
        """
        pass

    def __len__(self):
        """
        Returns the number of elements in the linked list.

        Parameters:
        - None

        Returns:
        - size (int): The number of elements in the list.

        Example:

            size = len(linked_list)
        """
        return self.size 

    def last(self):
        """
        Returns the data of the last element in the linked list.

        Parameters:
        - None

        Returns:
        - elem (Any): The data of the last node.

        Detailed Explanation:
        Retrieves the data from the tail node.

        Visual Illustration:

            Accessing the last element:

            head                         tail
             |                             |
            [Node1] -> [Node2] -> [Node3] -> None

            Returned element: data of Node3
        """
        return self.end.datum

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Parameters:
        - None

        Returns:
        - str: A string representing the linked list elements.

        Example:

            print(linked_list)  # Output: [elem1, elem2, elem3]
        """
        return ''

class DoublyLinkedNode(Node):
    """
    Represents a node in a doubly linked list.

    Attributes:
    - node_id (Any): A unique identifier for the node.
    - datum (Any): The data stored in the node.
    - prev (DoublyLinkedNode or None): Reference to the previous node in the list.
    - next (DoublyLinkedNode or None): Reference to the next node in the list.

    Detailed Explanation:
    A DoublyLinkedNode is an element of a doubly linked list, where each node has pointers to both the previous and next nodes. This allows traversal in both directions.

    The attribute node_id is NOT A FUNCTIONING ATTRIBUTE; IT IS SOLEY FOR DEBUGGING - SO YOU CAN ASSIGN ANY VALUE. However, it is advised to assign unique values for node_id, since it would be useful for the debugging. 

    Practical Usages:
    Doubly linked nodes are useful in data structures where bidirectional traversal is needed, such as in implementing deques, or in certain algorithms like LRU caches.

    Visual Illustration:

        [Prev Node] <-> [Current Node] <-> [Next Node]
    """
    def __init__(self, node_id, datum, prev = None, next = None):
        """
        Initializes a new instance of DoublyLinkedNode.

        Parameters:
        - node_id (Any): A unique identifier for the node.
        - datum (Any): The data to store in the node.
        - prev (DoublyLinkedNode or None, optional): The previous node in the list. Defaults to None.
        - next (DoublyLinkedNode or None, optional): The next node in the list. Defaults to None.

        Returns:
        - None

        Visual Illustration:

            +---------+---------+---------+
            |  prev   |  datum  |  next   |
            +---------+---------+---------+
              ^                         ^
              |                         |
            None or Node          None or Node
        """
        self.node_id = node_id 
        self.datum = datum
        self.next = next 
        self.prev = prev 

class DoublyLinkedList:
    """
    Represents a doubly linked list data structure.

    Attributes:
    - head (DoublyLinkedNode or None): The first node in the doubly linked list.
    - tail (LinkedNode or None): The LinkedList instance excluding the first element in the original LinkedList.
    - end (LinkedNode or None): The last node in the linked list. 
    - size (int): The number of elements in the list.

    Detailed Explanation:
    A DoublyLinkedList is a sequence of nodes where each node points to both its previous and next nodes. This allows efficient insertion and deletion from both ends of the list and bidirectional traversal.

    Practical Usages:
    Doubly linked lists are useful when you need to traverse data in both directions, or when implementing data structures like deques or certain cache mechanisms.

    Visual Illustration:

        head                                   tail
         |                                       |
        [Node1] <-> [Node2] <-> [Node3] <-> [Node4]
    """
    def __init__(self, elements):
        """
        Initializes a new instance of DoublyLinkedList.

        Parameters:
        - elements (iterable): An iterable of elements to initialize the doubly linked list with.

        Returns:
        - None

        Detailed Explanation:
        Creates a new doubly linked list and populates it with the elements provided. If 'elements' is empty, it initializes an empty list.

        Visual Illustration:

            elements = [1, 2, 3]

            head                           
             |                               
            [1] <-> [2] <-> [3] <-> None 
        """
        if elements is None:
            elements = []
        elements = list(elements)

        if not elements:
            self.head = None
            self.tail = None
            self.size = 0
        else:
            pass

    def append_to_head(self, elem): 
        """
        Adds an element to the beginning of the doubly linked list.

        Parameters:
        - elem (Any): The element to be added to the head of the list.

        Returns:
        - None

        Detailed Explanation:
        Inserts a new node containing 'elem' at the beginning of the list. Updates pointers accordingly.

        Visual Illustration:

            Before insertion:

            head                           
             |                             
            [Node1] <-> [Node2] <-> [Node3] <-> ... 

            After insertion of 'elem':

            head                               
             |                                   
            [elem] <-> [Node1] <-> [Node2] <-> [Node3] <-> ...
        """
        pass

    def remove_from_head(self):
        """
        Removes and returns the element at the beginning of the doubly linked list.

        Parameters:
        - None

        Returns:
        - elem (Any): The data from the node that was removed.

        Detailed Explanation:
        Removes the head node and updates pointers. If the list becomes empty, tail is set to None.

        Visual Illustration:

            Before removal:

            head                           
             |                               
            [Node1] <-> [Node2] <-> [Node3] <-> ...

            After removal:

            head                       
             |                           
            [Node2] <-> [Node3] <-> ...

            Returned element: data of Node1
        """
        pass

    def append(self, elem):
        """
        Adds an element to the end of the doubly linked list.

        Parameters:
        - elem (Any): The element to be added to the end of the list.

        Returns:
        - None

        Detailed Explanation:
        Inserts a new node containing 'elem' at the end of the list. Updates pointers accordingly.

        Visual Illustration:

            Before append:

            head                           
             |                               
            [Node1] <-> [Node2] <-> [Node3] <-> None

            After append of 'elem':

            head                                   
             |                                       
            [Node1] <-> [Node2] <-> [Node3] <-> [elem] <-> None
        """
        pass
    
    def pop(self, idx = None):
        """
        Removes and returns the element at the specified index.

        Parameters:
        - idx (int, optional): The index of the element to remove. If None, removes and returns the last element. Defaults to None.

        Returns:
        - elem (Any): The data from the node that was removed.

        Detailed Explanation:
        Removes the node at the specified index and returns its data. If 'idx' is None, removes the last element.

        Visual Illustration:

            Removing element at index idx:

            Before removal:

            head
             |
            [Node0] <-> [Node1] <-> [Node2] <-> None

            Suppose idx = 1

            After removal:

            head
             |
            [Node0] <-> [Node2] <-> None

            Returned element: data of Node1
        """
        pass

    def insert(self, idx, elem):
        """
        Inserts an element at the specified index in the linked list.

        Parameters:
        - idx (int): The index at which to insert the new element.
        - elem (Any): The element to insert.

        Returns:
        - None

        Detailed Explanation:
        Inserts a new node containing 'elem' at position 'idx'. Nodes are re-linked to include the new node.

        Visual Illustration:

            Inserting 'elem' at index idx:

            Before insertion:

            head
             |
            [Node0] <-> [Node1] <-> [Node2] <-> None

            Suppose idx = 1

            After insertion:

            head
             |
            [Node0] <-> [elem] <-> [Node1] <-> [Node2] <-> None
        """
        pass
    
    def __getitem__(self, idx):
        """
        Returns the element at the specified index.

        Parameters:
        - idx (int): The index of the element to retrieve.

        Returns:
        - elem (Any): The data of the node at the specified index.

        Detailed Explanation:
        Allows access to elements using indexing syntax.

        Visual Illustration:

            Accessing element at index idx:

            head
             |
            [Node0] <-> [Node1] <-> [Node2] <-> None

            Suppose idx = 1

            Returned element: data of Node1
        """
        pass

    def __setitem__(self, idx, elem):
        """
        Sets the element at the specified index to a new value.

        Parameters:
        - idx (int): The index of the element to set.
        - elem (Any): The new value to set at the specified index.

        Returns:
        - None

        Detailed Explanation:
        Updates the data of the node at position 'idx' to 'elem'.

        Visual Illustration:

            Setting element at index idx to 'elem':

            Before:

            head
             |
            [Node0] <-> [Node1] <-> [Node2] <-> None

            Suppose idx = 1

            After:

            head
             |
            [Node0] <-> [elem] <-> [Node2] <-> None
        """
        pass

    def __iter__(self):
        """
        Returns an iterator over the elements of the doubly linked list.

        Parameters:
        - None

        Returns:
        - iterator: An iterator over the elements in the list.

        Detailed Explanation:
        Allows iteration over the list using a for-loop.

        Visual Illustration:

            for elem in linked_list:
                # Process elem

            Traverses the list from head to tail.
        """
        pass

    def __len__(self):
        """
        Returns the number of elements in the doubly linked list.

        Parameters:
        - None

        Returns:
        - size (int): The number of elements in the list.

        Example:

            size = len(doubly_linked_list)
        """
        return self.size 

    def last(self):
        """
        Returns the data of the last element in the doubly linked list.

        Parameters:
        - None

        Returns:
        - elem (Any): The data of the last node.

        Detailed Explanation:
        Retrieves the data from the tail node.

        Visual Illustration:

            Accessing the last element:

            head                           tail
             |                               |
            [Node1] <-> [Node2] <-> [Node3]

            Returned element: data of Node3
        """
        return self.end.datum

if __name__ == '__main__':
    from random import randint 

    lst = LinkedList([1,2,3])
    print(lst) 
    
    assert len(lst) == 3 

    for elem in lst:
        print(elem)

    assert lst[0] == 1
    assert lst[1] == 2
    assert lst[2] == 3

    lst.append_to_head(4)
    print(lst)
    assert len(lst) == lst.size == 4
    lst.append(5)
    print(lst)
    assert len(lst) == lst.size == 5

    lst.insert(3, -1)
    # 4 1 2 -1 3 5 
    print(lst)
    assert len(lst) == 6

    assert 4 == lst.remove_from_head()
    # 1 2 -1 3 5 
    print(lst)
    assert len(lst) == 5

    assert -1 == lst.pop(2)
    # 1 2 3 5 
    print(lst) 
    assert len(lst) == 4

    assert 2 == lst.pop(1) 
    # 1 3 5 
    assert 5 == lst.pop(2) 
    print(lst)
    # print(lst.pop(0))
    assert 1 == lst.pop(0)
    assert 3 == lst.pop(0)
    print(lst)

    for i in range(10):
        lst.insert(i, i+1)
        assert len(lst) == i+1 

    print(lst)

    for i in range(10):
        lst[i] = i+2 
    print(lst)

    # print(lst.pop(10))
    print(lst.pop())
    print(lst)
    print(lst.last())
