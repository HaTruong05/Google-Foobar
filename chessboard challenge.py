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
    source_dict = {0: [src]}

    end_row, end_col = __find_pos(dest)

    if src == dest:
        return 0
    
    for i in range (6):
        for source in source_dict[i]:
            start_row, start_col = __find_pos(source)
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

def __find_poss_moves(poss_moves, start_row, start_col):

    if UP_LEFT in poss_moves:
        if start_row == 1 or start_row == 2 or start_col == 1:
            poss_moves.remove(UP_LEFT)
    
    if UP_RIGHT in poss_moves:
        if start_row == 1 or start_row == 2 or start_col == 8:
            poss_moves.remove(UP_RIGHT)

    if DOWN_LEFT in poss_moves:
        if start_row == 7 or start_row == 8 or start_col == 1:
            poss_moves.remove(DOWN_LEFT)

    if DOWN_RIGHT in poss_moves:
        if start_row == 7 or start_row == 8 or start_col == 8:
            poss_moves.remove(DOWN_RIGHT)
    
    if LEFT_DOWN in poss_moves:
        if start_col == 1 or start_col == 2 or start_row == 8:
            poss_moves.remove(LEFT_DOWN)
    
    if LEFT_UP in poss_moves:
        if start_col == 1 or start_col == 2 or start_row == 1:
            poss_moves.remove(LEFT_UP)
    
    if RIGHT_DOWN in poss_moves:
        if start_col == 7 or start_col == 8 or start_row == 8:
            poss_moves.remove(RIGHT_DOWN)

    if RIGHT_UP in poss_moves:
        if start_col == 8 or start_col == 8 or start_row == 1:
            poss_moves.remove(RIGHT_UP)
            

def __find_pos(src):
    return __find_start_row(src), __find_start_col(src)


def __find_start_row(src):
    return POSS_ROWS[src // 8]


def __find_start_col(src):
    return POSS_COLS[src % 8]


if __name__ == "__main__":
    print(solution(0, 63))
