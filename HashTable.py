# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:17:32 2019

@author: 245_01
"""

class HashTable():
    def __init__(self):
        self.FACTOR = 0.75
        self.l = 0
        self.size = 3
        self.data = [None] * self.size
        self.slots = [None] * self.size
        
    def hashfunction(self, key, size):
        return key%size
    
    def rehash(self, oldhash, size):
        return (oldhash+1)%size
    
    def put(self, key, val):
        hashval = self.hashfunction(key, self.size)
        if self.slots[hashval] == None:
            self.slots[hashval] = key
            self.data[hashval] = val
            self.l += 1
        else:
            if self.slots[hashval] == key:
                self.data[hashval] = val
            else:
                rehashval = self.rehash(hashval, self.size)      #没有做满容量检测，实际上哈希散列表应由负载系数决定是否扩张散列表
                while(self.slots[rehashval] != None and self.slots[rehashval] != key):
                    rehashval = self.rehash(rehashval, self.size)
                if self.slots[rehashval] == None:  
                    self.slots[rehashval] = key
                    self.data[rehashval] = val
                    self.l += 1
                else:
                    self.data[rehashval] = val
        if self.isFull():                           #load factor检测
            self.increase()
            
    
    def isFull(self):             #判断是否需要扩充容量
        return (self.l/self.size) >= self.FACTOR
    
    def increase(self):              #扩充容量至原来的两倍，并对原数据重新hash
        oldslots = self.slots
        olddata = self.data
        self.l = 0
        self.size *= 2
        self.slots = [None] * self.size
        self.data = [None] * self.size
        for i in range(len(oldslots)):
            if oldslots[i] != None:
                self.put(oldslots[i], olddata[i])
        
    def get(self, key):
        startslot = self.hashfunction(key, self.size)
        
        data = None
        found = False
        stop = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, self.size)
                if position == startslot:
                    stop = True
        
        return data
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, val):
        return self.put(key, val)

    def __len__(self):
        return self.l
    
    def __contains__(self, key):
        startslot = self.hashfunction(key, self.size)
        found = False
        stop = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
            else:
                position = self.rehash(position, self.size)
                if position == startslot:
                    stop = True
        return found
    
    