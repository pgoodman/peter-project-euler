
from math import log10, floor, ceil
from project_euler import import_problem

is_even = import_problem(2, 'is_even')

def num_digits_in(x):
    """
    num_digits_in(int) -> int

    Returns the number of digits in a given number.
    """
    y = log10(x)
    if is_even(y) and not divides(10, x):
        return int(y)
    
    return int(floor(y) + 1)

def reverse_digits(x):
    """
    reverse_digits(int) -> int
    
    Returns the number with its digits reversed. Note: the reversed form of
    multiples of 10 aren't meaningful.
    """
    r = 0
    while x > 0:
        r = (r + (x % 10)) * 10
        x = int(x / 10)
    
    return int(r / 10)

def digit_aware_brute_force_palindromes(min_mult, max_mult):
    """
    Brute from the palindromes so we have a list of correct results to
    check against.
    
    This method figures out what the maximum number of palindromic numbers
    we should find are, gets only that many, and stops. While this method
    reduces overall loop interations, it does not allow for the quick 
    dismissal as we need to explicitly count each possible palindrome."""
    max_palindrome = 0
    max_palindrom_pair = (1, 1)
    num_palindromes_found = 0
    
    # figure out the maximum number of palindromes we should find to know that
    # we have found the largest number of palindromes.
    digits_min = int(ceil(num_digits_in(min_mult**2) / 2))
    digits_max = int(ceil(num_digits_in(max_mult**2) / 2))
    max_to_look_for = (10**(digits_max - 1) * 9) - (10**(digits_min - 1) * 9)
    the_range = xrange(max_mult, min_mult-1, -1)

    for i in the_range:
        for j in the_range:
            res = j * i
            if res == reverse_digits(res):
                num_palindromes_found = num_palindromes_found + 1
                if res > max_palindrome:
                    max_palindrome = res
                    max_palindrom_pair = (j, i)
                    
                if num_palindromes_found >= max_to_look_for:
                    return (max_palindrome, max_palindrom_pair)
                
        max_mult = max_mult - 1
        
    return (max_palindrome, max_palindrom_pair)

def quick_dismiss_brute_force_palindromes(min_mult, max_mult):
    """
    Brute from the palindromes so we have a list of correct results to
    check against.

    This method tries to dismiss numbers as quickly as possible. If the product
    of two numbers is less than our currently found maximum palindrome then that
    product is dismissed outright."""
    
    max_palindrome = 0
    max_palindrom_pair = (1, 1)
    the_range = xrange(max_mult, min_mult-1, -1)
    
    for i in the_range:
        for j in the_range:
            res = j * i
            
            # quickly dismiss results that are less than our current maximum
            # palindrome
            if res < max_palindrome:
                break
            
            if res == reverse_digits(res):              
                max_palindrome = res
                max_palindrom_pair = (j, i)
            
        max_mult = max_mult - 1

    return (max_palindrome, max_palindrom_pair)

if __name__ == "__main__":
    print quick_dismiss_brute_force_palindromes(100, 999)
