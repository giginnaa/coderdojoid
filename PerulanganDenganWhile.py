class Segitiga():
    def hitung_luas(self,alas, tinggi):
        return (alas * tinggi)/2

segitiga = Segitiga()
print(segitiga.hitung_luas(2,5))
#print(segitiga.hitung_luas_segitiga(2,5)) karena fungsi sudah merupakan bagian dari kelas segitiga sehingga mengulangi
#menyebut segitiga akan sungguh merupakan perbuatan yang sia-sia

#cara lain menghitung luas segitiga

class Segitiga():
    def __init__(self,alas,tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self):
        return (self.alas * self.tinggi) /2

    def get_info(self):
        print('Informasi segitiga. Alas = ', self.alas, ', tinggi = ', self.tinggi)

segitiga = Segitiga(2,5)
segitiga.get_info()
print(segitiga.hitung_luas())
