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
        "4": "",
        }
    return database.get(myquery)

def query3():
    pass

def query4():
    pass

def query5():
    pass

daftar = {
    "query1": query1,
    "query2": query2,
    "query3": query3,
    "query4": query4,
    "query5": query5,
    }

def query(pilih, myquery, data=None):
    fungsi = daftar.get(pilih)
    if data == None:
        return fungsi(myquery)
    return fungsi(myquery, data)