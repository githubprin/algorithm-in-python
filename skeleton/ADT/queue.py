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

    def elements(self):
        if self.backend == list:
            return self.list 

        elif self.backend == LinkedList:
            res = []
            cur = self.linked_list.head

            while cur is not None:
                res.append(cur.datum)
                cur = cur.next

            return res

    def enqueue(self, elem):
        if self.backend == list:
            self.list = [elem] + self.list

        elif self.backend == LinkedList:
            self.linked_list.add_to_front(elem)

    def dequeue(self):
        if self.backend == list:
            return self.list.pop()
                
        elif self.backend == LinkedList:
            return self.linked_list.delete_from_back()

    def front(self):
        if self.backend == list:
            return self.list[-1]

        elif self.backend == LinkedList:
            return self.linked_list.end.datum

    def size(self):
        if self.backend == list:
            return len(self.list)
    
        elif self.backend == LinkedList:
            return len(self.linked_list)
     

    def is_empty(self):
        if self.backend == list:
            return self.list == []

        elif self.backend == LinkedList:
            return self.linked_list.size == 0

    def __str__(self):
        return str(self.elements())

    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.elements == other.elements 
        return False 


class PriorityQueue:
    def __init__(self, *elements_with_priority, backend = list):
        """Get list of 2-tuple containing (obj, number), which denotes object and its priority. Higher the number, the element have hight priority. 
        """
        assert isinstance(elements_with_priority, list) or isinstance(elements_with_priority, tuple)

        self.backend = backend
        if self.backend == list:
            self.list = []

            for element in sorted(elements_with_priority, key=lambda x: x[1]):
                self.list.insert(0, element)

        elif self.backend == LinkedList:
            self.linked_list = LinkedList([])

            for element in sorted(elements_with_priority, key=lambda x: x[1], reverse = True):
                self.linked_list.add_to_front(element)

        elif self.backend == DoublyLinkedList:
            self.doubly_linked_list = DoublyLinkedList([])

            for element in sorted(elements_with_priority, key=lambda x: x[1]):
                self.doubly_linked_list.add_to_front(element)

    
    def elements(self):
        if self.backend == list:
            return sorted(self.list, key=lambda x: x[1])

        elif self.backend == LinkedList:
            res = []
            cur = self.linked_list.head

            while cur is not None:
                res.append(cur.datum)
                cur = cur.next
            
            return sorted(res, key=lambda x: x[1])

        elif self.backend == DoublyLinkedList:
            res = []
            cur = self.doubly_linked_list.head

            while cur is not None:
                res.append(cur.datum)
                cur = cur.next

            return sorted(res, key=lambda x: x[1])

    def enqueue(self, elem):
        if self.backend == list:
            self.list = [elem] + self.list
        elif self.backend == LinkedList:
            self.linked_list.add_to_front(elem)
        elif self.backend == DoublyLinkedList:
            self.doubly_linked_list.add_to_front(elem)

    def dequeue(self):
        if self.backend == list:
            return self.list.pop(0)

        elif self.backend == LinkedList:
            highest_priority = self.linked_list.end.datum
            self.linked_list.delete_from_back()
            return highest_priority

        elif self.backend == DoublyLinkedList:
            highest_priority = self.doubly_linked_list.end.datum
            self.doubly_linked_list.delete_from_back()
            return highest_priority
                
    def front(self):
        if self.backend == list:
            return max(self.list, key=lambda x: x[1])
        elif self.backend == LinkedList:
            return self.linked_list.end.datum
        elif self.backend == DoublyLinkedList:
            return self.doubly_linked_list.end.datum

    def size(self):
        if self.backend == list:
            return len(self.list)
        elif self.backend == LinkedList:
            return self.linked_list.size 

        elif self.backend == DoublyLinkedList:
            # return sum(1 for item in self.doubly_linked_list if isinstance(item, tuple))
            return self.doubly_linked_list.size 

    def is_empty(self):
        if self.backend == list:
            return self.list == []
        
        elif self.backend == LinkedList:
            return self.linked_list.size == 0 

        elif self.backend == DoublyLinkedList:
            return self.doubly_linked_list.size == 0

    def __str__(self):
        return str(self.elements())

    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.elements == other.elements 
        return False 

if __name__ == '__main__':
    available_backends = [list, LinkedList, DoublyLinkedList]

    for backend in available_backends:
        q1 = Queue(1,2,3,4, backend = backend)
        
        assert q1.elements() == [1,2,3,4]
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
        
        if backend == LinkedList:
            print(q1.linked_list, q2.linked_list)

        q2 = PriorityQueue(('c',1), ('d',4), ('e',2), ('b',3), backend = backend)

        assert q2.elements() == [('c',1), ('e',2), ('b',3), ('d',4)], backend
        assert q2.size() == 4
        assert q2.front() == ('d', 4), backend
        assert not q2.is_empty()
        q2.dequeue()
        
        assert q2.elements() == [('c',1), ('e',2), ('b',3)], backend
        assert q2.size() == 3 
        assert q2.front() == ('b', 3) 
        assert not q2.is_empty()

        q2.enqueue(('x', 0))
        q2.enqueue(('y', 4))
        q2.enqueue(('z', 2))

        assert q2.elements() == [('x', 0), ('c',1), ('z', 2), ('e',2), ('b',3), ('y', 4)]

        assert q2.size() == 6
        q2.dequeue()
        q2.dequeue()
        q2.dequeue()
        q2.dequeue()
        q2.dequeue()
        q2.dequeue()

        assert q2.is_empty()


