import csv

def login():
    username = input("masukan username = ")
    password = input("masukkan password = ")
    user=[]
    with open("user.csv") as data:
        user = csv.reader(data)
        for i in user:
            if username == i[0] and password == i[1]:
                if i[2] == '1':
                    tampilan_admin()
                elif i[2] == '2':
                    tampilan_user()
                else:
                    continue
                
def tampilan_user():
    print("selamat datang di homepage user")
def tampilan_admin():
    print("selamat datang di homepage admin")

login() 