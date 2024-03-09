import re
import json

class Authentication:
    def __init__(self, users_file='users.json'):
        self.users_file = users_file
        self.logged_in_user_email = None

    def validatePhoneNumber(self, phone_number):
        pattern = r'^01[0-9]{9}$'
        return re.match(pattern, phone_number) is not None

    def validateEmailAddress(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def register(self):
        try:
            with open(self.users_file, 'r') as file:
                users_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            users_data = []

        print("Please complete the requested data below:")
        first_name = input("Enter Your First Name: ")
        last_name = input("Enter Your Last Name: ")
        email = input("Enter Your Email: ")
        if not self.validateEmailAddress(email):
            print("Invalid Email Address, please use the format example@email.com")
            return self.register()
        password = input("Enter The Password: ")
        password_confirmation = input("Confirm The Password: ")
        if password != password_confirmation:
            print("The password doesn't match")
            return self.register()
        phone_number = input("Enter An Egyptian Mobile number: ")
        if not self.validatePhoneNumber(phone_number):
            print("Invalid Phone Number")
            return self.register()
        user = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password,
            "phone_number": phone_number,
        }
        users_data.append(user)
        with open(self.users_file, 'w') as file:
            json.dump(users_data, file, indent=4)
        print("Registration successful")
    
    def login(self):
        try:
            with open(self.users_file, 'r') as file:
                users_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            users_data = []

        email = input("Enter Your Email Address: ")
        password = input("Enter Your Password: ")

        if not self.validateEmailAddress(email):
            print("Invalid Email Address, please use the format example@email.com")
            return

        for user in users_data:
            if user['email'] == email:
                if user['password'] == password:
                    print("Welcome To Your Account, You logged in successfully")
                    self.logged_in_user_email = email
                    return True
                else:
                    print("Incorrect Password")
                    return
        print("Email doesn't exist")

    def get_logged_in_user_email(self):
            return self.logged_in_user_email