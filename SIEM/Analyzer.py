def specific_port(cnx, cursor):
    query = "SELECT SRC_IP, PORT from fwlogs"
    cursor.execute(query)
    hackers = set([])
    for log in cursor:
        if log[1] == 444 or log[1] == 4445:
            hackers.add(log[0])
    return hackers


def portscan(cursor):
    query = 'SELECT SRC_IP, DST_IP, PORT from fwlogs'
    cursor.execute(query)
    dct = {}
    for log in cursor:
        key = log[0] + '_' + log[1]
        if key in dct.keys():
            dct[key].add(log[2])
        else:
            dct[key] = set([log[2]])
    return [key for key, value in dct.items() if len(value) >= 10]



