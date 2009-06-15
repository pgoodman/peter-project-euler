
import __builtin__
from os import listdir
import re

files = listdir('.')

def import_problem(n, ident, *idents_opt):
	"""
	import_problem(int, string[, string[, ...]]) -> (object, ...) | object
	
	Import functions/variables/objects used in the solution to a particular
	problem. This is quite hack but oh well, it makes it much easier to 
	reference and use functions from other problems.
	"""
	
	pattern = re.compile("^(0*%d\s.*)\.py$" % int(n))
	
	# keep it ordered
	identifiers = [ident, ]
	identifiers.extend(idents_opt)
	
	for file in files:
		match = pattern.match(file)
		if match:
			module =__import__(match.group(1))
			
			if len(identifiers) is 1:
				return getattr(module, ident)
			else:
				return [getattr(module, name) for name in identifiers]
	
	return None
