import os

# user authentification to database server 
pguser = os.getenv("POSTGRES_USER")
pgpassword = os.getenv("POSTGRES_PASSWORD")
pgdb = os.getenv("POSTGRES_DB")

package_dir = os.path.dirname(__file__)

path_data = os.path.join(
	package_dir, os.getenv("CSV_FILENAME"))
