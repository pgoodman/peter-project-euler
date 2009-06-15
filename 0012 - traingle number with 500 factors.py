
from math import sqrt
from project_euler import import_problem

sum_one_to = import_problem(1, 'sum_one_to')
factorize, divides = import_problem(3, 'factorize', 'divides')

def num_factors(n):
    """
    num_factors(int) -> int
    
    Return the number of factors (prime or not) for a given number.
    """
    factors = factorize(n)
    num = 1
    for x, exp in factors:
        num *= (exp+1)
    return num

def triangle_with_min_num_factors_slowest(min_num_factors):
    """
    triangle_with_min_num_factors_slower(int) -> (int, int, int)
    
    Find the first triangle number that has at least min_num_factors factors.
    This method uses the prime factorizer from a previous question to find
    all of the prime factors for each triangle number and by extension the
    number of factors for the number.
    """
    i = 1
    factor_count = 1
    num = 1
    
    while factor_count < min_num_factors:
        i = i+1
        num = sum_one_to(i)
        factor_count = num_factors(num)
    else:
        return i, num, factor_count

def triangle_with_min_num_factors_slower(min_num_factors):
    """
    triangle_with_min_num_factors_slower(int) -> (int, int, int)
    
    Find the first triangle number that has at least min_num_factors factors.
    This method works by noticing that half of the factors for a given number
    will be contributed by a number's square root.
    """
    i = 0
    num = 0
    num_factors = 0
    
    while num_factors < 500:
        i = i+1
        num += i
        num_factors = 0
        root = int(sqrt(num))

        for n in xrange(1, root+1):
            if divides(n, num):
                num_factors += 2

        if pow(root, 2) is num:
            num_factors -= 1
    else:
        return i, num, num_factors

def triangle_with_min_num_factors_slow(min_num_factors):
    """
    triangle_with_min_num_factors_slower(int) -> (int, int, int)
    
    Find the first triangle number that has at least min_num_factors factors.
    This method is similar to the one that used prime factorization; however,
    this method uses memoization in order to avoid doing redundant factorization
    by noticing that the sum from 1 to n is n*(n+1) / 2.
    """
    i = 1
    factor_count = 0
    factor_table = {1:1}
    
    while factor_count < min_num_factors:
        i += 1
        j = i+1
        
        if (i & 1) is 0:
            factor_count = factor_table[i / 2]
        else:
            j /= 2
            factor_count = factor_table[i]
        
        factor_table[j] = num_factors(j)
        factor_count *= factor_table[j]
    else:
        return i, sum_one_to(i), factor_count
        
if __name__ == "__main__":
    num, triangle, num_factors = triangle_with_min_num_factors_slow(500)
    
    print """First triangle number with >= 500 factors is triangle(%d)=%d
    %d has %d factors.""" % (num, triangle, triangle, num_factors)
