import json
import os

def add_user(url_data : str, user):

    new_user = {
        "username" : user.username,
        "company_name" : user.company_name,
        "logo" : user.logo,
        "admin" : user.admin,
        "password" : user.password
    }
    # print(str(new_user))

    with open(url_data, 'w', encoding='UTF-8') as file:
        json.dump(new_user, file, ensure_ascii=False, indent=4)



# class User:
#     def __init__(self,username,company_name,logo,password):
#         self.username = username
#         self.company_name = company_name
#         self.logo = logo
#         self.password = password

# usuario = User("maurizio","sadf","swaddf","sawdf")

# add_user("E:\\programacion\\sistema de empresas (EL puro)\\backend\\client\\routers\\data\\data.json",
#         usuario)
