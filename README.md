# Info
Several useful functions for simple work with date, postgresql.

# Functions for work with date
def string_to_date_time_custom(date_string, date_time_custom_format):
def string_to_date_full(date_string):
def string_to_date_short(date_string):
def get_current_date_time_custom_format(date_time_custom_format):
def get_current_date():
def get_current_date_time():
def get_date_period(current_date, period, date_time_format=date_format_short):
def get_tomorrow():
def get_yesterday():
def get_month_period(date_string, period):
def get_month_next(date_string):
def get_month_previous(date_string):
def get_first_day_of_month(date_string):
def get_first_day_of_next_month(date_string):
def get_last_day_of_month(date_string):
def get_last_day_of_next_month(date_string):
def get_first_day_of_previous_month(date_string):
def get_days_number(date_string):
def get_last_day_of_previous_month(date_string):

# Functions for work with Postgresql
def open_connection_with_db(dbname, dbuser, dbpass, dbhost="localhost", dbport=5432, debug=False):
def close_connection_with_db(cursor):
def run_query(cursor, query, debug=False):
def truncate_table(cursor, table_name, debug=False):
def drop_table(cursor, table_name, debug=False):
def create_table(cursor, table_name, data_types, debug=False):
def set_search_path_db(cursor, dbname, debug=False):

# Required packages
dateutils, calendar, psycopg2, datetime
