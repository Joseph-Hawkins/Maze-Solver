
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

    
    path = "arrs\\backTrackerMazes\\" + sys.argv[1]
    f = open(path, "r")
    ##txt = f.read()
    ##print(txt)
    Z = np.loadtxt(path, delimiter = ' ')
    print(Z)
    

