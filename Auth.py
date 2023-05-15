import re
import os
import json

# ---------class Auth----------
class Auth:
    def __init__(self):
        self.users = []
# ---------Auth menu func----------
    def menu(self):
        print("Welcome to Main Menu :)")
        print("1- Register")
        print("2- Login")
        print("3- Exit")
        choice = input("Enter your choice :) ")
        while True:
            if choice == "1":
                self.reg()
            elif choice == "2":
                self.login()
            elif choice == "3":
                break
            else:
                print("Invalid input")
                
# ---------Reg func----------

    def reg(self):
        self.fname = self.check_first_name()
        self.lname = self.check_last_name()
        self.email = self.check_email()
        self.passw = self.get_password()
        self.phone = self.get_phone()

        self.user = {
            "first_name": self.fname,
            "last_name": self.lname,
            "email": self.email,
            "password": self.passw,
            "phone": self.phone
        }

        self.users.append(self.user)
        print("Registration success :)")
        print(self.users)
        self.file_txt()
        self.menu()
        
        
# ---------check first name func----------
    def check_first_name(self):
        f_name = input("Enter your first name :) ")
        if len(f_name.strip()) == 0:
            print("First name cannot be empty")
            return self.check_first_name()
        else:
            return f_name
# ---------check last name func----------
    def check_last_name(self):
        l_name = input("Enter your last name :) ")
        if len(l_name.strip()) == 0:
            print("Last name cannot be empty")
            return self.check_last_name()
        else:
            return l_name
# ---------check email func----------
    def check_email(self):
        em = input("Enter your email :")
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
        if (re.fullmatch(regex, em)):
            print("Valid email")
            return em
        else:
            print("Invalid email")
            return self.check_email()
# ---------Pssw and confirm passw func----------
    def get_password(self):
        self.password = input("Enter your password :) ")
        self.confirm_password()
        return self.password

    def confirm_password(self):
        con_pass = input("Confirm your password: ")
        if (con_pass == self.password):
            return con_pass
        else:
            print("Passwords do not match.")
            return self.confirm_password()

# ---------check phone egyptian num func----------
    def get_phone(self):
        phone_num = input(
            "Enter your phone number (should be Egyptian number): ")
        phone_regex = r"^01[0125][0-9]{8}$"
        if (re.fullmatch(phone_regex, phone_num)):
            print("Valid phone number")
            return phone_num
        else:
            print("Invalid phone number")
            return self.get_phone()

# ---------making func to append and write users data in data.txt----------
    def file_txt(self):
        my_file = "data.txt"
        if os.path.isfile(my_file):
            with open(my_file, "a") as f:
                f.write(json.dumps(self.user) + "\n")
        else:
            with open(my_file, "w") as f:
                f.write(json.dumps(self.user) + "\n")

