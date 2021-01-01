import sqlite3


class Barang :
    def __init__(self):
        self.con = sqlite3.connect('ebako.db')
        self.cursor = self.con.cursor()
    
    def executeQuery(self, query, retVal=False):
        self.cursor.execute(query)
        all_results = self.cursor.fetchall()
        self.con.commit()
        if retVal:
            return all_results

    def setBarang(self, Kode_Barang, Nama_Barang, Harga_Modal, Harga_Jual, Stok, Keterangan):
        self.query = 'INSERT INTO Barang (Kode_Barang, Nama_Barang, Harga_Modal, Harga_Jual, Stok, Keterangan) VALUES (%s, \'%s\', %s, %s, \'%s\',\'%s\')' 
        self.query = self.query % (Kode_Barang, Nama_Barang, Harga_Modal, Harga_Jual, Stok, Keterangan)
        self.executeQuery(self.query)
    
    def setUbahBarang(self, Kode_Barang, Nama_Barang, Harga_Modal, Harga_Jual, Stok, Keterangan):
        self.query = 'UPDATE Barang SET Kode_Barang = %s, Nama_Barang = \'%s\', Harga_Modal = %s,  Harga_Jual = %s, Stok = \'%s\', Keterangan = \'%s\'  WHERE Kode_Barang = %s'
        self.query = self.query % (Kode_Barang, Nama_Barang, Harga_Modal, Harga_Jual, Stok, Keterangan, Kode_Barang)
        self.executeQuery(self.query)

    def getDataBarang(self):
        self.query = 'SELECT * FROM Barang'
        Kode_Barang = self.executeQuery(self.query, retVal=True)
        return Kode_Barang
        
barang = Barang()
pilihanUrutan = True
def iniBarang():
    print('1. Melihat Data Sembako')
    print('2. Menambah Data Sembako')
    print('3. Mengubah Data Sembako')
    pilihanUrutan = input('Masukkan pilihan: ')
    print()
    return pilihanUrutan

def tambahDataBarang():
    global barang
    print('\nTambah Data Sembako')
    Kode_Barang = input('Masukkan Kode Sembako : ')
    Nama_Barang = input ('Masukkan Nama Sembako :  ') 
    Harga_Modal = input('Memasukkan Harga Modal : ')
    Harga_Jual = input('Memasukkan Harga Jual : ')
    Stok = input('Memasukkan Stok : ')
    Keterangan = input('Masukkan Keterangan Sembako : ')
    barang.setBarang(Kode_Barang, Nama_Barang, Harga_Modal, Harga_Jual, Stok, Keterangan)
    print('\n')
    print('Data Berhasil Ditambahkan')

def tampilkanDataBarang():
    global barang
    print('\nDaftar Sembako')
    daftarBarang = barang.getDataBarang()
    for user_row in daftarBarang:
        print(user_row)
    print('\n')

def ubahDataBarang():
    global barang
    print('\n----------PILIHAN UBAH SEMBAKO------------')
    Kode_Barang = input('Masukkan Kode Sembako: ')
    Nama_Barang = input ('Masukkan Nama Sembako: ') 
    Harga_Modal = input('Memasukkan Harga Modal: ')
    Harga_Jual = input('Memasukkan Harga Jual: ')
    Stok = input('Memasukkan Stok: ')
    Keterangan = input('Masukkan Keterangan Sembako : ')
    barang.setUbahBarang(Kode_Barang, Nama_Barang, Harga_Modal, Harga_Jual, Stok, Keterangan)
    print('\n')
    print('Data Berhasil Diubah')

barang_jalan = True
while barang_jalan :
    pilihanUrutan = iniBarang()
    if pilihanUrutan == '1':
        tampilkanDataBarang()
    elif pilihanUrutan == '2':
        tambahDataBarang()
    elif pilihanUrutan == '3':
        ubahDataBarang()