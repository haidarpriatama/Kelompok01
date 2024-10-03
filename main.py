from jadwal import JadwalKuliah

def tampilkan_menu():
    print("\n1. Tambah Jadwal")
    print("2. Tampilkan Semua Jadwal")
    print("3. Keluar")
    pilihan = int(input("Pilih opsi: "))
    return pilihan

if __name__ == "__main__":
    jadwal_kuliah = JadwalKuliah()

    while True:
        pilihan = tampilkan_menu()

        if pilihan == 1:
            hari = input("\nMasukkan hari: ")
            mata_kuliah = input("Masukkan mata kuliah: ")
            jadwal_kuliah.tambah_jadwal(hari, mata_kuliah)

        elif pilihan == 2:
            jadwal_kuliah.tampilkan_jadwal()

        elif pilihan == 3:
            print("\nProgram selesai.")
            break
        else:
            print("\nPilihan tidak valid, coba lagi.")
