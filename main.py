"Program Manajemen Kontak"

def melihat_kontak():
    if kontak:
        for num, item in enumerate(kontak, start=1):
            print(f'{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
    else:
        print("Kontak masih kosong")
        return 1

def menambah_kontak():
    # menambahkan kontak
    nama = input("masukkan nama kontak baru: ")
    HP = input("masukkan nomor hp baru: ")
    email = input("masuukan email baru: ")
    kontak_baru = {'nama': nama, 'HP': HP, "email": email}
    kontak.append(kontak_baru)
    print(f'\nKontak berhasil ditambahkan dengan nama {nama}')

def menghapus_kontak():
        if melihat_kontak() == 1:
            return
        else:
            i_hapus = int(input("Masukkan nomor yang akan dihapus: "))

            # if i_hapus < 1 or i_hapus > len(kontak):
            #     print("Nomor yang dimasukkan tidak ada dalam daftar kontak.")
            #     continue

            del kontak[i_hapus - 1]
            print("Kontak berhasil dihapus.")

    #     index di mulai dari 1 karena start nya 1 jadi harus dikurangi 1
    #     print(f'\nKontak berhasil dihapus dengan nama {i_hapus}')

kontak1 = {'nama' : 'Andi', 'HP' : '081234567', 'email': 'Amdi@python.com'}
kontak2 = {'nama' : 'Ani', 'HP' : '088686868', 'email': 'Ami@python.com'}
kontak = [kontak1, kontak2]

while True:
    print("\nMenu Kontak")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar Dari Kontak")

    pilihan = input("Masukkan pilihan menu kontak (1,2,3 atau 4): ")

    if pilihan == '1':
        # if len(kontak)>0
        # melihat semua kontak
        melihat_kontak()

    elif pilihan == '2':
        menambah_kontak()
    elif pilihan == '3':
        # menghapus kontak
        # print("\n")
        menghapus_kontak()


    elif pilihan == '4':
        # keluar dari kontak
        break
    else:
        print("Anda memasukkan pilihan yang salah")