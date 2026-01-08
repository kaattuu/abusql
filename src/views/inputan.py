from src.config.my_config import my_global
from src.service.inplogic import logika

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
    nm_tabel = input("nama tabel: ").strip()
    if nm_tabel == "":
        nm_tabel = my_global("mytb")
    my_tabel = nm_tabel,
    kolom, place = logika("1", my_tabel)
    print("silahkan masukkan data, pakai koma pemisah antar kolom.")
    valuee = input("").strip()
    values = logika("2", valuee)
    my_global("ubah_tb", nm_tabel)
    return nm_tabel, kolom, place, values

def input12():
    nm_tabel = input("nama tabel: ").strip()
    if nm_tabel == "":
        nm_tabel = my_global("mytb")
    my_tabel = nm_tabel,
    seeet, where = logika("3", my_tabel)
    print("silahkan masukkan data, pakai koma pemisah antar kolom.")
    valuee = input("").strip()
    values = logika("2", valuee)
    value  = logika("4", values)
    my_global("ubah_tb", nm_tabel)
    return nm_tabel, seeet, where, value

def input13():
    nm_tabel = input("nama tabel: ").strip()
    if nm_tabel == "":
        nm_tabel = my_global("mytb")
    my_tabel = nm_tabel,
    wheree = logika("5", my_tabel)
    print("silahkan masukan id data yang mau di hapus.")
    no_id = input("nomor_id: ").strip()
    no_id = no_id,
    my_global("ubah_tb", nm_tabel)
    return nm_tabel, wheree, no_id

def input14():
    nm_tabel = input("nama tabel: ").strip()
    if nm_tabel == "":
        nm_tabel = my_global("mytb")
    my_tabel = nm_tabel,
    logika("6", my_tabel)
    print("masukkan struktur kolom tambahan")
    struktur = input("").strip()
    my_global("ubah_tb", nm_tabel)
    return nm_tabel, struktur

def input15():
    print("silahkan pilih nama tabel")
    nm_tabel = input("nama tabel: ").strip()
    if nm_tabel == "":
        nm_tabel = my_global("mytb")
    my_tabel = nm_tabel,
    logika("6", my_tabel)
    my_global("ubah_tb", nm_tabel)

def input16():
    print("silahkan pilih nama tabel")
    nm_tabel = input("nama tabel: ").strip()
    if nm_tabel == "":
        nm_tabel = my_global("mytb")
    my_tabel = nm_tabel,
    logika("6", my_tabel)
    print("masukkan struktur kolom tambahan")
    struktur1 = input("").strip()
    struktur2 = logika("2", struktur1)
    struktur  = logika("7", struktur2)
    my_global("ubah_tb", nm_tabel)
    return nm_tabel, struktur

def input17():
    nm_tabel = input("nama tabel: ").strip()
    if nm_tabel == "":
        nm_tabel = my_global("mytb")
    my_tabel = nm_tabel,
    logika("6", my_tabel)
    print("masukkan struktur kolom tambahan   :")
    struktur = input("").strip()
    print("silahkan pilih kolom after/setelah :")
    setelah  = input("").strip()
    my_global("ubah_tb", nm_tabel)
    return nm_tabel, struktur, setelah

def input18():
    nm_tabel = input("nama tabel: ").strip()
    if nm_tabel == "":
        nm_tabel = my_global("mytb")
    my_tabel = nm_tabel,
    logika("6", my_tabel)
    print("silahkan pilih kolom yang akan diubah :")
    nm_lama  = input("").strip()
    print("masukkan struktur dan type kolom baru :")
    struktur = input("").strip()
    my_global("ubah_tb", nm_tabel)
    return nm_tabel, nm_lama, struktur

def input19():
    nm_tabel = input("nama tabel: ").strip()
    if nm_tabel == "":
        nm_tabel = my_global("mytb")
    my_tabel = nm_tabel,
    logika("6", my_tabel)
    print("silahkan pilih kolom lengkapi dengan type data yang baru : ")
    struktur = input("").strip()
    my_global("ubah_tb", nm_tabel)
    return nm_tabel, struktur

