
from project_euler import import_problem

sum_one_to = import_problem(1, 'sum_one_to')

def sum_of_squares(n):
	"""
	sum_of_squares(int) -> int
	
	For a set S = {1, 2, .., n}, return sum{i^2 | i in S}. This takes 
	advantage of Faulhaber's Formula to calculate the sum in O(1).
	"""
	return ((pow(n, 3) / 3) + (pow(n, 2) / 2) + (n / 6))

def square_of_sums(n):
	"""
	square_of_sums(int) -> int
	
	For some set S = {1, 2, .., n}, return sum{S}^2.
	"""
	return pow(sum_one_to(n), 2)

if __name__ == "__main__":
	print abs(square_of_sums(100) - sum_of_squares(100))