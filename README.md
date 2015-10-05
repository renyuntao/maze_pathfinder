#Synopsis
Find the path from bottom-right corner to top-left corner in maze.  
#Example
run program as  
`$ python maze_pathfinder.py`  
then Input thedata as follows:    
13 9  
1111101110111   
0010001000001    
1011111111111  
1000000010100    
1111111110101    
0010000010001    
1111101010111    
1010001000100    
1011111111111      
and the program will output as  
[False, True, True, False, False, False, False, False, False, False, False, False, False]  
[False, False, True, False, False, False, False, False, False, False, False, False, False]  
[False, False, True, True, True, True, True, True, True, False, False, False, False]  
[False, False, False, False, False, False, False, False, True, False, False, False, False]  
[False, False, True, True, True, True, True, True, True, False, False, False, False]  
[False, False, True, False, False, False, False, False, False, False, False, False, False]  
[False, False, True, False, False, False, False, False, False, False, False, False, False]  
[False, False, True, False, False, False, False, False, False, False, False, False, False]  
[False, False, True, True, True, True, True, True, True, True, True, True, True]    
**True** denote the path.    
