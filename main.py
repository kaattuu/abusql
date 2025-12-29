# from src.control.control1 import start

# start()

from src.views.table import tabel
from src.control.kakas1 import clear_view

data1 = ("satu kolom satu baris",)
data2 = ("kolom satu", "kolom dua")
data3 = ("kolom satu", "kolom dua", "kolom tiga")
data4 = ("kolom satu baris satu",), ("kolom satu baris dua",)

clear_view()
tabel("tabel0", data4)