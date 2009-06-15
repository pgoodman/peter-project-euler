
from math import log, floor
from project_euler import import_problem

divides = import_problem(1, 'divides')
factorize = import_problem(3, 'factorize')

def default_list(num_elms, default_val):
    """
    default_list(int, ~) -> [~, ...]
    
    Create a list of num_elms elements, each of which has the value
    default_val.
    """
    return [default_val for i in xrange(0, num_elms)]

def primes_less_than(n):
    """
    primes_less_than(int) -> [int, ...]
    
    Find the set of prime numbers less-than-or-equal to n.
    """
    total = n
    for j in xrange(n-1, 1, -1):
        if not divides(j, total):
            total *= j
    
    return [prime for (prime, exponent) in factorize(total)]

def smallest_number_divisible_by_series(n):
    """
    smallest_number_divisible_by_series(int) -> int
    
    Return the smallest number evenly divisible by all of the numbers in the
    series 1 .. n.
    """
    
    primes = primes_less_than(n)
    prime_exps = dict(zip(primes, default_list(len(primes), 0)))
    log_n = log(n)

    for num in xrange(1, n+1):
        # if we have found a prime then record its multiplicity (in the case 
        # that we are looking at too many primes)
        if num in prime_exps:
            prime_exps[num] = 1
            continue
        
        # go over the primes and increase their exponents if we can
        for p in primes:
            if p > num:
                break
            elif divides(p, num):
                prime_exps[p] = max(floor(log_n / log(p)), prime_exps[p])
    
    # find the product of the primes raised to their respective exponents
    total = 1
    for prime in prime_exps:
        total *= pow(prime, prime_exps[prime])
    
    return int(total)

if __name__ == "__main__":
    print smallest_number_divisible_by_series(20)
