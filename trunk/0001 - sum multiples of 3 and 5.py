
def divides(a, b):
    """
    divides(int, int) -> bool
    
    Return whether or not a evenly divides b.
    """
    return (b % a) == 0

def sum_one_to(n):
    """
    choose2(int) -> int
    
    Return the number of subsets of length 2 that can be formed from a set
    of size n, or alternatively: sum the numbers from 1 to n, inclusive.
    """
    n = int(n)+1
    return int((n * (n-1)) / 2)

def linear_solution(n):
    """Sum of multiples of 3 or 5 that are less than 1000 in O(n) expected
    time."""
    s = 0
    for i in range(1, n):
        if divides(3, i) or divides(5, i):
            s = s + i
    return s

def constant_solution(n):
    """Sum of multiples of 3 or 5 that are less than 1000 in O(1) expected
    time."""
    n = int(n) - 1
    return int(3 * sum_one_to(n/3)) + int(5 * sum_one_to(n/5)) - int(15 * sum_one_to(n/15))

if __name__ == "__main__":
    print constant_solution(1000)
