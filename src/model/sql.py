from src.config.my_config import my_global

def query1(myquery):
    monitoring = {
        "1": "",
        "2": "SHOW VARIABLES LIKE 'char%'",
        "3": "SHOW STATUS",
        "4": "SHOW ENGINE INNODB STATUS",
        "5": """
            SELECT 
                CONNECTION_ID() as 'Connection id',
                DATABASE() as 'Current database',
                USER() as 'Current user',
                VERSION() as 'Server version',
                @@version_compile_os as 'Protocol version',
                @@version_compile_machine as 'Architecture'
            """,
        }
    return monitoring.get(myquery)

def query2(myquery, data=None):
    database = {
        "1": "SHOW DATABASES",
        "2": f"CREATE DATABASE IF NOT EXISTS {data}",
        "3": f"USE {data}",
        "4": f"DROP DATABASE {data}",
        }
    return database.get(myquery)

def query3(myquery, data=None):
    data = data if data is not None else ()
    padd = (data + (None,) * 4)[:4]
    p1, p2, p3, p4 = padd
    user = {
        "1" : "SELECT user, host, password FROM mysql.user",
        "2" : f"CREATE USER '{p1}'@'{p2}' IDENTIFIED BY '{p3}'",
        "3" : f"RENAME USER '{p1}'@'{p2}' TO '{p3}'@'{p4}'",
        "4" : f"ALTER USER '{p1}'@'{p2}' IDENTIFIED BY '{p3}'",
        "5" : f"SHOW GRANTS FOR '{p1}'@'{p2}'",
        "6" : f"GRANT ALL PRIVILEGES ON {p1}.* TO '{p2}'@'{p3}'",
        "7" : f"REVOKE ALL PRIVILEGES ON {p1}.* FROM '{p2}'@'{p3}'",
        "8" : "FLUSH PRIVILEGES",
        "9" : "SHOW PROCESSLIST",
        "10": f"KILL {p1}",
        "11": f"DROP USER '{p1}'@'{p2}'",
        }
    return user.get(myquery)

def query4(myquery, data=None):
    data = data if data is not None else ()
    padd = (data + (None,) * 4)[:4]
    p1, p2, p3, p4 = padd
    tabel = {
        "1": f"",
        "2": f"SHOW TABLES FROM {my_global("mydb")}",
        "3": f"",
        "4": f"CREATE TABLE IF NOT EXISTS {my_global("mydb")}.{p1} ({p2})",
        "5": f"SHOW COLUMNS FROM {my_global("mydb")}.{p1}",
        "6": f"SHOW CREATE TABLE {my_global("mydb")}.{p1}",
        "7": f"",
        "8": f"RENAME TABLE {my_global("mydb")}.{p1} TO {my_global("mydb")}.{p2}",
        "9": f"DROP TABLE IF EXISTS {my_global("mydb")}.{p1}",
        }
    return tabel.get(myquery)

def query5(myquery, data=None):
    data = data if data is not None else ()
    padd = (data + (None,) * 4)[:4]
    p1, p2, p3, p4 = padd
    menu_data = {
        "1" : f"",
        "2" : f"",
        "3" : f"",
        "4" : f"INSERT INTO {my_global("mydb")}.{p1} ({p2}) VALUES ({p3})",
        "5" : f"",
        "6" : f"SELECT * FROM {my_global("mydb")}.{p1}",
        "7" : f"UPDATE {my_global("mydb")}.{p1} SET {p2} WHERE {p3}",
        "8" : f"DELETE FROM {my_global("mydb")}.{p1} WHERE {p2}",
        "9" : f"TRUNCATE TABLE {my_global("mydb")}.{p1}",
        "10": f"DELETE FROM {my_global("mydb")}.{p1}",
        }
    return menu_data.get(myquery)

def query6(myquery, data=None):
    data = data if data is not None else ()
    padd = (data + (None,) * 4)[:4]
    p1, p2, p3, p4 = padd
    operasi_kolom = {
        "1"  : f"",
        "2"  : f"ALTER TABLE {my_global("mydb")}.{p1} ADD COLUMN {p2}",
        "3"  : f"ALTER TABLE {my_global("mydb")}.{p1} {p2}",
        "4"  : f"ALTER TABLE {my_global("mydb")}.{p1} ADD COLUMN {p2} FIRST;",
        "5"  : f"",
        "6"  : f"",
        "7"  : f"",
        "8"  : f"",
        "9"  : f"",
        "10" : f"",
        }
    return operasi_kolom.get(myquery)

daftar = {
    "query1": query1,
    "query2": query2,
    "query3": query3,
    "query4": query4,
    "query5": query5,
    "query6": query6,
    }

def query(pilih, myquery, data=None):
    fungsi = daftar.get(pilih)
    if data == None:
        return fungsi(myquery)
    return fungsi(myquery, data)