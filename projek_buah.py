import json, csv, os, time, sys
from colorama import Fore as F
from colorama import Style as S

def insert_buah():
    os.system("cls")
    print("         === ADMIN ===\n")
    list_barang = []
    dict_barang = {}
    nama = input("Nama buah: ").capitalize()
    berat = input("Berat buah: ")
    harga = input("Harga buah: ")
    dict_barang["Buah"]=nama
    dict_barang["Berat"]=berat
    dict_barang["Harga"]=harga
    dict_barang["Value"]=str(int(harga)/int(berat))
    try:
        with open("projek smt 2/buah.json", "r") as bc:
            baca = json.load(bc)
            for c in baca:
                list_barang.append(c)
    except:
        pass
    list_barang.append(dict_barang)
    with open("projek smt 2/buah.json", "w") as bu:
        tulis = json.dump(list_barang, bu, indent=2)
    list_barang.clear()
    dict_barang.clear()
    input("Enter untuk kembali")
    menu_seller()

def daftar_buah(isi):
    os.system("cls")
    daftar_sementara = []
    try:
        with open("projek smt 2/{}.json".format(isi),"r") as bu:
            baca = json.load(bu)
            for i in baca:
                daftar_sementara.append(i)
    except:
        print("Tidak ada buah yang ditambahkan")
    index = 1
    print(f"{'No': ^6} {'Buah': ^12} {'Berat': ^12} {'Harga': ^12}")
    print("="*45)
    for j in daftar_sementara:
        harga = ("Rp. {0:}/Kg".format(j["Harga"]))
        berat = ("{0:} Kg".format(j["Berat"]))
        print(f"{index : ^6} {j['Buah'] : ^12} {berat : ^12} {harga : ^12}")
        index += 1
    input("Enter untuk kembali")
    menu_seller()

def hapus():
    os.system("cls")
    print("         === ADMIN ===\n")
    daftar_sementara = []
    with open("projek smt 2/buah.json","r") as bu:
        baca = json.load(bu)
        for i in baca:
            daftar_sementara.append(i)
    index = 1
    print(f"{'No': ^6} {'Buah': ^12} {'Berat': ^12} {'Harga': ^12}")
    print("="*45)
    for j in daftar_sementara:
        harga = ("Rp. {0:}/Kg".format(j["Harga"]))
        berat = ("{0:} Kg".format(j["Berat"]))
        print(f"{index : ^6} {j['Buah'] : ^12} {berat : ^12} {harga : ^12}")
        index += 1
    print("0. Kembali")
    tanya = int(input("Buah mana yang ingin anda hapus: "))
    if tanya == 0:
        menu_seller()
    for k, item in enumerate(daftar_sementara):
        if (tanya-1) == k:
            daftar_sementara.pop(k)
    with open("projek smt 2/buah.json","w") as tu:
        tulis = json.dump(daftar_sementara, tu, indent=2)
        print("Buah berhasil dihapus dari daftar\n")
    input("Enter untuk kembali")
    menu_seller()

def update():
    os.system("cls")
    print("         === ADMIN ===\n")
    daftar_sementara = []
    with open("projek smt 2/buah.json","r") as bu:
        baca = json.load(bu)
        for i in baca:
            daftar_sementara.append(i)
    index = 1
    print(f"{'No': ^6} {'Buah': ^12} {'Berat': ^12} {'Harga': ^12}")
    print("="*45)
    for j in daftar_sementara:
        harga = ("Rp. {0:}/Kg".format(j["Harga"]))
        berat = ("{0:} Kg".format(j["Berat"]))
        print(f"{index : ^6} {j['Buah'] : ^12} {berat : ^12} {harga : ^12}")
        index += 1
    print("0. Kembali")
    tanya = int(input("Buah mana yang ingin anda perbarui datanya: "))
    if tanya == 0:
        menu_seller()
    os.system("cls")
    print(f"{'Buah': ^12} {'Berat': ^12} {'Harga': ^12}")
    print("="*45)
    for k, item in enumerate(daftar_sementara):
        if (tanya-1) == k:
            print(f"{item['Buah']: ^12} {item['Berat']: ^12} {item['Harga']: ^12}")
            list_barang = []
            dict_barang = {}
            nama = input("Nama buah: ").capitalize()
            berat = input("Berat buah: ")
            harga = input("Harga buah: ")
            dict_barang["Buah"]=nama
            dict_barang["Berat"]=berat
            dict_barang["Harga"]=harga
            dict_barang["Value"]=str(int(harga)/int(berat))
            list_barang.append(dict_barang)
            daftar_sementara.pop(k)
            daftar_sementara.insert(k, list_barang[0])
            
    with open("projek smt 2/buah.json","w") as tu:
        tulis = json.dump(daftar_sementara, tu, indent=2)
        print("Data berhasil diperbarui\n")
    input("Enter untuk kembali")
    menu_seller()
    
