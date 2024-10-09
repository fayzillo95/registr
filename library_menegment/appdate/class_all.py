import os
import json
import shutil
import string
import random as rd
from abc import ABC,abstractmethod

   
class Muallif:
    def __init__(self):
        if "appdate" in os.listdir():
            os.chdir("appdate")
        if "info" in os.listdir():
            os.chdir("info")
        if "author" in os.listdir():
            os.chdir("author")

    def search_author(self,nomi):

        os.chdir("../../..")
        if "appdate" in os.listdir():
            os.chdir("appdate")
        if "info" in os.listdir():
            os.chdir("info")
        if "books" in os.listdir():
            os.chdir("books")

        with open("Kitoblar.json", "r") as f:

            kitob_list = json.load(f)
        
            for key, value in kitob_list["books"].items():
                if nomi == value["muallif"]["Ismi"]:
                    print(f"\nKitob topildi nomi >> {value["Nomi"]} \nJaniri >>> {value["janiri"]}\nMuallif   \"{value["muallif"]["Ismi"]} {value["muallif"]["Familiya"]}\"")
        os.chdir("../../..")

    def printer(self):
        os.chdir("../../..")
        if "appdate" in os.listdir():
            os.chdir("appdate")
        if "info" in os.listdir():
            os.chdir("info")
        if "books" in os.listdir():
            os.chdir("books")

        with open("Kitoblar.json", "r") as f:

            kitob_list = json.load(f)
            print("\n____________________________________________________________________________________________")    

            for key, value in kitob_list["books"].items():
                print(f"Muallifi >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\
                       \nIsmi    {value["muallif"]["Ismi"]} \nFamiliya {value["muallif"]["Familiya"]} \nYozgan kitobi {value["Nomi"]} \nJaniri {value["janiri"]}\n")
                print("\n____________________________________________________________________________________________")    
        os.chdir("../../..")

    def aftor_list(self):

        os.chdir("../../..")
        if "appdate" in os.listdir():
            os.chdir("appdate")
        if "info" in os.listdir():
            os.chdir("info")
        if "books" in os.listdir():
            os.chdir("books")

        with open("Kitoblar.json", "r") as f:

            kitob_list = json.load(f)
            print("\n____________________________________________________________________________________________")    

            for key, value in kitob_list["books"].items():
                self.key = key
                print(f"Nomi {value["Nomi"]} \nJaniri {value["janiri"]}\nMuallifi >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\
                       \nIsmi    {value["muallif"]["Ismi"]} \nFamiliya {value["muallif"]["Familiya"]} ")
                print("\n____________________________________________________________________________________________")    
        os.chdir("../../..")


class Kitoblar(Muallif):

                       
    def __init__(self):
        if "appdate" in os.listdir():
            os.chdir("appdate")
        if "info" in os.listdir():
            os.chdir("info")
        if "books" in os.listdir():
            os.chdir("books")

    def search_book(self,nomi):
        os.system("cls")
        with open("Kitoblar.json", "r") as f:

            kitob_list = json.load(f)
        
            for key, value in kitob_list["books"].items():
                if nomi == value["Nomi"]:
                    print(f"\nMuallif   \"{value["muallif"]["Ismi"]} {value["muallif"]["Familiya"]}\"\
                          \nKitob topildi nomi >> {value["Nomi"]} \nJaniri >>> {value["janiri"]}")
        os.chdir("../../..")

    def printer(self):

        with open("kitob_list.json", "r") as f:

            kitob_list = json.load(f)
            print("\n____________________________________________________________________________________________")    

            for key, value in kitob_list.items():
                print(f"Nomi {value["Nomi"]} \nJaniri {value["janiri"]} \nNarxi {value["Narxi"]}")
                print("\n____________________________________________________________________________________________")    
        os.chdir("../../..")

    def file_writer(self):

        with open("Kitoblar.json", "r") as f:

            kitob_list = json.load(f)
            kitoblar = {}
            
            for key, value in kitob_list["books"].items():
                print(f"{value["Nomi"]}   {value["muallif"]["Ismi"]}\n_______________________________________________")    
                narx = int(input("Narxini bering : "))
                kitoblar[key] = {}  
                kitoblar[key] = {"Nomi":value["Nomi"],
                                "janiri":value["janiri"],
                                "Narxi": narx,
                                "muallif":{"Ismi": value["muallif"]["Ismi"],
                                            "Familiya":value["muallif"]["Familiya"]
                                            }}


        with open("kitob_narxli_list.json", "w") as file1:
            json.dump(kitoblar, file1, indent=3)
        os.chdir("../../..")

    def add_book(self):

        with open("kitob_narxli_list.json", "r") as f:
            kitob_list = json.load(f)
            nomi = input("Kitob nomini kiriting : ")
            janr = input("Kitob janirini kiriting : ")

            muallifi_name = input("muallif ismini kiriting : ")
            muallifi_fname = input("muallif familiyasini kiriting : ")
            muallifi_tahallus = input("muallif tahallusi kiriting : ")
            muallifi_tugilgan_shaxri = input("muallif tug'ilgan shaxarini kiriting : ")
            muallifi_tugilgan_sana = input("muallif tug'ilgan sanani kiriting\n namuna 2024.01.01 : ")
            narx = int(input("Narxini kiriting : "))

            for key, value in kitob_list.items():
                a = key

            c = int(a[len(a)-2::])
            c = c+1
            b = a[0:len(a)-2]+(str(c))
            print(b)
        
        kitob_list[b] = {"Nomi":nomi,
                        "janiri":janr,
                        "muallif":{"Ismi":muallifi_name,
                                    "Familiya":muallifi_fname,
                                    "Narxi": narx}}
        
        with open("kitoblar_new.json", "w+") as file2:
              json.dump(kitob_list,file2,indent=4)  
        
        with open("mualliflar.json", "r") as file1:
              muallif = json.load(file1)
              
              muallif [f"muallif_{c}"] = {
             "Ismi": muallifi_name,
             "Familiya": muallifi_fname,
             "Tahallus": muallifi_tahallus,
             "Tug'ilgan sana": muallifi_tugilgan_sana,
             "Tug'ilga shaxar": muallifi_tugilgan_shaxri,
             "kitobi": nomi}
              
        with open("muallif_new.json", "w+") as file3:
              json.dump(muallif,file3,indent=3)
        os.chdir("../../..")
        
