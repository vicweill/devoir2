import unittest
from manager import connect_to_db_server, csv_to_table, table_to_csv, csv_to_tuples
import os

class TestVarEnvPresents(unittest.TestCase):
	def test_postgres_env_vars_set(self):
		""" assert whether env variables are defined """
		self.assertIn("POSTGRES_PASSWORD", os.environ)
		self.assertIn("POSTGRES_USER", os.environ)
		self.assertIn("POSTGRES_DB", os.environ)

	def test_CSV_and_OUPUT_FILE_set(self):
		""" assert the CSV and OUTPUT_FILE are set """
		self.assertIn("CSV_FILENAME", os.environ)
		self.assertIn("OUTPUT_CSV_FILENAME", os.environ)


class TestConnectPostgres(unittest.TestCase):

	def setUp(self):
		self.pgpass = os.getenv("POSTGRES_PASSWORD")
		self.pguser = os.getenv("POSTGRES_USER")
		self.pgdb = os.getenv("POSTGRES_DB")
		self.connection = None

	def test_connection_to_db_server(self):
		""" using db as host server name """
		self.connection = connect_to_db_server(
				self.pguser, self.pgpass, self.pgdb)
		self.assertIsNotNone(self.connection)
			
	def tearDown(self):
		""" This is called even if the test method raised an exception and if the setUp() succeeds """
		if self.connection is not None:
			self.connection.close()

class TestPostgresOperations(TestConnectPostgres):

	def setUp(self):
		super().setUp()
		self.connection = connect_to_db_server(
			self.pguser, self.pgpass, self.pgdb)
		self.cursor = self.connection.cursor()
		self.table_name = "persons"

	def test_table_exists(self):
		""" Check for existence of the table, using EXISTS doesn't require that all rows be retrieved, but merely that at least one such row exists """
		self.cursor.execute(f"select * from {self.table_name} limit 0;")
		#colnames = [desc[0] for desc in self.cursor.description]
		a = self.cursor.fetchone()
		print( a )
		self.assertTrue(a[0])

	def test_csv_upload(self):
		# replace by hand crafted file
		csv_filename = "./data/testing_data.csv"
		csv_output_filename = "./data/fetched.csv"

		csv_to_table(self.connection, self.table_name, csv_filename)
		table_to_csv(self.connection, self.table_name, csv_output_filename)
		self.assertEqual(
			csv_to_tuples(csv_filename),
			csv_to_tuples(csv_output_filename))

	def tearDown(self):
		super().tearDown()

