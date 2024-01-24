import getpass as gp

class PasswordManager:
    def get_password(self):
        try:
            password = gp.getpass("Enter your password: ")

            return password

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

password_manager = PasswordManager()

try:
    user_password = password_manager.get_password()
    #print("Password entered:",user_password)

    passwordd = list(user_password)
    for i in range(0,len(user_password),2):
        passwordd[i] = "*"
    print("Password entered:","".join(passwordd))

except KeyboardInterrupt:
    print("\nPassword input was interrupted.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
