


class Login:
    def masuk():    
        global connection
        print('=' * 20, 'Ingin Masuk Menjadi Apa?', '=' * 20)
        print('1. Admin')
        print('2. Pembeli')
 
        # input pilihan
        pilihan = input('Pilih Login: ')
 
        # pilihan menu
        if pilihan == '1':
            Admin() 
        elif pilihan == '2':
            Pembeli()
        else:
            print('')
            exit()

    def Admin():
        global connection
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

    def Google():
        global connection
        print('=' * 20)
        print('Halaman Login Google')
        username = input("Username: ")
            password = input("Password: ")
            query = f'SELECT*FROM Admin WHERE username = "{username}" AND password = "{password}"'
            hasil = self.execute(query)
            for row in hasil:
                if username and password in row:
                    print("Selamat Datang Admin")
                    from Utama import Utama
                    
            else:
                print("Username dan Password Salah")
 
# membuat fungsi authentifikasi sederhana
def NomorTelepon():
    global connection
    print('=' * 20)
    print('Halaman Login Nomor Telepon')
    nomortelepon = input('masukan nomor telepon anda: ')
 
    if nomortelepon == '081234567890' :
        print('login berhasil...\n\n')
        main_menu()
    else:
        print('login gagal coba lagi..')
        NomorTelepon()
        

def Pembeli():
    global connection
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
    global connection
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
    global connection
    print('=' * 20)
    print('Halaman Login Nomor Telepon')
    nomortelepon = input('masukan nomor telepon anda: ')
 
    if nomortelepon == '081230784383' :
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

while True:
    user=int(input("1.Pemilik \n2.Kasir \nPilih: "))
    if user == 1:
        loginPemilik()
    elif user == 2:
        loginKasir()
    else:
        print("Pilihan tidak ada")