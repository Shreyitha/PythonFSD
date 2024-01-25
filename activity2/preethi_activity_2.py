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
    print("Password entered: ********")  # Display asterisks instead of the actual password

except KeyboardInterrupt:
    print("\nPassword input was interrupted.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
