import csv
from datetime import datetime
import os


#NAMA FILE CSV
name_file_csv = 'ini_gudang.csv'
name_akun_csv = 'data.csv'

#LIHAT GUDANG
def lihat_gudang():
    
    clear_screen()

    # MEMBACA FILE CSV 
    data_barang = []
    with open(name_file_csv, mode='r') as file_csv:
        fieldnames = ['ID Barang', 'Nama Barang', 'Stock Barang', 'Satuan Barang', 'Waktu']
        csv_reader = csv.DictReader(file_csv, fieldnames=fieldnames)
        for row in csv_reader:
            data_barang.append(row)
    

    print('='*70)
    print(f"{'DAFTAR STOCK BARANG ANDA':^70}")
    print("="*70)
    print("ID BARANG \t | NAMA BARANG \t | JUMLAH BARANG \t | SATUAN BARANG \t | WAKTU")
    print("="*70)
    

    for data in data_barang:
        print(f"{data['ID Barang']} \t {data['Nama Barang']} \t {data['Stock Barang']} \t {data['Satuan Barang']} \t {data['Waktu']}")
        print('-'*70)

    back_to_gudang()

# INPUT BARANG MASUK
def tulis_barang_masuk():
    clear_screen()

    # MEMBACA FILE CSV
    data_barang = []
    with open(name_file_csv, mode='r') as file_csv:
        fieldnames = ['ID Barang', 'Nama Barang', 'Stock Barang', 'Satuan Barang', 'Waktu']
        csv_reader = csv.DictReader(file_csv, fieldnames=fieldnames)
        for row in csv_reader:
            data_barang.append(row)
    
        print('='*70)
        print(f"{'SILAHKAN ENTRY BARANG ANDA':^70}")
        print('='*70)

        # INPUT TAMBAH BARANG
        id_barang = len(data_barang) + 1
        nama_barang = str(input("Masukkan Nama Barang Anda\t: "))
        stock_barang = int(input("Masukkan Jumlah Stock Barang And\t: "))
        satuan = str(input("Masukkan Satuan dari Barang Anda\t: "))
        waktu = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # MENAMBAHKAN DATA BARANG KE FILE CSV
    with open(name_file_csv, mode='a', newline='') as file_csv:
        fieldnames = ['ID Barang', 'Nama Barang', 'Stock Barang', 'Satuan Barang', 'Waktu']
        writer = csv.DictWriter(file_csv, fieldnames=fieldnames)
        writer.writerow({'ID Barang': id_barang, 'Nama Barang': nama_barang, 'Stock Barang': stock_barang, 'Satuan Barang': satuan, 'Waktu': waktu})

    back_to_gudang()

# EDIT BARANG YANG INGIN DIUBAH

def edit_barang():

    # MEMBACA FILE CSV
    data_barang = []
    with open(name_file_csv, mode='r') as file_csv:
        fieldnames = ['ID Barang', 'Nama Barang', 'Stock Barang', 'Satuan Barang', 'Waktu']
        csv_reader = csv.DictReader(file_csv, fieldnames=fieldnames)
        for row in csv_reader:
            data_barang.append(row)

    print('='*70)
    print(f"{'DAFTAR STOCK BARANG ANDA':^70}")
    print("="*70)
    
    # MENAMPILKAN DATA BARANG
    for data in data_barang:
        print(f"{data['ID Barang']} \t {data['Nama Barang']} \t {data['Stock Barang']} \t {data['Satuan Barang']} \t{data['Waktu']}")
        print('-'*70)

    # INPUT EDIT BARANG
    cari_id_barang = int(input("Masukkan ID BARANG yang ingin diganti: "))
    barang_baru = str(input("Masukkan NAMA BARANG Terbaru: "))
    stock_baru = int(input("Masukkan STOCK BARANG Terbaru: "))
    satuan_baru = str(input("Masukkan SATUAN BARANG Terbaru: "))
    update_waktu = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # MENENTUKAN INDEKS DATA BARANG DENGAN DATA YANG BARU
    indeks = 0
    for data_update in data_barang:
        if (int(data_update['ID Barang']) == cari_id_barang):
            data_barang[indeks]['Nama Barang'] = barang_baru
            data_barang[indeks]['Stock Barang'] = stock_baru
            data_barang[indeks]['Satuan Barang'] = satuan_baru
            data_barang[indeks]['Waktu'] = update_waktu
        indeks = indeks + 1
    
    # MENGEDIT DATA BARANG DI FILE CSV 
    with open(name_file_csv, mode='w') as file_csv:
        fieldnames = ['ID Barang', 'Nama Barang', 'Stock Barang', 'Satuan Barang', 'Waktu']
        writer = csv.DictWriter(file_csv, fieldnames=fieldnames)
        for new_data in data_barang:
            writer.writerow({'ID Barang': new_data['ID Barang'], 'Nama Barang': new_data['Nama Barang'], 'Stock Barang': new_data['Stock Barang'], 'Satuan Barang': new_data['Satuan Barang'], 'Waktu': new_data['Waktu']})
        if file_csv.tell() == 0:
            writer.writeheader()
    clear_screen()
    print('-'*70)
    print(f"{'DATA BERHASIL DIUBAH':^70}")
    print('-'*70)    
    
    back_to_gudang()

