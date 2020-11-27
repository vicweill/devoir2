from . import create_new_table, connect_to_db_server,insert_rows_to_table, csv_to_tuples, csv_to_table
from . import path_data

try:
	# open connection to db
	con = connect_to_db_server()
	# create a new table "person"
	create_new_table(con)
	# convert dataset to list of rows
	#data = csv_to_tuples(path_data)
	# populate table
	csv_to_table(con, "persons", path_data)
	# close connection
	con.close()
except Exception as e:
        print(f"An error occured:\n {e}")
finally:
    if con is not None:
        con.close()	
	

"""
runs tkinter/__main__.py, which has this line:

from . import _test as main

In this context, . is tkinter, so importing . imports tkinter, which runs tkinter/__init__.py.  _test is a function defined within that file. So calling main() (next line) has the same effect as running python -m tkinter.__init__ at the command line.

"""
