class JadwalKuliah:
    def _init_(self):
        self.jadwal = {}

    def tambah_jadwal(self, hari, mata_kuliah):
        if hari in self.jadwal:
            self.jadwal[hari].append(mata_kuliah)
        else:
            self.jadwal[hari] = [mata_kuliah]
        print(f"\nMata kuliah {mata_kuliah} ditambahkan pada hari {hari}.")

    def tampilkan_jadwal(self):
        if not self.jadwal:
            print("\nJadwal kosong.")
        else:
            for hari, mata_kuliah in self.jadwal.items():
                print(f"\n{hari}: {', '.join(mata_kuliah)}")


def cek_jadwal(jadwal, hari):
    if hari in jadwal.jadwal:
        return jadwal.jadwal[hari]
    else:
        return []
