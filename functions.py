import sqlite3

import pandas as pd
from termcolor import colored
from datetime import date
from global_statics import DATABASE_NAME
from helpers import *


# from sql_scripts import SELECT_BY_ROUTE
def variance_to_between_request_response_time_to_csv():
    result = []
    sqlite_connection = None
    try:
        sqlite_connection = sqlite3.connect(DATABASE_NAME)
        cursor = sqlite_connection.cursor()
        statement = '''SELECT ID, request, request_time, upstream_response_time  FROM logs '''
        cursor.execute(statement)
        output = cursor.fetchall()
        for item in output:
            try:
                val1 = float(item[2])
                val2 = float(item[3])
                if not val1 > 1.0:
                    continue
            except:
                continue

            variance_val = val1 - val2
            # if variance_val < 0: variance_val = 0.0
            item = item + (variance_val,)
            result.append(item)

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    except PermissionError as error:
        print(colored("Permission DENIED error while opening file, close file if exists and is open", 'red'))
    except:
        print(colored("Unexpected error", 'red'))
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("The SQLite connection is closed.")

    log_entries = result
    logs_df = pd.DataFrame(log_entries)
    file_name = f"request_response_time_exceed_1ms_with_variance{"{:%Y_%m_%d_%H_%M_%S}".format(datetime.now())}.csv"
    header_list = ['ID', 'request', 'request_time', 'upstream_response_time', 'variance']
    logs_df.to_csv(file_name, index=False, header=header_list, na_rep='N/A', index_label='ID')
    print(colored("process finished successfully.", 'green'))


def info_by_route_name(to_find):
    sqlite_connection = None
    try:
        sqlite_connection = sqlite3.connect(DATABASE_NAME)
        cursor = sqlite_connection.cursor()
        statement = ''' SELECT ID, request, request_time, upstream_response_time, request_method, status FROM logs WHERE request LIKE ? '''
        print(f"searching similar routes for value {{to_find}} ...")
        cursor.execute(statement, (f"%{to_find}%",))
        output = cursor.fetchall()
        print("writing results to excel file has been started...")

        log_entries = output
        logs_df = pd.DataFrame(log_entries)
        file_name = f"report_with_route_name{"{:%Y_%m_%d_%H_%M_%S}".format(datetime.now())}.csv"
        header_list = ['ID', 'request', 'request_time', 'upstream_response_time', 'request_method', 'status']
        logs_df.to_csv(file_name, header=header_list, index=False, na_rep='N/A', index_label='ID')
        print(colored("process finished successfully.", 'green'))

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    except PermissionError as error:
        print(colored("Permission DENIED error while opening file, close file if exists and is open", 'red'))
    except:
        print(colored("Unexpected error", 'red'))
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("The SQLite connection is closed")


def request_time_value_exceed_n(n):
    result = []
    sqlite_connection = None
    try:
        sqlite_connection = sqlite3.connect(DATABASE_NAME)
        cursor = sqlite_connection.cursor()
        statement = '''SELECT ID, request, request_time, upstream_response_time  FROM logs '''
        cursor.execute(statement)
        output = cursor.fetchall()
        for item in output:
            try:
                val1 = float(item[2])
                if val1 > float(n):
                    result.append(item)
            except:
                continue

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    except PermissionError as error:
        print(colored("Permission DENIED error while opening file, close file if exists and is open", 'red'))
    except:
        print(colored("Unexpected error", 'red'))
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("The SQLite connection is closed.")

    log_entries = result
    logs_df = pd.DataFrame(log_entries)
    file_name = f"request_time_value_exceed_n_{"{:%Y_%m_%d_%H_%M_%S}".format(datetime.now())}.csv"
    header_list = ['ID', 'request', 'request_time', 'upstream_response_time']
    logs_df.to_csv(file_name, index=False, header=header_list, na_rep='N/A', index_label='ID')
    print(colored("process finished successfully.", 'green'))
