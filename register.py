def register() :
    username = input("Masukkan Username Baru :")
    password = input("Masukkan Password Baru : ")

    with open('user.csv', 'r') as file :
        csv_reader = csv.reader(file, delimiter=",")
        for row in csv_reader :
            dataa
def Login() :
    pass

pilihan = input("Login / Register? (L/R) : ")

if pilihan == "R":
    Register()
elif pilihan == "L" :
    Login()
else :
    print("Tidak Sesuai")