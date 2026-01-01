from src.config.db_config import mypool
from src.config.my_config import my_global
from mysql.connector import Error

def eksekusi1():
    try:
        with mypool.get_connection() as conn:
            return (conn.user, conn.server_host, my_global("mydb"))
    except Error as db_error:
        print(f"db_error: {db_error}")
    except Exception as e:
        print(f"error: {e}")

def eksekusi2():
    pass

def eksekusi3():
    pass

def eksekusi4():
    pass

def eksekusi5():
    pass

daftar = {
    "eksekusi1": eksekusi1,
    "eksekusi2": eksekusi2,
    "eksekusi3": eksekusi3,
    "eksekusi4": eksekusi4,
    "eksekusi5": eksekusi5,
    }

def eksekusi(pilih):
    fungsi = daftar.get(pilih)
    return fungsi()