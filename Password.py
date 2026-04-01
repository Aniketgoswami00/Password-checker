password = input("enter the password: ")
uppercase = False
lowercase = False 
digit     = False
has_special   = False

specialchar  = "@#*"

for char in password:
    if char.isupper():
        uppercase = True
    elif char.islower():
         lowercase = True
    elif char.isdigit():
         digit     = True
    elif char in specialchar:
        has_special = True
 
if (len(password) >= 8 and uppercase and lowercase and digit
    and has_special):
                    print("strong password")
else:                   
      print("weak password") 
    
