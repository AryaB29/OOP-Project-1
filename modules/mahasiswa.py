class Mahasiswa:
    def __init__(self,Name,NIM,Jurusan,IPK):
        self.Name = Name
        self.NIM = NIM
        self.Jurusan = Jurusan
        self.IPK = IPK

    def tampilkan_info(self):
        print("Mahasiswa ini bernama {}, dari jurusan {}, dan memiliki IPK {}".format(self.Name, self.Jurusan, self.IPK))
    
    def penghitungan_ipk(self):
        print("Untuk penghitungan IPK nya semuanya merupakan rahasia universitas")

    





