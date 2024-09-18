class TreeNode:
    """
    Represents a node in a tree structure.

    Attributes:
    - node_id (Any): A unique identifier for the node.
    - datum (Any): The data stored in the node.

    Detailed Explanation:
    A `TreeNode` is the fundamental building block of a tree data structure. Each node contains data (`datum`) and a unique identifier (`node_id`). Nodes are connected in a hierarchical manner to form the tree.

    Practical Usages:
    - File Systems: Nodes represent files or directories.
    - Organizational Charts: Nodes represent positions or employees.
    - Decision Trees: Nodes represent decisions or outcomes in algorithms.

    Visual Illustration:

        [node_id: datum]
    """
    def __init__(self, node_id, datum):
        """
        Initializes a new instance of TreeNode.

        Parameters:
        - node_id (Any): A unique identifier for the node.
        - datum (Any): The data to store in the node.

        Returns:
        - None

        Example:
            node = TreeNode('A1', 'Manager')

        Visual Illustration:

            +---------+---------+
            | node_id |  datum  |
            +---------+---------+
            |  'A1'   | 'Manager'|
            +---------+---------+
        """
        self.node_id = node_id
        self.datum = datum 

class Tree:
    """
    Represents a general tree data structure where each node can have an arbitrary number of children.

    Attributes:
    - root (TreeNode): The root node of the tree.
    - children (list of Tree): A list of child trees (subtrees) of the root node.

    Detailed Explanation:
    The `Tree` class models hierarchical data using `TreeNode` instances connected in a parent-child relationship. Each `Tree` instance has a `root` node and a list of `children`, which are themselves `Tree` instances. This recursive structure allows for the representation of complex hierarchies.

    Practical Usages:
    - File Systems: Represent directories and files.
    - Organization Hierarchies: Model company structures.
    - XML/HTML Document Trees: Represent nested elements.

    Visual Illustration:

        [Root]
        ├── [Child1]
        │   ├── [Grandchild1]
        │   │   └── [GreatGrandchild1]
        │   │       └── [GreatGreatGrandchild1]
        │   └── [Grandchild2]
        └── [Child2]
            ├── [Grandchild3]
            └── [Grandchild4]
    """

    def __init__(self, root, children = []):
        """
        Initializes a new instance of Tree.

        Parameters:
        - root (Any or TreeNode): The root node's data or a `TreeNode` instance.
        - children (list of Tree or Any, optional): A list of child trees or data to initialize the tree with. Defaults to an empty list.

        Returns:
        - None

        Detailed Explanation:
        Converts `root` into a `TreeNode` if it isn't one already. Each element in `children` is converted into a `Tree` instance if necessary. This flexibility allows for easy construction of trees from raw data or existing `Tree` instances.

        Visual Illustration:

            Constructing a tree with height > 3:

            [CEO]
            ├── [VP of Engineering]
            │   └── [Engineering Manager]
            │       ├── [Senior Engineer]
            │       │   └── [Engineer Intern]
            │       └── [QA Lead]
            │           └── [QA Tester]
            └── [VP of Sales]
                └── [Sales Manager]
                    ├── [Senior Sales Rep]
                    └── [Sales Intern]
        """
        if not isinstance(root, TreeNode):
            root = TreeNode('0', root)
        self.root = root 
        
        children = list(children)
        for idx, child in enumerate(children):
            if not isinstance(child, Tree):
                children[idx] = Tree(root = TreeNode(str(idx), child))
            
        self.children = children 

    def iter_nodes(self):
        """
        Yields all `TreeNode` instances in the tree using a depth-first traversal.

        Parameters:
        - None

        Returns:
        - generator: An iterator over all `TreeNode` instances in the tree.

        Detailed Explanation:
        Performs a depth-first traversal starting from the root node, recursively yielding nodes from each subtree.

        Visual Illustration:

            Traversal Order in a tree with height > 3:

            1. CEO
            2. VP of Engineering
            3. Engineering Manager
            4. Senior Engineer
            5. Engineer Intern
            6. QA Lead
            7. QA Tester
            8. VP of Sales
            9. Sales Manager
            10. Senior Sales Rep
            11. Sales Intern
        """
        yield self.root 

        for child in self.children:
            for n in child.iter_nodes():
                yield n 

    def iter_nodes_with_address(self):
        """
        Yields all `TreeNode` instances along with their addresses in the tree using a depth-first traversal.

        Parameters:
        - None

        Returns:
        - generator: An iterator over tuples of (address, `TreeNode`), where `address` is a list representing the path to the node.

        Detailed Explanation:
        Each address is a list of indices that represent the path from the root to the node. The root node's address is an empty list `[]`.

        Visual Illustration:

            Tree Structure with Addresses:

            CEO (Address: [])
            ├── VP of Engineering (Address: [0])
            │   └── Engineering Manager (Address: [0, 0])
            │       ├── Senior Engineer (Address: [0, 0, 0])
            │       │   └── Engineer Intern (Address: [0, 0, 0, 0])
            │       └── QA Lead (Address: [0, 0, 1])
            │           └── QA Tester (Address: [0, 0, 1, 0])
            └── VP of Sales (Address: [1])
                └── Sales Manager (Address: [1, 0])
                    ├── Senior Sales Rep (Address: [1, 0, 0])
                    └── Sales Intern (Address: [1, 0, 1])
        """
        yield [], self.root 

        for idx, child in enumerate(self.children):
            for addr, n in child.iter_nodes_with_address():
                yield [idx] + addr, n 

    def __iter__(self):
        """
        Yields the data of all nodes in the tree using a depth-first traversal.

        Parameters:
        - None

        Returns:
        - generator: An iterator over the data (`datum`) of each `TreeNode` in the tree.

        Detailed Explanation:
        Allows iteration over the tree's data directly.

        Visual Illustration:

            Iteration over data in a tree with height > 3:

            CEO, VP of Engineering, Engineering Manager, Senior Engineer, Engineer Intern, QA Lead, QA Tester, VP of Sales, Sales Manager, Senior Sales Rep, Sales Intern
        """
        yield self.root.datum

        for child in self.children:
            for n in child.iter_nodes():
                yield n 

    def insert(self, address, elem):
        """
        Inserts a new subtree or element at the specified address in the tree.

        Parameters:
        - address (list of int): A list representing the path to the parent node where the new element will be inserted. The last integer specifies the index at which to insert the new element in the parent's children list.
        - elem (Any or Tree): The data or subtree to insert.

        Returns:
        - None

        Detailed Explanation:
        Navigates to the node specified by `address` and inserts `elem` into its `children` list at the position specified by the last index in the address. If `elem` is not a `Tree` instance, it is converted into one.

        Visual Illustration:

            Inserting a new department under 'Engineering Manager':

            Before Insertion:

            Engineering Manager (Address: [0, 0])
            ├── Senior Engineer (Address: [0, 0, 0])
            │   └── Engineer Intern (Address: [0, 0, 0, 0])
            └── QA Lead (Address: [0, 0, 1])
                └── QA Tester (Address: [0, 0, 1, 0])

            Insert Address: [0, 0, 1]
            Element to Insert: 'DevOps Team'

            After Insertion:

            Engineering Manager
            ├── Senior Engineer
            │   └── Engineer Intern
            ├── DevOps Team   # New node inserted at index 1
            └── QA Lead
                └── QA Tester
        """
        if not isinstance(elem, Tree):
            elem = Tree(elem) 

        cur = self 
        for addr in address[:-1]:
            cur = cur.children[addr]
        cur.children.insert(address[-1], elem)

    def delete(self, address):
        """
        Deletes a subtree or node at the specified address in the tree.

        Parameters:
        - address (list of int): A list representing the path to the node to be deleted.

        Returns:
        - Any: The data (`datum`) of the root node of the deleted subtree.

        Detailed Explanation:
        Navigates to the parent node of the node to be deleted and removes the child at the specified index. If the address is empty, it means we are attempting to delete the root node, which is not allowed in this implementation.

        Visual Illustration:

            Deleting 'QA Lead' and its subtree:

            Before Deletion:

            Engineering Manager (Address: [0, 0])
            ├── Senior Engineer (Address: [0, 0, 0])
            │   └── Engineer Intern (Address: [0, 0, 0, 0])
            ├── DevOps Team (Address: [0, 0, 1])
            └── QA Lead (Address: [0, 0, 2])
                └── QA Tester (Address: [0, 0, 1, 0])

            Delete Address: [0, 0, 2]

            After Deletion:

            Engineering Manager
            ├── Senior Engineer
            │   └── Engineer Intern
            └── DevOps Team

            Deleted Data: 'QA Lead'
        """
        cur = self 
        
        for addr in address[:-1]:
            cur = cur.children[addr] 

        res = cur.children[address[-1]].root.datum 
        del cur.children[address[-1]]

        return res 
        
    def search(self, elem):
        """
        Searches for a node with the specified data and returns its address.

        Parameters:
        - elem (Any): The data to search for in the tree.

        Returns:
        - list of int or None: The address (path) to the node containing `elem`, or `None` if not found.

        Detailed Explanation:
        Traverses the tree using `iter_nodes_with_address` and compares each node's `datum` to `elem`.

        Visual Illustration:

            Searching for 'Engineer Intern' in a tree with height > 3:

            Nodes and Addresses:

            - CEO (Address: [])
            - VP of Engineering (Address: [0])
            - Engineering Manager (Address: [0, 0])
            - Senior Engineer (Address: [0, 0, 0])
            - Engineer Intern (Address: [0, 0, 0, 0])

            Search Result:

            Element: 'Engineer Intern' found at Address: [0, 0, 0, 0]
        """
        for addr, node in self.iter_nodes_with_address():
            if node.datum == elem:
                return addr 

    def root_datum(self):
        """
        Returns the data of the root node of the tree.

        Parameters:
        - None

        Returns:
        - Any: The data stored in the root node.

        Example:
            tree = Tree('CEO')
            print(tree.root_datum())  # Output: 'CEO'
        """
        return self.root.datum 

    def height(self):
        """
        Calculates and returns the height of the tree.

        Parameters:
        - None

        Returns:
        - int: The height of the tree.

        Detailed Explanation:
        The height is the length of the longest path from the root to a leaf node. This method computes the maximum depth encountered during traversal.

        Visual Illustration:

            Calculating the height of a tree with height > 3:

            Levels:

            Level 1: CEO
            Level 2: VP of Engineering, VP of Sales
            Level 3: Engineering Manager, Sales Manager
            Level 4: Senior Engineer, QA Lead, Senior Sales Rep, Sales Intern
            Level 5: Engineer Intern, QA Tester

            The height is 5 (since the deepest nodes are at level 5).
        """
        h = 0 

        for addr, node in self.iter_nodes_with_address():
            if len(addr) + 1 > h:
                h = len(addr) + 1

        return h 

    def __str__(self):
        """
        Returns a string representation of the tree in a hierarchical format.

        Parameters:
        - None

        Returns:
        - str: A string representing the tree structure.

        Detailed Explanation:
        Creates a visual representation of the tree, displaying the hierarchy using lines and indentation.

        Visual Illustration:

            Tree Structure (height > 3):

            CEO
            ├── VP of Engineering
            │   └── Engineering Manager
            │       ├── Senior Engineer
            │       │   └── Engineer Intern
            │       ├── DevOps Team
            │       └── QA Lead
            │           └── QA Tester
            └── VP of Sales
                └── Sales Manager
                    ├── Senior Sales Rep
                    └── Sales Intern
        """
        res = str(self.root.datum) 

        for idx, child in enumerate(self.children):
            res += '\n'
            if idx < len(self.children) - 1:
                res += '├── '
                res += str(child).replace('\n', '\n│   ')
            else:
                res += '└── '
                res += str(child).replace('\n', '\n    ')
        
        return res 


