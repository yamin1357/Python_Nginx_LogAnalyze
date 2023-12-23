import os
import re
import shlex
import sqlite3

from global_statics import DB_LOG_COLUMN_NAMES, DATABASE_NAME
from global_statics import KEY_WORDS


def remove_keywords(objDic):
    for key in objDic.keys():
        for item in KEY_WORDS:
            if item in objDic[key]:
                objDic[key] = objDic[key].replace(item, '')
    return objDic


def parse_log_file(line):
    sqlite_connection = None
    try:
        sqlite_connection = sqlite3.connect(DATABASE_NAME)
        cursor = sqlite_connection.cursor()
        print("Database created and Successfully Connected to SQLite")

        line = re.sub(r"[\[\]]", "", line)
        data = shlex.split(line)

        result = {
            "0": data[DB_LOG_COLUMN_NAMES["datetime"]],
            "1": data[DB_LOG_COLUMN_NAMES["client"]],
            "2": data[DB_LOG_COLUMN_NAMES["request_method"]],
            "3": data[DB_LOG_COLUMN_NAMES["request"]],
            "4": data[DB_LOG_COLUMN_NAMES["request_length"]],
            "5": data[DB_LOG_COLUMN_NAMES["status"]],
            "6": data[DB_LOG_COLUMN_NAMES["bytes_sent"]],
            "7": data[DB_LOG_COLUMN_NAMES["body_bytes_sent"]],
            "8": data[DB_LOG_COLUMN_NAMES["referer"]],
            "9": data[DB_LOG_COLUMN_NAMES["upstream_addr"]],
            "10": data[DB_LOG_COLUMN_NAMES["upstream_status"]],
            "11": data[DB_LOG_COLUMN_NAMES["request_time"]],
            "12": data[DB_LOG_COLUMN_NAMES["upstream_response_time"]],
            "13": data[DB_LOG_COLUMN_NAMES["upstream_connect_time"]],
            "14": data[DB_LOG_COLUMN_NAMES["upstream_header_time"]],
            "15": data[DB_LOG_COLUMN_NAMES["user_agent"]]
        }

        # remove all texts extra from columns then insert to database
        result = remove_keywords(result)

        sqlite_insert_query = ' INSERT INTO logs VALUES (?, ?, ? ,?, ? ,? ,? ,?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '

        data_tuple = (
            None,
            result["0"],
            result["1"],
            result["2"],
            result["3"],
            result["4"],
            result["5"],
            result["6"],
            result["7"],
            result["8"],
            result["9"],
            result["10"],
            result["11"],
            result["12"],
            result["13"],
            result["14"],
            result["15"]
        )
        cursor.execute(sqlite_insert_query, data_tuple)
        sqlite_connection.commit()
        print(f"Record inserted successfully into {DATABASE_NAME} table ", cursor.rowcount)
        cursor.close()
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("The SQLite connection is closed")


def start_parse_log_file():
    print("Trying to find log file directory and the file ...")

    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    rel_path = f"dir_log_file/"
    abs_file_path = os.path.join(script_dir, rel_path)

    for file in os.listdir(abs_file_path):
        if file.endswith(".log"):
            with open(os.path.join(abs_file_path, file), "r") as f:
                for line in f:
                    print("Parsing the log file process started ... ")
                    parse_log_file(line)
            break
    print("Parsing the log file process is finished.")
