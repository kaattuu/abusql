from src.config.my_config import my_global

def input1():
    print("silahkan masukan nama database:")
    nm_dbase = input("nama database: ").strip()
    return my_global("ubah_db", nm_dbase)

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
    print("masukkan data user.")
    nama_user = input("nama user : ").strip()
    host_user = input("host user : ").strip()
    return nama_user, host_user

def input6():
    print("silahkan pilih database.")
    nama_db   = input("nama database : ").strip()
    print("silahkan pilih user")
    nama_user = input("nama user     : ").strip()
    host_user = input("host user     : ").strip()
    return nama_db, nama_user, host_user

def input7():
    print("masukan id user")
    id_user = input("id user : ").strip()
    return id_user,

def input8():
    print("silahkan pilih nama tabel")
    nm_tabel = input("nama tabel : ").strip()
    if nm_tabel == "":
        return my_global("mytb"),
    return my_global("ubah_tb", nm_tabel),

def input9():
    print("silahkan masukkan nama tabel")
    nm_tabel = input("nama tabel : ").strip()
    struktur = input("struktur   : ").strip()
    return my_global("ubah_tb", nm_tabel), struktur

def input10():
    print("silahkan pilih tabel yang mau diubah")
    nama_tabel = input("nama tabel : ").strip()
    if nama_tabel == "":
        nama_tabel = my_global("mytb")
    print("silahkan masukkan nama baru")
    tabel_baru = input("nama tabel : ").strip()
    if tabel_baru == "":
        tabel_baru = my_global("mytb")
    return nama_tabel, my_global("ubah_tb", tabel_baru)

def input11():
    pass

def input12():
    pass

def input13():
    pass

def input14():
    pass

def input15():
    pass

daftar = {
    "1" : input1,
    "2" : input2,
    "3" : input3,
    "4" : input4,
    "5" : input5,
    "6" : input6,
    "7" : input7,
    "8" : input8,
    "9" : input9,
    "10": input10,
    "11": input11,
    "12": input12,
    "13": input13,
    "14": input14,
    "15": input15,
    }

def inputs(pilih):
    fungsi = daftar.get(pilih)
    return fungsi()
