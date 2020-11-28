import os
# user authentification to database server
 
pguser = os.getenv("POSTGRES_USER")
pgpassword = os.getenv("POSTGRES_PASSWORD")
pgdb = os.getenv("POSTGRES_DB")

# dirname gives the last trailing directory in the absolute path defined by __file__
# again dirname will give the 2nd last trailing directory
package_dir = os.path.dirname(__file__)

path_data = os.path.join(
	package_dir, os.getenv("CSV_FILENAME"))
#### for testing only ####
path_output_data = os.path.join(
	package_dir, os.getenv('OUTPUT_CSV_FILENAME'))
