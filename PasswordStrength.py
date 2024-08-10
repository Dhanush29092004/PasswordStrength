import re
password=input("Enter the password.")
if len(password) <8:
    print("Password must contain atleast 8 letters.")
elif not re.search("[A-Z]",password):
    print("Password must conatin atleast one uppercase letter.")
elif not re.search("[a-z]",password):
    print("Password must contain atleast one lowercase letter .")
elif not re.search("[0-9]",password):
    print("Password must contain atleast one number.")
else:
    print("Password is Strong")

    