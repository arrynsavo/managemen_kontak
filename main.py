"Program Manajemen Kontak"

kontak1 = {'nama' : "Andi", 'HP' : '081234567', 'email': 'Amdi@python.com'}
kontak2 = {'nama' : "Ani", 'HP' : '088686868', 'email': 'Ami@python.com'}
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
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'\n{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
        else:
            print("Kontak masih kosong")
    elif pilihan == '2':
        # menambahkan kontak
        nama = input("masukkan nama kontak baru: ")
        HP = input("masukkan nomor hp baru: ")
        email = input("masuukan email baru: ")
        kontak_baru = {'nama': nama, 'HP': HP, "email": email}
        kontak.append(kontak_baru)
        print(f'\nKontak berhasil ditambahkan dengan nama {nama}')
    elif pilihan == '3':
        # menghapus kontak
        # print("\n")
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'\n{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
        else:
            print("data masih kosong")
            continue

        i_hapus = int(input("Masukkan nomor yang akan dihapus: "))
        # del kontak[i_hapus-1]

        # if not i_hapus.isdigit():
        #     print("Input harus berupa nomor valid.")
        #     continue

        # i_hapus = int(i_hapus)

        if i_hapus < 1 or i_hapus > len(kontak):
            print("Nomor yang dimasukkan tidak ada dalam daftar kontak.")
            continue

        del kontak[i_hapus - 1]
        print("Kontak berhasil dihapus.")

    #     index di mulai dari 1 karena start nya 1 jadi harus dikurangi 1
    #     print(f'\nKontak berhasil dihapus dengan nama {i_hapus}')

    elif pilihan == '4':
        # keluar dari kontak
        break
    else:
        print("Anda memasukkan pilihan yang salah")