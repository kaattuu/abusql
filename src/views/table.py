def tabel1(data):
    print(data)

def tabel2(data):
    pass

def tabel3(data):
    pass

def tabel4(data):
    pass

def tabel5(data):
    pass

daftar = {
    "tabel1": tabel1,
    "tabel2": tabel2,
    "tabel3": tabel3,
    "tabel4": tabel4,
    "tabel5": tabel5,
    }

def tabel(pilih, data):
    fungsi = daftar.get(pilih)
    return fungsi(data)