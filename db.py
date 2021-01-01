import sqlite3

connection = sqlite3.connect('ebako.db')

class User :

    def __init__(self, username, password, status) :
        self.username = username
        self.password = password
        
    @property
    def setUsername(self):
        pass

    @property
    def getUsername(self):
        pass

    @property
    def setPassword(self):
        pass

    @property
    def getPassword(self):
        pass
    
    @property
    def setStatus(self):
        pass

    @property
    def getStatus(self):
        pass

    @setUsername.setter
    def setUsername(self,input):
        self.username = input

    @getUsername.getter
    def getUsername(self):
        return self.username

    @setPassword.setter
    def setPassword(self,input):
        self.password = input

    @getPassword.getter
    def getPassword(self):
        return self.password

    @getStatus.getter
    def getStatus(self):
        return self.Status

    def getInfo(self):
        return "Username = {} \nPassword = {} \nStatus = {}".format(self.getUsername, self.getPassword, self.getStatus)

class Pembeli(User):
    def __init__(self, username, password, status) :
            self.username = username
            self.password = password
            self.status = status
        
    @property
    def setUsername(self):
        pass

    @property
    def getUsername(self):
        pass

    @property
    def setPassword(self):
        pass

    @property
    def getPassword(self):
        pass
    
    @property
    def setStatus(self):
        pass

    @property
    def getStatus(self):
        pass

    @setUsername.setter
    def setUsername(self,input):
        self.username = input

    @getUsername.getter
    def getUsername(self):
        return self.username

    @setPassword.setter
    def setPassword(self,input):
        self.password = input

    @getPassword.getter
    def getPassword(self):
        return self.password

    @getStatus.getter
    def getStatus(self):
        return self.Status

    def getInfo(self):
        return "Username = {} \nPassword = {} \nStatus = {}".format(self.getUsername, self.getPassword, self.getStatus)
    

class Admin(User):
    def __init__(self, status):
        super().__init__(username, password, status)
        self.status = status
            
    def setStatus(self):
        self.status = "Admin"

class Barang:
    def __init__(self,Kode_Barang, Nama_Barang, Harga_Modal, Harga_Jual, Stok, Keterangan):
        self.Kode_Barang = KodeBarang
        self.Nama_Barang = Nama_Barang
        self.Harga_Modal = Harga_Modal
        self.Harga_Jual = Harga_Jual
        self.Stok = Stok
        self.Keterangan = Keterangan

    @property
    def setKode_Barang(self):
        pass

    @setKode_Barang.setter
    def setKode_Barang(self,input):
        self.Kode_Barang = input

    @property
    def getKode_Barang(self):
        pass

    @getKode_Barang.getter
    def getKode_Barang(self):
        return self.Kode_Barang

    @property
    def setNama_Barang(self):
        pass

    @setNama_Barang.setter
    def setNama_Barang(self,input):
        self.Nama_Barang = input

    @property
    def getNama_Barang(self):
        pass

    @getNama_Barang.getter
    def getNama_Barang(self):
        return self.Nama_Barang

    @property
    def setHarga_Modal(self):
        pass

    @setHarga_Modal.setter
    def setHarga_Modal(self,input):
        self.Harga_Modal = input

    @property
    def getHarga_Modal(self):
        pass

    @getHarga_Modal.getter
    def getHarga_Modal(self):
        return self.Harga_Modal

    @property
    def setHarga_Jual(self):
        pass

    @setHarga_Jual.setter
    def setHarga_Jual(self,input):
        self.Harga_Jual = input

    @property
    def getHarga_Jual(self):
        pass

    @getHarga_Jual.getter
    def getHarga_Jual(self):
        return self.Harga_Jual

    @property
    def setStok(self):
        pass

    @setStok.setter
    def setStok(self,input):
        self.Stok = input

    @property
    def getStok(self):
        pass

    @getStok.getter
    def getStok(self):
        return self.Stok

    @property
    def setKeterangan(self):
        pass

    @setKeterangan.setter
    def setKeterangan(self,input):
        self.Keterangan = input

    @property
    def getKeterangan(self):
        pass

    @getKeterangan.getter
    def getKeterangan(self):
        return self.Keterangan


    def getInfo(self):
        return "Kode Barang = {} \nNama Barang = {} \nHarga Modal = {} \nHarga Jual = {} \nStok = {} \nKeterangan = {}".format(self.getKode_Barang, self.getNama_Barang, self.getHarga_Modal, self.getHarga_Jual, self.getStok, self.getKeterangan)
    
