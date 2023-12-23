DB_LOG_COLUMN_NAMES = {
    "datetime": 0,
    "client": 1,
    "request_method": 2,
    "request": 3,
    "request_length": 4,
    "status": 5,
    "bytes_sent": 6,
    "body_bytes_sent": 7,
    "referer": 8,
    "upstream_addr": 9,
    "upstream_status": 10,
    "request_time": 11,
    "upstream_response_time": 12,
    "upstream_connect_time": 13,
    "upstream_header_time": 14,
    "user_agent": 15
}

KEY_WORDS = [
    "client=",
    "request=",
    "method=",
    "request_length=",
    "upstream_status=",
    "status=",
    "body_bytes_sent=",
    "bytes_sent=",
    "referer=",
    "user_agent=",
    "upstream_addr=",
    "request_time=",
    "upstream_response_time=",
    "upstream_connect_time=",
    "upstream_header_time="
]

DATABASE_NAME = 'log_db.db'
LOG_FILE = 'log_file.log'
