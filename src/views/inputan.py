from src.config.my_config import ubah_db

def input1():
    print("silahkan masukan nama database:")
    nm_dbase = input("nama database: ").strip()
    ubah_db(nm_dbase)
    return nm_dbase

def input2():
    print("masukkan data user baru.")
    nama_user = input("nama user : ").strip()
    host_user = input("host user : ").strip()
    password  = input("password  : ").strip()
    return nama_user, host_user, password

def input3():
    print("masukkan data user lama.")
    nama_userr = input("nama user : ").strip()
    host_userr = input("host user : ").strip()
    print("masukkan data user baru.")
    nama_user  = input("nama user : ").strip()
    host_user  = input("host user : ").strip()
    return nama_userr, host_userr, nama_user, host_user

def input4():
    print("masukkan data user lama.")
    nama_user = input("nama user : ").strip()
    host_user = input("host user : ").strip()
    print("masukkan password baru.")
    password  = input("password  : ").strip()
    return nama_user, host_user, password

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
