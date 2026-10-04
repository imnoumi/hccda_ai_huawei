with open('password.txt', 'r') as f:
    password = f.read()

#change  password
old = input("Enter the old password: ")

if old == password:
    new = input("Enter the new password: ")
    with open('password.txt', 'w') as f:
        f.write(new)
    print("Password changed successfully. and your new password is: ", new)
else:
    print("Incorrect old password.")