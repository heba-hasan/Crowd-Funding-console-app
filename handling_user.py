from datetime import datetime
import User_Menu as menu

import json
import re

wrongpass=0
def read_id(filepath):
    try:
        fileobj = open(filepath, 'r')
    except Exception as e:
        print(e)
    else:
        ID = fileobj.read()
        fileobj.close()
        return ID


def generate_id(filepath, id):
    try:
        fileobj = open(filepath, 'w')
    except Exception as e:
        print(e)
    else:
        print(fileobj)
        generated_id = int(id) + 1
        fileobj.write(str(generated_id))
        fileobj.close()

def login():
    email = input("enter your Email\n")
    password = input("enter your Password\n")
    for u in users:
        if u["email"] == email and u["password"] == password:
            wrongpass = 0
            userid = u["id"]
            print("Logining Done!\n")
            menu.afterlog(userid)
            break
        else:
            wrongpass = 1
    if wrongpass == 1:
        print("wrong email or password\n\n")

def register():
    First_name = input("enter your first name\n")
    Last_name = input("enter your last name\n")
    Email = input("enter your Email\n")
    Password = input("enter your Password\n")
    confirm_password = input("enter your Password again\n")
    phone = input("enter your phone\n")
    if (confirm_password == Password) and mailvalidation(Email):
        generate_id("id.txt", read_id("id.txt"))
        user = {
            "id": read_id("id.txt"),
            "fname": First_name,
            "lname": Last_name,
            "email": Email,
            "password": Password,
            "phone": phone,
            "projects": []
        }
        save_json("users.json", user)
        print("Registration done!")
    else:
        print("your info not valid")
def readfromjson(file_path):
    try:
        fileobj = open(file_path, 'r')
        data = json.load(fileobj)
    except Exception as e:
        print(e)
        return []
    else:
        return data


def save_json(file_path, data):
    projs = readfromjson(file_path)
    # print(f"old book, {old_books}")
    projs.append(data)
    try:
        with open(file_path, 'w') as fileobj:
            json.dump(projs, fileobj)
            return True
    except Exception as e:
        print(e)
        return False


def save_json2(file_path, data):
    try:
        with open(file_path, 'w') as fileobj:
            json.dump(data, fileobj)
            return True
    except Exception as e:
        print(e)
        return False

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
users = readfromjson("users.json")
def mailvalidation(email):

    valid_email=0
    if re.match(regex, email):
        for u in users:
            print(u["email"])
            if u["email"] == email:
                valid_email = 0
                print("email exists")
                return False
            else:
                valid_email=1
        if valid_email==1:
            print("triuuuu")
            return True
    else:
        print("email not valid")
        return False


def validate_date(start_time, end_time):
    try:
        start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M')
        end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M')

        if start_time < end_time:
            print(f"Start time: {start_time}")
            print(f"End time: {end_time}")
            return True
        else:
            print("Start time should be earlier than end time. Please try again.")
            return False
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD HH:MM format.")
        return False

users = readfromjson("users.json")
