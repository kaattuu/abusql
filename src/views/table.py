def tabel0(data):
    print(data)

# satu kolom satu baris
def tabel1(data): 
    jumlah_elemen = len(data)
    jumlah_huruf  = [len(i) for i in data]
    padding       = 2
    garis_atas    = f"┌{"─" * (max(jumlah_huruf) + padding)}┐"
    garis_bawah   = f"└{"─" * (max(jumlah_huruf) + padding)}┘"
    print()
    print(garis_atas)
    hasil = ""
    for i in data:
        hasil += f"│ {i} │"
    print(hasil)
    print(garis_bawah)
    print()

# dua kolom satu baris
def tabel2(data): 
    # data diharapkan berupa tuple/list dengan 2 elemen, misal: ("Nama", "Hobi")
    padding = 2
    
    # Menghitung lebar masing-masing kolom berdasarkan panjang string elemennya
    lebar_kolom1 = len(str(data[0])) + padding
    lebar_kolom2 = len(str(data[1])) + padding
    
    # Membuat garis pembatas
    garis_atas   = f"┌{'─' * lebar_kolom1}┬{'─' * lebar_kolom2}┐"
    garis_tengah = f"│ {data[0]} │ {data[1]} │"
    garis_bawah  = f"└{'─' * lebar_kolom1}┴{'─' * lebar_kolom2}┘"
    
    print()
    print(garis_atas)
    print(garis_tengah)
    print(garis_bawah)
    print()


def tabel3(data):
    pass

def tabel4(data):
    pass

def tabel5(data):
    pass

daftar = {
    "tabel0": tabel0,
    "tabel1": tabel1,
    "tabel2": tabel2,
    "tabel3": tabel3,
    "tabel4": tabel4,
    "tabel5": tabel5,
    }

def tabel(pilih, data):
    fungsi = daftar.get(pilih)
    return fungsi(data)