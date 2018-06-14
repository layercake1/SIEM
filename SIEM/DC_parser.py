def log_to_dict(log):
    dct = {}
    log = log.split()
    dct['DATE'] = log[0] + " " + log[1]
    dct['SRC_IP'] = log[2]
    dct['USERNAME'] = log[3]
    dct['LOGIN_ATTEMPT'] = 0 if log[4] == 'Failed' else 1
    return dct


def InsertToDB(log, cnx, cursor):
    add_log = ("""INSERT INTO dc_logs
                (ID, DATE, SRC_IP, USERNAME, LOGIN_ATTEMPT)
                VALUES (NULL, %(DATE)s, %(SRC_IP)s, %(USERNAME)s, %(LOGIN_ATTEMPT)s)""")
    cursor.execute(add_log, log)
    cnx.commit()


def insert_logs(log_file, cnx, cursor):
    with open(log_file, 'r') as logs:
        count = 0
        for line in logs:
            dct = log_to_dict(line)
            InsertToDB(dct, cnx, cursor)
            count += 1
    return count