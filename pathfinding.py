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
from tree import Node

height = 10  # change later when maze gets larger
width = 10
expanded = 0


def initializeMaze(Z, gPosition, algo):  # creates Nodes for each cell in the grid
    gtype = True
    if algo == "s":
        gtype = False
    Maze = [[None for _ in range(height)] for _ in range(width)]
    for i, row in enumerate(Z):
        for j, cell in enumerate(row):
            Maze[i][j] = Node(None, (i, j), gPosition, gtype)
    return Maze


def findStart(Z):  # gets the coordinate of the start position
    start = np.where((Z == 2))  # starting position has value of 2
    row = start[0][0]
    column = start[1][0]
    #print("start position:", "(", row, ",", column, ")")
    return (row, column)


def findGoal(Z):  # gets the coordinate of the goal position
    goal = np.where((Z == 3))  # goal position has value of 3
    row = goal[0][0]
    column = goal[1][0]
    #print("goal position:", "(", row, ",", column, ")")
    return (row, column)


def goThroughTree(goal, start):
    solution = []
    while(goal is not start):
        coord = [goal.row, goal.col]
        solution.insert(0, coord)
        goal = goal.parent
    return solution


# gets the possible states from s given the action of moving one square in the maze
def getNeighbors(Maze, s, goal):
    neighbors = []
    # Northern neighbor
    if s.row + 1 in range(height) and (Z[s.row+1][s.col] != 1 or Maze[s.row+1][s.col].visible == 0):
        node = Maze[s.row+1][s.col]
        neighbors.append(node)
    # Southern neighbor
    if s.row - 1 in range(height) and (Z[s.row-1][s.col] != 1 or Maze[s.row-1][s.col].visible == 0):
        node = Maze[s.row-1][s.col]
        neighbors.append(node)
    # Eastern neighbor
    if s.col + 1 in range(width) and (Z[s.row][s.col+1] != 1 or Maze[s.row][s.col+1].visible == 0):
        node = Maze[s.row][s.col+1]
        neighbors.append(node)
    # Western neighbor
    if s.col - 1 in range(width) and (Z[s.row][s.col-1] != 1 or Maze[s.row][s.col-1].visible == 0):
        node = Maze[s.row][s.col-1]
        neighbors.append(node)
    #print("neighbors of", s.row, s.col, " ", neighbors)
    return neighbors


def isInClosedList(closedList, node):
    for x in closedList:
        if x.row == node.row and x.col == node.col:
            return True
    return False


def computePath(start, goal, Maze, counter, openList, closedList):
    ##print("current start position", start.row, start.col)
    heapq.heappush(openList, start)
    # if openList is empty or if no shorter path is found we exit
    while openList and goal.g >= (openList[0].g + openList[0].h):
        s = heapq.heappop(openList)
        ##print(s.row, " ", s.col)

        if s.row == goal.row and s.col == goal.col:
            ##print("*****PATH FOUND!*****")
            return goThroughTree(s, start)

        if isInClosedList(closedList, s):
            continue
        closedList.append(s)
        global expanded
        expanded = expanded + 1
        neighbors = getNeighbors(Maze, s, goal)
        for x in neighbors:  # for all actions a in A(s)
            if x.search < counter:  # reset nodes
                # print("test")
                x.g = 1000000
                x.search = counter

            if x.g > s.g+1:  # a cheaper cost has been found to reach state x
                # print("test2")
                x.g = s.g+1
                x.f = x.g + x.h
                x.parent = s  # we now get to x from state s
                # search through the open list and remove old g(x) this would take more time but reduce memory usage
                for y in openList:
                    if y.row == x.row and y.col == x.col:
                        openList.remove(y)
                heapq.heappush(openList, x)
                # print(openList)

    return None  # failed to find


def showPath(sol, Z):  # prints path computed by A*
    for x in sol:
        Z[x[0]][x[1]] = 9  # change path to *'s
    Z[goal.row][goal.col] = 3
    return Z
    # change so it writes into a text file