def delete_barang():
    
    clear_screen()
    
    # MEMBACA FILE CSV
    data_barang = []
    with open(name_file_csv, mode='r') as file_csv:
        fieldnames = ['ID Barang', 'Nama Barang', 'Stock Barang', 'Satuan Barang', 'Waktu']
        csv_reader = csv.DictReader(file_csv, fieldnames=fieldnames)
        for row in csv_reader:
            data_barang.append(row)

    # MENAMPILKAN DATA BARANG
    print('='*70)
    print(f"{'DAFTAR STOCK BARANG ANDA':^70}")
    print("="*70)
    

    for data in data_barang:
        print(f"{data['ID Barang']} \t {data['Nama Barang']} \t {data['Stock Barang']} \t {data['Satuan Barang']} \t{data['Waktu']}")
        print('-'*70)

    # MENENTUKAN ID BARANG YANG INGIN DIHAPUS
    id_barang = int(input("Masukkan ID Barang yang ingin dihapus: "))

    # MENETUKAN INDEKS BARANG DENGAN ID BARANG
    indeks = 0

    for delete in data_barang:
        if (int(delete['ID Barang']) == id_barang):
            data_barang.remove(data_barang[indeks])
        indeks = indeks + 1
    
    # MENGHAPUS DATA BARANG
    with open(name_file_csv, mode='w') as file_csv:
        fieldnames = ['ID Barang', 'Nama Barang', 'Stock Barang', 'Satuan Barang', 'Waktu']
        writer = csv.DictWriter(file_csv, fieldnames=fieldnames)
        for new_data in data_barang:
            writer.writerow({'ID Barang': new_data['ID Barang'], 'Nama Barang': new_data['Nama Barang'], 'Stock Barang': new_data['Stock Barang'], 'Satuan Barang': new_data['Satuan Barang'], 'Waktu': new_data['Waktu']})
        if file_csv.tell() == 0:
            writer.writeheader()

    clear_screen()
    print('-'*70)
    print(f"{'DATA TELAH DIHAPUS':^70}")
    print('-'*70)

    back_to_gudang()

def history_gudang():
    print("lihat aktivitas anda sebelumnya")

def back_to_gudang():
    print("\n")
    kembali = input("Tekan Enter untuk Kembali ke Menu")
    print(kembali) 
    homepage_gudang()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def homepage_gudang():
    
    clear_screen()

    print('='*70)
    print(f"{'SELAMAT DATANG DI INVENTOFARM':^70} \n {'KELOLA GUDANG PERTANIAN ANDA ':^70}")
    print('='*70)

    print(" [1]. LIHAT PERSEDIAAN DI GUDANG ANDA \n [2]. ENTRY BARANG MASUK \n [3]. ENTRY EDIT BARANG \n [4]. HAPUS BARANG \n [5]. LIHAT HISTORY \n\n [0]. KELUAR")
    
    opsi = int(input("Pilih Opsi yang ingin digunakan: "))
    while(True):
        if opsi == 1:
            lihat_gudang()
        
        elif opsi == 2:
            tulis_barang_masuk()
 
        elif opsi == 3:
            edit_barang()

        elif opsi == 4:
            delete_barang()

        elif opsi == 5:
            history_gudang()

        elif opsi == 0:
            clear_screen()

            print('-'*70)
            print(f"{'TERIMA KASIH TELAH BERKUNJUNG':^70}")
            print('-'*70)

            exit()
            
        else:
            print("Input salah")
        back_to_gudang()

def Register():
    clear_screen()

    Username = input("Masukkan Username: ")
    Password = input("Masukkan Password: ")

    data_akun = []

    with open(name_akun_csv, 'r') as file:
        csv_reader = csv.reader(file, delimiter=",")
        for row in csv_reader:
            data_akun.append({'Username': row[0], 'Password': row[1]})

    username_ada = True
    while username_ada == True:
        username_ada = False
        for akun in data_akun: 
            if Username == akun['Username']:
                print("Username sudah ada ganti yang lain")
                username_ada = True
                break

    print(f"SELAMAT DATANG {Username} DI INVENTOFARM")

    if username_ada == False:
        databaru =  {'Username' : Username, 'Password': Password}
        with open(name_akun_csv, 'a', newline="") as file:
            writer = csv.DictWriter(file, fieldnames=databaru.keys())
            writer.writerow(databaru)
    
    back_to_gudang()

# Login

def Login():

    clear_screen()

    username = input("Masukkan Username : ")
    password = input("Masukkan Password : ")

    data_akun = []
    with open(name_akun_csv, 'r') as file :
        csv_reader = csv.reader(file, delimiter=",")
        for row in csv_reader :
            data_akun.append({'username' : row[0], 'password' : row[1]})
        
    datalogin = []
    for i in data_akun :
        if username == i['username'] and password == i['password'] :
            datalogin.append(i)
            print("berhasil Login")
            back_to_gudang()
            break

    if len(datalogin) == 0 :
        print("Akun tidak ditemukan")
        tampilan='''
        1. kembali
        2. Register
        '''
        print(tampilan)
        while True:
            inputan=input("Pilihan >")
            if inputan == "1":
                pilihan()
            elif inputan == "2":
                Register()


# Pilihan = input("Login / Register? (L/R) : ")
def pilihan():
    clear_screen()

    tampilan='''
    1. Login
    2. Register
    '''
    print (tampilan)
    while True:
        inputan = input("Pilihan >")
        if inputan == "1":
            Login()
        elif inputan == "2":
            Register()
    

if __name__ == "__main__":
    while True:
        pilihan()