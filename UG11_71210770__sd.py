class RakObat:
    def __init__(self):
        self.size = 10  # Ukuran hash table
        self.map = [None] * self.size
        self.daftar_obat = [] # list untuk menyimpan semua obat yang ditambahkan ke rak

    def hash_function(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.size

    def tambahObat(self, jenisObat, namaObat):
        if len(self.daftar_obat) >= self.size:
            print("Rak obat sudah penuh")
            return False
        index = self.hash_function(jenisObat)
        if self.map[index] is None or self.map[index][0] == "deleted":
            self.map[index] = (jenisObat, namaObat)
            self.daftar_obat.append((jenisObat, namaObat))
            return True
        else:
            # Collision occurred, perform linear probing
            next_index = (index + 1) % self.size
            while next_index != index:
                if self.map[next_index] is None or self.map[next_index][0] == "deleted":
                    self.map[next_index] = (jenisObat, namaObat)
                    self.daftar_obat.append((jenisObat, namaObat))
                    return True
                next_index = (next_index + 1) % self.size
            return False

    def lihatObat(self, jenisObat):
        index = self.hash_function(jenisObat)
        if self.map[index] is not None and self.map[index][0] == jenisObat:
            return self.map[index][1]
        else:
            next_index = (index + 1) % self.size
            while next_index != index:
                if self.map[next_index] is not None and self.map[next_index][0] == jenisObat:
                    return self.map[next_index][1]
                next_index = (next_index + 1) % self.size
            return None

    def ambilObat(self, jenisObat):
        index = self.hash_function(jenisObat)
        if self.map[index] is not None and self.map[index][0] == jenisObat:
            self.map[index] = ("deleted", None)
            print(f"{self.map[index][1]} telah diambil dari rak")
            return True
        else:
            next_index = (index + 1) % self.size
            while next_index != index:
                if self.map[next_index] is not None and self.map[next_index][0] == jenisObat:
                    self.map[next_index] = ("deleted", None)
                    print(f"{self.map[next_index][1]} telah diambil dari rak")
                    return True
                next_index = (next_index + 1) % self.size
            return False

    def printAll(self):
        if not self.daftar_obat:
            print("Rak obat kosong")
        else:
            for item in self.daftar_obat:
                print(f"{item[0]}: {item[1]}")

if __name__ == "__main__":
    rak1 = RakObat()
    rak1.tambahObat("Covid", "AstraZeneca (A01)")
    rak1.tambahObat("Flu", "UltraFlu (A02)")
    rak1.tambahObat("Sakit Kepala", "Paramex (A03)")
    rak1.tambahObat("Maag", "Pro Maag (A04)")
    rak1.tambahObat("Sakit Kepala", "Bodrex (A05)")
    rak1.tambahObat("Vitamin", "Vitacimin")

    print(rak1.lihatObat("Sakit Kepala"))
    print(rak1.lihatObat("Migraine"))

    rak1.ambilObat("Flu")
    rak1.ambilObat("Malaria")
    rak1.printAll()