with open('../data/day20.txt') as f:
    lines = f.read().strip().split('\n')

# enc = [1,2,-3,3,-2,0,4] # example case for dev
enc = list(map(eval, lines))

# Node to store each value
class Node:
    """A class representing a node in a linked list.

    Attributes:
    - val: the value stored in the node.
    - nxt: a reference to the next node in the linked list (default None).
    - prv: a reference to the previous node in the linked list (default None).
    """
    def __init__(self, val, nxt=None, prv=None) -> None:
        self.val = val
        self.nxt = nxt
        self.prv = prv

class DoublyLinkedList:
    """Circular doubly linked list to represent the input of the "Encrypted file"
    """
    def __init__(self) -> None:
        self.nodes = []     # list to hold nodes (list stores them in their original order)
        self.head = None    # keep track of the start of the list
    
    def apply(self, lam):
        """Apply a function to every node in a circular linked list.

        Parameters:
        - lam: a function to apply to each node. This function should take a single argument, which will be a node from the linked list.
        """
        cur = self.head
        while cur.nxt and cur.nxt != self.head:
            lam(cur)
            cur = cur.nxt
        lam(cur)
        
    def show(self):
        """Print out the value of all nodes in the linked list"""
        self.apply(lambda x: print(x.val, end=', '))
        print('\n')

    def link(self):
        """Link the nodes in a circular linked list.

        This function sets the `nxt` (next) attribute of each node to the
        next node in the list, and the `prv` (previous) attribute of each
        node to the previous node in the list. It also sets the `head`
        attribute of the linked list to the first node in the list.
        """
        for l, r in zip(self.nodes, self.nodes[1:]):
            l.nxt = r
            r.prv = l
        self.nodes[0].prv = self.nodes[-1]
        self.nodes[-1].nxt = self.nodes[0]
        self.head = self.nodes[0]
        
    def shuffle(self):
        # shuffle the nodes going by their original order
        for cur in self.nodes:
            if cur == self.head and cur.val != 0:
                self.head = cur.nxt
            # remove curent node from current position in the linked list
            cur.prv.nxt = cur.nxt
            cur.nxt.prv = cur.prv
            # initialize left and right neighbors
            l = cur.prv
            for _ in range(cur.val % (len(self.nodes) - 1)):
                l = l.nxt
            r = l.nxt
            # insert new node between neighbors
            l.nxt = cur
            r.prv = cur
            # set node to point to neighbords
            cur.prv = l
            cur.nxt = r

    def find_grove_coordinates(self):
        """
        Then, the grove coordinates can be found by looking at the 1000th, 
        2000th, and 3000th numbers after the value 0, wrapping around the 
        list as necessary. 
        """
        cur = self.head
        while cur.nxt and cur.nxt != self.head:
            if cur.val == 0:
                break
            cur = cur.nxt
        res = 0
        for i in [1000, 2000, 3000]:
            tmp = cur
            for _ in range(i % len(self.nodes)):
                tmp = tmp.nxt
            res += tmp.val
        return res

    def to_list(self):
        """Convert a circular linked list to a list.

        Returns:
        - a list containing the values of the nodes in the linked list, in the order that they appear in the linked list.
        """
        cur = self.head
        r = []
        while cur.nxt and cur.nxt != self.head:
            r.append(cur.val)
            cur = cur.nxt
        r.append(cur.val)
        return r

pt1 = DoublyLinkedList()
pt2 = DoublyLinkedList()
KEY = 811589153
for e in enc:
    pt1.nodes.append(Node(e))
    pt2.nodes.append(Node(e * KEY))
pt1.link()
pt2.link()

pt1.shuffle()
print('Part 1:', pt1.find_grove_coordinates())

# takes around 7 sec
for i in range(10):
    pt2.shuffle()
print('Part 2:', pt2.find_grove_coordinates())