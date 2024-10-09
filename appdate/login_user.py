import json
import os
import random as rd
import string

from datetime import datetime as d_time

sana = d_time.today()
sana = d_time.strftime(sana, "%Y.%m.%d %H:%M")

class Person:

    def __init__(self, user_dct):
        
        
        new_items = self.name_test(user_dct["Username"]) 
        f_name = self.fname_test(user_dct["Firstname"]) 
        l_name = self.lname_test(user_dct["Lastname"]) 
        email = self.email_test(user_dct ["Email"])
        password = self.password_test(user_dct ["Password"]) 
        user_id = user_dct ["id"]

        user_dct = {
            "Username": new_items,
            "Firstname": f_name,
            "Lastname": l_name,
            "id": user_id,
            "Email": email,
            "Password": password,
            "Sana": sana
        }
        
        self.file_reader(user_dct,"appdate","userinfo")
        self.__name = new_items
        self.__l_name = l_name
        self.__f_name = f_name
        self.email = email
        self.__id = user_id
        self.__password = password

        print(self.__name)
        print(self.__f_name)
        
   
    def name_test(self,new_name):
        
        if str.isalpha(new_name[0]):
            if new_name[0] == str.upper(new_name[0]):
                if len(new_name) > 4:
                    return new_name
                else:
                    print("Ismning bosh harfi katta harf bo'lishi kerak : ") 
                    new_items = input("Ismingizni qaytadan kiriting : ")
                    return self.name_test(new_items)
            else:    
                print("Ismningizda kamida 5 ta harf bo'lishi kerak : ") 
                new_items = input("Ismingizni qaytadan kiriting : ")
                return self.name_test(new_items)
        else:
            print("Ism harf bilan boshlanishi kerak : ")
            new_items = input("Ismingizni qaytadan kiriting : ")
            return self.name_test(new_items)

    def fname_test(self,new):

        if len(new) > 5:
            if new[0].isalpha():
                if  new[0].isupper():    
                     return new
                else:    
                    print("Familiyangiz harf bilan boshlanishi kerak : ")
                    new_items = input("Familiyangizni qaytadan kiriting : ")
                    return self.fname_test(new_items)

            else:
                print("Familiyaning bosh harfi katta harf bo'lishi kerak : ") 
                new_items = input("Familiyangizni qaytadan kiriting : ")
                return self.fname_test(new_items)
        else:
            print("Familiyaning uzuligi kamida 6 ta bo'lishi kerak : ") 
            new_items = input("Familiyangizni qaytadan kiriting : ")
            return self.fname_test(new_items)

    def lname_test(self,new):
        
        if str.endswith(str.lower(new),"o'g'li") or str.endswith(str.lower(new),"qizi"):
             if str.isupper(new[0]):
                return new
             else:
                print("Sharifingizning bosh harfi katta harf bo'lishi kerak: ") 
                new_items = input("Sharifingizni qaytadan kiriting: ")
                return self.lname_test(new_items)
        else:
            print("Sharifingiz 'o'g'li' yoki 'qizi' bilan tugashi kerak.")
            new_items = input("Sharifingizni qaytadan kiriting: ")
            return self.lname_test(new_items)
    

    def password_test(self,new):

        up_char = string.ascii_uppercase
        lwr_char = string.ascii_lowercase
        pnct_char = string.punctuation
        ls_all_char = [up_char,lwr_char,pnct_char]
        ball = 0
        ls_index = 0
        s = 0

        if len(new) > 8:

            while ls_index<3:
                s = 0    
                for i in new:
                    if i in ls_all_char[ls_index]:
                        s+=1 
                if s > 0:
                    ball +=1
                ls_index+=1

            if ball > 2:
                return new
            else:
                print("Paro'lda belgila katta harf va kichik harf qatnashgan bo'lishi lozim")
                new_items = input("Parolingizni qaytadan kiriting: ")
                return self.password_test(new_items)

        else:        
                print("Paro'lingiz kamida 8 ta bo'lishi kerak: ") 
                new_items = input("Parolingizni qaytadan kiriting: ")
                return self.password_test(new_items)
        
    def email_test(self,new):
        if "@" in new:
 
            p_index = str.index(new,"@")
 
            if p_index >= 3:
                 if new[p_index+1:] == "gmail.com" or new[p_index+1:] == "mail.ru":
                     return new   

                 else:        
                        print("Emailingizning @ dan keyingi qismida gmail.com yoki mail.ru  bo'lishi kerak: ") 
                        new_items = input("Emailingizni qaytadan kiriting: ")
                        return self.email_test(new_items)
            else:        
                    print("Emailingizning @ dan oldingi qismida kamida 4 ta harf bo'lishi kerak: ") 
                    new_items = input("Emailingizni qaytadan kiriting: ")
                    return self.email_test(new_items)
        else:        
                print("Emailingizda 2 bo'lishi kerak: ") 
                new_items = input("Emailingizni qaytadan kiriting: ")
                return self.email_test(new_items)

    @staticmethod
    def file_reader(dct_user_info: dict, path_one: str, path_two: str):
        
        if path_one in os.listdir():
            os.chdir(path_one)

        if path_two in os.listdir():
            os.chdir(path_two)
        
        user_file_json = f"{dct_user_info['Username']}_{dct_user_info['Firstname']}_.json"
        # user_file_ = f"{dct_user_info['Username']}_{dct_user_info['Fristname']}"  # print uchun
        try:
            with open(user_file_json, "w+") as f:
                json.dump(dct_user_info, f, indent=4)
                f.seek(0)

                os.chdir("../..")
        except:
            print("Fayl ochilmadi : ")
            os.chdir("../..")
        return 0

def open_path(username, user_fname):

    user_id = int(rd.randint(12345, 99999))
    if "appdate" in os.listdir():
        os.chdir("appdate")

    if "user_info" in os.listdir():
        os.chdir("user_info")

    test = f"{username}_{user_fname}_.json"


    
    if  test not in os.listdir():

         user_lname = input("Sharifingiz : ")
         u_email = input("Pochtangiz : ")
         password = input("Parolingiz : ")

         if "appdate" in os.listdir():
             os.chdir("appdate")

             if "user_info" not in os.listdir():
                 os.mkdir("user_info")

         if "user_info" in os.listdir():
             os.chdir("user_info")

         user_dct = {
             "Username": username,
             "Firstname": user_fname,
             "Lastname": user_lname,
             "id": user_id,
             "Email": u_email,
             "Password": password,
             "Sana": sana
         }


    else:
        print(f"{username} {user_fname} nomli foydalanuvchi oldin Ro'yhatga olingan : ")
        return 0
    print(os.getcwd())
    object_user = Person(user_dct)
