def query1():
    pass

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

def query(pilih):
    fungsi = daftar.get(pilih)
    return fungsi()