# updates surrounding squares that become visible when the agent moves
def updateVisibleNodes(s, Maze):
    if s.row + 1 in range(height) and Maze[s.row+1][s.col].visible == 0:
        Maze[s.row+1][s.col].visible = 1  # make northern neighbor visible
        # Maze[s.row+1][s.col].blocked = Z[s.row+1][s.col] #change blocked or unblocked value
    if s.row - 1 in range(height) and Maze[s.row-1][s.col].visible == 0:
        Maze[s.row-1][s.col].visible = 1  # make southern neighbor visible
    if s.col + 1 in range(width) and Maze[s.row][s.col+1].visible == 0:
        Maze[s.row][s.col+1].visible = 1  # make eastern neighbor visible
    if s.col - 1 in range(width) and Maze[s.row][s.col-1].visible == 0:
        Maze[s.row][s.col-1].visible = 1  # make western neighbor visible
    return Maze


def printVisibleNodes(Maze):  # prints nodes seen while performing search
    visible = [[0 for row in range(height)] for col in range(width)]
    print("*****Positions of seen nodes*****")
    for i, row in enumerate(Maze):
        for j, cell in enumerate(row):
            visible[i][j] = Maze[i][j].visible
        print(visible[i])


def adaptiveUpdate(closedList, fval):
    for x in closedList:
        x.h = fval-x.g


# writes algorithm details to a file
def statReport(sol, maze, algExecuted, expansions, Z):
    fileName = sys.argv[4]
    with open(fileName, 'a') as f:
        f.write('Maze file: ' + maze + '\n')
        f.write('A* executions: ' + str(algExecuted) + '\n')
        f.write('Expanded Cells: ' + str(expansions) + '\n')
        if sol is not None:
            f.write('Path length: ' + str(len(sol)) + '\n')
        f.write('Solution: ')
        if sol is None:  # unsolvable mazes
            f.write('no Solution')
            f.write('\n' + '\n')
            f.close()
            return
        for item in sol:
            f.write(str(item))
        f.write('\n' + '\n')
    f.close()
    plt.figure()
    plt.imshow(Z, cmap=plt.cm.plasma, interpolation='nearest')
    plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == "__main__":
    # handles mac or windows path differences
    if sys.argv[2] == "m":
        path = "arrs/backTrackerMazes/" + sys.argv[1]
    if sys.argv[2] == "w":
        path = "arrs\\backTrackerMazes\\" + sys.argv[1]

    # l forward large g, s for forward small g, b for backward, a for adaptive
    alg = sys.argv[3]
    #print('Maze: ' + sys.argv[1])
    Z = np.loadtxt(path, delimiter=' ').astype(int)
    # print(Z)
    counter = 0
    # find the start and goal nodes
    gpos = findGoal(Z)
    spos = findStart(Z)
    if alg == "b":
        Z[gpos[0]][gpos[1]] = 2
        Z[spos[0]][spos[1]] = 3
        temp = gpos
        gpos = spos
        spos = temp

    # initial the maze which is like a gridworld
    Maze = initializeMaze(Z, gpos, alg)

    start = Maze[spos[0]][spos[1]]
    goal = Maze[gpos[0]][gpos[1]]

    Maze = updateVisibleNodes(start, Maze)  # update visible nodes

    fsol = []
    while start.row != goal.row or start.col != goal.col:
        counter = counter + 1
        start.search = counter
        goal.search = counter
        start.g = 0
        goal.g = 1000000
        closedList = []
        openList = []
        sol = computePath(start, goal, Maze, counter, openList, closedList)
        ##print("compute path number: ", counter,sol)
        # printVisibleNodes(Maze)

        if sol is None:
            print("No solution found")
            statReport(sol, sys.argv[1], counter, expanded, Z)
            # handle report for no solution
            exit()
        for x in sol:
            if Z[x[0]][x[1]] == 1:  # checks if nodes on our A* path are blocked
                break
            start = Maze[x[0]][x[1]]
            fsol.append((start.row, start.col))

            Maze = updateVisibleNodes(start, Maze)  # update visible nodes
        if alg == 'a':
            adaptiveUpdate(closedList, goal.g)
        # print(start.row, " ", start.col) # prints the end of our solution

    start = Maze[spos[0]][spos[1]]
    # print(fsol)

    Z = showPath(fsol, Z)
    # printVisibleNodes(Maze)

    #print("A* executes ", counter, "times")
    #print("Algorithim expands ", expanded, "times")
    statReport(fsol, sys.argv[1], counter, expanded, Z)
