def validemail(email, password):
    emailvalid = False
    passwordlength = False
    passwordint = False
    passwordupper = False
    if type(email) != str:
        print ("Error: Your email must be in a string datatype format.")
    if type(password) != str: 
        print ("Error: Your password must be in a string datatype format.")
    if "@" not in email:
        print ("Error: Invalid Email Format. Your email must contain an @ symbol.")
    else: 
        emailvalid = True
    if len(password) < 8:
        print ("Error: Your password must be at least 8 digits.")
    else:
        passwordlength = True
    for i in password:
        if i.isdigit():
            passwordint = True
        if i.isupper():
            passwordupper = True
    if passwordint != True:
        print ("Error: Your password must contain at least one numerical digit.")
    if passwordupper != True:
        print ("Error: Your password must contain at least one uppercase letter.")
    if emailvalid == passwordlength == passwordint == passwordupper == True:
        print (f"Your account has successfully been created. Here is your email: {email} and password: {password}.")
validemail("testing@gmail.com", "Testing12")
