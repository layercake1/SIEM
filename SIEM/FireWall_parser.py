def log_to_dict(log):
    dct = {}
    log = log.split()
    dct['DATE'] = log[0] + " " + log[1]
    dct['SRC_IP'] = log[2]
    dct['DST_IP'] = log[3]
    dct['PORT'] = log[4]
    dct['ACTION'] = log[5]
    add_protocol(dct)
    return dct


def port_num_to_name(num):
    port_dict = {'21':'FTP', '22':'SSH', '23': 'TELNET', '25': 'SMTP', '67': 'DHCP', '53': 'DNS', '80': 'HTTP', '445':
        'SMB','443': 'HTTPS'}
    if num in port_dict.keys():
        return port_dict[num]
    else:
        return 'UNKNOWN'


def add_protocol(dct):
    dct['PROTOCOL'] = port_num_to_name(dct['PORT'])
    return dct


def InsertToDB(log, cnx, cursor):
    add_log = ("""INSERT INTO fwlogs
                (ID, date, SRC_IP, DST_IP, PORT, PROTOCOL, ACTION)
                VALUES (NULL, %(DATE)s, %(SRC_IP)s, %(DST_IP)s, %(PORT)s, %(PROTOCOL)s, %(ACTION)s)""")
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