from src.config.my_config import ubah_db

def input1():
    print("silahkan masukan nama database:")
    nm_dbase = input("").strip()
    ubah_db(nm_dbase)
    return nm_dbase

def input2():
    pass

def input3():
    pass

def input4():
    pass

def input5():
    pass

daftar = {
    "1": input1,
    "2": input2,
    "3": input3,
    "4": input4,
    "5": input5,
    }

def inputs(pilih):
    fungsi = daftar.get(pilih)
    return fungsi()
