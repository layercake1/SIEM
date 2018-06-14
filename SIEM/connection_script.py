import mysql.connector, FireWall_parser, DC_parser, Analyzer
from mysql.connector import errorcode

log_file = "C:\Users\Owner\Downloads\Port_Scan.txt"
dc_log_file = "C:\Users\Owner\Downloads\dc_logs.txt"
user = 'root'
password = 'P@ssw0rd'
host = '192.168.44.130'
database = 'siem'


def ConnectToDB():
    try:
        cnx = mysql.connector.connect(user=user, password=password,
                                      host=host, database=database)
        return cnx, cnx.cursor(buffered=True)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None



def main():
    cnx, cursor = ConnectToDB()
    query = ("SELECT * FROM fwlogs")
    cursor.execute(query)
    #print FireWall_parser.insert_logs(log_file, cnx, cursor)
    #print DC_parser.insert_logs(dc_log_file, cnx, cursor)
    print Analyzer.portscan(cursor)
    cursor.close()
    cnx.close()


if __name__ == '__main__':
    main()