def input20():
    nm_tabel = input("nama tabel: ").strip()
    if nm_tabel == "":
        nm_tabel = my_global("mytb")
    my_tabel = nm_tabel,
    logika("6", my_tabel)
    print("silahkan pilih kolom lengkapi dengan type datanya : ")
    struktur = input("").strip()
    print("silahkan pilih kolom after/setelah :")
    setelah  = input("").strip()
    my_global("ubah_tb", nm_tabel)
    return nm_tabel, struktur, setelah

def input21():
    nm_tabel = input("nama tabel: ").strip()
    if nm_tabel == "":
        nm_tabel = my_global("mytb")
    my_tabel = nm_tabel,
    logika("6", my_tabel)
    print("silahkan pilih kolom lengkapi dengan type datanya : ")
    struktur = input("").strip()
    my_global("ubah_tb", nm_tabel)
    return nm_tabel, struktur

def input22():
    nm_tabel = input("nama tabel: ").strip()
    if nm_tabel == "":
        nm_tabel = my_global("mytb")
    my_tabel = nm_tabel,
    logika("6", my_tabel)
    print("silahkan pilih kolom yang akan dihapus : ")
    struktur = input("").strip()
    my_global("ubah_tb", nm_tabel)
    return nm_tabel, struktur

def input23():
    nm_tabel = input("nama tabel: ").strip()
    if nm_tabel == "":
        nm_tabel = my_global("mytb")
    my_tabel = nm_tabel,
    logika("6", my_tabel)
    print("silahkan pilih kolom sebagai primary key : ")
    nm_kolom = input("").strip()
    my_global("ubah_tb", nm_tabel)
    return nm_tabel, nm_kolom

def input24():
    nm_tabel = input("nama tabel: ").strip()
    if nm_tabel == "":
        nm_tabel = my_global("mytb")
    my_tabel = nm_tabel,
    logika("6", my_tabel)
    print("silahkan masukan nama tabel ")
    nm_tabel = input("nama tabel: ").strip()
    if nm_tabel == "":
        nm_tabel = my_global("mytb")
    my_global("ubah_tb", nm_tabel)
    return nm_tabel,

def input25():
    nm_tabel = input("nama tabel: ").strip()
    if nm_tabel == "":
        nm_tabel = my_global("mytb")
    my_tabel = nm_tabel,
    logika("6", my_tabel)
    print("silahkan pilih kolom sebagai unique key : ")
    nm_kolom = input("").strip()
    my_global("ubah_tb", nm_tabel)
    return nm_tabel, nm_kolom

def input26():
    nm_tabel = input("nama tabel: ").strip()
    if nm_tabel == "":
        nm_tabel = my_global("mytb")
    my_tabel = nm_tabel,
    logika("6", my_tabel)
    print("silahkan pilih kolom yang akan di hapus unique key : ")
    nm_kolom = input("").strip()
    my_global("ubah_tb", nm_tabel)
    return nm_tabel, nm_kolom

def input27():
    nm_tabel = input("nama tabel: ").strip()
    if nm_tabel == "":
        nm_tabel = my_global("mytb")
    my_tabel = nm_tabel,
    logika("6", my_tabel)
    print("silahkan masukkan fk_nama constraint ")
    fk_nama   = input("fk_nama  : ").strip()
    print("silahkan pilih kolom sebagai foreign key")
    kolom_fk  = input("kolom_fk : ").strip()
    print("silahkan masukkan nama tabel tujuan")
    nm_tabel1 = input("nm_tabel : ").strip()
    nm_tabel2 = nm_tabel1,
    logika("6", nm_tabel2)
    print("silahkan pilih kolom yang menjadi referensi")
    kolom_ref = input("nm_kolom : ").strip()
    my_global("ubah_tb", nm_tabel)
    return nm_tabel, fk_nama, kolom_fk, nm_tabel1, kolom_ref

def input28():
    nm_tabel = input("nama tabel: ").strip()
    if nm_tabel == "":
        nm_tabel = my_global("mytb")
    my_tabel = nm_tabel,
    logika("6", my_tabel)
    print("silahkan pilih fk_nama constraint yang mau dihapus")
    fk_nama   = input("fk_nama  : ").strip()
    my_global("ubah_tb", nm_tabel)
    return nm_tabel, fk_nama

