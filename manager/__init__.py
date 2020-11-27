from .utils_postgres import (create_new_table, 
							 connect_to_db_server, 
							 insert_rows_to_table,
							 csv_to_table)
from .utils import csv_to_tuples

import os

# dirname gives the last trailing directory in the absolute path defined by __file__
# again dirname will give the 2nd last trailing directory
package_dir = os.path.dirname(__file__)
path_data = os.path.join(
	package_dir, os.getenv("CSV_FILE"))

