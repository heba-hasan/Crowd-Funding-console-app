import handling_user as hs
import maain

def isempty(word):
    if word.strip() and word:
        return True
    else:
        print("filed should not be empty")
        return False

def createproject(u_id):
    Title = input("title:")
    Details = input("Details:")
    Total_target = input("Total target:")
    start_date = input("start data:")
    end_date = input("end data:")
    if hs.validate_date(start_date, end_date) and isempty(Title) and isempty(Details) and isempty(Total_target) and Total_target.isdigit()  :
        hs.generate_id("pr_id.txt", hs.read_id("pr_id.txt"))
        project = {
            "id": hs.read_id("pr_id.txt"),
            "title": Title,
            "details": Details,
            "total_target": Total_target,
            "start_date": start_date,
            "end_date": end_date,
        }
        for u in hs.users:
            if u["id"] == u_id:
                u["projects"].append(project)
                hs.save_json2("users.json", hs.users)
                break



def editproject(u_id):
    found_p_id=0
    edited = 0
    while True:
        pro_id = input("enter your project ID\n")
        if pro_id.isdigit():
            for u in hs.users:
                if u["id"] == u_id:
                    for p in u["projects"]:
                        if pro_id == p["id"]:
                            found_p_id = 0
                            field = input("enter the filed you want to update:")
                            if field in p:
                                newvalue = input("enter new value:")
                                p[field] = newvalue
                                hs.save_json2("users.json", hs.users)
                                edited=1
                                print("project edited")
                                break
                            else:
                                print("invalid field")
                        else:
                            found_p_id=1

                    if found_p_id==1:
                        print("invalid project ID")
                        continue
                    break
            if edited==1:
                break

def delproject(u_id):
    found_p_id = 0
    deleted=0
    while True:
        pro_id = input("enter your project ID:")
        if pro_id.isdigit():
            for u in hs.users:
                if u["id"] == u_id:
                    for i in range(len(u["projects"])):
                        if pro_id == u["projects"][i]["id"]:
                            found_p_id = 0
                            u["projects"].pop(i)
                            hs.save_json2("users.json",hs.users)
                            deleted = 1
                            print("deleted")
                            break
                        else:
                            found_p_id = 1
                    if found_p_id == 1:
                        print("invalid project ID")
                    break
                if deleted == 1:
                    break
        break

def searchproject(u_id):
    found_p_id=0
    while True:
        pro_id = input("enter your project ID")
        if pro_id.isdigit():
            for u in hs.users:
                if u["id"] == u_id:
                    for i in range(len(u["projects"])):
                        if pro_id == u["projects"][i]["id"]:
                            print(u["projects"][i])
                            break
                        else:
                            found_p_id = 1
                    if found_p_id == 1:
                        print("invalid project ID")
            break
def viewprojects(u_id):
    for u in hs.users:
        if u["id"] == u_id:
            print(u["projects"])
            break

