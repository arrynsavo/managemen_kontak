"Program Manajemen Kontak"

import kontak

def main():
    kontak_kantor = kontak.Kontak()
    kontak_keluarga = kontak.Kontak()

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
            # kontak_kantor.melihat_kontak()
            kontak_keluarga.melihat_kontak()

        elif pilihan == '2':
            # kontak_kantor.menambah_kontak()
            kontak_keluarga.menambah_kontak()
        elif pilihan == '3':
            # menghapus kontak
            # print("\n")
            # kontak_kantor.menghapus_kontak()
            kontak_keluarga.menghapus_kontak()


        elif pilihan == '4':
            # keluar dari kontak
            kontak_keluarga.keluar_kontak()
            break
        else:
            print("Anda memasukkan pilihan yang salah")

if __name__ == "__main__":
    main()