from datetime import date
from datetime import datetime
from dateutil import relativedelta
import calendar
import psycopg2


#   open connection with database
#   open_connection_with_db(...)
def open_connection_with_db(dbname, dbuser, dbpass, dbhost="localhost", dbport=5432, debug=False):
    if debug is True:
        print("DB_HOST = " + dbhost)
        print("DB_PORT = " + dbport)
        print("DB_NAME = " + dbname)
        print("DB_USER = " + dbuser)
        print("DB_PASS = " + dbpass)

    exception_text = None
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(database=dbname, user=dbuser, password=dbpass, host=dbhost, port=dbport)
        cursor = connection.cursor()
        return cursor
    except psycopg2.Error as e:
        exception_text = e.diag.message_primary
        print(exception_text)
    return exception_text


#   close connection with database
#   close_connection_with_db
def close_connection_with_db(cursor):
    cursor.close()
    cursor.connection.close()


#   execute simple query
#   run_simple(cursor, "select * from family")
def run_query(cursor, query, debug=False):
    exception_text = None
    if debug is True:
        print("run_query - " + query)
    try:
        cursor.execute(query)
        cursor.connection.commit()
    except psycopg2.Error as e:
        exception_text = e.pgerror + " - " + e.diag.message_primary
        print(exception_text)
    return exception_text


#   Truncate table
#   truncate_table(cursor, "table_name")
def truncate_table(cursor, table_name, debug=False):
    query = "TRUNCATE TABLE " + table_name + ";"
    if debug is True:
        print(query)
    return run_query(cursor=cursor, query=query, debug=debug)


#   Drop same table
#   drop_table
def drop_table(cursor, table_name, debug=False):
    if debug is True:
        print("Drop table - " + table_name)
    return run_query(cursor=cursor, query=("DROP TABLE IF EXISTS " + table_name + ";"), debug=debug)


#   Create table
#   create_table()
def create_table(cursor, table_name, data_types, debug=False):
    query = "CREATE TABLE IF NOT EXISTS " + table_name + " ( " + data_types + " ); "
    if debug is True:
        print("table_name - " + table_name)
        print("data_types - " + data_types)
        print("query - " + query)
    return run_query(cursor=cursor, query=query, debug=debug)


#   Set search path
#   set_search_path_db(...)
def set_search_path_db(cursor, dbname, debug=False):
    query = "SET search_path TO " + dbname + ", public;"
    if debug is True:
        print(dbname)
    return run_query(cursor=cursor, query=query)


#   Convert string to date
def str_to_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d").date()


#   Get today
def get_today():
    return str(date.today().strftime("%Y-%m-%d"))


#   Get next date
def get_next_date(date_str):
    return str(datetime.strptime(str(date_str), "%Y-%m-%d").date() + relativedelta.relativedelta(days=1))


#   Get last day of month
def get_last_day_of_month(date_str):
    in_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    _, num_days = calendar.monthrange(in_date.year, in_date.month)
    return str(str(in_date.year) + "-" + str(in_date.month) + "-" + str(num_days))


#   Get first day of month
def get_first_day_of_month(date_str):
    in_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    return str(in_date.year) + "-" + str(in_date.month) + "-01"


#   Get next month
def get_next_month(date_str):
    return str(datetime.strptime(str(date_str), "%Y-%m-%d").date() + relativedelta.relativedelta(months=1))


#   Get previous month
def get_prev_month(date_str):
    return str(datetime.strptime(str(date_str), "%Y-%m-%d").date() + relativedelta.relativedelta(months=-1))


#   Get first day of next month
def get_first_day_of_next_month(date_str):
    return str(get_first_day_of_month(get_next_month(date_str)))


#   Get last day of next month
def get_last_day_of_next_month(date_str):
    return str(get_last_day_of_month(get_next_month(date_str)))


#   Get next/previous date by period
def get_date_by_period(date_str, period):
    return datetime.strptime(str(date_str), "%Y-%m-%d").date() + relativedelta.relativedelta(days=period)


#   Get next period
def get_next_period(date_str):
    return get_date_by_period(date_str=str(date_str), period=30)


#   Get previous date
def get_previous_period(date_str):
    return get_date_by_period(date_str=str(date_str), period=-30)
