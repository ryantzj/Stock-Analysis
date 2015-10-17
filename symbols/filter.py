from os import listdir 
from os import remove
import re

files = listdir('/Users/ryan/DevOps/python/project_2_stock_analytic/symbols/')

for file in files:
	with open(file, 'r') as f:
	    	first_line = f.readline()
	if re.match(r"<.*",first_line):
			remove(file)
