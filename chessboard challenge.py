# Represents the moves the knight can make
UP_RIGHT = -15
UP_LEFT = -17

DOWN_RIGHT = 17
DOWN_LEFT = 15

RIGHT_UP = -6
RIGHT_DOWN = 10

LEFT_UP = -10
LEFT_DOWN = 6

POSS_ROWS = [1, 2, 3, 4, 5, 6, 7, 8]
POSS_COLS = [1, 2, 3, 4, 5, 6, 7, 8]


def solution(src, dest):
    """Given a starting square and a destination on an 8x8 board, 
    return the smallest number of moves the knight need to reach 
    the end 

    Args:
        src (int): the starting square
        dest (int): the destination

    Returns:
        int: the smallest number of moves needed
    """        
    source_dict = {0: [src]}

    end_row, end_col = __find_position(dest)

    # If destination is same as starting square, the knight doesn't have to move
    if src == dest:
        return 0
    
    # The largest number of moves a knight need to reach any square on an 8x8 baord is 6
    for i in range (6):
        for source in source_dict[i]:
            start_row, start_col = __find_position(source)
            poss_moves = __remove_unnecessary_moves(start_row, end_row, start_col, end_col)
            __find_poss_moves(poss_moves, start_row, start_col)
            for move in poss_moves:
                new_dest = source + move
                if new_dest == dest:
                    print(source)
                    return i + 1
                else:
                    source_dict[i+1] = source_dict.get(i + 1, []) + [new_dest]


def __remove_unnecessary_moves(start_r, end_r, start_c, end_c):
    """Remove the non optimal moves for the knight. For example, 
    if the destination is to the right of the starting square, 
    the knight shouldn't consider moving to the left

    Args:
        start_r (int): the row the knight is in
        end_r (int): the row the knight wants to reach
        start_c (int): the col the knight is in
        end_c (int): the col the knight wants to reach

    Returns:
        list: Contains only the optimal moves
    """
    poss_moves = [UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT, RIGHT_UP, RIGHT_DOWN, LEFT_UP, LEFT_DOWN]
    if end_c < start_c:
            poss_moves.remove(RIGHT_DOWN)
            poss_moves.remove(RIGHT_UP)
    elif end_c > start_c:
            poss_moves.remove(LEFT_DOWN)
            poss_moves.remove(LEFT_UP)

    if end_r < start_r:
            poss_moves.remove(DOWN_LEFT)
            poss_moves.remove(DOWN_RIGHT)
    elif end_r > start_r:
            poss_moves.remove(UP_LEFT)
            poss_moves.remove(UP_RIGHT)
    return poss_moves

def __find_poss_moves(moves, start_row, start_col):
    """Remove illegal moves. For example, if the knight starts on
    the first or second column, meaning the edge of the board is
    on the left, the knight can't make moves that involve moving
    2 squares to the left

    Args:
        moves (list): contains the moves the knight can make if we
            don't consider the starting position 
        start_row (int): the starting row
        start_col (int): the starting column
    """
    if UP_LEFT in moves:
        if start_row == 1 or start_row == 2 or start_col == 1:
            moves.remove(UP_LEFT)
    
    if UP_RIGHT in moves:
        if start_row == 1 or start_row == 2 or start_col == 8:
            moves.remove(UP_RIGHT)

    if DOWN_LEFT in moves:
        if start_row == 7 or start_row == 8 or start_col == 1:
            moves.remove(DOWN_LEFT)

    if DOWN_RIGHT in moves:
        if start_row == 7 or start_row == 8 or start_col == 8:
            moves.remove(DOWN_RIGHT)
    
    if LEFT_DOWN in moves:
        if start_col == 1 or start_col == 2 or start_row == 8:
            moves.remove(LEFT_DOWN)
    
    if LEFT_UP in moves:
        if start_col == 1 or start_col == 2 or start_row == 1:
            moves.remove(LEFT_UP)
    
    if RIGHT_DOWN in moves:
        if start_col == 7 or start_col == 8 or start_row == 8:
            moves.remove(RIGHT_DOWN)

    if RIGHT_UP in moves:
        if start_col == 8 or start_col == 8 or start_row == 1:
            moves.remove(RIGHT_UP)
            

def __find_position(src):
    """Given a square, find the position of the square

    Args:
        src (int): the given square

    Returns:
        tuple: contains the row and the column the square is in
    """
    return __find_row(src), __find_col(src)


def __find_row(src):
    """Given a square, find the row of the square

    Args:
        src (int): the given square

    Returns:
        int: the row the square is in
    """
    return POSS_ROWS[src // 8]


def __find_col(src):
    """Given a square, find the column of the square

    Args:
        src (int): the given square

    Returns:
        int: the column the square is in
    """
    return POSS_COLS[src % 8]


if __name__ == "__main__":
    print(solution(0, 63))
