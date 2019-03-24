#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: suchit
"""
import numpy as np

def search(directions, path):
    """
    Search the directions array for path
    """
    global lis
    lis=[] # to store the starting element of paths
    if len(path) == 0:
        return 0
    suffix_table = good_suffix(path)
    shift_table = shift(path)
    i = len(path) - 1
    while i < len(directions):
        j = len(path) - 1
        while path[j] == directions[i]:
            if j == 0:
                lis.append(i)
                i=i+len(path)
            i -= 1
            j -= 1
        i += max(shift_table[len(path) - 1 - j], suffix_table.get(directions[i]));
    if len(lis)!=0:
        print(len(lis)," Paths Detected")
    else:
        print("No Paths Detected")
    return -1
 
     
def shift(needle):
    table = {}
    for i in range(len(needle) - 1):
        table[needle[i]] = len(needle) - 1 - i
    return table
     
def good_suffix(needle):
    table = []
    last_prefix_position = len(needle)
    for i in reversed(range(len(needle))):
        if is_prefix(needle, i + 1):
            last_prefix_position = i + 1
        table.append(last_prefix_position - i + len(needle) - 1)
    for i in range(len(needle) - 1):
        slen = suffix_length(needle, i)
        table[slen] = len(needle) - 1 - i + slen
    return table
     
def is_prefix(needle, p):
    #prefix check
    j = 0
    for i in range(p, len(needle)):
        if needle[i] != needle[j]:
            return 0
        j += 1   
    return 1
     
def suffix_length(needle, p):
    #max suffix length
    length = 0;
    j = len(needle) - 1
    for i in reversed(range(p + 1)):
        if needle[i] == needle[j]:
            length += 1
        else:
            break
        j -= 1
    return length

def get_direction(sample):
    """
    sample is a 300*2 array - each row an x and y value
    """
    directions=[]
    for i in range(299):
        if(sample[i+1,0]==sample[i,0] and sample[i+1,1]>sample[i,1]):
            directions.append("U")
        elif(sample[i+1,0]==sample[i,0] and sample[i+1,1]<sample[i,1]):
            directions.append("D")
        elif(sample[i+1,0]>sample[i,0] and sample[i+1,1]==sample[i,1]):
            directions.append("R")
        elif(sample[i+1,0]<sample[i,0] and sample[i+1,1]==sample[i,1]):
            directions.append("L")
    return directions
        
def main():
    sample = np.random.rand(300,2) #redefine this to generated array
    directions = get_direction(sample)
    path = ["U","L","R","D","U","D"]
    search(directions,path)
    
main()