def input29():
    nm_tabel = input("nama tabel: ").strip()
    if nm_tabel == "":
        nm_tabel = my_global("mytb")
    my_tabel = nm_tabel,
    logika("6", my_tabel)
    print("silahkan buat dulu idx_nama ")
    idx_nama  = input("idx_nama : ").strip()
    print("silahakn pilih kolom yang akan di beri index")
    kolom_idx = input("nm_kolom : ").strip()
    my_global("ubah_tb", nm_tabel)
    return nm_tabel, idx_nama, kolom_idx

def input30():
    nm_tabel = input("nama tabel: ").strip()
    if nm_tabel == "":
        nm_tabel = my_global("mytb")
    my_tabel = nm_tabel,
    logika("6", my_tabel)
    print("silahkan pilih idx_nama yang akan di hapus ")
    idx_nama  = input("idx_nama : ").strip()
    my_global("ubah_tb", nm_tabel)
    return nm_tabel, idx_nama

def input31():
    nm_tabel = input("nama tabel: ").strip()
    if nm_tabel == "":
        nm_tabel = my_global("mytb")
    my_tabel = nm_tabel,
    logika("6", my_tabel)
    print("silahkan buat dulu chk_nama")
    chk_nama  = input("chk_nama  : ").strip()
    print("silahkan pilih kolom dan lengkapi dengan logika chk")
    kolom_chk = input("kolom_chk : ").strip()
    my_global("ubah_tb", nm_tabel)
    return nm_tabel, chk_nama, kolom_chk

def input32():
    nm_tabel = input("nama tabel: ").strip()
    if nm_tabel == "":
        nm_tabel = my_global("mytb")
    my_tabel = nm_tabel,
    logika("6", my_tabel)
    print("silahkan pilih chk_nama yang akan di hapus ")
    chk_nama  = input("chk_nama : ").strip()
    my_global("ubah_tb", nm_tabel)
    return nm_tabel, chk_nama

def input33():
    nm_tabel = input("nama tabel: ").strip()
    if nm_tabel == "":
        nm_tabel = my_global("mytb")
    my_tabel = nm_tabel,
    logika("6", my_tabel)
    print("silahkan buat dulu nama_constraint")
    nm_constraint = input("nm_constraint : ").strip()
    print("silahkan pilih dua kolom yang akan di gabung ")
    kolom1        = input("kolom1        : ").strip()
    kolom2        = input("kolom2        : ").strip()
    my_global("ubah_tb", nm_tabel)
    return nm_tabel, nm_constraint, kolom1, kolom2

def input34():
    nm_tabel = input("nama tabel: ").strip()
    if nm_tabel == "":
        nm_tabel = my_global("mytb")
    my_tabel = nm_tabel,
    logika("6", my_tabel)
    print("silahkan pilih nama_constraint yang akan di hapus ")
    nm_constraint = input("nm_constraint : ").strip()
    my_global("ubah_tb", nm_tabel)
    return nm_tabel, nm_constraint

def input35():
    nm_tabel = input("nama tabel: ").strip()
    if nm_tabel == "":
        nm_tabel = my_global("mytb")
    my_tabel = nm_tabel,
    logika("6", my_tabel)
    print("silahkan pilih nama kolom")
    nm_kolom = input("nm_kolom : ").strip()
    print("silahkan masukkan nilai default")
    default  = input("default  : ").strip()
    my_global("ubah_tb", nm_tabel)
    return nm_tabel, nm_kolom, default

def input36():
    pass

def input37():
    pass

def input38():
    pass

def input39():
    pass

def input40():
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
    "16": input16,
    "17": input17,
    "18": input18,
    "19": input19,
    "20": input20,
    "21": input21,
    "22": input22,
    "23": input23,
    "24": input24,
    "25": input25,
    "26": input26,
    "27": input27,
    "28": input28,
    "29": input29,
    "30": input30,
    "31": input31,
    "32": input32,
    "33": input33,
    "34": input34,
    "35": input35,
    "36": input36,
    "37": input37,
    "38": input38,
    "39": input39,
    "40": input40,
    }

def inputs(pilih):
    fungsi = daftar.get(pilih)
    return fungsi()
