# 0 = walls, 1 = path, 2 = end
easy_maze = [
    [0,0,0,1,0,0,0,0,0,0],
    [0,0,0,1,0,1,1,1,1,1],
    [0,0,0,1,0,0,0,1,0,1],
    [0,0,0,1,0,0,0,1,1,1],
    [0,0,0,1,0,0,0,0,0,0],
    [0,0,0,1,0,1,1,1,0,0],
    [0,0,0,1,0,1,0,1,0,0],
    [0,0,0,1,1,1,0,1,0,0],
    [0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,2]
]

hard_maze = [
    [0,0,0,1,0,0,0,0,0,0],
    [0,0,0,1,1,1,1,1,1,1],
    [0,0,0,1,0,0,1,1,0,1],
    [1,1,1,1,0,0,0,1,1,1],
    [0,0,0,1,0,0,0,0,0,1],
    [0,0,0,1,0,1,0,1,0,1],
    [0,0,0,1,0,1,0,1,0,1],
    [0,0,0,1,1,1,0,1,0,1],
    [0,0,0,0,0,0,0,1,0,1],
    [0,0,0,0,0,0,0,1,1,2]
]

def escape_maze(maze):
    memory = [row[:] for row in maze]

    escape_maze_continued(memory, 0, 3)

def escape_maze_continued(maze, row, column_pos):
    left = column_pos-1
    right = column_pos+1
    up = row-1
    down = row+1
    
    # invalid bounds
    if row >= len(maze) or row < 0 or column_pos < 0 or column_pos >= len(maze[row]):
        return 

    # invalid states
    if maze[row][column_pos] == -1 or maze[row][column_pos] == 0:
        return

    # winning state
    if maze[row][column_pos] == 2:
        print "winhnewr!"
        print str(row) + " " + str(column_pos)
        return
    
    maze[row][column_pos] = -1

    escape_maze_continued( maze, row, left )
    escape_maze_continued( maze, row, right )
    escape_maze_continued( maze, down, column_pos )
    escape_maze_continued( maze, up, column_pos )

escape_maze(easy_maze)
escape_maze(hard_maze)