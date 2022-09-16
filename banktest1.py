
print("welcome to my bank")
account_creation =  input("would you like to create a account\n")
if account_creation == "yes":
    account_name = input("What do you want to name your account \n")
    account_pass = input("what password do you want \n")


else:
    print("no")



loginacc = account_name
loginpass = account_pass
login_attempt = input("Login \n User:")

if login_attempt == loginacc:
    print("Correct")

else:
    print("Try again")

login_attempt = input("Password:  ")

if login_attempt == loginpass:
    print("good")

else:
    print("bad")