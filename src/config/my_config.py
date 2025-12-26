my_db = None
my_tb = None

mydb = lambda: my_db
mytb = lambda: my_tb

def ubah_db(data):
    global my_db
    my_db = data
    return data

def ubah_tb(data):
    global my_tb
    my_tb = data
    return data

config_dict = {
    "mydb"   : mydb,
    "mytb"   : mytb,
    "ubah_db": ubah_db,
    "ubah_tb": ubah_tb,
    }

def my_global(pilih, data=None):
    fungsi = config_dict.get(pilih)
    if data is None:
        return fungsi()
    return fungsi(data)