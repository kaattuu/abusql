# from src.control.control1 import start

# start()

from src.views.table import tabel
from src.control.kakas1 import clear_view

data1 = ("satu kolom satu baris",)
data2 = ("kolom satu", "kolom dua")
data3 = ("kolom satu", "kolom dua", "kolom tiga")
data4 = (("kolom satu baris satu",), ("kolom satu baris dua",))
data5 = (
    ("judul kolom", "judul kolom"),
    ("isi baris", "isi baris")
)
data6 = (
    ("judul kolom", "judul kolom", "judul kolom", "judul kolom"),
    ("isi baris", "isi baris", "isi baris", "isi baris"),
    ("isi baris", "isi baris", "isi baris", "isi baris"),
    ("isi baris", "isi baris", "isi baris", "isi baris"),
    ("isi baris", "isi baris", "isi baris", "isi baris"),
    ("isi baris", "isi baris", "isi baris", "isi baris"),
)

clear_view()
tabel("tabel6", data6)