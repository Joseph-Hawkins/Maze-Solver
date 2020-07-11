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
from tree import Node# might be broken

height=10 # change later when maze gets larger
width=10

def initializeMaze(Z, gPosition):   ##creates Nodes for each cell in the grid
    Maze = [[None for _ in range(height)] for _ in range(width)]

    for i, row in enumerate(Z):
        for j, cell in enumerate(row):
            Maze[i][j] = Node(None,(i,j),gPosition)
            if Z[i][j] == 1:
                Maze[i][j].ctype = 1
            if Z[i][j] == 2:
                Maze[i][j].ctype =2
                Maze[i][j].g = 0
            if Z[i][j] == 3:
                Maze[i][j].ctype= 3
    return Maze
    
def findStart(Z):#gets the coordinate of the start position
    start = np.where((Z==2)) # starting position has value of 2
    print("position of start", start)
    row=start[0][0]
    column=start[1][0]
    print("start position" , Z[row][column])
    return (row, column)

def findGoal(Z):#gets the coordinate of the goal position
    goal =np.where((Z==3))  # goal position has value of 3
    print("position of goal", goal)
    row=goal[0][0]
    column=goal[1][0]
    print("goal position" , Z[row][column])
    return (row, column)

def goThroughTree(goal, start):
    solution = []
    while(goal is not start):
        coord = [goal.row, goal.col] 
        solution.append(coord)
        goal = goal.parent
    return solution


def getNeighbors(Maze, s, goal): # gets the possible states from s given the action of moving one square in the maze 
    neighbors = []
    if s.row + 1  in range(height) and Z[s.row+1][s.col] != 1:
        node = Maze[s.row+1][s.col]
        neighbors.append(node)
    if s.row - 1  in range(height) and Z[s.row-1][s.col] != 1:
        node = Maze[s.row-1][s.col]
        neighbors.append(node)
    if s.col + 1  in range(width) and Z[s.row][s.col+1] != 1:
        node = Maze[s.row][s.col+1]
        neighbors.append(node)
    if s.col - 1  in range(width) and Z[s.row][s.col-1] != 1:
        node = Maze[s.row][s.col-1]
        neighbors.append(node)
    return neighbors

def isInClosedList(closedList, node):
    for x in closedList:
        if x.row == node.row and x.col == node.col:
            return True
    return False

def computePath(start, goal, Maze):
    openList = [] ##initialize Open List
    heapq.heappush(openList,start)
    closedList = []
    while openList and goal.g >= (openList[0].g + openList[0].h): # if openList is empty this will throw an error
        s = heapq.heappop(openList)
        print(s.row, " ", s.col)

        if s.row == goal.row and s.col == goal.col:
            print("found found found found found!")
            return goThroughTree(s,start)
   
        if isInClosedList(closedList, s):
            continue
        closedList.append(s)
        neighbors = getNeighbors(Maze, s, goal)
        for x in neighbors:#for all actions a in A(s)
            if x.g > s.g+1: # a cheaper cost has been found to reach state x
                x.g = s.g+1
                x.f = x.g + x.h
                x.parent = s # we now get to x from state s
                # search through the open list and remove old g(x) this would take more time but reduce memory usage
                for y in openList:
                    if y.row == x.row and y.col == x.col:
                            openList.remove(y)
                heapq.heappush(openList, x)






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

    #find the start and goal nodes
    
    gpos = findGoal(Z)
    spos = findStart(Z)
    Maze = initializeMaze(Z,gpos);  ## initial the maze which is like a gridworld

    start = Maze[spos[0]][spos[1]]
    goal = Maze[gpos[0]][gpos[1]]

    sol = computePath(start, goal, Maze)
    print(sol)


    


    

