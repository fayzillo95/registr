import os
import json
import shutil
import string
import random as rd
from abc import ABC,abstractmethod

   
class Muallif:
    def __init__(self):
        pass

    def search_author(self,nomi):
        os.system("cls")
        with open("Kitoblar.json", "r") as f:

            kitob_list = json.load(f)
        
            for key, value in kitob_list["books"].items():
                if nomi == value["muallif"]["Ismi"]:
                    print(f"\nKitob topildi nomi >> {value["Nomi"]} \nJaniri >>> {value["janiri"]}\nMuallif   \"{value["muallif"]["Ismi"]} {value["muallif"]["Familiya"]}\"")

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
                                "muallif":{"Ismi": value["muallif"]["Ismi"],
                                            "Familiya":value["muallif"]["Familiya"],
                                            "Narxi": narx}}


        with open("kitob_narxli_list.json", "w") as file1:
            json.dump(kitoblar, file1, indent=3)

    def aftor_list(self):

        with open("Kitoblar.json", "r") as f:

            kitob_list = json.load(f)
            print("\n____________________________________________________________________________________________")    

            for key, value in kitob_list["books"].items():
                print(f"Nomi {value["Nomi"]} \nJaniri {value["janiri"]}\nMuallifi >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\
                       \nIsmi    {value["muallif"]["Ismi"]} \nFamiliya {value["muallif"]["Familiya"]} ")
                print("\n____________________________________________________________________________________________")    


class Kitoblar(Muallif):

    def __init__(self):
        super().__init__()

    def search_book(self,nomi):
        os.system("cls")
        with open("Kitoblar.json", "r") as f:

            kitob_list = json.load(f)
        
            for key, value in kitob_list["books"].items():
                if nomi == value["Nomi"]:
                    print(f"\nKitob topildi nomi >> {value["Nomi"]} \nJaniri >>> {value["janiri"]}\nMuallif   \"{value["muallif"]["Ismi"]} {value["muallif"]["Familiya"]}\"")

    def printer(self):

        with open("Kitoblar.json", "r") as f:

            kitob_list = json.load(f)
            print("\n____________________________________________________________________________________________")    

            for key, value in kitob_list["books"].items():
                print(f"Nomi {value["Nomi"]} \nJaniri {value["janiri"]}\nMuallifi >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\
                       \nIsmi    {value["muallif"]["Ismi"]} \nFamiliya {value["muallif"]["Familiya"]} ")
                print("\n____________________________________________________________________________________________")    

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
        


def head():
    ls = Kitoblar()
    ls.add_book()

head()    

