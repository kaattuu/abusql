from src.config.db_config import mypool
from src.config.my_config import my_global
from mysql.connector import Error

def eksekusi1():
    try:
        with mypool.get_connection() as conn:
            return (conn.user, conn.server_host, my_global("mydb"), my_global("mytb"))
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

def eksekusi3(query):
    try: 
        with mypool.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                kolom = list(cursor.column_names)
                kolom.insert(0, "parameter")
                baris = cursor.fetchall()
                baris = [[str(j) for j in i] for i in baris]
                baris[0].insert(0, "details")
                baris.insert(0, kolom)
                return list(zip(*baris))
    except Error as db_error:
        print(f"db_error: {db_error}")
    except Exception as e:
        print(f"error: {e}")

def eksekusi4(query):
    try: 
        with mypool.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
            print("success...!")
    except Error as db_error:
        print(f"db_error: {db_error}")
    except Exception as e:
        print(f"error: {e}")

def eksekusi5(query):
    try: 
        with mypool.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                kolom = cursor.column_names
                baris = cursor.fetchall()
                return kolom
    except Error as db_error:
        print(f"db_error: {db_error}")
    except Exception as e:
        print(f"error: {e}")

def eksekusi6(query, value):
    try: 
        with mypool.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, value)
            conn.commit()
            print("success...!")
    except Error as db_error:
        print(f"db_error: {db_error}")
    except Exception as e:
        print(f"error: {e}")

def eksekusi7(query, value):
    try: 
        with mypool.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.executemany(query, value)
            conn.commit()
            print("success...!")
    except Error as db_error:
        print(f"db_error: {db_error}")
    except Exception as e:
        print(f"error: {e}")

def eksekusi8():
    pass

def eksekusi9():
    pass

daftar = {
    "eksekusi1": eksekusi1,
    "eksekusi2": eksekusi2,
    "eksekusi3": eksekusi3,
    "eksekusi4": eksekusi4,
    "eksekusi5": eksekusi5,
    "eksekusi6": eksekusi6,
    "eksekusi7": eksekusi7,
    "eksekusi8": eksekusi8,
    "eksekusi9": eksekusi9,
    }

def eksekusi(pilih, query=None, value=None):
    fungsi = daftar.get(pilih)
    if query is None and value is None:
        return fungsi()
    if value is None:
        return fungsi(query)
    return fungsi(query, value)