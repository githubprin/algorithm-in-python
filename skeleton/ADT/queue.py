import sys 
sys.path.append('../data_structure')

try:
    from linked_list import LinkedList, LinkedNode, DoublyLinkedNode, DoublyLinkedList
except ModuleNotFoundError:
    from data_structure.linked_list import LinkedList, LinkedNode, DoublyLinkedNode, DoublyLinkedList

class Queue:
    def __init__(self, *elements, backend = list):
        assert isinstance(elements, list) or isinstance(elements, tuple)

        self.backend = backend

        if self.backend == list:
            self.list = list(elements)

        elif self.backend == LinkedList:
            self.linked_list = LinkedList(elements)

        elif self.backend == DoublyLinkedList:
            self.linked_list = DoublyLinkedList(elements)

    def elements(self):
        if self.backend == list:
            return self.list 

        elif self.backend == LinkedList:
            pass 
        
        elif self.backend == DoublyLinkedList:
            pass 

    def enqueue(self, elem):
        if self.backend == list:
            self.list = [elem] + self.list

        elif self.backend == LinkedList:
            pass 
        
        elif self.backend == DoublyLinkedList:
            pass

    def dequeue(self):
        if self.backend == list:
            return self.list.pop()
                
        elif self.backend == LinkedList:
            pass 

        elif self.backend == DoublyLinkedList:
            pass
    
    def front(self):
        if self.backend == list:
            return self.list[-1]

        elif self.backend == LinkedList:
            pass
        
        elif self.backend == DoublyLinkedList:
            pass

    def size(self):
        if self.backend == list:
            return len(self.list)
    
        elif self.backend == LinkedList:
            pass
        
        elif self.backend == LinkedList:
            pass

    def is_empty(self):
        return self.size() == 0
        
    def __str__(self):
        return str(self.elements())

    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.elements() == other.elements() 
        return True 


class PriorityQueue:
    def __init__(self, *elements_with_priority, backend = list):
        """Get list of 2-tuple containing (obj, number), which denotes object and its priority. Higher the number, the element have hight priority. 
        """
        assert isinstance(elements_with_priority, list) or isinstance(elements_with_priority, tuple)

        self.backend = backend

        if self.backend == list:
            self.list = sorted(elements_with_priority, key=lambda x: x[1])
        
        elif self.backend == LinkedList:
            pass
        
        elif self.backend == DoublyLinkedList:
            pass

    def elements(self):
        if self.backend == list:
            return self.list
        
        elif self.backend == LinkedList:
            pass
        
        elif self.backend == DoublyLinkedList:
            pass
        
    def enqueue(self, elem):
        if self.backend == list:
            pass
            
        elif self.backend == LinkedList:
            pass 

        elif self.backend == DoublyLinkedList:
            pass

    def dequeue(self):
        if self.backend == list:
            return self.list.pop(-1)

        elif self.backend == LinkedList:
            pass

        elif self.backend == DoublyLinkedList:
            pass
                
    def front(self):
        if self.backend == list:
            return max(self.list, key=lambda x: x[1])
        elif self.backend == LinkedList:
            pass 
        elif self.backend == DoublyLinkedList:
            pass

    def size(self):
        if self.backend == list:
            return len(self.list)
        elif self.backend == LinkedList:
            pass

        elif self.backend == DoublyLinkedList:
            pass

    def is_empty(self):
        if self.backend == list:
            return self.list == []
        
        elif self.backend == LinkedList:
            pass

        elif self.backend == DoublyLinkedList:
            pass

    def __str__(self):
        return str(self.elements())

    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.elements == other.elements 
        return True 

if __name__ == '__main__':
    available_backends = [LinkedList, LinkedList, DoublyLinkedList]

    for backend in available_backends:
        q1 = Queue(1,2,3,4, backend = backend)
        if backend == DoublyLinkedList:
            print(q1)
        assert q1.elements() == [1,2,3,4], backend
        assert q1.size() == 4
        
        q1.enqueue(5)
        assert q1.elements() == [5,1,2,3,4]
        assert q1.size() == 5
        assert q1.dequeue() == 4
        assert q1.size() == 4
        assert q1.elements() == [5,1,2,3]
        assert q1.front() == 3 


        q2 = Queue(backend = backend)

        assert q2.elements() == []
        assert q2.size() == 0
        assert q2.is_empty()
        
        q2.enqueue(1)

        assert q2.elements() == [1]
        assert q2.size() == 1
        assert not q2.is_empty()
    
        q2 = PriorityQueue(('c',1), ('d',4), ('e',2), ('b',3), backend = backend)
        assert q2.elements() == [('c',1), ('e',2), ('b',3), ('d',4)], backend  
    
        assert q2.size() == 4
        assert q2.front() == ('d', 4), backend
        assert not q2.is_empty()
        
        q2.dequeue()
        
        assert q2.elements() == [('c',1), ('e',2), ('b',3)], backend
        
        assert q2.size() == 3, backend
        assert q2.front() == ('b', 3) 
        assert not q2.is_empty()

        q2.enqueue(('x', 0))
        q2.enqueue(('y', 4))
        q2.enqueue(('z', 2))

    
        assert q2.elements() == [('x', 0), ('c',1), ('z', 2), ('e',2), ('b',3), ('y', 4)], backend
        
        assert q2.size() == 6, backend
        q2.dequeue()
        q2.dequeue()
        q2.dequeue()
        q2.dequeue()
        q2.dequeue()
        q2.dequeue()
        
        assert q2.is_empty()

