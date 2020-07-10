class Node:
    def __init__(self, blocked):
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.data = blocked # 1 if blocked and 0 if unblocked
        self.g = None
        self.h = None
        self.position = None
        #heuristic and cost to come needed

def manhattan(): #h(n)
    x1=5
    y1=5
    x2=0
    y2=0
    distance = abs(x1-x2)+abs(y1-y2)
    return distance

#function to calculate f(n) = g(n) + h(n)

if __name__ == "__main__":
    print(manhattan())

