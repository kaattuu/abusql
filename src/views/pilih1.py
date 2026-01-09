from src.control.kakas1 import clear_view
from .menu1 import daftar_menu
from src.control.control2 import kendali

def pilih_utama():
    daftar_menu("utama")
    while True:
        pilihan = input("")
        match pilihan:
            case "1" : return menu_pilihan("user")
            case "2" : return menu_pilihan("database")
            case "3" : return menu_pilihan("tabel")
            case "4" : return menu_pilihan("data")
            case "5" : return menu_pilihan("monitoring")
            case ""  : return menu_pilihan("utama")
            case "0" : break
            case _   : print(f"nomor pilihanmu '{pilihan}'. tidak cocok...!")

def pilih_user():
    daftar_menu("user")
    while True:
        pilihan = input("")
        match pilihan:
            case "1"  : kendali("kendali2", "config3", "c1")
            case "2"  : kendali("kendali3", "config3", "c2")
            case "3"  : kendali("kendali3", "config3", "c3")
            case "4"  : kendali("kendali3", "config3", "c4")
            case "5"  : kendali("kendali4", "config3", "c5")
            case "6"  : kendali("kendali3", "config3", "c6")
            case "7"  : kendali("kendali3", "config3", "c7")
            case "8"  : kendali("kendali5", "config3", "c8")
            case "9"  : kendali("kendali2", "config3", "c9")
            case "10" : kendali("kendali3", "config3", "c10")
            case "11" : kendali("kendali3", "config3", "c11")
            case ""   : return menu_pilihan("user")
            case "0"  : break
            case "00" : return menu_pilihan("utama")
            case _    : print(f"nomor pilihanmu '{pilihan}'. tidak cocok...!")

def pilih_database():
    daftar_menu("database")
    while True:
        pilihan = input("")
        match pilihan:
            case "1"  : kendali("kendali2", "config2", "c1")
            case "2"  : kendali("kendali3", "config2", "c2")
            case "3"  : kendali("kendali3", "config2", "c3")
            case "4"  : kendali("kendali3", "config2", "c4")
            case ""   : return menu_pilihan("database")
            case "0"  : break
            case "00" : return menu_pilihan("utama")
            case _    : print(f"nomor pilihanmu '{pilihan}'. tidak cocok...!")

def pilih_tabel():
    daftar_menu("tabel")
    while True:
        pilihan = input("")
        match pilihan:
            case "1"  : kendali("kendali3", "config2", "c3")
            case "2"  : kendali("kendali2", "config4", "c2")
            case "3"  : kendali("kendali6", "config4", "c3")
            case "4"  : kendali("kendali3", "config4", "c4")
            case "5"  : kendali("kendali4", "config4", "c5")
            case "6"  : kendali("kendali4", "config4", "c6")
            case "7"  : return menu_pilihan("struktur")
            case "8"  : kendali("kendali3", "config4", "c8")
            case "9"  : kendali("kendali3", "config4", "c9")
            case ""   : return menu_pilihan("tabel")
            case "0"  : break
            case "00" : return menu_pilihan("utama")
            case _    : print(f"nomor pilihanmu '{pilihan}'. tidak cocok...!")

def pilih_data():
    daftar_menu("data")
    while True:
        pilihan = input("")
        match pilihan:
            case "1"  : kendali("kendali3", "config2", "c3")
            case "2"  : kendali("kendali2", "config4", "c2")
            case "3"  : kendali("kendali6", "config4", "c3")
            case "4"  : kendali("kendali7", "config5", "c4")
            case "5"  : kendali("kendali7", "config5", "c5")
            case "6"  : kendali("kendali4", "config5", "c6")
            case "7"  : kendali("kendali7", "config5", "c7")
            case "8"  : kendali("kendali8", "config5", "c8")
            case "9"  : kendali("kendali3", "config5", "c9")
            case "10" : kendali("kendali3", "config5", "c10")
            case ""   : return menu_pilihan("data")
            case "0"  : break
            case "00" : return menu_pilihan("utama")
            case _    : print(f"nomor pilihanmu '{pilihan}'. tidak cocok...!")

def pilih_monitoring():
    daftar_menu("monitoring")
    while True:
        pilihan = input("")
        match pilihan:
            case "1"  : kendali("kendali1", "config1", "c1")
            case "2"  : kendali("kendali2", "config1", "c2")
            case "3"  : kendali("kendali2", "config1", "c3")
            case "4"  : kendali("kendali2", "config1", "c4")
            case "5"  : kendali("kendali2", "config1", "c5")
            case ""   : return menu_pilihan("monitoring")
            case "0"  : break
            case "00" : return menu_pilihan("utama")
            case _    : print(f"nomor pilihanmu '{pilihan}'. tidak cocok...!")

