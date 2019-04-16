# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 14:32:59 2019

@author: 245_01

各种排序算法
"""

def BubbleSort(l):    #冒泡排序，大往上
    for i in range(len(l)-1, 0, -1):
        for j in range(i):
            if l[j] > l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
    return l

def BubbleSortShort(l):    #冒泡排序，包含有序检测，比较过程发现有序即退出排序
    exchange = True
    i = len(l) - 1
    while i>0 and exchange:
        exchange = False
        for j in range(i):
            if l[j] > l[j+1]:
                exchange = True
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
    return l

def upDownBubbleSort(l):
    return l

def SelectionSort(l):      #选择排序，每一循环选出最大的一个放在最后
    for i in range(len(l), 0, -1):
        maxIndex = 0
        for j in range(1, i):
            if l[maxIndex] < l[j]:
                maxIndex = j
        temp = l[maxIndex]
        l[maxIndex] = l[i-1]
        l[i-1] = temp
            
    return l

def InsertSort(l):       #插入排序，对有序数列效率较高
    for i in range(1, len(l)):
        currval = l[i]
        index = i
        while index>0 and l[index-1]>currval:
            l[index] = l[index-1]
            index -= 1
        l[index] = currval
    return l

def GapSelectionSort(l, startpos, gap):
    for i in range(startpos+gap, len(l), gap):
        currval = l[i]
        index = i
        while index>0 and l[index-gap]>currval:
            l[index] = l[index-gap]
            index -= gap
        l[index] = currval
    return l
        
def ShellSort(l):        #希尔排序，利用插入排序对有序数列效率较高的特性，每隔一定间隙进行排序，得到局部有序数列，再进行插入排序
    g = len(l)//2
    while g>0:
        for i in range(g):
            l = GapSelectionSort(l, i, g)
        g = g//2
    return l

def MergeSort(l):       #归并排序，递归思想
    if len(l) > 1:
        mid = len(l)//2
        leftsort = l[:mid]
        rightsort = l[mid:]
        
        leftsort = MergeSort(leftsort)
        rightsort = MergeSort(rightsort)
        
        i=0
        j=0
        k=0
        
        while i<len(leftsort) and j<len(rightsort):
            if leftsort[i]<rightsort[j]:
                l[k] = leftsort[i]
                i += 1
            else:
                l[k] = rightsort[j]
                j += 1
            k += 1
        
        while i<len(leftsort):
            l[k] = leftsort[i]
            k += 1
            i += 1

        while j<len(rightsort):
            l[k] = rightsort[j]
            k += 1
            j += 1
    return l
    
def QuickSort(l):
    QuickSortHelper(l, 0, len(l)-1)
    return l

def QuickSortHelper(l, first, last):
    if first < last:
        par = partition(l, first, last)
        
        QuickSortHelper(l, first, par-1)
        QuickSortHelper(l, par+1, last)
        
        
def partition(l, first, last):
    pivot = l[first]     #pivot选择可以更加有效率，random等方式
    left = first + 1
    right = last
    done = False
    while not done:
        while l[left]<pivot and left <= right:
            left += 1
        while l[right]>pivot and right >= left:
            right -= 1
        if right < left:
            done = True
        else:
            temp = l[left]
            l[left] = l[right]
            l[right] = temp
    temp = l[first]
    l[first] = l[right]
    l[right] = temp
    return right
        

a=[54,26,93,17,77,31,44,55,20]
print(QuickSort(a))