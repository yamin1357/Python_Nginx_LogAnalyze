CREATE_LOGS_TBL = """ CREATE TABLE IF NOT EXISTS logs (
                                        ID integer PRIMARY KEY,                                        
                                        datetime text,
                                        client text,
                                        request_method text,
                                        request text,
                                        request_length text,
                                        status text,
                                        bytes_sent text,
                                        body_bytes_sent text,
                                        referer text,
                                        user_agent text,
                                        upstream_addr text,
                                        upstream_status text,
                                        request_time text,
                                        upstream_response_time text,
                                        upstream_connect_time text,
                                        upstream_header_time text
                                    ) """

# SELECT_BY_ROUTE = ''' SELECT ID, request, request_time, upstream_response_time, request_method, status FROM logs WHERE request LIKE 'GET /api/Mobile/v1/Accounts?appVersion=%'  '''
