#!/bin/python3

import src.GridOrder as go

if __name__ == '__main__':
    with open('examples.txt', 'r') as file:
        t = int(file.readline())

        for _ in range(t):
            n = int(file.readline())

            grid = []

            for _ in range(n):
                grid_item = file.readline().strip()
                grid.append(grid_item)

            grid_object = go.Grid(grid)
            result = grid_object.grid_challenge()

            print(result)