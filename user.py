import database as db

print("Fill in the following fields to continue")
contact=input("Enter contact :")
def login():

    if len(contact)==10 and contact.isdigit()==True:
        pin=input("Pin : ")
        if len(pin)==5 and pin.isdigit() ==True:
            return db.user_login(contact,pin)
        else:
            print("Wrong pin entry")            
    else:
        print("Invalid contact")
def send():
    return db.user_send(contact)
def withdraw():
    return db.withdraw(contact)                        
def account():
    pin=input("Pin : ")
    if len(pin)==5 and pin.isdigit() ==True:
            return db.view_useraccount(contact,pin)
    else:
            print("Wrong pin entry")
            print("1. Forgot pin")
            print("0. Exit")
            num=input("Choose option : ")
            if num=="0":
                return
            elif num=="1":
                return forgotpin()    
            else:
                print("Invalid MMI code")   
def changepin():
    return db.changeuserpin(contact)
def airtimebalance():
    return db.user_airtime(contact)
    
def setrecovery():
    return db.set_userrecovery(contact)
def forgotpin():
    return db.forgotpin(contact)

def main():
    login()
    while True:
        print("-------------Welcome----------")
        print("1.Airtme/bundles")
        print("2.Send  money")
        print("3. Withdraw cash")
        print("4.My number ")
        print("5. Self help")
        

main()