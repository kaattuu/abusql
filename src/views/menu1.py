menu_utama = (
    "manajemen user...",
    "manajemen database...",
    "manajemen tabel...",
    "manajemen data...",
    "monitoring..."
    )

menu_user = (
    "lihat user",
    "buat user baru",
    "rename user",
    "ubah password user",
    "lihat hak akses user",
    "beri user hak akses",
    "cabut hak akses user",
    "memuat ulang konfigurasi hak akses",
    "lihat user yang sedang aktif",
    "kill user yang sedang aktif",
    "hapus user"
    )

menu_database = (
    "lihat database",
    "buat database baru",
    "pilih database",
    "hapus database"
    )

menu_tabel = (
    "pilih database",
    "lihat tabel",
    "pilih tabel",
    "buat tabel baru",
    "lihat struktur tabel",
    "lihat kode pembuatan tabel",
    "ubah struktur tabel...",
    "rename tabel",
    "hapus tabel"
    )

menu_data = (
    "pilih database",
    "lihat tabel",
    "pilih tabel",
    "input data",
    "input data banyak",
    "lihat data",
    "ubah data",
    "hapus data",
    "hapus semua data level 1",
    "hapus semua data level 2"
    )

menu_monitoring = (
    "pengecekan koneksi",
    "lihat konfigurasi server mysql",
    "lihat statistik runtime server",
    "informasi detail internal innodb",
    "informasi ringkas koneksi mysql aktif"
    )

menu_struktur = (
    "operasi kolom (tambah-hapus)...",
    "operasi constraint (tambah-hapus)...",
    "operasi property dan utulitas tabel...",
    "operasi partisi (opsional-lanjutan)..."
    )

menu_kolom = (
    "lihat struktur dan kolom tabel",
    "menambah kolom biasa",
    "menambah beberapa kolom sekaligus",
    "menambah kolom di posisi awal",
    "menambah kolom di posisi tertentu",
    "mengubah nama kolom",
    "mengubah tipe data kolom",
    "mengubah kolom ke posisi tertentu",
    "mengubah kolom menjadi NOT NULL",
    "mengubah kolom menjadi NULL",
    "menghapus kolom"
    )

menu_constraint = (
    "menambah primary key",
    "menghapus primary key",
    "menambah unique key",
    "menghapus uniquie key",
    "menambah foreign key",
    "menghapus foreign key",
    "menambah index",
    "menghapus index",
    "menambah check constraint",
    "menghapus check constraint",
    "menambah constraint gabungan multi-kolom",
    "menghapus constraint dengan nama otomatis",
    "mengubah default value",
    "menghapus default value"
    )

menu_properti = (
    "mengganti nama tabel",
    "mengubah engine tabel",
    "mengubah charset dan collation",
    "mengatur ualang auto increment",
    "mengatur comment tabel",
    "mengubah format penyimpanan baris",
    "menonaktifkan key sementara",
    "mengaktifkan key sementara"
    )

menu_partisi = (
    "menambah partition",
    "menghapus partition"
    )

data_dict = {
    "utama"     : menu_utama,
    "user"      : menu_user,
    "database"  : menu_database,
    "tabel"     : menu_tabel,
    "data"      : menu_data,
    "monitoring": menu_monitoring,
    "struktur"  : menu_struktur,
    "kolom"     : menu_kolom,
    "constraint": menu_constraint,
    "properti"  : menu_properti,
    "partisi"   : menu_partisi
    }

config_dict = {
    "utama"     :{"judul": "menu utama",      "opsi": True},
    "user"      :{"judul": "menu user",       "opsi": False},
    "database"  :{"judul": "menu database",   "opsi": False},
    "tabel"     :{"judul": "menu tabel",      "opsi": False},
    "data"      :{"judul": "menu data",       "opsi": False},
    "monitoring":{"judul": "menu monitoring", "opsi": False},
    "struktur"  :{"judul": "menu struktur",   "opsi": False},
    "kolom"     :{"judul": "menu kolom",      "opsi": False},
    "constraint":{"judul": "menu constraint", "opsi": False},
    "properti"  :{"judul": "menu properti",   "opsi": False},
    "partisi"   :{"judul": "menu partisi",    "opsi": False}
    }

def daftar_menu(nama_menu):
    lebar  = 57
    data   = data_dict.get(nama_menu)
    config = config_dict.get(nama_menu)

    if data is None or config is None:
        print("=" * lebar)
        print(f"nama 'menu {nama_menu}' tidak cocok...!")
        print("=" * lebar)
        return
    
    judul = config["judul"]
    opsi  = config["opsi"]
    print(f" {judul} ".center(lebar, "="))
    print()

    for i, j in enumerate(data):
        print(f"{i+1:>2}. {j}")
    
    print()
    if opsi:
        print(f"{"keluar [0]":>{lebar}}")
    else:
        keluar = "[0] keluar"
        print(f"{keluar}{"kembali [00]":>{lebar-len(keluar)}}")
    print("=" * lebar)