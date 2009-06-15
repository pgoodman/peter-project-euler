
sum_one_to = __import__("001 - sum multiples of 3 and 5").sum_one_to

def sum_of_squares(n):
    return ((n**3 / 3) + (n**2 / 2) + (n / 6))

def square_of_sums(n):
    return sum_one_to(n)**2

if __name__ == "__main__":
    print abs(square_of_sums(100) - sum_of_squares(100))