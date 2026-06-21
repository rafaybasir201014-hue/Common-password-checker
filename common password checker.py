import time
time.sleep(1)
print("Hi! so lets check the password which you have entered is a common one or not")
time.sleep(2)
while True:
    password=input("Enter your password here").strip()
    if len(password)<8:
        print("password is too short at least have 8 characters")
        continue
    elif not any(char.isupper() for char in password):
        print("At least have one upper case character")
        continue
    else:
        print("password meets basic requirements.Checking if its too common or not")

        with open ("common passwords" ,"r" ) as file:
                                            common_passwords=[line.strip().lower() for line in file]
        if password.lower() in common_passwords:
            print("The password is way too common select a new one")
        else:
            print("Good this password will work")
            break