class Pemesanan:
    def __init__(self,noPemesanan,tanggal,alamat,noTelepon):
        self.noPemesanan = noPemesanan
        self.tanggal = tanggal
        self.alamat = alamat
        self.noTelepon = noTelepon

    @property
    def setNoPemesanan(self):
        pass

    @setNoPemesanan.setter
    def setNoPemesanan(self,input):
        self.noPemesanan = input

    @property
    def getNoPemesanan(self):
        pass

    @getNoPemesanan.getter
    def getNoPemesanan(self):
        return self.noPemesanan

    @property
    def setTanggal(self):
        pass

    @setTanggal.setter
    def setTanggal(self):
        import datetime
        self.tanggal = datetime.date.today()

    @property
    def getTanggal(self):
        pass

    @getTanggal.getter
    def getTanggal(self):
        return self.tanggal
    
    @property
    def setAlamat(self):
        pass

    @setAlamat.setter
    def setAlamat(self,input):
        self.alamat = input

    @property
    def getAlamat(self):
        pass

    @getAlamat.getter
    def getAlamat(self):
        return self.alamat

    @property
    def setNoTelepon(self):
        pass

    @setNoTelepon.setter
    def setNoTelepon(self,input):
        self.noTelepon = input

    @property
    def getNoTelepon(self):
        pass

    @getNoTelepon.getter
    def getNoTelepon(self):
        return self.noTelepon
    
    def getInfo(self):
        return "No Pemesanan = {} \nTanggal = {} \nAlamat = {} \nNoTelepon = {}".format(self.getNoPemesanan, self.getTanggal, self.getAlamat, self.getNoTelepon)
    
class Pembayaran:
    def __init__(self,KodePembayaran,noPemesanan,StatusPembayaran,TanggalPembayaran,MetodePembayaran):
        self.KodePembayaran = KodePembayaran
        self.noPemesanan = noPemesanan
        self.StatusPembayaran = StatusPembayaran
        self.TanggalPembayaran = TanggalPembayaran
        self.MetodePembayaran = MetodePembayaran
    
    @property
    def setKodePembayaran(self):
        pass

    @setKodePembayaran.setter
    def setKodePembayaran(self,input):
        self.KodePembayaran = input

    @property
    def getKodePembayaran(self):
        pass

    @getKodePembayaran.getter
    def getKodePembayaran(self):
        return self.KodePembayaran

    @property
    def setNoPemesanan(self):
        pass

    @setNoPemesanan.setter
    def setNoPemesanan(self,input):
        self.noPemesanan = input

    @property
    def getNoPemesanan(self):
        pass

    @getNoPemesanan.getter
    def getNoPemesanan(self):
        return self.noPemesanan
    
    @property
    def setStatusPembayaran(self):
        pass

    @setStatusPembayaran.setter
    def setStatusPembayaran(self,input):
        self.StatusPembayaran = input

    @property
    def getStatusPembayaran(self):
        pass

    @getStatusPembayaran.getter
    def getStatusPembayaran(self):
        return self.StatusPembayaran
    
    @property
    def setTanggalPembayaran(self):
        pass

    @setTanggalPembayaran.setter
    def setTanggalPembayaran(self):
        import datetime
        self.TanggalPembayaran = datetime.date.today()

    @property
    def getTanggalPembayaran(self):
        pass

    @getTanggalPembayaran.getter
    def getTanggalPembayaran(self):
        return self.TanggalPembayaran

    @property
    def setMetodePembayaran(self):
        pass

    @setMetodePembayaran.setter
    def setMetodePembayaran(self,input):
        self.MetodePembayaran = input

    @property
    def getMetodePembayaran(self):
        pass

    @getMetodePembayaran.getter
    def getMetodePembayaran(self):
        return self.MetodePembayaran

    def getInfo(self):
        return "Kode Pemabayaran = {} \nNo Pemesanan = {} \nStatus Pembayaran = {} \nTanggal Pembayaran = {} \nMetode Pembayaran = {}".format(self.getKodePembayaran, self.getNoPemesanan, self.getStatusPembayaran, self.getTanggalPembayaran, self.getMetodePembayaran)

