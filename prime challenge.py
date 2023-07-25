
def solution(i):
    """Given an index, return the 5 digits in a string of 
    primes starting at the given index

    Args:
        i (int): the given index

    Returns:
        str: contains the 5 digits starting at the given index
    """
    primes = prime_gen(100000)
    return primes[i:i+5]

def prime_gen(upper_bound):
    """Given an interger, find all prime numbers up until
    that integer

    Args:
        upper_bound (int): the upper bound

    Returns:
        str: contains all the primes found
    """
    num_list = [True for i in range(upper_bound+1)]
    
    # Number to check 
    poss_prime = 2
    
    # Flag all powers of primes as non primes
    while poss_prime**2 < upper_bound+1:
        if num_list[poss_prime]:
            for i in range(poss_prime**2, upper_bound+1, poss_prime):
                num_list[i] = False
        poss_prime += 1
        
    # Add all the primes found to a string
    primes_str = ""
    for idx in range(2, upper_bound+1):
        if num_list[idx]:
            primes_str += str(idx)
      
    return primes_str


if __name__ == "__main__":
    print(solution(10000))