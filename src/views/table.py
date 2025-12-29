def tabel0(data):
    print(data)
    print(type(data))

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

# satu sampai n kolom satu baris
def tabel3(data):
    # Mengonversi semua elemen ke string dan menghitung lebar tiap kolom
    padding = 2
    lebar_kolom = [len(str(item)) + padding for item in data]
    
    # 1. Membuat garis atas
    # Bagian tengah menggunakan '┬' sebagai penyambung antar kolom
    isi_atas = "┬".join(["─" * lebar for lebar in lebar_kolom])
    garis_atas = f"┌{isi_atas}┐"
    
    # 2. Membuat baris data
    # Menggabungkan elemen dengan separator ' │ '
    isi_tengah = " │ ".join([str(item) for item in data])
    garis_tengah = f"│ {isi_tengah} │"
    
    # 3. Membuat garis bawah
    # Bagian tengah menggunakan '┴' sebagai penyambung antar kolom
    isi_bawah = "┴".join(["─" * lebar for lebar in lebar_kolom])
    garis_bawah = f"└{isi_bawah}┘"
    
    print()
    print(garis_atas)
    print(garis_tengah)
    print(garis_bawah)
    print()

# satu kolom dua baris
def tabel4(data):
    pass

# dua kolom dua baris
def tabel5(data):
    pass

# satu sampai n kolom dan satu sampai n baris
def tabel6(data):
    pass

daftar = {
    "tabel0": tabel0,
    "tabel1": tabel1,
    "tabel2": tabel2,
    "tabel3": tabel3,
    "tabel4": tabel4,
    "tabel5": tabel5,
    "tabel6": tabel6,
    }

def tabel(pilih, data):
    fungsi = daftar.get(pilih)
    return fungsi(data)