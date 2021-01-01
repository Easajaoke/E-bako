import sqlite3

class Pembeli:
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

class Admin:
    def __init__(self, status):
        super().__init__(username, password, status)
        self.status = status
            
    def setStatus(self):
        self.status = "Admin"

class Barang :
    def __init__(self,kode_barang,nama_barang,jenis_barang,merk,jumlah,total):
        self.Kode_Barang = Kode_Barang
        self.Nama_Barang = Nama_Barang
        self.Harga_Modal = Harga_Modal
        self.Harga_Jual = Harga_Jual
        self.jumlah = jumlah
        self.Stok = Stok
        self.Keterangan = Keterangan

    @property
    def setKode_Barang(self):
        pass

    @setKode_Barang.setter
    def setKodeBarang(self,input):
        self.kodeBarang = input

    @property
    def getKode_Barang(self):
        pass

    @getKode_Barang.getter
    def getKodeBarang(self):
        return self.kodeBarang

    @property
    def setNama_Barang(self):
        pass

    @setNama_Barang.setter
    def setNamaBarang(self,input):
        self.namaBarang = input

    @property
    def getNama_Barang(self):
        pass

    @getNama_Barang.getter
    def getNamaBarang(self):
        return self.namaBarang

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

    @setMerk.setter
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
        return self.stok

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
    def setTotal(self):
        pass

    @setTotal.setter
    def setKeterangan(self,input):
        self.Total = input

    @property
    def getTotal(self):
        pass

    @getTotal.getter
    def getTotal(self):
        return self.Total

    def getInfo(self):
        return "Kode Barang = {} \nNama Barang = {} \nHarga Modal = {} \nHarga Jual = {} \nStok = {} \nKeterangan = {} \nTotal barang = {}".format(self.getKode_Barang, self.getNama_Barang, self.getHarga_Modal, self.getHarga_Jual, self.getStok, self.getKeterangan, self.getTotal)
    
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

    @setNoPemesanan.setter
    def setNoPemesanan(self,input):
        self.noPemesanan = input

    @property
    def getNoPemesanan(self):
        pass

    @getNoPemesanan.getter
    def getNoPemesanan(self):
        return self.noPemesanan

