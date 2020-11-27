def csv_to_tuples(csv_file):
	""" Convert csv to list of tuples of rows """
	
	import csv
	with open(csv_file) as f:
	    data=[tuple(line) for line in csv.reader(f)]
	    return data