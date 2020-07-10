
import numpy as np
import random as rr
import matplotlib.pyplot as plt
import os
import sys
import shutil
import multiprocessing
import glob
import IPython


if __name__ == "__main__":

    # if mac or if windows
    if sys.argv[2] == "m":
        path = "arrs/backTrackerMazes/" + sys.argv[1]
    if sys.argv[2] == "w":
        path = "arrs\\backTrackerMazes\\" + sys.argv[1]

    f = open(path, "r")
    #txt = f.read()
    #print(txt)
    Z = np.loadtxt(path, delimiter = ' ').astype(int)
    print(Z)

    #get start and end positions and make nodes for them
    #start is a 2 
    #end is a 3

    start = np.where((Z==2))
    print("position of start", start)
    row=start[0][0]
    column=start[1][0]
    print("start position" , Z[row][column])

    goal =np.where((Z==3))
    print("position of goal", goal)
    row=goal[0][0]
    column=goal[1][0]
    print("goal position" , Z[row][column])
    
    f.close()

    

