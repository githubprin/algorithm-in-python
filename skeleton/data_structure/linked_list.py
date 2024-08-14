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
    
        if not elements:
            self.head = None 
            self.tail = None 
            self.end = None
            self.size = 0
        else:
            '''
            elements = list(elements)
            
            for idx, e in enumerate(elements):    
                n = LinkedNode(node_id = idx, datum = e)
                elements[idx] = n

            for idx, e in enumerate(elements)
                if idx != len(elements)-1:    
                    e.next = elements[idx+1]
            elements[-1].next = None

            self.head = elements[0]
            self.end = elements[-1]
            '''
            elements = list(elements)

            for idx, elem in enumerate(elements):
                if not isinstance(elem, LinkedNode):
                   elements[idx] = LinkedNode(idx, elem)
                    
            self.head = elements[0]
            self.end = elements[-1]

            for idx, elem in enumerate(elements):
                if idx == len(elements)-1:
                    elem.next = None
                else:  
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

    def delete_from_back(self):
        # 큐가 비어있을 때
        if self.size == 0:
            return None

        # 큐에 하나의 요소만 있을 때
        if self.size == 1:
            deleted_node = self.end
            self.head = None
            self.end = None
            self.size -= 1
            
            return deleted_node.datum

        # 큐에 두 개 이상의 요소가 있을 때
        cur = self.head
        while cur.next != self.end:
            cur = cur.next
        
        deleted_node = self.end
        self.end = cur
        self.end.next = None
        self.size -= 1

        return deleted_node.datum

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
        if elements is None:
            elements = []
        elements = list(elements)

        if not elements:
            self.head = None
            self.tail = None
            self.size = 0
       
        else:
            for idx, elem in enumerate(elements):
                if not isinstance(elem, DoublyLinkedNode):
                   elements[idx] = DoublyLinkedNode(idx, elem)
                    
            self.head = elements[0]
            self.end = elements[-1]

            for idx, elem in enumerate(elements):
                if idx == len(elements)-1:
                    elem.next = None
                else:  
                    elem.next = elements[idx+1]

            for idx, elem in enumerate(elements):
                if idx == 0:
                    elem.prev = None
                else:  
                    elem.prev = elements[idx-1]
                
            self.tail = DoublyLinkedList(elements[1:])
            self.size = len(elements)  

    def add_to_front(self, elem):
        new_node = DoublyLinkedNode(0, elem)
        
        if self.head is None:
            self.head = new_node
            self.end = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
        self.size += 1

    def delete_from_back(self):
        if self.size == 0:
            return None

        deleted_node = self.end

        if self.size == 1:
            self.head = None
            self.end = None
        else:
            self.end = self.end.prev
            self.end.next = None

        self.size -= 1
        return deleted_node.datum
        
    def __iter__(self):
        yield None 

    def __str__(self):
        res = ''

        return res 
