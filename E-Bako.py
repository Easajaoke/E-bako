def main_login():
    print('=' * 20, 'Plih Cara Masuk Anda', '=' * 20)
    print('1. Google')
    print('2. Nomor Telepon')
    print('3. Tidak Jadi')
 
    # input pilihan
    pilihan = input('Pilih Login: ')
 
    # pilihan menu
    if pilihan == '1':
        Google()
    elif pilihan == '2':
        NomorTelepon()
    else:
        print('Tidak Jadi')
        exit()
 
 
# membuat fungsi authentifikasi sederhana
def Google():
    print('=' * 20)
    print('Halaman Login Google')
    username = input('masukan username anda: ')
    password = input('masukan password: ')
 
    if username == 'easfrida@gmail.com' and password == 'projekpbo':
        print('login berhasil...\n\n')
        main_menu()
    else:
        print('login gagal coba lagi..')
        Google()
 
def tanya():
    tanya = input('kembali ke menu..? (y/n)')
    if tanya == 'y':
        main_menu()
    elif tanya == 't':
        exit()
    else:
        print('input salah')
        print('masukan input dengan benar')

# membuat fungsi authentifikasi sederhana
def NomorTelepon():
    print('=' * 20)
    print('Halaman Login Nomor Telepon')
    nomortelepon = input('masukan nomor telepon anda: ')
 
    if nomortelepon == '+62 812 3078 4383' :
        print('login berhasil...\n\n')
        main_menu()
    else:
        print('login gagal coba lagi..')
        NomorTelepon()
 
def tanya():
    tanya = input('kembali ke menu..? (y/n)')
    if tanya == 'y':
        main_menu()
    elif tanya == 't':
        exit()
    else:
        print('input salah')
        print('masukan input dengan benar')

def main_menu():
    # membuat daftar fitur pada E-Bako
    print('=' * 10, 'WELCOME TO E-BAKO', '=' * 10)
    print('MUDAH, BERMUTU, DAN TERPERCAYA')
    print('=' * 20, 'Pilih Fitur Aplikasi', '=' * 20)
    print('1. I-Bako')
    print('2. Mosi-Bako')
 
    # input pilihan
    pilihan = input('pilih menu: ')
 
    # pilihan menu
    if pilihan == '1':
        I_Bako()
    elif pilihan == '2':
        Mosi_Bako()
    else:
        print(' ')
        exit()

 
def I_Bako():
    # masukan input dari user
    nama_barang = input('masukan pesanan anda: ')
    harga = int(input('masukan harga barang: '))
    jumlah_beli = int(input('masukan jumlah barang yang anda beli: '))
 
    # mengitung jumlah harga
    total = harga * jumlah_beli
     
    # cetak total harga
    print(f'harga total: {nama_barang}, = {total}')
 
    # input pembayaran dari user
    bayar = int(input('masukan pembayaran: '))
 
    # mengecek apakah pembayaran kurang atau ada kembalian
    kurang = total - bayar
    kembalian = bayar - total
 
    if bayar > total:
        print(f'jumlah kembalian anda adalah {kembalian}')
        tanya()
     
    elif bayar == total:
        print('uang anda pas, terimakasih telah berbelanja ')
 
    else:
        print(f'maaf uang anda tidak cukup, uang anda kurang {kurang}')
        counter_kasir()

# membuat program kasir resto sederhana
def counter_kasir():
    counter = input('hitung lagi: (y/n)')
    if counter == 'y':
         
        kasir()
     
    elif counter == 'n':
        print('ingin hitung lagi..?')
        tanya()
     
    else:
        print('input program salah harap ulangi')

        
# membuat kalkulator
def Mosi_Bako():
    print('=' * 10)
    print('Program Kalukator')
 
    print()
    print('Operator')
    print('=' * 10)
    print('1. tambah')
    print('2. kurang ')
    print('3. bagi')
    print('4. kali')
    print('5. sisa bagi/modulus')
 
    a = int(input('masukan bilangan pertama: '))
    b = int(input('masukan bilangan ke-dua: '))
 
    operator = input('masukan operator: ')
 
    if operator == '1':
        print('hasil dari {} + {} = {}'.format(a, b, a + b))
    elif operator == '2':
        print('hasil dari {} - {} adalah {}'.format(a, b, a - b))
    elif operator == '3':
        print('hasil dari {} / {} = {}'.format(a, b, a / b))
    elif operator == '4':
        print('hasil dari {} * {} = {}'.format(a, b, a * b))
    elif operator == '5':
        print('hasil dari {} % {} = {}'.format(a, b, a % b))
    else:
        print('masukan input yang benar sesuai menu diatas')
 
# main program
if __name__=='__main__':
    main_login()