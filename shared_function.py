from datetime import date
from datetime import datetime
from dateutil import relativedelta
import calendar
import psycopg2

date_format_short = "%Y-%m-%d"
date_format_long = "%Y-%m-%d %H:%M:%S"


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


#   Convert string to date in custom format
def string_to_date_time_custom(date_string, date_time_custom_format):
    return datetime.strptime(date_string, date_time_custom_format).date()


#   Convert string to date time in long (%Y-%m-%d %H:%M:%S) format
def string_to_date_full(date_string):
    return string_to_date_time_custom(date_string=date_string, date_time_custom_format=date_format_long)


#   Convert string to date in short (%Y-%m-%d) format
def string_to_date_short(date_string):
    return string_to_date_time_custom(date_string=date_string, date_time_custom_format=date_format_short)


#   Get current date in custom format
def get_current_date_time_custom_format(date_time_custom_format):
    return datetime.today().strftime(date_time_custom_format)


#   Get current date in short format
def get_current_date():
    return get_current_date_time_custom_format(date_time_custom_format=date_format_short)


#   Get current date and time in long format
def get_current_date_time():
    return get_current_date_time_custom_format(date_time_custom_format=date_format_long)


#   Get next date in period
def get_date_period(current_date, period, date_time_format=date_format_short):
    return str(datetime.strptime(str(current_date), date_time_format).date() + relativedelta.relativedelta(days=period))


#   Get next date (tomorrow)
def get_tomorrow():
    return get_date_period(current_date=get_current_date(), date_time_format=date_format_short, period=1)


#   Get previous date (yesterday)
def get_yesterday():
    return get_date_period(current_date=get_current_date(), date_time_format=date_format_short, period=-1)


#   Get month next, previous in custom format, by default in short
def get_month_period(date_string, period):
    return str(datetime.strptime(str(date_string), date_format_short).date() + relativedelta.relativedelta(months=period))


#   Get next month in short format
def get_month_next(date_string):
    return str(get_month_period(date_string=date_string, period=1))


#   Get previous month in short format
def get_month_previous(date_string):
    return str(get_month_period(date_string=date_string, period=-1))


#   Get first day of month
def get_first_day_of_month(date_string):
    in_date = datetime.strptime(date_string, date_format_short).date()
    return str(string_to_date_short(str(in_date.year) + "-" + str(in_date.month) + "-01"))


#   Get first day of next month
def get_first_day_of_next_month(date_string):
    return get_month_next(get_first_day_of_month(date_string))


#   Get last day of month
def get_last_day_of_month(date_string):
    in_date = datetime.strptime(date_string, date_format_short).date()
    _, num_days = calendar.monthrange(in_date.year, in_date.month)
    return str(string_to_date_short(str(in_date.year) + "-" + str(in_date.month) + "-" + str(num_days)))


#   Get last day of next month
def get_last_day_of_next_month(date_string):
    return get_last_day_of_month(get_month_next(date_string))


#   Get first day of previous month
def get_first_day_of_previous_month(date_string):
    return get_first_day_of_month(get_month_previous(date_string))


#   Get number of days in month
def get_days_number(date_string):
    in_date = datetime.strptime(date_string, date_format_short).date()
    _, num_days = calendar.monthrange(in_date.year, in_date.month)
    return str(num_days)


#   Get last day of previous month
def get_last_day_of_previous_month(date_string):
    return get_last_day_of_month(get_month_previous(date_string))
