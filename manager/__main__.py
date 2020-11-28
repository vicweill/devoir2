from . import *

try:
	con = None
	# open connection to db
	con = connect_to_db_server(pguser, pgpassword, pgdb)
	# create a new table "person"
	create_new_table(con)
	# populate table from csv file
	csv_to_table(con, "persons", path_data)
	# read table again
	table_to_csv(con, "persons", path_output_data)
except Exception as e:
	print(f"An error occured:\n {e}")
finally:
	# close connection if exists
    if con is not None:
        con.close()	

"""
runs tkinter/__main__.py, which has this line:

from . import _test as main

In this context, . is tkinter, so importing . imports tkinter, which runs tkinter/__init__.py.  _test is a function defined within that file. So calling main() (next line) has the same effect as running python -m tkinter.__init__ at the command line.

"""
