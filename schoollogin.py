def validemail(email, password):
    if type(email) != str:
        return ("Error: Your email must be in a string datatype format.")
    if type(password) != str: 
        return ("Error: Your password must be in a string datatype format.")
    if "@" not in email:
        return ("Error: Invalid Email Format. Your email must contain an @ symbol.")
    if len(password) < 8:
        return ("Error: Your password must be at least 8 digits.")
    if not any (i.isdigit() for i in password):
        return ("Error: Your password must contain at least one mumerical digit.")
    if not any (i.isupper() for i in password):
        return ("Error: Your password must contain at least one uppercase letter.")
    else:   
        return (f"Your account has successfully been created. Here is your email: {email} and password: {password}.")
print (validemail("testing@gmail.com", "Testing2")) 