if __name__ == '__main__':
    t1 = Tree(1, [
                Tree(11, [Tree(111), Tree(112)],), 
                Tree(12, [Tree(121), Tree(122), Tree(123),])
             ]
         )
    print(t1)
    
    assert t1.root_datum() == 1 
    assert t1.height() == 3

    for addr, n in t1.iter_nodes_with_address():
        assert [int(e)-1 for e in list(str(n.datum))[1:]] == addr 
        assert t1.search(n.datum) == addr 

    t1.insert([2], Tree(13, [Tree(131), Tree(132), Tree(133)]))
    t1.insert([1, 1], Tree(122, [Tree(1221), Tree(1222)]))

    print(t1)
    
    assert 122 == t1.delete([1,2])
    assert 123 == t1.delete([1,2])

    for addr, n in t1.iter_nodes_with_address():
        assert [int(e)-1 for e in list(str(n.datum))[1:]] == addr 
        assert t1.search(n.datum) == addr 

    print(t1)

    # Constructing a company hierarchy tree
    company_tree = Tree('CEO', [
        Tree('VP of Engineering', [
            Tree('Engineering Manager', [
                Tree('Senior Engineer', [
                    Tree('Engineer Intern')
                ]),
                Tree('QA Lead', [
                    Tree('QA Tester')
                ])
            ])
        ]),
        Tree('VP of Sales', [
            Tree('Sales Manager', [
                Tree('Senior Sales Rep'),
                Tree('Sales Intern')
            ])
        ])
    ])

    print(company_tree)
    # Output:
    # CEO
    # ├── VP of Engineering
    # │   └── Engineering Manager
    # │       ├── Senior Engineer
    # │       │   └── Engineer Intern
    # │       └── QA Lead
    # │           └── QA Tester
    # └── VP of Sales
    #     └── Sales Manager
    #         ├── Senior Sales Rep
    #         └── Sales Intern

    # The height of the tree
    print(f"Height of the tree: {company_tree.height()}")  # Output: Height of the tree: 5

    # Searching for an employee
    address = company_tree.search('Engineer Intern')
    if address is not None:
        print(f"'Engineer Intern' found at address: {address}")
    else:
        print("'Engineer Intern' not found.")

    # Output: 'Engineer Intern' found at address: [0, 0, 0, 0]

    # Inserting a new department under 'Engineering Manager'
    company_tree.insert([0, 0, 2], Tree('DevOps Team', [
        Tree('DevOps Engineer'),
        Tree('Cloud Specialist')
    ]))

    print("\nAfter inserting 'DevOps Team' under 'Engineering Manager':")
    print(company_tree)

    # Deleting 'QA Lead' and its subtree
    deleted_data = company_tree.delete([0, 0, 1])
    print(f"\nDeleted subtree root data: {deleted_data}")

    print("\nAfter deleting 'QA Lead':")
    print(company_tree)

    # Validate addresses after modifications
    print("\nAddresses after modifications:")
    for addr, n in company_tree.iter_nodes_with_address():
        print(f"Address: {addr}, Data: {n.datum}")

    # The tree now has updated height
    print(f"\nUpdated height of the tree: {company_tree.height()}")
