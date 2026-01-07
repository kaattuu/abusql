import ast
from src.model.sql import query
from src.model.executor import eksekusi
from src.views.table import tabel

def logika1(data):
    data1  = query("query5", "6", data)
    kolom1 = eksekusi("eksekusi5", data1)
    kolom2 = eksekusi("eksekusi2", data1)
    colom  = ", ".join(kolom1)
    place  = ", ".join(["%s"] * len(kolom1))
    tabel("tabel7", kolom2)
    return colom, place

def logika2(data):
    value = ast.literal_eval(data)      # konversi string ke tuple menggunakan modul ast - abstrak syntax tree
    return value

def logika3(data):
    data1  = query("query5", "6", data)
    kolom1 = eksekusi("eksekusi5", data1)
    kolom2 = eksekusi("eksekusi2", data1)
    seeet  = [f"{i} = %s" for i in kolom1 if i != "id"]
    where  = [f"{i} = %s" for i in kolom1 if i == "id"]
    tabel("tabel7", kolom2)
    return ", ".join(seeet), "".join(where)

def logika4(data):
    value = data[1:] + data[0:1]
    return value

def logika5(data):
    data1  = query("query5", "6", data)
    kolom1 = eksekusi("eksekusi5", data1)
    kolom2 = eksekusi("eksekusi2", data1)
    wheree = kolom1[0] + "= %s"
    tabel("tabel7", kolom2)
    return wheree

def logika6(data):
    data1    = query("query5", "6", data)
    data2    = query("query4", "5", data)
    kolom    = eksekusi("eksekusi5", data1)
    struktur = eksekusi("eksekusi2", data2)
    tabel("tabel7", struktur)
    tabel("tabel3", kolom)

def logika7(data):
    data1 = [f"ADD COLUMN {i}" for i in data]
    data2 = ", ".join(data1)
    return data2

def logika8():
    pass

def logika9():
    pass

daftar = {
    "1": logika1,
    "2": logika2,
    "3": logika3,
    "4": logika4,
    "5": logika5,
    "6": logika6,
    "7": logika7,
    "8": logika8,
    "9": logika9,
    }

def logika(pilih, data):
    fungsi = daftar.get(pilih)
    return fungsi(data)