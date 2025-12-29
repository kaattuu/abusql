# from src.control.control1 import start

# start()

from src.views.table import tabel
from src.control.kakas1 import clear_view

data1 = ("satu kolom satu baris",)
data2 = ("kolom satu", "kolom dua")

clear_view()
tabel("tabel2", data2)