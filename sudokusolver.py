# -- coding: utf-8 --
"""
Created on Mon Jul  6 17:41:22 2020

@author: Lalit Arora
"""

last_solved_cell = []

def isSafetoaddinrow(grid,row,column,num):
    if num in grid[row]:
        return False
    else:
        return True

def isSafetoaddincol(grid,row,column,num):
    length = len(grid)
    for i in range(length):
        if grid[i][column]==num:
            return False
        
    return True

def isSafetoaddinbox(grid,row,column,num):
    row_start = 3*int(row/3)
    col_start = 3*int(column/3)
    for i in range(row_start,row_start+3):
        for j in range(col_start,col_start+3):
            if grid[i][j]==num:
                return False
    return True

def isSafetoadd(grid,row,column,num):
    return isSafetoaddinbox(grid,row,column,num) and isSafetoaddincol(grid,row,column,num) and isSafetoaddinrow(grid,row,column,num)
    
def checkemptyspace(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==0:
                return (i,j)
    return (-1,-1)
                
                
def printgrid(grid):
    for i in range(len(grid)):
        print (grid[i])


def solvecell(grid,row,column,last):
    if grid[row][column] != 0 and last != 1 :
        return True
    for i in range(grid[row][column]+1,10):
        if (isSafetoadd(grid,row,column,i)):
            grid[row][column] = i
            last_solved_cell.append((row,column))
            return True
    grid[row][column] = 0
    coordinates = last_solved_cell.pop()
    return (solvecell(grid,coordinates[0],coordinates[1],1))          


if _name=="main_": 

    import time
    start_time = time.time()
    
    # Creating the Empty Board
    grid =[[0 for x in range(9)]for y in range(9)] 
      
    # Initial Stage of Board
    grid =[[8, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 3, 6, 0, 0, 0, 0, 0], 
          [0, 7, 0, 0, 9, 0, 2, 0, 0], 
          [0, 5, 0, 0, 0, 7, 0, 0, 0], 
          [0, 0, 0, 0, 4, 5, 7, 0, 0], 
          [0, 0, 0, 1, 0, 0, 0, 3, 0], 
          [0, 0, 1, 0, 0, 0, 0, 6, 8], 
          [0, 0, 8, 5, 0, 0, 0, 1, 0], 
          [0, 9, 0, 0, 0, 0, 4, 0, 0]] 

    row = 0
    col = 0

    while (row != -1 or col != -1):
        if solvecell(grid,row,col,0):
            (row,col) = checkemptyspace(grid)
    
    printgrid(grid)
    print("--- %s seconds ---" % (time.time() - start_time))