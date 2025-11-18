def validemail(email, password):
    passwordcount = 0
    passwordint = False
    if "@" not in email:
        return "Error: Invalid Email Format"
    for i in password:
        passwordcount+=1
        if password.isdigit():
            passwordint = True
    if passwordint != True:
        return "Error: Your password must contain at least one numerical digit."
    if passwordcount < 8:
        return "Error: Your password is too short. It must be at least 8 characters."
        
        
        
        print ("Your account has successfully been created.")
validemail()
    