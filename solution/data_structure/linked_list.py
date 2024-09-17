try:
    from node import Node 
except ModuleNotFoundError:
    from data_structure.node import Node

class LinkedNode:
    def __init__(self, node_id, datum, next = None):
        self.node_id = node_id 
        self.datum = datum
        self.next = next 

    def set_next(self, next_node):
        assert isinstance(next_node, LinkedNode) or next_node is None

        self.next = next_node     

class LinkedList:
    def __init__(self, elements):
        if not elements:
            self.head = None 
            self.tail = None 
            self.end = None
            self.size = 0
        

    def append_to_head(self, elem): 
        if not isinstance(elem, LinkedNode):
            elem = LinkedNode(self.size, elem)
        
        elem.set_next(self.head)
        self.head = elem 

        if self.size == 0:
            self.end = elem
            self.tail = None 
        
        self.size += 1 

    def remove_from_head(self):
        res = self.head 
        self.head = res.next 
        self.size -= 1 
        return res.datum 

    def append(self, elem):
        if not isinstance(elem, LinkedNode):
            elem = LinkedNode(self.size, elem)
        
        if self.end is None:
            self.head = elem 

        self.end.set_next(elem)
        self.end = elem 
        self.size += 1 
    
    def pop(self, idx = None):
        if idx is None:
            idx = self.size - 1
        if self.size  <= idx: 
            raise IndexError('out of index')
        cur = self.head 
        cur_idx = 0 

        while cur_idx < idx-1:
            cur = cur.next 
            cur_idx += 1 

        # cur가 idx-1번째 노드 
        #  idx-1       idx             idx+1 
        # [cur] -> [cur.next] -> [cur.next.next]
        # if idx == 0: cur = self.head 
        if idx == 0:
            return self.remove_from_head()            
        else:
            res = cur.next
            cur.set_next(cur.next.next)
            if idx == self.size - 1:
                self.end = cur 
            self.size -= 1 
        return res.datum 

    def insert(self, idx, elem):
        if not isinstance(elem, LinkedNode):
            elem = LinkedNode(self.size, elem)
        
        if self.size + 1 <= idx: 
            raise IndexError('out of index')
        
        cur = self.head 
        cur_idx = 0 

        while cur_idx < idx-1:
            cur = cur.next 
            cur_idx += 1 

        # cur가 idx-1번째 노드 
        #  idx-1       idx             idx+1 
        # [cur] -> [cur.next] -> [cur.next.next]

        #  idx-1     idx        idx+1 
        # [cur] -> [elem] -> [cur.next]
        
        if self.size == 0:
            self.head = elem 
            self.end = elem 
            elem.set_next(None)
        else:
            elem.set_next(cur.next)
            cur.set_next(elem) 
            if self.size == idx:
                self.end = elem
        self.size += 1

    def __getitem__(self, idx):
        # lst[1]
        # LinkedList.__getitem__(1)
        if self.size <= idx: 
            raise IndexError('out of index')
        
        cur = self.head 
        cur_idx = 0 

        while cur_idx < idx:
            cur = cur.next 
            cur_idx += 1 
     
        return cur.datum

    def __setitem__(self, idx, elem):
        # lst[1] = 3
        # LinkedList.__setitem__(1, 3)
        if self.size <= idx: 
            raise IndexError('out of index')
        
        cur = self.head 
        cur_idx = 0 

        while cur_idx < idx:
            cur = cur.next 
            cur_idx += 1 
     
        if isinstance(elem, LinkedNode):
            cur.datum = elem.datum 
        else:
            cur.datum = elem

    def __iter__(self):
        cur = self.head 
        while cur is not None:
            yield cur.datum 
            cur = cur.next 
        
    def __str__(self):
        # [head] -> [..] -> [..] ... -> [end] -> None 
        res = '[head]->'

        for node in self:
            try:
                res += f'[{node}] ->'
            except AttributeError:
                print(node)
                assert False 
        
        res += 'None'
        return res 

    def __len__(self):
        return self.size 

    def last(self):
        return self.end.datum

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

    def add_to_head(self, elem):
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
        current = self.head
        while current is not None:
            yield current.datum
            current = current.next

    def __str__(self):
        res = []
        current = self.head
        while current is not None:
            res.append(str(current.datum))
            current = current.next
        return ' -> '.join(res) 

if __name__ == '__main__':
    # lst.__init__, lst.__str__, lst.__len__
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


    


    
    