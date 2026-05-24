import database as db
print("Fill in the following fields to continue")
contact=input("Enter contact :")

def login():

    if len(contact)==10 and contact.isdigit()==True:
        pin=input("Pin : ")
        if len(pin)==5 and pin.isdigit() ==True:
            db.agent_login(contact,pin)
        else:
            print("Wrong pin entry")            
    else:
        print("Invalid contact")
           
login()    