try:
    from node import Node 
except ModuleNotFoundError:
    from data_structure.node import Node

class LinkedNode:
    def __init__(self, node_id, datum, next = None):
        self.node_id = node_id 
        self.datum = datum
        self.next = next 

class LinkedList:
    def __init__(self, elements):
    
        if elements == []:
            self.head = None 
            self.tail = None 
            self.end = None
            self.size = 0
        else:
            elements = list(elements)

            for idx, elem in enumerate(elements):
                if not isinstance(elem, LinkedNode):
                   elements[idx] = LinkedNode(idx, elem)
                    
            self.head = elements[0]
            self.end = elements[-1]

            for idx, elem in enumerate(elements):
                if idx == len(elements)-1:
                    elem.next = None
                    break
                elem.next = elements[idx+1]
                
            self.tail = LinkedList(elements[1:])
            self.size = len(elements)

    def add_to_front(self, elem):
        new_node = LinkedNode(0, elem)
        new_node.next = self.head
        self.head = new_node
        
        if self.end is None:
            self.end = new_node
        self.size += 1

    def __iter__(self):
        yield None 

    def __str__(self):
        res = ''
        
        return res 

    def __len__(self):
        return self.size



class DoublyLinkedNode(Node):
    def __init__(self, node_id, datum, prev = None, next = None):
        self.node_id = node_id 
        self.datum = datum
        self.next = next 
        self.prev = prev 

class DoublyLinkedList:
    def __init__(self, elements):
        if elements == []:
            self.head = None 
            self.tail = None 
            self.end = None
            self.size = 0
        else:
            self.head = None 
            self.tail = None 
            self.end = None
            self.size = 0

    def __iter__(self):
        yield None 

    def __str__(self):
        res = ''

        return res 

