from src.model.sql import query
from src.model.executor import eksekusi
from src.views.table import tabel
from src.views.inputan import inputs

def kendali1(myeks, mytab):
    data = eksekusi(myeks)
    return tabel(mytab, data)

def kendali2(myque, mynum, myeks, mytab):
    data1 = query(myque, mynum)
    data2 = eksekusi(myeks, data1)
    return tabel(mytab, data2)

def kendali3(myinp, myque, mynum, myeks):
    data1 = inputs(myinp)
    data2 = query(myque, mynum, data1)
    eksekusi(myeks, data2)

def kendali4(myinp, myque, mynum, myeks, mytab):
    data1 = inputs(myinp)
    data2 = query(myque, mynum, data1)
    data3 = eksekusi(myeks, data2)
    return tabel(mytab, data3)

def kendali5():
    pass

daftar = {
    "kendali1": kendali1,
    "kendali2": kendali2,
    "kendali3": kendali3,
    "kendali4": kendali4,
    "kendali5": kendali5,
    }

config1 = {
    # monitoring
    "c1": {"myinp": "", "myque": "",       "mynum": "",  "myeks": "eksekusi1", "mytab": "tabel6"},
    "c2": {"myinp": "", "myque": "query1", "mynum": "2", "myeks": "eksekusi2", "mytab": "tabel7"},
    "c3": {"myinp": "", "myque": "query1", "mynum": "3", "myeks": "eksekusi2", "mytab": "tabel7"},
    "c4": {"myinp": "", "myque": "query1", "mynum": "4", "myeks": "eksekusi2", "mytab": "tabel7"},
    "c5": {"myinp": "", "myque": "query1", "mynum": "5", "myeks": "eksekusi3", "mytab": "tabel7"},
    }

config2 = {
    # database
    "c1": {"myinp": "",  "myque": "query2", "mynum": "1", "myeks": "eksekusi2", "mytab": "tabel7"},
    "c2": {"myinp": "1", "myque": "query2", "mynum": "2", "myeks": "eksekusi4", "mytab": ""},
    "c3": {"myinp": "1", "myque": "query2", "mynum": "3", "myeks": "eksekusi4", "mytab": ""},
    "c4": {"myinp": "1", "myque": "query2", "mynum": "4", "myeks": "eksekusi4", "mytab": ""},
    }

config3 = {
    "c1": {"myinp": "",  "myque": "query3", "mynum": "1", "myeks": "eksekusi2", "mytab": "tabel7"},
    "c2": {"myinp": "2", "myque": "query3", "mynum": "2", "myeks": "eksekusi4", "mytab": ""},
    "c3": {"myinp": "3", "myque": "query3", "mynum": "3", "myeks": "eksekusi4", "mytab": ""},
    "c4": {"myinp": "4", "myque": "query3", "mynum": "4", "myeks": "eksekusi4", "mytab": ""},
    "c5": {"myinp": "5", "myque": "query3", "mynum": "5", "myeks": "eksekusi2", "mytab": "tabel7"},
    "c6": {"myinp": "6", "myque": "query3", "mynum": "6", "myeks": "eksekusi4", "mytab": ""},
    "c7": {"myinp": "6", "myque": "query3", "mynum": "7", "myeks": "eksekusi4", "mytab": ""},
    }

config = {
    "config1": config1,
    "config2": config2,
    "config3": config3,
    }

def kendali(myken, myconf, mycon):
    fungsi = daftar.get(myken)
    sett   = config.get(myconf)
    konfig = sett.get(mycon)

    myinp = konfig.get("myinp")
    myque = konfig.get("myque")
    mynum = konfig.get("mynum")
    myeks = konfig.get("myeks")
    mytab = konfig.get("mytab")

    if myken == "kendali1":
        return fungsi(myeks, mytab)
    if myken == "kendali2":
        return fungsi(myque, mynum, myeks, mytab)
    if myken == "kendali3":
        return fungsi(myinp, myque, mynum, myeks)
    if myken == "kendali4":
        return fungsi(myinp, myque, mynum, myeks, mytab)