class Pengiriman:
    def __init__(self,NoPengiriman,NamaPenerima,StatusPengiriman,TanggalKirim,TanggalTerima):
        self.NoPengiriman = NoPengiriman
        self.NamaPenerima = NamaPenerima
        self.StatusPengiriman = StatusPengiriman
        self.TanggalKirim = TanggalKirim
        self.TanggalTerima = TanggalTerima

    @property
    def setNoPengiriman(self):
        pass

    @setNoPengiriman.setter
    def setNoPengiriman(self,input):
        self.NoPengiriman = input

    @property
    def getNoPengiriman(self):
        pass

    @getNoPengiriman.getter
    def getNoPengiriman(self):
        return self.NoPengiriman

    @property
    def setNamaPenerima(self):
        pass

    @setNamaPenerima.setter
    def setNamaPenerima(self,input):
        self.NamaPenerima = input

    @property
    def getNamaPenerima(self):
        pass

    @getNamaPenerima.getter
    def getNamaPenerima(self):
        return self.NamaPenerima
    
    @property
    def setStatusPengiriman(self):
        pass

    @setStatusPengiriman.setter
    def setStatusPengiriman(self,input):
        self.StatusPengiriman = input

    @property
    def getStatusPengiriman(self):
        pass

    @getStatusPengiriman.getter
    def getStatusPengiriman(self):
        return self.StatusPengiriman
    
    @property
    def setTanggalKirim(self):
        pass

    @setTanggalKirim.setter
    def setTanggalKirim(self):
        import datetime
        self.TanggalKirim = datetime.date.today()

    @property
    def getTanggalKirim(self):
        pass

    @getTanggalKirim.getter
    def getTanggalKirim(self):
        return self.TanggalKirim

    @property
    def setTanggalTerima(self):
        pass

    @setTanggalTerima.setter
    def setTanggalTerima(self):
        import datetime
        self.TanggalTerima = datetime.date.today()

    @property
    def getTanggalTerima(self):
        pass

    @getTanggalTerima.getter
    def getTanggalTerima(self):
        return self.TanggalKirim

    def getInfo(self):
        return "No Pengiriman = {} \nNama Penerima = {} \nStatus Pengiriman = {} \nTanggal Kirim = {} \nTanggal Terima = {}".format(self.getNoPengiriman, self.getNamaPenerima, self.getStatusPengiriman, self.getTanggalKirim, self.getTanggalTerima)

class Jarak:
    def __init__(self,KodeJarak,Jarak,BiayaKirim):
        self.KodeJarak = KodeJarak
        self.Jarak = Jarak
        self.BiayaKirim = BiayaKirim   

    @property
    def setKodeJarak(self):
        pass

    @setKodeJarak.setter
    def setKodeJarak(self,input):
        self.KodeJarak = input

    @property
    def getKodeJarak(self):
        pass

    @getKodeJarak.getter
    def getKodeJarak(self):
        return self.KodeJarak

    @property
    def setJarak(self):
        pass

    @setJarak.setter
    def setJarak(self,input):
        self.Jarak = input

    @property
    def getJarak(self):
        pass

    @getJarak.getter
    def getJarak(self):
        return self.Jarak
    
    @property
    def setBiayaKirim(self):
        pass

    @setBiayaKirim.setter
    def setBiayaKirim(self,input):
        self.BiayaKirim = input

    @property
    def getBiayaKirim(self):
        pass

    @getBiayaKirim.getter
    def getBiayaKirim(self):
        return self.BiayaKirim
    
    def getInfo(self):
        return "Kode Jarak = {} \nJarak = {} \nBiaya Kirim = {}".format(self.getKodeJarak, self.getJarak, self.getBiayaKirim)

class Detail_Pemesanan:
    def __init__(self,NoDetail,NoPemesanan,KodeBarang,Jumlah):
        self.NoDetail = NoDetail
        self.NoPemesanan = NoPemesanan
        self.KodeBarang = KodeBarang
        self.Jumlah = Jumlah

    @property
    def setNoDetail(self):
        pass

    @setNoDetail.setter
    def setNoDetail(self,input):
        self.NoDetail = input

    @property
    def getNoDetail(self):
        pass

    @getNoDetail.getter
    def getNoDetail(self):
        return self.NoDetail

    @property
    def setNoPemesanan(self):
        pass

    @setNoPemesanan.setter
    def setNoPemesanan(self,input):
        self.NoPemesanan = input

    @property
    def getNoPemesanan(self):
        pass

    @getNoPemesanan.getter
    def getNoPemesanan(self):
        return self.NoPemesanan
    
    @property
    def setKodeBarang(self):
        pass

    @setKodeBarang.setter
    def setKodeBarang(self,input):
        self.KodeBarang = input

    @property
    def getKodeBarang(self):
        pass

    @getKodeBarang.getter
    def getKodeBarang(self):
        return self.KodeBarang
    
    @property
    def setJumlah(self):
        pass

    @setJumlah.setter
    def setJumlah(self,input):
        self.Jumlah = input

    @property
    def getJumlah(self):
        pass

    @getJumlah.getter
    def getJumlah(self):
        return self.Jumlah
    
    def getInfo(self):
        return "No Detail = {} \nNo Pemesanan = {} \nKode Barang = {} \nJumlah".format(self.getNoDetail, self.getNoPemesanan, self.getKodeBarang, self.getJumlah)

