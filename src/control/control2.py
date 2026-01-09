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

def kendali5(myque, mynum, myeks):
    data1 = query(myque, mynum)
    data2 = eksekusi(myeks, data1)

def kendali6(myinp):
    inputs(myinp)
    print("success...!")

def kendali7(myinp, myque, mynum, myeks):
    nm_tabel, kolom, place, values = inputs(myinp)
    data1 = nm_tabel, kolom, place
    data2 = query(myque, mynum, data1)
    eksekusi(myeks, data2, values)

def kendali8(myinp, myque, mynum, myeks):
    nm_tabel, wheree, no_id = inputs(myinp)
    data1 = nm_tabel, wheree
    data2 = query(myque, mynum, data1)
    eksekusi(myeks, data2, no_id)

def kendali9(myinp):
    inputs(myinp)

daftar = {
    "kendali1": kendali1,
    "kendali2": kendali2,
    "kendali3": kendali3,
    "kendali4": kendali4,
    "kendali5": kendali5,
    "kendali6": kendali6,
    "kendali7": kendali7,
    "kendali8": kendali8,
    "kendali9": kendali9,
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
    "c1" : {"myinp": "",  "myque": "query3", "mynum": "1",  "myeks": "eksekusi2", "mytab": "tabel7"},
    "c2" : {"myinp": "2", "myque": "query3", "mynum": "2",  "myeks": "eksekusi4", "mytab": ""},
    "c3" : {"myinp": "3", "myque": "query3", "mynum": "3",  "myeks": "eksekusi4", "mytab": ""},
    "c4" : {"myinp": "4", "myque": "query3", "mynum": "4",  "myeks": "eksekusi4", "mytab": ""},
    "c5" : {"myinp": "5", "myque": "query3", "mynum": "5",  "myeks": "eksekusi2", "mytab": "tabel7"},
    "c6" : {"myinp": "6", "myque": "query3", "mynum": "6",  "myeks": "eksekusi4", "mytab": ""},
    "c7" : {"myinp": "6", "myque": "query3", "mynum": "7",  "myeks": "eksekusi4", "mytab": ""},
    "c8" : {"myinp": "",  "myque": "query3", "mynum": "8",  "myeks": "eksekusi4", "mytab": ""},
    "c9" : {"myinp": "",  "myque": "query3", "mynum": "9",  "myeks": "eksekusi2", "mytab": "tabel7"},
    "c10": {"myinp": "7", "myque": "query3", "mynum": "10", "myeks": "eksekusi4", "mytab": ""},
    "c11": {"myinp": "5", "myque": "query3", "mynum": "11", "myeks": "eksekusi4", "mytab": ""},
    }

config4 = {
    "c1": {"myinp": "",   "myque": "",       "mynum": "",  "myeks": "",          "mytab": ""},
    "c2": {"myinp": "",   "myque": "query4", "mynum": "2", "myeks": "eksekusi2", "mytab": "tabel7"},
    "c3": {"myinp": "8",  "myque": "",       "mynum": "",  "myeks": "",          "mytab": ""},
    "c4": {"myinp": "9",  "myque": "query4", "mynum": "4", "myeks": "eksekusi4", "mytab": ""},
    "c5": {"myinp": "8",  "myque": "query4", "mynum": "5", "myeks": "eksekusi2", "mytab": "tabel7"},
    "c6": {"myinp": "8",  "myque": "query4", "mynum": "6", "myeks": "eksekusi2", "mytab": "tabel7"},
    "c7": {"myinp": "",   "myque": "",       "mynum": "",  "myeks": "",          "mytab": ""},
    "c8": {"myinp": "10", "myque": "query4", "mynum": "8", "myeks": "eksekusi4", "mytab": ""},
    "c9": {"myinp": "8",  "myque": "query4", "mynum": "9", "myeks": "eksekusi4", "mytab": ""},
    }

config5 = {
    "c1" : {"myinp": "",   "myque": "",       "mynum": "",   "myeks": "",          "mytab": ""},
    "c2" : {"myinp": "",   "myque": "",       "mynum": "",   "myeks": "",          "mytab": ""},
    "c3" : {"myinp": "",   "myque": "",       "mynum": "",   "myeks": "",          "mytab": ""},
    "c4" : {"myinp": "11", "myque": "query5", "mynum": "4",  "myeks": "eksekusi6", "mytab": ""},
    "c5" : {"myinp": "11", "myque": "query5", "mynum": "4",  "myeks": "eksekusi7", "mytab": ""},
    "c6" : {"myinp": "8",  "myque": "query5", "mynum": "6",  "myeks": "eksekusi2", "mytab": "tabel7"},
    "c7" : {"myinp": "12", "myque": "query5", "mynum": "7",  "myeks": "eksekusi6", "mytab": ""},
    "c8" : {"myinp": "13", "myque": "query5", "mynum": "8",  "myeks": "eksekusi6", "mytab": ""},
    "c9" : {"myinp": "8",  "myque": "query5", "mynum": "9",  "myeks": "eksekusi4", "mytab": ""},
    "c10": {"myinp": "8",  "myque": "query5", "mynum": "10", "myeks": "eksekusi8", "mytab": ""},
    }

