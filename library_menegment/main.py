import json
import os
from appdate import head







# with open("Kitoblar.json", "r") as f:

#     kitob_list = json.load(f)
#     mualliflar = {}
#     kitoblar = {}
#     raqami = 1

#     for key, value in kitob_list["books"].items():

#         mualliflar[f"muallif_{raqami}"] = value["muallif"]

#         mualliflar[f"muallif_{raqami}"]["kitobi"] = value["Nomi"]

#         kitoblar[key] = {}  
#         kitoblar[key] = {"Nomi":value["Nomi"],
#                           "janiri":value["janiri"],
#                           "muallif":{"Ismi": value["muallif"]["Ismi"],
#                                       "Familiya":value["muallif"]["Familiya"]}}

#         raqami += 1

# with open("mualliflar.json", "w") as file1:
#     json.dump(mualliflar, file1, indent=3)
