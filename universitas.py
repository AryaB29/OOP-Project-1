from modules.mahasiswa import Mahasiswa

class Universitas(Mahasiswa):
    def __init__(self,Name,NIM,Jurusan,IPK):
        Mahasiswa.__init__(Name,NIM,Jurusan,IPK)
        
    
    def __init__(self):
        self.daftar_mahasiswa = []
    
    def tambah_mahasiswa(self,mahasiswa):
        self.daftar_mahasiswa.append(mahasiswa)
    
    def hapus_mahasiswa(self,mahasiswa):
        if mahasiswa in self.daftar_mahasiswa:
            self.daftar_mahasiswa.remove(mahasiswa)
        else:
            print("Mahasiswa tidak ditemukan")
    
    def tampilkan_daftar_mahasiswa(self):
        if self.daftar_mahasiswa:
            print("Daftar Mahasiswa di kampus")
            for mahasiswa in self.daftar_mahasiswa:
                print("Mahasiswa ini bernama {}, dari jurusan {}, dan memiliki IPK {}".format(mahasiswa.Name, mahasiswa.Jurusan, mahasiswa.IPK))
    
    def jumlah_mahasiswa(self):
        print("Jumlah mahasiswanya adalah : {}".format(len(self.daftar_mahasiswa)))




univ = Universitas()
mahasiswa_1 = Mahasiswa("Arya","123","Fisika",4.0)
mahasiswa_3 = Mahasiswa("John","123","Kimia",3.0)
univ.tambah_mahasiswa(mahasiswa_1)
univ.tambah_mahasiswa(mahasiswa_3)
univ.tampilkan_daftar_mahasiswa()
univ.jumlah_mahasiswa()
