'Berisi kelas kontak untuk menjalankan program kontak'

import dokumen

class Kontak:
    def __init__(self):
        # self.kontak = []
        self.kontak = dokumen.membuka_kontak()

    def melihat_kontak(self):
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                # print(f'{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
                print(f'{num}. ' + item)
        else:
            print("Kontak masih kosong")
            return 1

    def menambah_kontak(self):
        # menambahkan kontak
        nama = input("masukkan nama kontak baru: ")
        HP = input("masukkan nomor hp baru: ")
        email = input("masuukan email baru: ")
        # kontak_baru = {'nama': nama, 'HP': HP, "email": email}
        kontak_baru = f'{nama} ({HP}, {email})' + '\n'
        self.kontak.append(kontak_baru)
        print(f'\nKontak berhasil ditambahkan dengan nama {nama}')

    def menghapus_kontak(self):
            if self.melihat_kontak() == 1:
                return
            else:
                try:
                    i_hapus = int(input("Masukkan nomor yang akan dihapus: "))

                    if i_hapus < 1 or i_hapus > len(self.kontak):
                        print("Nomor yang dimasukkan tidak ada dalam daftar kontak.")
                        return

                    del self.kontak[i_hapus - 1]
                    print("Kontak berhasil dihapus.")
                except:
                    print("Input yg anda masukkan salah")

    def keluar_kontak(self):
        dokumen.menyimpan_kontak(isi=self.kontak)

    #     index di mulai dari 1 karena start nya 1 jadi harus dikurangi 1
    #     print(f'\nKontak berhasil dihapus dengan nama {i_hapus}')

# kontak1 = {'nama' : 'Andi', 'HP' : '081234567', 'email': 'Amdi@python.com'}
# kontak2 = {'nama' : 'Ani', 'HP' : '088686868', 'email': 'Ami@python.com'}
# kontak = [kontak1, kontak2]