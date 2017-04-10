"""
Example of using class PyPSQL.
"""
import pypsql

database = "hh"
datauser = "python"
datapass = "qqqqqQ!1"
psql = pypsql.PyPSQL(dbname=database, dbuser=datauser, dbpass=datapass)
print(psql.dsn_string())
psql.connect()
psql.set_search_path()
if psql.connected:
    a = psql.query(query="SELECT * FROM vacancies LIMIT 1;")
    for r in a.fetchall():
        print(r[0])
    psql.create_table(table_name="IDs", table_schema="ID NUMERIC")
    psql.query(query="INSERT INTO IDs SELECT vac_id FROM vacancies;")
    a = psql.query(query="SELECT count(*) FROM IDs;")
    print(str(a.fetchone()[0]))
    psql.truncate(table_name="IDs")
    psql.rename_table(old_table_name="IDs", new_table_name="IDs_new")
    a = psql.check_table_exist(table_name="IDs")
    print(str(a))
    psql.drop_table(table_name="IDs_new")
    del psql