class Ibako:
    def __init__(self,getKodeBarang,NamaBarang,Harga,Keterangan):
        self.KodeBarang = KodeBarang
        self.NamaBarang = NamaBarang
        self.Harga = Harga
        self.Keterangan = Keterangan
    
    @property
    def setKodeBarang(self):
        pass

    @setKodeBarang.setter
    def setKodeBarang(self,input):
        self.KodeBarang = input

    @property
    def getKodeBarang(self):
        pass

    @getKodeBarang.getter
    def getKodeBarang(self):
        return self.KodeBarang
    
    @property
    def setNamaBarang(self):
        pass

    @setNamaBarang.setter
    def setNamaBarang(self,input):
        self.NamaBarang = input

    @property
    def getNamaBarang(self):
        pass

    @getNamaBarang.getter
    def getNamaBarang(self):
        return self.NamaBarang
    
    @property
    def setHarga(self):
        pass

    @setHarga.setter
    def setHarga(self,input):
        self.Harga = input

    @property
    def getHarga(self):
        pass

    @getHarga.getter
    def getHarga(self):
        return self.Harga

    @property
    def setKeterangan(self):
        pass

    @setKeterangan.setter
    def setKeterangan(self,input):
        self.Keterangan = input

    @property
    def getKeterangan(self):
        pass

    @getKeterangan.getter
    def getKeterangan(self):
        return self.Keterangan
    
    def getInfo(self):
        return "Kode Barang = {} \nNama Barang = {} \nHarga = {} \nKeterangan".format(self.getKodeBarang, self.getNamaBarang, self.getHarga, self.getKeterangan)

class Ebako:
    def __init__(self,getKodeBarang,NamaBarang,Harga,Keterangan,Diskon,Hadiah):
        self.KodeBarang = KodeBarang
        self.NamaBarang = NamaBarang
        self.Harga = Harga
        self.Keterangan = Keterangan
        self.Diskon = Diskon
        self.Hadiah = Hadiah
    
    @property
    def setKodeBarang(self):
        pass

    @setKodeBarang.setter
    def setKodeBarang(self,input):
        self.KodeBarang = input

    @property
    def getKodeBarang(self):
        pass

    @getKodeBarang.getter
    def getKodeBarang(self):
        return self.KodeBarang
    
    @property
    def setNamaBarang(self):
        pass

    @setNamaBarang.setter
    def setNamaBarang(self,input):
        self.NamaBarang = input

    @property
    def getNamaBarang(self):
        pass

    @getNamaBarang.getter
    def getNamaBarang(self):
        return self.NamaBarang
    
    @property
    def setHarga(self):
        pass

    @setHarga.setter
    def setHarga(self,input):
        self.Harga = input

    @property
    def getHarga(self):
        pass

    @getHarga.getter
    def getHarga(self):
        return self.Harga

    @property
    def setKeterangan(self):
        pass

    @setKeterangan.setter
    def setKeterangan(self,input):
        self.Keterangan = input

    @property
    def getKeterangan(self):
        pass

    @getKeterangan.getter
    def getKeterangan(self):
        return self.Keterangan
    
    @property
    def setDiskon(self):
        pass

    @setDiskon.setter
    def setDiskon(self,input):
        self.Diskon = input

    @property
    def getDiskon(self):
        pass

    @getDiskon.getter
    def getDiskon(self):
        return self.Diskon

    @property
    def setHadiah(self):
        pass

    @setHadiah.setter
    def setHadiah(self,input):
        self.Hadiah = input

    @property
    def getHadiah(self):
        pass

    @getHadiah.getter
    def getHadiah(self):
        return self.Hadiah
    
    def getInfo(self):
        return "Kode Barang = {} \nNama Barang = {} \nHarga = {} \nKeterangan \nDiskon = {} \nHadiah = {}".format(self.getKodeBarang, self.getNamaBarang, self.getHarga, self.getKeterangan, self.getDiskon, self.getHadiah)

while True:
    """
1. Login
    """