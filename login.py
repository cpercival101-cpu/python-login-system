username = "Cpercival"
password = "489150"
attempts = 3

while attempts > 0:
    input_username = input("Enter username: ")
    input_password = input("Enter password: ")
    if input_username == username and input_password == password:
        print(f"Hello {input_username}, happy to see you're back!")
        break
    else:
        attempts -= 1
        print(f"Incorrect username or password. You have {attempts} attempts left.")
        if attempts == 0:
            print(f"Too many failed attempts. Account locked for 24 hours.")
