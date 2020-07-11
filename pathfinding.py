import numpy as np
import random as rr
import matplotlib.pyplot as plt
import os
import sys
import shutil
import multiprocessing
import glob
import IPython
import heapq
import tree # might be broken

height=10 # change later when maze gets larger
width=10

def findStart(Z):#gets the coordinate of the start position
    start = np.where((Z==2)) # starting position has value of 2
    print("position of start", start)
    row=start[0][0]
    column=start[1][0]
    print("start position" , Z[row][column])
    return [row, column]

def findGoal(Z):#gets the coordinate of the goal position
    goal =np.where((Z==3))  # goal position has value of 3
    print("position of goal", goal)
    row=goal[0][0]
    column=goal[1][0]
    print("goal position" , Z[row][column])
    return [row, column]

def goThroughTree(goal, start)
    solution = []
    while(goal is not start)
        coord = [goal.row, goal.col] 
        solution.append([coord])
        goal = goal.parent
    return solution

def visitNeighbors(Z, start, goal, openList):#checks for unblocked neighbors of a current node in the N,S,E,W
    if start.row + 1  in range(height)
        node = Node(curr, (start.row+1,start.col), curr.g+1, [goal.row, goal.col])
        heapq.heappush(openList, node)
    if start.row - 1  in range(height)
        node = Node(curr, (start.row+1,start.col), curr.g+1, [goal.row, goal.col])
        heapq.heappush(openList, node)
    if start.col + 1  in range(width)
        node = Node(curr, (start.row+1,start.col), curr.g+1, [goal.row, goal.col])
        heapq.heappush(openList, node)
    if start.col - 1  in range(width)
        node = Node(curr, (start.row+1,start.col), curr.g+1, [goal.row, goal.col])
        heapq.heappush(openList, node)

def getNeighbors(Z, s, goal): # gets the possible states from s given the action of moving one square in the maze 
    neighbors = []
    if s.row + 1  in range(height) and Z[s.row+1][s.col] == 0
        node = Node(curr, (s.row+1,s.col), curr.g+1, [goal.row, goal.col])
        neighbors.append(node)
    if s.row - 1  in range(height) and Z[s.row-1][s.col] == 0
        node = Node(curr, (s.row+1,s.col), curr.g+1, [goal.row, goal.col])
        neighbors.append(node)
    if s.col + 1  in range(width) and Z[s.row][s.col+1] == 0
        node = Node(curr, (s.row+1,s.col), curr.g+1, [goal.row, goal.col])
        neighbors.append(node)
    if s.col - 1  in range(width) and Z[s.row][s.col-1] ==0
        node = Node(curr, (s.row+1,s.col), curr.g+1, [goal.row, goal.col])
        neighbors.append(node)
    return neighbors

def isInClosedList(closedList, node):
    for x in closedList:
        if x.row == node.row and x.col = node.col
            return true
    return false

def computePath(start, goal, Z):
    #initialize open list
    openList = []
    visitNeighbors(Z, start, goal, openList)
    closedList = []
    while goal.g > openList[0]: # if openList is empty this will throw an error
        s = heapq.pop(openList)
        if s.row == goal.row and s.col == goal.col:
            goThroughTree(goal, start)
            
        if isInClosedList(closedList, s):
            continue
        closedList.append(s)

        neighbors = getNeighbors(Z, s, goal)
        for x in neighbors:#for all actions a in A(s)
            if x.g > s.g+1: # a cheaper cost has been found to reach state x
                x.g = s.g+1
                x.parent = s # we now get to x from state s
                # search through the open list and remove old g(x) this would take more time but reduce memory usage
                heapq.heappush(openList, x)

        #if open list empty stop





#*** NEED****
# Open list that supports nodes in a heap structure ordered by f(s)=h(s)+g(s) for tie breaker cases
# Closed list (2D array or list) 

# tie breaking ( large and small g(s) ) 
# Additionally prioritize N,S,E,W directions

if __name__ == "__main__":

    # if mac or if windows
    if sys.argv[2] == "m":
        path = "arrs/backTrackerMazes/" + sys.argv[1]
    if sys.argv[2] == "w":
        path = "arrs\\backTrackerMazes\\" + sys.argv[1]

    Z = np.loadtxt(path, delimiter = ' ').astype(int) 
    print(Z)

    counter = 0

    #initialize the start and goal nodes
    start = Node(start, None, findStart(Z), 0, 0) #start is represented as a 2 in the txt document
    goal = Node(goal, None, findGoal(Z), 0, 0) #goal is represented as a 3 in the txt document


    #create an open list
    #create a closed list that is a 2D array 
    
    f.close()

    

