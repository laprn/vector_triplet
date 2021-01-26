import numpy as np
from icecream import ic

def det(matrix):
    return np.linalg.det(matrix)

def main():
    print('input lenght of matrix')
    lenght = int(input())
    matrix = np.zeros((lenght,lenght))
    for i in range(lenght):
        print(f'input row num.{i} with space')
        row = [int(i) for i in input().split()]
        matrix[i] = row
    ic(matrix)
    return np.linalg.det(matrix)

if __name__ == '__main__':
    ic(main())
