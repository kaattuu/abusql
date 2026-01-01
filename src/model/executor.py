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

def eksekusi2(query):
    try: 
        with mypool.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                kolom = cursor.column_names
                baris = cursor.fetchall()
                baris.insert(0, kolom)
                return baris
    except Error as db_error:
        print(f"db_error: {db_error}")
    except Exception as e:
        print(f"error: {e}")

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

def eksekusi(pilih, query=None):
    fungsi = daftar.get(pilih)
    if pilih == "eksekusi1":
        return fungsi()
    if pilih == "eksekusi2":
        return fungsi(query)