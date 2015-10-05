#!/usr/bin/env python
def recursiveSolve(x,y):
	if x == endX and y == endY:
		return True
	if maze[x][y] == 0 or wasHere[x][y]:  # 0 = wall and 1 = path.
		return False
	wasHere[x][y] = True
	if x != 0:   #Checks if not on left edge
		if recursiveSolve(x-1,y):
			correctPath[x][y] = True
			return True
	if x != height - 1:   #Checks if not on right edge
		if recursiveSolve(x+1,y):
			correctPath[x][y] = True
			return True
	if y != 0:     #Checks if not on top edge
		if recursiveSolve(x,y-1):  
			correctPath[x][y] = True
			return True
	if y != width-1:    #Checks if not on bottom edge
		if recursiveSolve(x,y+1):
			correctPath[x][y] = True
			return True
	return False
width,height = [int(i) for i in input().split()]   #input the weight and height of maze
wasHere = [[False for j in range(width)] for i in range(height)]  # 'wasHere[x][y]=True' denote already use the x,y before 
correctPath = [[False for j in range(width)] for i in range(height)]  #Set boolean array to default value,here is False
endX,endY = 0,0     #Ending X and Y values of maze
startX,startY = height-1,width-1   # Starting X and Y values of maze
maze = [[] for i in range(height)]
for i in range(height):   # initial maze
	input_ = input()
	for j in input_:
		maze[i].append(int(j))
recursiveSolve(startX,startY)
for i in range(height):
	print(correctPath[i])    #print the path

