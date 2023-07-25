
def solution(i):
    # Your code here
    primes = prime_gen(100000)
    return primes[i:i+5]

def prime_gen(n):
    num_list = [True for i in range(n+1)]
    
    # Number to check 
    poss_prime = 2
    
    while poss_prime**2 < n+1:
        if num_list[poss_prime]:
            for i in range(poss_prime**2, n+1, poss_prime):
                num_list[i] = False
        poss_prime += 1
        
    primes_str = ""
    
    for idx in range(2, n+1):
        if num_list[idx]:
            primes_str += str(idx)
      
    return primes_str


if __name__ == "__main__":
    print(solution(10000))