# ---------login func to go to projects menu----------
    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        with open("data.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                user_data = json.loads(line.strip())
                if (user_data["email"] == email and user_data["password"] == password):
                    print("Login successful!")
                    class_project = Project()
                    class_project.display()

        print("Invalid email or password.")
        self.menu()


class Project:
    def __init__(self):
        self.data = []
        self.project_menu()

    def project_menu(self):
        print("Welcome to Projects Menu :)")
        print("1- Create Project")
        print("2- View all Projects")
        print("3- Edit Project")
        print("4- Delete Project")
        print("5- Exit")
        choice = input("Enter your choice :) ")
        while True:
            if choice == "1":
                self.create_project()
            elif choice == "2":
                self.view_all()
            elif choice == "3":
                self.edit()
            elif choice == "4":
                self.delete()
            elif choice == "5":
                break
            else:
                print("Invalid input")
                self.project_menu()

    def create_project(self):
        self.project_name = input("Enter project name: ")
        self.project_description = input("Enter project description: ")
        self.total_target = input("Enter your total target: " )
        self.project_start_date = input("Enter project start date: ")
        self.project_end_date = input("Enter project end date: ")
        self.owner_project_phone = input("Enter your Phone for every project must be one phone num: ")

        self.project = {
            "project_name": self.project_name,
            "project_description": self.project_description,
            "total_target": self.total_target,
            "project_start_date": self.project_start_date,
            "project_end_date": self.project_end_date,
            "owner":self.owner_project_phone
        }
        self.data.append(self.project)
        print("Project created successffully :)")
        print(self.project)
        self.file_txt()
        self.project_menu()

        
    def file_txt(self):
        my_file = "projects.txt"
        if os.path.isfile(my_file):
            with open(my_file, "a") as f:
                f.write(json.dumps(self.project) + "\n")
        else:
            with open(my_file, "w") as f:
                f.write(json.dumps(self.project) + "\n")

    def view_all(self):
        try:
            with open("projects.txt", "r") as f:
                my_file = f.read()
        finally:
            f.close()  
        print(my_file)
        self.project_menu()
        
        
    #--------edit function i connect it with user phone number because it will be unique-------
    
    def edit(self):
        project_name = input("Enter project name: ")
        owner_phone = input("Enter your phone number: ")  # Prompt the user for their phone number
        found_project = None
        with open("projects.txt", "r") as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                user_data = json.loads(line.strip())
                if user_data["project_name"] == project_name and user_data["owner"] == owner_phone:
                    found_project = user_data
                    break

            if found_project is None:
                print("Project not found or you are not the owner :(")
                self.project_menu()
                return

            print("Editing project...")
            new_project_name = input(f"Enter new project name ({found_project['project_name']}): ")
            found_project["project_name"] = new_project_name if new_project_name else found_project["project_name"]
            new_project_description = input(f"Enter new project description ({found_project['project_description']}): ")
            found_project["project_description"] = new_project_description if new_project_description else found_project["project_description"]
            new_total_target = input(f"Enter new total target ({found_project['total_target']}): ")
            found_project["total_target"] = new_total_target if new_total_target else found_project["total_target"]
            new_start_date = input(f"Enter new start date ({found_project['project_start_date']}): ")
            found_project["project_start_date"] = new_start_date if new_start_date else found_project["project_start_date"]
            new_end_date = input(f"Enter new end date ({found_project['project_end_date']}): ")
            found_project["project_end_date"] = new_end_date if new_end_date else found_project["project_end_date"]

            # Update the line in the file with the updated project data
            lines[i] = json.dumps(found_project) + "\n"

            # Rewrite the entire file with the updated data
            with open("projects.txt", "w") as f:
                f.writelines(lines)

            print("Project updated successfully :)")
            self.project_menu()
        
    def delete(self):
        owner_phone = input("Enter your phone number: ")
        project_name = input("Enter project name: ")

        found_project = None
        with open("projects.txt", "r") as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                project_data = json.loads(line.strip())
                if project_data["owner"] == owner_phone and project_data["project_name"] == project_name:
                    found_project = project_data
                    break

            if found_project is None:
                print("Project not found or you are not the owner")
            

            if found_project["owner"] != owner_phone:
                print("You are not the owner of this project")
            

            del self.data[i]

            with open("projects.txt", "w") as f:
                for project in self.data:
                    f.write(json.dumps(project) + "\n")

            print("Project deleted successfully")
    

    

            
aut_system = Auth()
aut_system.menu()




    # def delete(self):
    #     project_name = input("Enter project name: ")
    #     owner_phone = input("Enter your phone number: ")

    #     found_project = None
    #     with open("projects.txt", "r") as f:
    #         lines = f.readlines()
    #         for i, line in enumerate(lines):
    #             project_data = json.loads(line.strip())
    #             print (project_data)
                # if project_data["project_name"] == project_name and project_data["owner"] == owner_phone:
                #     found_project = project_data
                #     self.data.append(found_project)
                #     print (self.data)
                #     print (i)
        #         break

        # if found_project is None:
        #     print("Project not found or you are not the owner :)")
        #     self.project_menu()
        #     return
        # print (self.data)
        # print (i)
        # print (self.data[i])
        # del self.data[i]

        # with open("projects.txt", "w") as f:
        #     for project in self.data:
        #         f.write(json.dumps(project) + "\n")

        # print("Project deleted successfully :)")
        # self.project_menu()

# def edit (self):
        # project_name = input("Enter project name: ")
        # owner_project_phone = input("Enter your phone: ")
        # found_project = None
        # with open ("projects.txt","r") as f :
        #     lines = f.readlines()
        #     for line in lines:
        #         user_data = json.loads(line.strip())
                # print(user_data["project_name"])
                # if(user_data["project_name"] == project_name and user_data["owner"] == owner_project_phone):
                #     print(user_data)
                #     print("you can edit in this file")
                    # self.project_menu()
                    # new_project_name = input("Enter your new project name: ")
                    # new_project_description = input("Enter your new project description: ")
                    # new_total_target = input("Enter your new total target: ")
                    # new_start_date = input("Enter your new start date: ")
                    # new_End_date = input("Enter your new end date: ")
                    # owner_project_phone = input("Enter your phone number : ")
                    # user_data["project_name"] = new_project_name
                    # user_data["project_description"] = new_project_description
                    # user_data["total_target"] = new_total_target
                    # user_data["project_start_date"] = new_start_date
                    # user_data["project_end_date"] = new_End_date
                    # user_data["owner"] = owner_project_phone
                    # print(user_data)
                # else:
                #     print("you cant edit on file... you are not the owner or the project is not found")
                #     self.project_menu()