import json
import os
from player import LeagueMember

def W1_saveData():
    ans = []
    file_path = 'C:/Users/cookk/MyProjects/BrawlAchivments/data/S17 - League Database - Week1.tsv'
    with open(file_path, 'r') as f:
        for line in f:
            l = line.strip().split('\t')
            if l[2] != '':
                ans.append(l)
    # for elem in ans:
    #     print(elem)
    return ans

def W2_saveData():
    ans = []
    file_path = 'C:/Users/cookk/MyProjects/BrawlAchivments/data/S17 - League Database - Week2.tsv'
    with open(file_path, 'r') as f:
        for line in f:
            l = line.strip().split('\t')
            if l[2] != '':
                ans.append(l)
    # for elem in ans:
    #     print(elem)
    return ans

def W3_saveData():
    ans = []
    file_path = 'C:/Users/cookk/MyProjects/BrawlAchivments/data/S17 - League Database - Week3.tsv'
    with open(file_path, 'r') as f:
        for line in f:
            l = line.strip().split('\t')
            if l[2] != '':
                ans.append(l)
    # for elem in ans:
    #     print(elem)
    return ans

def W4_saveData():
    ans = []
    file_path = 'C:/Users/cookk/MyProjects/BrawlAchivments/data/S17 - League Database - Week4.tsv'
    with open(file_path, 'r') as f:
        for line in f:
            l = line.strip().split('\t')
            if l[2] != '':
                ans.append(l)
    # for elem in ans:
    #     print(elem)
    return ans
        