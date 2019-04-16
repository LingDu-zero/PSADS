# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 23:39:38 2019

@author: asus
"""

class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[len(self.items)-1]
        
    def isEmpty(self):
        return self.items == []
        
    def size(self):
        return len(self.items)
        
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeue(self):
        return self.items.pop()
        
    def isEmpty(self):
        return self.items == []
        
    def size(self):
        return len(self.items)
        
class Deque:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
        
    def addFront(self, item):
        self.items.append(item)
        
    def addRear(self, item):
        self.items.insert(0, item)
        
    def removeFront(self, item):
        return self.items.pop()
        
    def removeRear(self, item):
        return self.items.pop(0)
        
    def size(self):
        return len(self.items)
