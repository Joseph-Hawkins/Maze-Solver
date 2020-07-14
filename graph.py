import sys
import numpy as np
import matplotlib.pyplot as plt


def average(list):
    return sum(list)/len(list)


def forwardCompare():
        # large g
    lExp = [0 for i in range(50)]
    sExp = [0 for i in range(50)]
# format
# 0 #Maze file: #.txt
#1 #A* executions: #
#2 #Expanded Cells: #
#3 #Path length: #
#4 #
#5 #
# 6 #Maze file: #.txt
#7 #A* executions: #
#8 #Expanded Cells: #
#9 #Path length: #
#
#

# each maze uses 6 lines
# mazeno stored on lines# mod 6 == 0
# expanded cells #lines with line# mod 6 == 2
#

    f = open('largeG_report.txt', 'r')
    lines = f.readlines()
    n = len(lines)-7
    i = 0
    while i < n:
        # print(i)
        #print('index:', int(lines[i][11:13])-50, 'value:', lines[i+2][16:])
        lExp[int(lines[i][11:13]) - 50] = int(lines[i+2][16:])
        i += 6

    print('large G')
    print(lExp)

    f = open('smallG_report.txt', 'r')
    lines = f.readlines()
    n = len(lines)-7
# print(n)
    i = 0
    while i < n:
        # print(i)
        #print('index:', int(lines[i][11:13])-50, 'value:', lines[i+2][16:])
        sExp[int(lines[i][11:13]) - 50] = int(lines[i+2][16:])
        i += 6

    print('\n\n\n small G')
    print(sExp)
    # put into graph
    print('average small g expansions', str(average(sExp)))
    print('average large g expansions', str(average(lExp)))

    plt.plot(sExp, label='small g')
    plt.plot(lExp, label='large g')
    plt.title('Small vs Large g')
    plt.ylabel('Number of cells expanded')
    plt.xlabel('Maze number')
    plt.legend()
    plt.show()


def forwardAdaptCompare():
            # large g
    lExp = [0 for i in range(50)]
    aExp = [0 for i in range(50)]
# format
# 0 #Maze file: #.txt
#1 #A* executions: #
#2 #Expanded Cells: #
#3 #Path length: #
#4 #
#5 #
# 6 #Maze file: #.txt
#7 #A* executions: #
#8 #Expanded Cells: #
#9 #Path length: #
#
#

# each maze uses 6 lines
# mazeno stored on lines# mod 6 == 0
# expanded cells #lines with line# mod 6 == 2
#

    f = open('largeG_report.txt', 'r')
    lines = f.readlines()
    n = len(lines)-7
    i = 0
    while i < n:
        # print(i)
        #print('index:', int(lines[i][11:13])-50, 'value:', lines[i+2][16:])
        lExp[int(lines[i][11:13]) - 50] = int(lines[i+2][16:])
        i += 6

    print('large G')
    print(lExp)

    f = open('adaptive_report.txt', 'r')
    lines = f.readlines()
    n = len(lines)-7
# print(n)
    i = 0
    while i < n:
        # print(i)
        #print('index:', int(lines[i][11:13])-50, 'value:', lines[i+2][16:])
        aExp[int(lines[i][11:13]) - 50] = int(lines[i+2][16:])
        i += 6

    print('\n\n\n adaptive')
    print(aExp)
    # put into graph
    print('average adaptive expansions', str(average(aExp)))
    print('average large g expansions', str(average(lExp)))

    plt.plot(aExp, label='adaptive')
    plt.plot(lExp, label='large g')
    plt.title('Adaptive vs Forward A*')
    plt.ylabel('Number of cells expanded')
    plt.xlabel('Maze number')
    plt.legend()
    plt.show()


# read all graph stats that apply
# plot comparisons between
if __name__ == "__main__":
    forwardAdaptCompare()