def beli_buah():
    os.system("cls")
    banner()
    tampung = []
    tampung_pembelian = []
    tampung_buah = []
    riwayat_user = []
    with open("projek smt 2/buah.json", "r") as b:
        baca = json.load(b)
        for i in baca:
            tampung.append(i)
    try:
        with open("projek smt 2/riwayat_{}.json".format(ambil_info[0]), "r") as baca_his:
            baca_riwayat = json.load(baca_his)
            for ru in baca_riwayat:
                riwayat_user.append(ru)
    except:
        pass
    with open("projek smt 2/{}.json".format(ambil_info[0]), "r") as bd:
        baca = json.load(bd)
        for bc in baca:
            tampung_buah.append(bc)
    print(f"{'No': ^6} {'Buah': ^12} {'Berat': ^12} {'Harga': ^12}")
    print("="*44)
    index = 1
    for j in tampung:
        harga = ("Rp. {0:}/Kg".format(j["Harga"]))
        berat = ("{0:} Kg".format(j["Berat"]))
        print(f"{index : ^6} {j['Buah'] : ^12} {berat : ^12} {harga : ^12}")
        index += 1
    print("0. Kembali")
    tanya = int(input("\nBuah yang ingin dibeli: "))
    if tanya == 0:
        menu_reseller()
    for pembelian in tampung:
        if tampung.index(pembelian) == (tanya-1):
            tampung_pembelian.append(pembelian)
            tampung_buah.append(pembelian)
    os.system("cls")
    ambil_info_beli = []
    print(f"{'Buah': ^12} {'Berat': ^12} {'Harga': ^12}")
    print("="*38)
    for beli in tampung_pembelian:
        ambil_info_beli.append(beli["Buah"])
        harga = ("Rp. {0:}/Kg".format(beli["Harga"]))
        berat = ("{0:} Kg".format(beli["Berat"]))
        print(f"{beli['Buah']: ^12} {berat: ^12} {harga: ^12}")
    tanya_beli = int(input("\nBerapa kilo yang ingin dibeli: "))
    for transaksi in tampung:
        if ambil_info_beli[0] == transaksi["Buah"]:
            tampung[tanya-1]["Berat"] = str(int(tampung[tanya-1]["Berat"]) - tanya_beli)
            if tampung[tanya-1]["Berat"] == "0":
                tampung.pop(tanya-1)
            else:
                tampung[tanya-1]["Value"] = str(int(tampung[tanya-1]["Harga"])/int(tampung[tanya-1]["Berat"]))
            with open("projek smt 2/buah.json", "w") as tulis_ulang:
                tulis = json.dump(tampung ,tulis_ulang, indent=2)
            tampung_buah[len(tampung_buah)-1]["Berat"] = str(tanya_beli)
            with open("projek smt 2/{}.json".format(ambil_info[0]), "w") as ps2:
                tulis_baru = json.dump(tampung_buah, ps2, indent=2)
            riwayat_user.append(tampung[tanya-1])
            riwayat_user[len(riwayat_user)-1]["Berat"] =  str(tanya_beli)
            with open("projek smt 2/riwayat_{}.json".format(ambil_info[0]), "w") as his:
                tulis_hist = json.dump(riwayat_user, his, indent=2)
    input("Enter untuk kembali")
    menu_reseller()

