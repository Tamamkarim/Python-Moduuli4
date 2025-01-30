
correct_username = 'Karim'
correct_password = '123'

attempts = 0
max_attempts = 5

while attempts < max_attempts:
    username = input("Username: ")
    password = input("password : ")
    if username == correct_username and password == correct_username:
        print("Welcome")
        break
    attempts += 1
else:
    print("access denied")