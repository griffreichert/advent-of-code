import numpy as np
from aoc_tools import *
import copy


with open('../data/day20.txt') as f:
    lines = f.read().strip().split('\n')


enc = list(map(eval, lines))
enc = [1,2,-3,3,-2,0,4]

tests = [
    # [811589153, 1623178306, -2434767459, 2434767459, -1623178306, 0, 3246356612],
    [0, -2434767459, 3246356612, -1623178306, 2434767459, 1623178306, 811589153],
    [0, 2434767459, 1623178306, 3246356612, -2434767459, -1623178306, 811589153],
    [0, 811589153, 2434767459, 3246356612, 1623178306, -1623178306, -2434767459],
    [0, 1623178306, -2434767459, 811589153, 2434767459, 3246356612, -1623178306],
]

# Node to store each value
class Node:
    def __init__(self, val, nxt=None, prv=None) -> None:
        self.val = val
        self.nxt = nxt
        self.prv = prv
        self.visited = False

# Circular doubly linked list to represent the input of the "Encrypted file"
class DoublyLinkedList:

    def __init__(self) -> None:
        self.head = None    # keep track of the start of the list
        self.tail = None    # keep track of the end of the list

    def append(self, val):
        """Append a node with the given value to the end of the linked list.

        Args:
            val: The value of the node to be appended.
        """
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        cur = self.head
        while cur.nxt:
            cur = cur.nxt
        cur.nxt = node
        node.prv = cur
        self.tail = node

    def show(self):
        cur = self.head
        while cur.nxt and cur.nxt != self.head:
            if cur.visited:
                print('*', end='')
            print(cur.val, end=', ')
            cur = cur.nxt
        if cur.visited:
            print('*', end='')
        print(cur.val)

    def close_loop(self):
        h = self.head
        t = self.tail
        h.prv = t 
        t.nxt = h

    def shuffle(self):
        cur = self.head
        # number of nodes visited
        v = 0
        while v < N:
            # if you have visited a node, go to the next one
            if cur.visited:
                cur = cur.nxt
                continue
            
            # if the node is 0, dont move it
            if cur.val == 0:
                cur.visited = True
                v += 1
                cur = cur.nxt
                continue

            # if you havent visited the node, move it <val> number of spaces
            old_l = cur.prv
            old_r = cur.nxt
            if cur == self.head:
                self.head = old_r
            # set the previous node to point to the next node
            old_l.nxt = old_r
            # set next node to point to the previous node
            old_r.prv = old_l

            # # move the node backwards in the list
            if cur.val < 0:
                new_r = cur
                # print('moving', cur.val, -cur.val % (N - 1))
                for _ in range((-cur.val) % (N - 1)):
                    new_r = new_r.prv
                new_l = new_r.prv
            # move the node forwards in the list
            else:
                new_l = cur
                # print('moving', cur.val, cur.val % (N - 1))
                for _ in range(cur.val % (N - 1)):
                    new_l = new_l.nxt
                new_r = new_l.nxt
            # set node in position +val to point nxt to node
            new_l.nxt = cur
            # set node in position +val+1 to point prv to node
            new_r.prv = cur
            # set node to point prv to +val
            cur.prv = new_l
            # set node to point nxt to +val+1
            cur.nxt = new_r
            # self.show()
            cur.visited = True
            cur = old_r
            v += 1
        # reset visited property of all nodes once shuffling is done 
        cur = self.head
        while cur.nxt and cur.nxt != self.head:
            cur.visited = False
            cur = cur.nxt
        cur.visited = False
        # reset tail 
        self.tail = self.head.prv
        # self.tail.visited = False


    def find_grove_coordinates(self):
        cur = self.head
        n = 0
        while cur.nxt and cur.nxt is not self.head:
            if cur.val == 0:
                break
            n += 1
            cur = cur.nxt
        res = 0
        for i in [1000, 2000, 3000]:
            tmp = cur
            for _ in range(i % N):
                tmp = tmp.nxt
            res += tmp.val
        return res

    def to_list(self):
        cur = self.head
        r = []
        while cur.nxt and cur.nxt != self.head:
            r.append(cur.val)
            cur = cur.nxt
        r.append(cur.val)
        return r
        

encrypted = DoublyLinkedList()
N = len(enc)
KEY = 811589153
# KEY = 1
for e in enc:
    encrypted.append(e * KEY)
encrypted.close_loop()
encrypted.show()
for i in range(10):
    encrypted.shuffle()
    encrypted.show()
    e = encrypted.to_list()
    print(i, f'\nmine: {e}, \ntest: {tests[i]}')
    assert all(a == b for a, b in zip(e, tests[i]))

print('Part 1:', encrypted.find_grove_coordinates())

