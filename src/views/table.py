def tabel0(data):
    print(data)

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

def tabel2(data):
    pass

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