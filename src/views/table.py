def tabel0(data):
    print(data)
    print(type(data))

# satu kolom satu baris
def tabel1(data): 
    jumlah_elemen = len(data)
    jumlah_huruf  = [len(i) for i in data]
    padding       = 2
    garis_atas    = f"┌{"─" * (max(jumlah_huruf) + padding)}┐"
    garis_bawah   = f"└{"─" * (max(jumlah_huruf) + padding)}┘"
    print()
    print(garis_atas)
    hasil = ""
    for i in data:
        hasil += f"│ {i} │"
    print(hasil)
    print(garis_bawah)
    print()

# dua kolom satu baris
def tabel2(data): 
    # data diharapkan berupa tuple/list dengan 2 elemen, misal: ("Nama", "Hobi")
    padding = 2
    
    # Menghitung lebar masing-masing kolom berdasarkan panjang string elemennya
    lebar_kolom1 = len(str(data[0])) + padding
    lebar_kolom2 = len(str(data[1])) + padding
    
    # Membuat garis pembatas
    garis_atas   = f"┌{'─' * lebar_kolom1}┬{'─' * lebar_kolom2}┐"
    garis_tengah = f"│ {data[0]} │ {data[1]} │"
    garis_bawah  = f"└{'─' * lebar_kolom1}┴{'─' * lebar_kolom2}┘"
    
    print()
    print(garis_atas)
    print(garis_tengah)
    print(garis_bawah)
    print()

# satu sampai n kolom satu baris
def tabel3(data):
    # Mengonversi semua elemen ke string dan menghitung lebar tiap kolom
    padding = 2
    lebar_kolom = [len(str(item)) + padding for item in data]
    
    # 1. Membuat garis atas
    # Bagian tengah menggunakan '┬' sebagai penyambung antar kolom
    isi_atas = "┬".join(["─" * lebar for lebar in lebar_kolom])
    garis_atas = f"┌{isi_atas}┐"
    
    # 2. Membuat baris data
    # Menggabungkan elemen dengan separator ' │ '
    isi_tengah = " │ ".join([str(item) for item in data])
    garis_tengah = f"│ {isi_tengah} │"
    
    # 3. Membuat garis bawah
    # Bagian tengah menggunakan '┴' sebagai penyambung antar kolom
    isi_bawah = "┴".join(["─" * lebar for lebar in lebar_kolom])
    garis_bawah = f"└{isi_bawah}┘"
    
    print()
    print(garis_atas)
    print(garis_tengah)
    print(garis_bawah)
    print()

# satu kolom dua baris
def tabel4(data):
    # Data diharapkan berupa tuple dengan 2 elemen, misal: ("Baris 1", "Baris 2")
    padding = 2
    # Mencari string terpanjang di antara kedua baris agar lebar kolom konsisten
    lebar_maks = max(len(str(data[0])), len(str(data[1]))) + padding
    
    garis_horizontal = "─" * lebar_maks
    
    # Konstruksi tabel
    garis_atas    = f"┌{garis_horizontal}┐"
    baris_1       = f"│ {str(data[0]).ljust(lebar_maks - 1)}│"
    garis_tengah  = f"├{garis_horizontal}┤"
    baris_2       = f"│ {str(data[1]).ljust(lebar_maks - 1)}│"
    garis_bawah   = f"└{garis_horizontal}┘"
    
    print()
    print(garis_atas)
    print(baris_1)
    print(garis_tengah)
    print(baris_2)
    print(garis_bawah)
    print()

# dua kolom dua baris
def tabel5(data):
    # Data diharapkan berupa tuple of tuples atau list of lists
    # Contoh: (("A1", "B1"), ("A2", "B2"))
    padding = 2
    
    # Mengambil elemen untuk memudahkan penulisan
    r1c1, r1c2 = data[0]
    r2c1, r2c2 = data[1]
    
    # Menghitung lebar maksimal tiap kolom
    lebar_k1 = max(len(str(r1c1)), len(str(r2c1))) + padding
    lebar_k2 = max(len(str(r1c2)), len(str(r2c2))) + padding
    
    # Konstruksi Garis
    garis_atas   = f"┌{'─' * lebar_k1}┬{'─' * lebar_k2}┐"
    garis_tengah = f"├{'─' * lebar_k1}┼{'─' * lebar_k2}┤"
    garis_bawah  = f"└{'─' * lebar_k1}┴{'─' * lebar_k2}┘"
    
    # Konstruksi Baris Data
    baris1 = f"│ {str(r1c1).ljust(lebar_k1-1)}│ {str(r1c2).ljust(lebar_k2-1)}│"
    baris2 = f"│ {str(r2c1).ljust(lebar_k1-1)}│ {str(r2c2).ljust(lebar_k2-1)}│"
    
    print()
    print(garis_atas)
    print(baris1)
    print(garis_tengah)
    print(baris2)
    print(garis_bawah)
    print()

