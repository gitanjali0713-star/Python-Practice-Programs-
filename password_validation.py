import re 
password = input("Enter your password :")
pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
if re.match(pattern,password): 
    print("Valid password")
else:
    print("Invalid password.")
