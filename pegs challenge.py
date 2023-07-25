def solution(pegs):
    peg_count = len(pegs)
    first_peg = pegs[0]
    second_peg = pegs[1]
    first_distance = second_peg - first_peg
    if peg_count == 2:
        if first_distance % 3 == 0:
            return [int(first_distance * 2 / 3), 1]
        elif first_distance > 1:
            return [int(first_distance * 2), 3]
        else:
            return [-1, -1]
    else: 
        last_peg = pegs[-1]
        sec_last_peg = pegs[-2]
        last_distance = last_peg - sec_last_peg

        largest_poss_last_radius = min(first_distance // 2 * 3, last_distance * 3)

        for last_radius in range(3, largest_poss_last_radius + 1):
            if last_radius % 3 == 0:
                denominator = 1
                next_peg_radius = last_distance - last_radius
            else:
                denominator = 3
                next_peg_radius = last_distance * 3 - last_radius

            for idx in range(-2, -peg_count, -1):
                if next_peg_radius / denominator >= 1:
                    current_peg = pegs[idx]
                    next_peg = pegs[idx - 1]
                    distance = current_peg - next_peg

                    if denominator == 1:
                        next_peg_radius = distance - next_peg_radius
                    else:
                        next_peg_radius = distance * 3 - next_peg_radius

            # next_peg_radius is the first peg's radius after the loop runs
            if next_peg_radius == last_radius * 2:
                if next_peg_radius % 3 == 0 and denominator == 3:
                    return [next_peg_radius / 3, 1]
                else: 
                    return [next_peg_radius, denominator]
        return [-1, -1]
            

if __name__ == "__main__":
    print(solution([3, 7, 9, 11]))
    print(solution([1, 7]))
    print(solution([4, 30, 50]))
    print(solution([1, 5, 9, 13]))
    print(solution([1, 7]))
    print(solution([4, 17, 50]))
    print(solution([1, 27, 50]))
    print(solution([1, 170, 300, 400]))

