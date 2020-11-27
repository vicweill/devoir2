from .utils_postgres import (create_new_table, 
							 connect_to_db_server,
							 csv_to_table,
							 table_to_csv)

import os

# dirname gives the last trailing directory in the absolute path defined by __file__
# again dirname will give the 2nd last trailing directory
package_dir = os.path.dirname(__file__)
path_data = os.path.join(
	package_dir, os.getenv("CSV_FILE"))