def beli_otomatis():
    os.system("cls")
    banner()
    tampung_value = []
    tampung = []
    riwayat_user = []
    try:
        with open("projek smt 2/riwayat_{}.json".format(ambil_info[0]), "r") as baca_his:
            baca_riwayat = json.load(baca_his)
            for ru in baca_riwayat:
                riwayat_user.append(ru)
    except:
        pass
    with open("projek smt 2/buah.json","r") as bu:
        baca = json.load(bu)
        for i in baca:
            tampung.append(i)
            tampung_value.append(float(i["Value"]))
    tampung_value.sort()
    tampung_value.reverse()
    tampung_bobot = 0
    ambil_value = 0
    ambil_index = []
    ambil_nama = []
    bobot = int(input("Masukkan bobot: "))
    os.system("cls")
    for j, k in enumerate(tampung_value):
        for l in tampung:
            if tampung_bobot + int(l["Berat"]) <= bobot and str(k) in l["Value"] and j not in ambil_index:
                if l["Buah"] not in ambil_nama:
                    ambil_nama.append(l["Buah"])
                    tampung_bobot += int(l["Berat"])
                    ambil_index.append(j)
    batas = 0
    daftar_hapus = []
    daftar_tambah = []
    with open("projek smt 2/{}.json".format(ambil_info[0]), "r") as beli:
        tulis_beli = json.load(beli)
        for bel in tulis_beli:
            daftar_tambah.append(bel)
    for x in ambil_index:
        for y in tampung:
            if batas == len(ambil_index):
                break
            index = 1
            print("Buah yang anda dapatkan dengan keuntungan terbesar\n")
            print(f"{'No': ^6} {'Buah': ^12} {'Berat': ^12} {'Harga': ^12} {'Value': ^12}")
            print("="*55)
            if str(tampung_value[x]) in y["Value"]:
                harga = ("Rp. {0:}/Kg".format(y["Harga"]))
                berat = ("{0:} Kg".format(y["Berat"]))
                print(f"{index: ^6} {y['Buah']: ^12} {harga: ^12} {berat: ^12} {y['Value']: ^12}")
                index += 1
                daftar_hapus.append(y["Buah"])
                batas += 1
    for hapus in daftar_hapus:
        for count, daftar in enumerate(tampung):
            if hapus in daftar["Buah"]:
                daftar_tambah.append(daftar)
                riwayat_user.append(daftar)
                tampung.pop(count)
    with open("projek smt 2/riwayat_{}.json".format(ambil_info[0]), "w") as his:
        tulis_hist = json.dump(riwayat_user, his, indent=2)
    with open("projek smt 2/buah.json", "w") as b:
        tulis = json.dump(tampung, b, indent=2)
    with open("projek smt 2/{}.json".format(ambil_info[0]), "w") as beli2:
        tulis = json.dump(daftar_tambah, beli2, indent=2)
    if tampung_bobot == 0:
        print("Tidak ada buah yang dapat diangkut")             
    input("Enter untuk kembali")
    menu_reseller()

def riwayat_pembelian():
    os.system("cls")
    banner()
    tampung = []
    try:
        with open("projek smt 2/riwayat_{}.json".format(ambil_info[0]), "r") as his:
            baca = json.load(his)
            for i in baca:
                tampung.append(i)
        for t, item in enumerate(tampung, start=1):
            print(f"{t}. {item['Buah']: ^12} {item['Berat']}Kg")
    except:
        print("Tidak ada riwayat pembelian")
    input("Enter untuk kembali")
    menu_reseller()

def riwayat_penjualan():
    os.system("cls")
    banner()
    tampung = []
    try:
        with open("projek smt 2/riwayat2_{}.json".format(ambil_info[0]), "r") as his:
            baca = json.load(his)
            for i in baca:
                tampung.append(i)
        for t, item in enumerate(tampung, start=1):
            print(f"{t}. {item['Buah']: ^12} {item['Berat']}Kg")
    except:
        print("Tidak ada riwayat penjualan")
    input("Enter untuk kembali")
    menu_reseller()

def hitung_mundur(t):
	while t:
		menit, detik = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(menit, detik)
		print("Waktu estimasi: ", timer, end="\r")
		time.sleep(1)
		t -= 1
	input("Tekan enter untuk kembali")

nama_user = []
sandi_user = []
ambil_info = []
blok = 0

def login():
    global nama_user
    global sandi_user
    global ambil_info
    global blok
    with open("projek smt 2/save_data.csv", "r") as sd:
        baca = csv.reader(sd,delimiter=",")
        for i in baca:
            nama_user.append(i[0])
            sandi_user.append(i[1])
    while True:        
        os.system("cls")
        print("         === LOG IN ===\n")
        username = input("Username  : ")
        password = input("Password  : ")
        if username in nama_user:
            index = nama_user.index(username)
            if password == sandi_user[index]:
                input("Login berhasil\nTekan enter untuk melanjutkan")
                ambil_info.append(username)
                if username == "admin123":
                    menu_seller()
                else:
                    menu_reseller()
            else:
                blok += 1
                input("Password yang anda masukkan salah")
                if blok == 3:
                    blok -= blok
                    print("Akses anda diblokir sementara")
                    hitung_mundur(int(10))
                menu_awal()
        else:
            print("Username tidak ditemukan")
        input("Enter untuk kembali")
        menu_awal()
    
