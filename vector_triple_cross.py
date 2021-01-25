import numpy as np
from icecream import ic

def scan():
    print('Input vector "a"')
    ax, ay, az = map(int,input().split())
    print('Input vector "b"')
    bx, by, bz = map(int,input().split())
    print('Input vector "c"')
    cx, cy, cz = map(int,input().split())

    a = np.array([ax, ay, az])
    b = np.array([bx, by, bz])
    c = np.array([cx, cy, cz])
    
    return [a, b, c]

def vec_tri(array):
    'calculate vector triple product'
    return np.cross(np.cross(array[0],array[1]),array[2])

if __name__ == "__main__":
    ic(vec_tri(scan()))