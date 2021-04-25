import random

pwd_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%&*/-_+=?"

choice = 0
while choice != "n":
    pwd_len = int(input("Enter the length of password you require: "))
    no_of_pwd = int(input("How many passwords do you want? "))
    for i in range(0, no_of_pwd):
        password = ""
        for x in range(0, pwd_len):
            pwd = random.choice(pwd_chars)
            password = password + pwd
        print("Your password is:", password)
    choice = input("Do you want to continue?(Y/N)\n")
    choice = choice.lower()