def pilih_struktur():
    daftar_menu("struktur")
    while True:
        pilihan = input("")
        match pilihan:
            case "1"  : return menu_pilihan("kolom")
            case "2"  : return menu_pilihan("constraint")
            case "3"  : return menu_pilihan("properti")
            case "4"  : return menu_pilihan("partisi")
            case ""   : return menu_pilihan("struktur")
            case "0"  : break
            case "00" : return menu_pilihan("tabel")
            case _    : print(f"nomor pilihanmu '{pilihan}'. tidak cocok...!")

def pilih_kolom():
    daftar_menu("kolom")
    while True:
        pilihan = input("")
        match pilihan:
            case "1"  : kendali("kendali9", "config6", "c1")
            case "2"  : kendali("kendali3", "config6", "c2")
            case "3"  : kendali("kendali3", "config6", "c3")
            case "4"  : kendali("kendali3", "config6", "c4")
            case "5"  : kendali("kendali3", "config6", "c5")
            case "6"  : kendali("kendali3", "config6", "c6")
            case "7"  : kendali("kendali3", "config6", "c7")
            case "8"  : kendali("kendali3", "config6", "c8")
            case "9"  : kendali("kendali3", "config6", "c9")
            case "10" : kendali("kendali3", "config6", "c10")
            case "11" : kendali("kendali3", "config6", "c11")
            case ""   : return menu_pilihan("kolom")
            case "0"  : break
            case "00" : return menu_pilihan("struktur")
            case _    : print(f"nomor pilihanmu '{pilihan}'. tidak cocok...!")

def pilih_constraint():
    daftar_menu("constraint")
    while True:
        pilihan = input("")
        match pilihan:
            case "1"  : kendali("kendali9", "config6", "c1")
            case "2"  : kendali("kendali3", "config7", "c2")
            case "3"  : kendali("kendali3", "config7", "c3")
            case "4"  : kendali("kendali3", "config7", "c4")
            case "5"  : kendali("kendali3", "config7", "c5")
            case "6"  : kendali("kendali3", "config7", "c6")
            case "7"  : kendali("kendali3", "config7", "c7")
            case "8"  : kendali("kendali3", "config7", "c8")
            case "9"  : kendali("kendali3", "config7", "c9")
            case "10" : kendali("kendali3", "config7", "c10")
            case "11" : kendali("kendali3", "config7", "c11")
            case "12" : kendali("kendali3", "config7", "c12")
            case "13" : kendali("kendali3", "config7", "c13")
            case "14" : kendali("kendali3", "config7", "c14")
            case "15" : kendali("kendali3", "config7", "c15")
            case ""   : return menu_pilihan("constraint")
            case "0"  : break
            case "00" : return menu_pilihan("struktur")
            case _    : print(f"nomor pilihanmu '{pilihan}'. tidak cocok...!")

def pilih_properti():
    daftar_menu("properti")
    while True:
        pilihan = input("")
        match pilihan:
            case "1"  : kendali("kendali3", "config8", "c1")
            case "2"  : kendali("kendali3", "config8", "c2")
            case "3"  : kendali("kendali3", "config8", "c3")
            case "4"  : kendali("kendali3", "config8", "c4")
            case "5"  : kendali("kendali3", "config8", "c5")
            case "6"  : kendali("kendali3", "config8", "c6")
            case "7"  : kendali("kendali3", "config8", "c7")
            case "8"  : kendali("kendali3", "config8", "c8")
            case ""   : return menu_pilihan("properti")
            case "0"  : break
            case "00" : return menu_pilihan("struktur")
            case _    : print(f"nomor pilihanmu '{pilihan}'. tidak cocok...!")

def pilih_partisi():
    daftar_menu("partisi")
    while True:
        pilihan = input("")
        match pilihan:
            case "1"  : kendali("kendali3", "config9", "c1")
            case "2"  : kendali("kendali3", "config9", "c2")
            case "3"  : print(f"kamu memilih nomor '{pilihan}'. terimakasih!")
            case "4"  : print(f"kamu memilih nomor '{pilihan}'. terimakasih!")
            case "5"  : print(f"kamu memilih nomor '{pilihan}'. terimakasih!")
            case ""   : return menu_pilihan("partisi")
            case "0"  : break
            case "00" : return menu_pilihan("struktur")
            case _    : print(f"nomor pilihanmu '{pilihan}'. tidak cocok...!")

data_dict = {
    "utama"     : pilih_utama,
    "user"      : pilih_user,
    "database"  : pilih_database,
    "tabel"     : pilih_tabel,
    "data"      : pilih_data,
    "monitoring": pilih_monitoring,
    "struktur"  : pilih_struktur,
    "kolom"     : pilih_kolom,
    "constraint": pilih_constraint,
    "properti"  : pilih_properti,
    "partisi"   : pilih_partisi
    }

def menu_pilihan(nama_menu):
    clear_view()
    fungsi = data_dict.get(nama_menu)
    return fungsi()