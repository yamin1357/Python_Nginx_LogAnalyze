print(">>> Nginx log reader application by python built at October 28, 2023")

from database_generator import start_database_generation
from functions import *
from functions import variance_to_between_request_response_time_to_csv
from parser import start_parse_log_file
from helpers import *

if __name__ == '__main__':
    while True:
        command_r = input(
            "choose operation to run: \n a) parse nginx log file to sqlite3 database \n b) find all "
            "records with specified route url \n c) read variance request_times and response_times  \n d) generate database \n "
            "e) restart \n n) find requests from one value to the next as <<request_time starts from n=1.0 to=end>> \n o)"
            "exit \n ===> ")

        if command_r == 'a':
            start_parse_log_file()

        elif command_r == 'b':
            to_find = input("enter verb wanna search inside routes ===> ")
            while to_find == "":
                print(colored("CAN NOT SEARCH FOR NONE ! ENTER SOME PART OF REQUEST URL PLEASE.", 'red'))
                to_find = input("enter verb wanna search inside routes ===> ")

            confirm = input("Sure to continue generating report ? yes: 1 / no: 2 ===> ")
            if confirm == '1':
                info_by_route_name(to_find)

        elif command_r == 'c':
            variance_to_between_request_response_time_to_csv()

        elif command_r == 'd':
            start_database_generation()

        elif command_r == 'n':
            n_val = input("enter request_time lower bound wanna start to the end ===> ")
            while n_val == "":
                print(colored("CAN NOT SEARCH FOR NONE ! ENTER MINIMUM VALUE FOR <<request_time>> PLEASE.", 'red'))
                n_val = input("enter request_time lower bound wanna start to the end ===> ")
            confirm = input("Sure to continue generating report ? yes: 1 / no: 2 ===> ")

            if confirm == '1':
                request_time_value_exceed_n(n_val)

        elif command_r == 'r':
            continue

        elif command_r == 'o':
            break
    quit()