# satu sampai n kolom dan satu sampai n baris
def tabel6(data):
    if not data:
        return

    # --- VALIDASI & NORMALISASI DATA ---
    # Jika data hanya tuple/list 1D (satu baris), bungkus dalam list agar jadi 2D
    if not isinstance(data[0], (list, tuple)):
        data = [data]
    
    padding_kiri = 1
    padding_kanan = 1
    
    jumlah_baris = len(data)
    jumlah_kolom = len(data[0])

    # 1. Menghitung lebar maksimal tiap kolom
    lebar_kolom = []
    for j in range(jumlah_kolom):
        # Gunakan str().strip() dan proteksi jika ada baris yang kolomnya lebih sedikit
        maks = 0
        for baris in data:
            try:
                isi = str(baris[j]).strip()
                if len(isi) > maks:
                    maks = len(isi)
            except IndexError:
                continue 
        lebar_kolom.append(maks)

    # 2. Fungsi pembantu garis horizontal
    def buat_garis(kiri, tengah, kanan):
        bagian = []
        for l in lebar_kolom:
            bagian.append("─" * (l + padding_kiri + padding_kanan))
        return f"{kiri}{tengah.join(bagian)}{kanan}"

    # 3. Cetak tabel
    print()
    print(buat_garis("┌", "┬", "┐"))
    
    for i, baris in enumerate(data):
        isi_sel = []
        for idx in range(jumlah_kolom):
            # Ambil data jika ada, jika tidak ada (baris pendek) isi spasi kosong
            try:
                teks = str(baris[idx]).strip()
            except IndexError:
                teks = ""
                
            sel = f"{' ' * padding_kiri}{teks.ljust(lebar_kolom[idx])}{' ' * padding_kanan}"
            isi_sel.append(sel)
        
        print(f"│{'│'.join(isi_sel)}│")
        
        if i < jumlah_baris - 1:
            print(buat_garis("├", "┼", "┤"))
            
    print(buat_garis("└", "┴", "┘"))
    print()

def tabel7(data):
    if data is None:
        return print("data kosong...! tidak bisa menampilkan data tabel")
    tabel = list(data)
    jns_tabel = type(tabel)
    type_data = [[type(baris) for baris in row] for row in tabel]
    jml_huruf = [[len(str(baris)) for baris in row] for row in tabel]
    transpose = list(zip(*jml_huruf))
    max_huruf = [max(row) for row in transpose]
    jml_kolom = len(tabel[0])
    jml_baris = len(tabel) - 1
    tot_baris = len(tabel)
    print("")
    for index, kolom in enumerate(tabel):
        # garis atas
        if index == 0 and index != 1:
            garis_atas = ""
            for i, maks in enumerate(max_huruf):
                if i == jml_kolom - 1:
                    garis_atas += f"─{"─" * maks}─"
                else:
                    garis_atas += f"─{"─" * maks}─┬"
            print(f"┌{garis_atas}┐")
        # isi baris kolom tabel
        isi_baris = ""
        for baris, maks in zip(kolom, max_huruf):
            if baris == None:
                baris = str(baris)
            if index == 0:
                isi_baris += f"│ {baris:^{maks}} "
            elif isinstance(baris, float):
                isi_baris += f"│ {baris:>{maks}.3f} "
            else:
                isi_baris += f"│ {baris:{maks}} "
        print(f"{isi_baris}│")
        # garis pemisah judul kolom dan baris
        if index == 0 and tot_baris > 1:
            garis_pisah = ""
            for i, maks in enumerate(max_huruf):
                if i == jml_kolom - 1:
                    garis_pisah += f"─{"─" * maks}─"
                else:
                    garis_pisah += f"─{"─" * maks}─┼"
            print(f"├{garis_pisah}┤")
        # garis bawah
        if index == tot_baris - 1:
            garis_bawah = ""
            for i, maks in enumerate(max_huruf):
                if i == jml_kolom - 1:
                    garis_bawah += f"─{"─" * maks}─"
                else:
                    garis_bawah += f"─{"─" * maks}─┴"
            print(f"└{garis_bawah}┘")
    print("")

daftar = {
    "tabel0": tabel0,
    "tabel1": tabel1,
    "tabel2": tabel2,
    "tabel3": tabel3,
    "tabel4": tabel4,
    "tabel5": tabel5,
    "tabel6": tabel6,
    "tabel7": tabel7,
    }

def tabel(pilih, data):
    fungsi = daftar.get(pilih)
    return fungsi(data)