from src.model.sql import query
from src.model.executor import eksekusi
from src.views.table import tabel

def kendali1(myeks, mytab):
    data = eksekusi(myeks)
    return tabel(mytab, data)

def kendali2(myque, mynum, myeks, mytab):
    data1 = query(myque, mynum)
    data2 = eksekusi(myeks, data1)
    return tabel(mytab, data2)

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
    # monitoring
    "c1": {"myinp": "", "myque": "",       "mynum": "",  "myeks": "eksekusi1", "mytab": "tabel6"},
    "c2": {"myinp": "", "myque": "query1", "mynum": "2", "myeks": "eksekusi2", "mytab": "tabel7"},
    "c3": {"myinp": "", "myque": "",       "mynum": "",  "myeks": "",          "mytab": ""},
    "c4": {"myinp": "", "myque": "",       "mynum": "",  "myeks": "",          "mytab": ""},
    "c5": {"myinp": "", "myque": "",       "mynum": "",  "myeks": "",          "mytab": ""},
    }

def kendali(myken, mycon):
    fungsi = daftar.get(myken)
    konfig = config.get(mycon)

    myinp = konfig.get("myinp")
    myque = konfig.get("myque")
    mynum = konfig.get("mynum")
    myeks = konfig.get("myeks")
    mytab = konfig.get("mytab")

    if myken == "kendali1":
        return fungsi(myeks, mytab)
    if myken == "kendali2":
        return fungsi(myque, mynum, myeks, mytab)
