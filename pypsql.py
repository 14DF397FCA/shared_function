"""
Version 1.1
Simple Python3 class for work with PostgreSQL.
Allows to run basic queries, such as - create, drop, rename and truncate table. Checking exist of the table. Fast method to get number of rows. "query" for other queries.
Required module - psycopg2.
"""
try:
    import psycopg2
except ImportError:
    raise ImportError("Can not import psycopg2")


class PyPSQL:
    """
    Wrapper class for work with PostgreSQL from Python3
    """
    def __init__(self, dbname, dbuser, dbpass="", dbhost="localhost", dbport="5432"):
        if dbname:
            self.dbname = dbname
        else:
            raise ValueError("Database name can not be empty")
        if dbuser:
            self.dbuser = dbuser
        else:
            raise ValueError("Database user can not be empty")
        self.dbpass = dbpass
        self.dbhost = dbhost
        self.dbport = dbport
        self.cursor = None
        self.connected = False
        self._dbname = ""
        self._dbuser = ""

    def __del__(self):
        self.cursor.close()
        self.cursor.connection.close()

    def dsn_string(self):
        """
        Build DSN string
        :return: DSN string
        """
        return "dbname={db_name} dbuser={db_user} db_pass={db_pass} db_host={db_host} db_port={db_port}".\
            format(db_name=self.dbname, db_user=self.dbuser, db_pass=self.dbpass, db_host=self.dbhost, db_port=self.dbport)

    def connect(self):
        """
        Connect with specified database
        :return: cursor to database or error
        """
        connection = None
        try:
            connection = psycopg2.connect(database=self.dbname,
                                          user=self.dbuser,
                                          password=self.dbpass,
                                          host=self.dbhost,
                                          port=self.dbport)
        except psycopg2.Error as e:
            raise e.diag.message_primary
        try:
            self.cursor = connection.cursor()
            self.connected = True
        except psycopg2.Error as e:
            raise e.diag.message_primary

    def query(self, query):
        """
        Query to database
        :param query: Your query (SELECT, DROP etc)
        :return: result of query, in cursor
        """
        if not query:
            raise ValueError("Query is empty")
        try:
            self.cursor.execute(query)
            self.cursor.connection.commit()
            return self.cursor
        except psycopg2.Error as e:
            raise e.diag.message_primary

    def set_search_path(self, search_to=""):
        """
        Set search_path to your database
        :return:
        """
        if search_to == "":
            search_to = self.dbname
        self.query(query="SET search_path TO " + search_to + ";")

    def truncate(self, table_name):
        """
        Truncate specified table
        :param table_name: Name of table for truncate
        :return:
        """
        if not table_name:
            raise ValueError("Table name is empty")
        self.query(query="TRUNCATE TABLE " + table_name + ";")

    def create_table(self, table_name, table_schema):
        """
        Create table with specified parameters
        :param table_name: Name of table
        :param table_schema: Columns names and types
        :return:
        """
        if not table_name and not table_schema:
            raise ValueError("Table name or table schema is empty")
        self.query(query="CREATE TABLE IF NOT EXISTS " + table_name + " ( " + table_schema + " ); ")

    def drop_table(self, table_name):
        """
        Drop specified table
        :param table_name: Name of table for drop
        :return:
        """
        if not table_name:
            raise ValueError("Table name is empty")
        self.query(query="DROP TABLE IF EXISTS " + table_name + ";")

    def check_table_exists(self, table_name):
        """
        Checking exist of the table
        :param table_name: Name of table
        :return:
        """
        if not table_name:
            raise ValueError("Table name is empty")
        self.query(query="SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name='" + table_name + "');")
        return self.cursor.fetchone()[0]

    def rename_table(self, old_table_name, new_table_name):
        """
        Rename table
        :param old_table_name: Old name of table
        :param new_table_name: New name of table
        :return:
        """
        if not old_table_name and not new_table_name:
            raise ValueError("Old or New table news is empty")
        self.query(query="ALTER TABLE " + old_table_name + " RENAME TO " + new_table_name + ";")

    def count_rows_fast(self, table_name):
        """
        If you don't need an exact count, the current statistic from the catalog table pg_class might be good enough
        and is much faster to retrieve for big tables. See https://wiki.postgresql.org/wiki/Count_estimate for details.
        :param table_name: Table name
        :return: Row count
        """
        if not table_name:
            raise ValueError("Table name is empty")
        self.query(query="SELECT reltuples AS approximate_row_count FROM pg_class WHERE relname = " + table_name + ";")
        return self.cursor.fetchone()[0]

    def copy_expert(self, query, io_steam):
        """
        Submit a user-composed COPY statement. The method is useful to handle all the parameters that PostgreSQL makes
        available (see COPY command documentation)
        http://initd.org/psycopg/docs/cursor.html
        :param query:
        :param io_steam:
        :return:
        """
        self.cursor.copy_expert(query, io_steam)
