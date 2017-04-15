"""
Example of using class PyPSQL.
"""
#   Import wrapper class
import pypsql
#   Credentials for access to database
database = "hh"
datauser = "python"
datapass = "qqqqqQ!1"
#   Create exemplar of class
psql = pypsql.PyPSQL(dbname=database, dbuser=datauser, dbpass=datapass)
#   Print DSN connection string
print(psql.dsn_string())
#   Connect with database
psql.connect()
#   Change search path to your if you have several schemas in your database
psql.set_search_path()
#   If connection with database esteblished
if psql.connected:
    #   Run query
    a = psql.query(query="SELECT * FROM vacancies LIMIT 1;")
    for r in a.fetchall():
        print(r[0])
    #   Create table
    psql.create_table(table_name="IDs", table_schema="ID NUMERIC")
    psql.query(query="INSERT INTO IDs SELECT vac_id FROM vacancies;")
    a = psql.query(query="SELECT count(*) FROM IDs;")
    print(str(a.fetchone()[0]))
    #   Truncate table
    psql.truncate(table_name="IDs")
    #   Rename table
    psql.rename_table(old_table_name="IDs", new_table_name="IDs_new")
    #   Check exists of the table
    a = psql.check_table_exists(table_name="IDs")
    print(str(a))
    #   Drop table
    psql.drop_table(table_name="IDs_new")
    #   Delete exemplar of class
    del psql