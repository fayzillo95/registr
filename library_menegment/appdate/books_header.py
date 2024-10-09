import os
from class_all import Muallif,Kitoblar

def head():
     print(os.getcwd())
     casein = int(input(" 1. Kitoblar ro'yhati\
        \n 2. Mualliflar ro'yhati\n : "))
     
     match(casein):
          case 1:
               ls = Kitoblar()
               print(os.getcwd())
               ls.printer()
               os.chdir("../../..")
          case 2:
               ls = Muallif()
               print(os.getcwd())
               ls.aftor_list()
               print(os.getcwd())
               os.chdir("../../..")

head()          