def register():
    os.system("cls")
    print("         === REGISTER ===\n")
    username = input("Username  : ")
    password = input("Password  : ")
    pemilik = input("Pemilik   : ")
    toko = input("Nama Toko : ")
    valid = 0
    data_user = []
    ambil_toko = []
    ambil_info2 = []
    if username.isalnum() == False or password.isalnum() == False:
        valid += 1
        print("Username atau Password hanya berupa huruf dan angka")
    if len(username) < 6 or len(password) < 6:
        valid += 1
        print("Username atau password minimal harus terdiri dari 6 karakter")
    if username == password:
        valid += 1
        print("Username dan password tidak boleh sama")
    if valid == 0:
        data_user.append([username, password, pemilik, toko])
        ambil_toko.append([username ,pemilik, toko])
        with open("projek smt 2/save_data.csv", "a", newline="") as sd:
            tulis = csv.writer(sd, delimiter=",")
            for i in data_user:
                tulis.writerow(i)
        with open("projek smt 2/daftar_toko.csv", "a", newline="") as dt:
            tulis2 = csv.writer(dt, delimiter=",")
            for j in ambil_toko:
                tulis2.writerow(j)
        print("Akun Berhasil Dibuat")
        ambil_info2.append(username)
        with open("projek smt 2/{}.json".format(ambil_info2[0]), "w") as ps:
            tulis3 = json.dump([], ps, indent=2)
    else:
        pass
    input("Tekan enter untuk kembali")
    menu_awal() 
    
def banner():
    tampung_info = []
    with open("projek smt 2/save_data.csv","r") as sd:
        baca = csv.reader(sd)
        for cs in baca:
            if ambil_info[0] in cs:
                tampung_info.append(cs[3])
    print("         === TOKO {} ===\n".format(tampung_info[0]).upper().replace("'","").replace("[","").replace("]",""))
    
def menu_seller():
    os.system("cls")
    print("         === ADMIN ===\n")
    print("1. Tambah buah\n2. Daftar Buah\n3. Perbarui Data\n4. Hapus Buah\n0. Log Out")
    tanya = input("Menu: ")
    if tanya == "1":
        insert_buah()
    elif tanya == "2":
        teks = "buah"
        daftar_buah(teks)
    elif tanya == "3":
        update()
    elif tanya == "4":
        hapus()
    elif tanya == "0":
        ucap = "Terima Kasih"
        for i in ucap:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.1)
        menu_awal()

def menu_reseller():
    os.system("cls")
    banner()
    print("1. Beli buah\n2. Beli Otomatis\n3. Cek Keranjang\n4. Riwayat Pembelian\n5. Riwayat Penjualan\n0. Log Out")
    tanya = input("Menu: ")
    if tanya == "1":
        beli_buah()
    elif tanya == "2":
        beli_otomatis()
    elif tanya == "3":
        daftar_buah(ambil_info[0])
    elif tanya == "4":
        riwayat_pembelian()
    elif tanya == "5":
        riwayat_penjualan()
    elif tanya == "0":
        ucap = "Terima Kasih"
        for i in ucap:
            if i == "h":
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(1)
            else:
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(0.1)
        menu_awal()

