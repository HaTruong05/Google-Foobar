def solution(pegs):
    """Given a list of integers with each integer representing 
    the position of a peg, find the radius of the first peg given
    the following restrictions:
        - each peg must have a radius greater than 1
        - pegs must connect to one another, meaning the combined
        radii of two pegs must match the distance between them
        - the radius of the first peg must be twice the the radius
        of the final peg
    If a solution is not possible, return [-1, -1]

    Args:
        pegs (list): contains the position of the pegs

    Returns:
        list: represents the radius of the first peg as a fraction,
            with the first element representing the numerator, and 
            the second representing the denominator
    """
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

        # The radius of the last peg can't be greater than 2/3 of the distance between 
        # the first peg and the second peg nor can it be greater than the distance between 
        # itself and the second last peg
        # Multiply the bounds by 3 to find the upper bound for the numerator since 4/3 is 
        # represented as [4, 3] and so on
        largest_poss_last_radius_num = min(first_distance // 2 * 3, last_distance * 3)

        # Check every possible radius to see if any of them works
        for last_radius in range(3, largest_poss_last_radius_num + 1):
            if last_radius % 3 == 0:
                denominator = 1
                next_peg_radius = last_distance - last_radius
            else:
                denominator = 3
                next_peg_radius = last_distance * 3 - last_radius

            for idx in range(-2, -peg_count, -1):
                # If any of the radius we are trying out leads to a peg with
                # a radius of less than 1, stop exploring that branch
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

