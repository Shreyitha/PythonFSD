import getpass
class PasswordManager:
    def get_password(self):
        try:
            password = getpass.getpass("Enter your password: ")
            return password

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
password_manager = PasswordManager()

try:
    user_password = password_manager.get_password()
    if user_password.isnumeric() or len(user_password)<9 ==  True:
                 print("password is weak - contains only numbers.")
    elif user_password.isalpha() or len(user_password)<9 == True:
                 print("password is weak - contains only letters.")
    else:
                 print("Password is strong")             
   

except KeyboardInterrupt:
    print("\nPassword input was interrupted.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")