def menu_konsumen():
    os.system("cls")
    print("         === BUAHKU ===\n")
    tampung_toko = []
    tampung = []
    riwayat_pnj = []
    with open("projek smt 2/daftar_toko.csv","r") as dt:
        baca = csv.reader(dt)
        for b in baca:
            tampung_toko.append(b)
    print(f"{' No': ^5} {'Toko': ^20} {'Pemilik': ^15}")
    print("="*40)
    index = 1
    for i in tampung_toko:
        print(f"{index: ^5} {i[2]: ^20} {i[1]: ^15}")
        index += 1
    print("\n0. Kembali")
    tanya = int(input("\nPilih toko: "))
    if tanya == 0:
        menu_awal()
    tampung.append(tampung_toko[tanya-1][0])
    tampil_toko = []
    try:
        with open("projek smt 2/riwayat2_{}.json".format(tampung[0]), "r") as baca_his:
            baca_riwayat = json.load(baca_his)
            for ru in baca_riwayat:
                riwayat_pnj.append(ru)
    except:
        pass
    try:
        with open("projek smt 2/{}.json".format(tampung[0]),"r") as data_toko:
            baca = json.load(data_toko)
            for tk in baca:
                tampil_toko.append(tk)
    except:
        print("Tidak ada buah yang tersedia pada toko ini")
        input("Enter untuk kembali")
        menu_konsumen()
    os.system("cls")
    index_buah = 1
    tampung_beli = []
    print(f"{'No': ^6} {'Buah': ^12} {'Berat': ^12} {'Harga': ^12}")
    print("="*43)
    for tampil in tampil_toko:
        print(f"{index_buah: ^6} {tampil['Buah']: ^12} {tampil['Berat']: ^12} {tampil['Harga']: ^12}")
        index_buah += 1
    tanya_beli = int(input("\nBuah yang ingin dibeli: "))
    tampung_beli.append(tampil_toko[tanya_beli-1])
    os.system("cls")
    print(f"{'Buah': ^12} {'Berat': ^12} {'Harga': ^12}")
    print("="*38)
    for tb in tampung_beli:
        print(f"{tb['Buah']: ^12} {tb['Berat']: ^12} {tb['Harga']: ^12}")
    tanya_berat = int(input("\nBerapa kilo yang ingin dibeli: "))
    tampil_toko[tanya_beli-1]["Berat"] = str(int(tampil_toko[tanya_beli-1]["Berat"]) - tanya_berat)
    if tampil_toko[tanya_beli-1]["Berat"] == "0":
        tampil_toko.pop(tanya_beli-1)
    with open("projek smt 2/{}.json".format(tampung[0]),"w") as data_baru:
        tulis = json.dump(tampil_toko ,data_baru, indent=2)
    riwayat_pnj.append(tampil_toko[tanya_beli-1])
    riwayat_pnj[len(riwayat_pnj)-1]["Berat"] = str(tanya_berat)
    with open("projek smt 2/riwayat2_{}.json".format(tampung[0]), "w") as his:
        tulis_hist = json.dump(riwayat_pnj, his, indent=2)
    input("\nEnter untuk kembali")
    menu_konsumen()
    
def warna_teks():
    os.system("cls")
    print("=== WARNA FONT ===")
    print("[1] Merah\n[2] Kuning\n[3] Hijau\n[4] Biru\n[5] Cyan\n[6] Default")
    warna = input("=> Masukkan pilihan anda: ")
    if warna == "1":
        print(F.RED, S.BRIGHT, end = "")
    elif warna == "2":
        print(F.YELLOW, S.BRIGHT, end = "")
    elif warna == "3":
        print(F.GREEN, S.BRIGHT, end = "")
    elif warna == "4":
        print(F.BLUE, S.BRIGHT, end = "")
    elif warna == "5":
        print(F.CYAN, S.BRIGHT,end = "")
    elif warna == "6":
        print(F.WHITE, end = "")
    input("Enter untuk kembali")
    menu_awal()
    
def menu_awal():
    os.system("cls")
    nama_user.clear()
    sandi_user.clear()
    ambil_info.clear()
    login_user = []
    try:
        with open("projek smt 2/save_data.csv","r") as sd:
            baca = csv.reader(sd)
            for i in baca:
                login_user.append(i)
    except:
        pass
    if login_user == []:
        login_user.insert(0, ["admin123", "admin123", "admin123","admin123"])
        with open("projek smt 2/save_data.csv","w",newline="") as sd2:
            tulis = csv.writer(sd2)
            for i in login_user:
                tulis.writerow(i)
    
    print('''
        === SELAMAT DATANG DI BUAHKU ===
        
1. Beli Buah
2. Masuk ke Toko
3. Buat Toko
4. Atur Warna Font
0. Exit
''')
    tanya = input("Menu: ")
    if tanya == "1":
        menu_konsumen()
    elif tanya == "2":
        login()
    elif tanya == "3":
        register()
    elif tanya == "4":
        warna_teks()
    elif tanya == "0":
        exit()                

menu_awal()