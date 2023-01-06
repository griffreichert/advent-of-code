import numpy as np
from aoc_tools import *
import copy


with open('../data/day20.txt') as f:
    lines = f.read().strip().split('\n')

enc = [
    1,
    2,
    -3,
    3,
    -2,
    0,
    4,
]

# Node to store each value
class Node:
    def __init__(self, val, nxt=None, prv=None) -> None:
        self.val = val
        self.nxt = nxt
        self.prv = prv
        self.visited = False

# Doubly linked list to represent the input of the "Encrypted file"
class DoublyLinkedList:

    def __init__(self) -> None:
        self.head = None    # keep track of the start of the list
        self.tail = None    # keep track of the end of the list
        self.start = None   # keep track of the start (copy)

    def append(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
            self.start = node
            return
        cur = self.head
        while cur.nxt:
            cur = cur.nxt
        cur.nxt = node
        node.prev = cur
        self.tail = node

    def show(self):
        cur = self.head
        while cur.nxt != self.start:
            # print(cur.val, end=' -> ')
            print(f'{cur.val:2d}')
            cur = cur.nxt
        print(f'{cur.val:2d}')

    def close_loop(self):
        h = self.head
        t = self.tail
        h.prv = t 
        t.nxt = h

    def shuffle(self):
        cur = self.start
        # number of nodes visited
        v = 0
        while v < N:
            # if you have visited a node, go to the next one
            if cur.visited:
                cur = cur.nxt
                continue
            
            # if you havent visited the node, move it <val> number of spaces
            
            # move the node backwards in the list
            if cur.val < 0:
                # for _ in range(-cur.val):
                print('neg')

            # move the node forwards in the list
            else:
                print('moving ', cur.val)
                old_l = cur.prv
                old_r = cur.nxt
                # set the previous node to point to the next node
                old_l.nxt = old_r
                # set next node to point to the previous node
                old_r.prv = old_l
                
                for _ in range(cur.val):
                    new_l = cur.nxt
                new_r = new_l.nxt

                # set node in position +val to point nxt to node
                new_l.nxt = cur
                # set node in position +val+1 to point prv to node
                new_r.prv = cur
                # set node to point prv to +val
                cur.prv = new_l
                # set node to point nxt to +val+1
                cur.nxt = new_r
                # if cur == self.start:
                    # self.start = old_l
            cur.visited = True
            v = N

        

encrypted = DoublyLinkedList()
N = len(enc)
for e in enc:
    encrypted.append(e)
encrypted.close_loop()

encrypted.show()

print()
# print(encrypted.start.val)
# print(encrypted.head.val)
# print(encrypted.tail.val)

encrypted.shuffle()

encrypted.show()