config6 = {
    "c1"  : {"myinp": "15", "myque": "",       "mynum": "",   "myeks": "",          "mytab": ""},
    "c2"  : {"myinp": "14", "myque": "query6", "mynum": "2",  "myeks": "eksekusi4", "mytab": ""},
    "c3"  : {"myinp": "16", "myque": "query6", "mynum": "3",  "myeks": "eksekusi4", "mytab": ""},
    "c4"  : {"myinp": "14", "myque": "query6", "mynum": "4",  "myeks": "eksekusi4", "mytab": ""},
    "c5"  : {"myinp": "17", "myque": "query6", "mynum": "5",  "myeks": "eksekusi4", "mytab": ""},
    "c6"  : {"myinp": "18", "myque": "query6", "mynum": "6",  "myeks": "eksekusi4", "mytab": ""},
    "c7"  : {"myinp": "19", "myque": "query6", "mynum": "7",  "myeks": "eksekusi4", "mytab": ""},
    "c8"  : {"myinp": "20", "myque": "query6", "mynum": "8",  "myeks": "eksekusi4", "mytab": ""},
    "c9"  : {"myinp": "21", "myque": "query6", "mynum": "9",  "myeks": "eksekusi4", "mytab": ""},
    "c10" : {"myinp": "21", "myque": "query6", "mynum": "10", "myeks": "eksekusi4", "mytab": ""},
    "c11" : {"myinp": "22", "myque": "query6", "mynum": "11", "myeks": "eksekusi4", "mytab": ""},
    }

config7 = {
    "c1"  : {"myinp": "",   "myque": "",       "mynum": "",   "myeks": "",          "mytab": ""},
    "c2"  : {"myinp": "23", "myque": "query7", "mynum": "2",  "myeks": "eksekusi4", "mytab": ""},
    "c3"  : {"myinp": "24", "myque": "query7", "mynum": "3",  "myeks": "eksekusi4", "mytab": ""},
    "c4"  : {"myinp": "25", "myque": "query7", "mynum": "4",  "myeks": "eksekusi4", "mytab": ""},
    "c5"  : {"myinp": "26", "myque": "query7", "mynum": "5",  "myeks": "eksekusi4", "mytab": ""},
    "c6"  : {"myinp": "27", "myque": "query7", "mynum": "6",  "myeks": "eksekusi4", "mytab": ""},
    "c7"  : {"myinp": "28", "myque": "query7", "mynum": "7",  "myeks": "eksekusi4", "mytab": ""},
    "c8"  : {"myinp": "29", "myque": "query7", "mynum": "8",  "myeks": "eksekusi4", "mytab": ""},
    "c9"  : {"myinp": "30", "myque": "query7", "mynum": "9",  "myeks": "eksekusi4", "mytab": ""},
    "c10" : {"myinp": "31", "myque": "query7", "mynum": "10", "myeks": "eksekusi4", "mytab": ""},
    "c11" : {"myinp": "32", "myque": "query7", "mynum": "11", "myeks": "eksekusi4", "mytab": ""},
    "c12" : {"myinp": "33", "myque": "query7", "mynum": "12", "myeks": "eksekusi4", "mytab": ""},
    "c13" : {"myinp": "34", "myque": "query7", "mynum": "13", "myeks": "eksekusi4", "mytab": ""},
    "c14" : {"myinp": "35", "myque": "query7", "mynum": "14", "myeks": "eksekusi4", "mytab": ""},
    "c15" : {"myinp": "36", "myque": "query7", "mynum": "15", "myeks": "eksekusi4", "mytab": ""},
    }

config8 = {
    "c1"  : {"myinp": "37", "myque": "query8", "mynum": "1", "myeks": "eksekusi4", "mytab": ""},
    "c2"  : {"myinp": "38", "myque": "query8", "mynum": "2", "myeks": "eksekusi4", "mytab": ""},
    "c3"  : {"myinp": "39", "myque": "query8", "mynum": "3", "myeks": "eksekusi4", "mytab": ""},
    "c4"  : {"myinp": "40", "myque": "query8", "mynum": "4", "myeks": "eksekusi4", "mytab": ""},
    "c5"  : {"myinp": "41", "myque": "query8", "mynum": "5", "myeks": "eksekusi4", "mytab": ""},
    "c6"  : {"myinp": "42", "myque": "query8", "mynum": "6", "myeks": "eksekusi4", "mytab": ""},
    "c7"  : {"myinp": "43", "myque": "query8", "mynum": "7", "myeks": "eksekusi4", "mytab": ""},
    "c8"  : {"myinp": "43", "myque": "query8", "mynum": "8", "myeks": "eksekusi4", "mytab": ""},
    }

config9 = {
    "c1" : {"myinp": "", "myque": "", "mynum": "", "myeks": "", "mytab": ""},
    }

config = {
    "config1": config1,
    "config2": config2,
    "config3": config3,
    "config4": config4,
    "config5": config5,
    "config6": config6,
    "config7": config7,
    "config8": config8,
    "config9": config9,
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
    if myken == "kendali5":
        return fungsi(myque, mynum, myeks)
    if myken == "kendali6":
        return fungsi(myinp)
    if myken == "kendali7":
        return fungsi(myinp, myque, mynum, myeks)
    if myken == "kendali8":
        return fungsi(myinp, myque, mynum, myeks)
    if myken == "kendali9":
        return fungsi(myinp)
