# Software to generate secure passwords meeting advanced security criteria
# Password security requirements:
# - At least 8 characters
# - Maximum length chosen by the user
# - At least one uppercase letter
# - At least one lowercase letter
# - At least one number
# - At least one special character
# - No more than three identical consecutive characters
# Version 1.1
# Developed by Gualtiero @Gualty https://github.com/Gualty

import secrets
import string
import sys

# Constants
MIN_PASSWD_LEN = 8
MAX_PASSWD_LEN = 1000


def has_consecutive_identical_chars(password):
    """
    Checks if the password contains three identical consecutive characters.

    Args:
        password (str): The password to check.

    Returns:
        bool: True if the password contains three identical consecutive characters, False otherwise.
    """
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return True
    return False


def generate_password(passwd_len, special=True, numbers=True, uppercase=True):
    """
    Generates a secure password meeting the specified security criteria.

    Args:
        passwd_len (int): The length of the password to generate.
        special (bool): If True, includes special characters in the password.
        numbers (bool): If True, includes numbers in the password.
        uppercase (bool): If True, includes uppercase letters in the password.

    Returns:
        str: The generated password that meets the security criteria.
    """
    special_chars = "!@#%&/()=?"
    pool = string.ascii_lowercase
    required = [secrets.choice(string.ascii_lowercase)]

    if uppercase:
        pool += string.ascii_uppercase
        required.append(secrets.choice(string.ascii_uppercase))
    if numbers:
        pool += string.digits
        required.append(secrets.choice(string.digits))
    if special:
        pool += special_chars
        required.append(secrets.choice(special_chars))

    if len(pool) == 0:
        raise ValueError("You must select at least one character type to generate the password.")

    while True:
        password = required[:]
        while len(password) < passwd_len:
            password.append(secrets.choice(pool))
        secrets.SystemRandom().shuffle(password)
        passwd_str = ''.join(password[:passwd_len])
        if not has_consecutive_identical_chars(passwd_str):
            return passwd_str


def show_help():
    """
    Shows the help message with the description of available options.
    """
    help_message = """
            Usage: python3 secure_passwd_gen.py [LENGTH] [OPTIONS]
        
            Generates a secure password with the following options:
        
            LENGTH
                Specifies the length of the password to generate (minimum 8 characters).
        
            OPTIONS:
                --no-special    Excludes special characters from the password.
                --no-numbers    Excludes numbers from the password.
                --no-uppercase  Excludes uppercase letters from the password.
                -h, --help      Shows this help message.
        
            Example:
                python3 secure_passwd_gen.py 12 --no-special --no-numbers
                This command generates a 12-character password containing only lowercase and uppercase letters.
            """
    print(help_message)


def main():
    """
    Main function that handles user input and generates the password.
    """
    if len(sys.argv) > 1:
        if '-h' in sys.argv or '--help' in sys.argv:
            show_help()
            return

        try:
            passwd_len = int(sys.argv[1])
            if passwd_len < MIN_PASSWD_LEN or passwd_len > MAX_PASSWD_LEN:
                raise ValueError

            special = '--no-special' not in sys.argv
            numbers = '--no-numbers' not in sys.argv
            uppercase = '--no-uppercase' not in sys.argv

            password = generate_password(passwd_len, special, numbers, uppercase)
            print(f"\033[1m{password}\033[0m")
        except ValueError:
            print(
                f"The password must be at least {MIN_PASSWD_LEN} characters and at most {MAX_PASSWD_LEN}. Please enter only valid numeric values.")
    else:
        print("Secure Password Generator")
        while True:
            try:
                passwd_len = int(input("Enter the password length: "))
                if passwd_len < MIN_PASSWD_LEN or passwd_len > MAX_PASSWD_LEN:
                    raise ValueError

                special = input("Use special characters? (yes/no, default: yes): ").strip().lower() != 'no'
                numbers = input("Use numbers? (yes/no, default: yes): ").strip().lower() != 'no'
                uppercase = input("Use uppercase letters? (yes/no, default: yes): ").strip().lower() != 'no'

                break
            except ValueError:
                print(
                    f"The password must be at least {MIN_PASSWD_LEN} characters and at most {MAX_PASSWD_LEN}. Please enter only valid numeric values.")

        password = generate_password(passwd_len, special, numbers, uppercase)
        print(f"The generated password is: \033[1m{password}\033[0m")


if __name__ == "__main__":
    main()
