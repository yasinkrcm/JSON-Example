import json
import os

class User:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.emal = email
        

class UserRepository:
    def register(self):
        pass
    def login(self):
        pass
    def savetoFile(self):
        pass
     






while True:
    print("Menü".center(50,"*"))
    secim = input("1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\nSeçiminiz: ")
    if secim == "5":
        break
    else:
        if secim == "1":
            #register
            pass
        elif secim == "2":
            #Login
            pass
        elif secim == "3":
            pass #Logout
        elif secim == "4":
            pass #display username
        else:
            print("Lütfen belirtilen seçenekleri seçiniz")