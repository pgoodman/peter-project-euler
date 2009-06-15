
def sum_of_even_fibonacci_numbers(max_fib):
    """
    sum_of_even_fibonacci_numbers(int) -> int
    
    Return the sum of all even Fibonacci numbers that are less than max_fib.
    """
    
    f = 1
    i = 1
    total = 0
    
    while f < max_fib:
        f, i = f + i, f
        if f & 1 == 0:
            total += f
    else:
        return total

if __name__ == "__main__":
    print sum_of_even_fibonacci_numbers(4000000)