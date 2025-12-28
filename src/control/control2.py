from src.model.executor import eksekusi
from src.view.table import tabel

def kendali1(myeks, mytab):
    data = eksekusi(myeks)
    return tabel(mytab, data)

def kendali2():
    pass

def kendali3():
    pass

def kendali4():
    pass

def kendali5():
    pass

daftar = {
    "kendali1": kendali1,
    "kendali2": kendali2,
    "kendali3": kendali3,
    "kendali4": kendali4,
    "kendali5": kendali5,
    }

config = {
    "c1": {"myinp": "", "myque": "", "myeks": "eksekusi1", "mytab": "tabel1"},
    "c2": {"myinp": "", "myque": "", "myeks": "",          "mytab": ""},
    "c3": {"myinp": "", "myque": "", "myeks": "",          "mytab": ""},
    "c4": {"myinp": "", "myque": "", "myeks": "",          "mytab": ""},
    "c5": {"myinp": "", "myque": "", "myeks": "",          "mytab": ""},
    }

def kendali(mykend, mycon):
    fungsi = daftar.get(myken)
    konfig = config.get(mycon)

    myinp = konfig.get("myinp")
    myque = konfig.get("myque")
    myeks = konfig.get("myeks")
    mytab = konfig.get("mytab")

    if myken == "kendali1":
        return fungsi(myeks, mytab)
