def query1(myquery):
    monitoring = {
        "1": "",
        "2": "SHOW VARIABLES LIKE 'char%'",
        "3": "SHOW STATUS",
        "4": "",
        "5": "",
        }
    return monitoring.get(myquery)

def query2():
    pass

def query3():
    pass

def query4():
    pass

def query5():
    pass

daftar = {
    "query1": query1,
    "query2": query2,
    "query3": query3,
    "query4": query4,
    "query5": query5,
    }

def query(pilih, myquery):
    fungsi = daftar.get(pilih)
    return fungsi(myquery)