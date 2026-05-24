import database as db

password="admin@123"
Pin="12345"
contact=input("Enter contact to initialize account: ")
email="adminadams@gmail.com"
def register():
    Id =input("Enter numeric id: ")   
    if Id.isdigit()==True:
        name=input("Enter name of administrator: ")
        value=int(Id)
        if len(name)>=3:
            contact=input("Contact: ")
            if contact.isdigit()==True :
                if len(contact)==10:
                    password=input("Password")
                    if len(password)>2:
                        confirmpassword=input("Confirm password:")
                        if password==confirmpassword:
                            balance=90000000.00
                            print("Admin account created successfully.....")
                            print(f"Default pin: {Pin}")
                            print("1.Use defualt pin: ")
                            print("2. Change pin: ")
                            num=input("Enter option: ")
                            if num=="1":
                                pin=Pin
                            elif num=="2":
                                pin =input("Enter new pin: ") 
                                if pin.isdigit()==True and len(pin):  
                                    pin1=input("Confirm new pin: ")
                                    if pin1==pin:
                                        address=("Enter operation area: ")
                                        db.add_admin(value,name,email,contact,password,pin,balance,address)
                                    else:
                                        pin=Pin
                                        address="N/A"     
                                        db.add_admin(value,name,email,contact,password,pin,balance,address)                                                                            
                                        print(f"Pin:{pin}")   
                            else: 
                                 print("Invalid input")      
                                 return register                                                                                                                 
                        else:
                            print("Mismatching fields")   
                                             
                    else:
                        print("Password is too short ")   
                        return   register()                                   
                else: 
                    print("") 
                    print("Invalid phone contact:")
                    return register()                                                 
            else:
                print("Invalid phone contact:")
                return register()                                                                       
        else:
            print("Name is too short: ") 
            return   register()                                               
    else:
        print("Error! ")  
        print("Id must be numeric!") 
        return   register()

def add_agent():
    Id=input("Enter numeric id: ")
    if Id.isdigit()==True:
        value=int(Id)        
        name=input("Agent name: ")
        if len(name)>3:
            contact=input("Contact: ")
            if contact.isdigit()==True and len(contact):
                nin=input("Enter nin:")                        
                password=input("Enter password:")
                if len(password)>3:
                    confirmpassword=input("Confirm password: " )
                    if confirmpassword==password:                        
                        pin=input("Create agent pin:")
                        if pin.isdigit()==True:
                            if len(pin)==5:
                                confirmpin=input("Confirm pin: ")
                                if pin==confirmpin:
                                    db.add_agent(value,name,nin,contact,password,pin)
                                else:
                                  print(f"{pin} and {confirmpin} entered are mismatching!")   
                            else:
                                print("Invalid pin entry")                                                                         
                        else:
                            print("Invalid pin entry")
                            print("Pin must be a 5 digit number")                                            
                    else:
                        print(f"{password} and {confirmpassword} entered are mismatching!")                                        
                else:
                    print("Password is too short!")                                        
            else:
                print("Contact must be numeric")
                print("Check the contact")                                                        
        else:
            print("Name is too short:")                                                    
    else:
        print("Id must be numeric:")                            
                                   
                                   
                                   
def add_user():
     Id=input("Enter numeric id: ")
     if Id.isdigit()==True:
        value=int(Id)        
        name=input("User name: ")
        if len(name)>3:
            contact=input("Contact: ")
            if contact.isdigit()==True and len(contact):
                nin=input("Enter nin:")                        
                if len(nin)==10:                       
                    pin=input("Create agent pin:")
                    if pin.isdigit()==True:
                        if len(pin)==5:
                            confirmpin=input("Confirm pin: ")
                            if pin==confirmpin:
                                db.add_user(value,name,nin,contact,pin)
                            else:
                              print(f"{pin} and {confirmpin} entered are mismatching!")   
                        else:
                            print("PIN is too short!")                                                                                                   
                    else:
                        print("Pin must be numeric")                                                                 
                else:
                    print("Invalid NIN!")                                                              
            else:
                print("Invalid contact!")                                      
        else:
            print("User name is too short!")                                                           
     else:
        print("Id must be an integer")                                                    
                                                               
def login():
    
    pin=input("Enter pin:")
    db.admin_login(contact,pin)
def add_admin() :
    Id =input("Enter numeric id: ")   
    if Id.isdigit()==True:
        name=input("Enter name of administrator: ")
        value=int(Id)
        if len(name)>=3:
            contact=input("Contact: ")
            if contact.isdigit()==True :
                if len(contact)==10:
                    password=input("Password")
                    if len(password)>2:
                        confirmpassword=input("Confirm password:")
                        if password==confirmpassword:
                            balance=90000000.00
                            print("Admin account created successfully.....")
                            print(f"Default pin: {Pin}")
                            print("1.Use defualt pin: ")
                            print("2. Change pin: ")
                            num=input("Enter option: ")
                            if num=="1":
                                pin=Pin
                            elif num=="2":
                                pin =input("Enter new pin: ") 
                                if pin.isdigit()==True and len(pin):  
                                    pin1=input("Confirm new pin: ")
                                    if pin1==pin:
                                        address=("Enter operation area: ")
                                        db.add_admin(value,name,email,contact,password,pin,balance,address)
                                    else:
                                        pin=Pin
                                        address="N/A"     
                                        db.add_admin(value,name,email,contact,password,pin,balance,address)                                                                            
                                        print(f"Pin:{pin}")   
                            else: 
                                 print("Invalid input")      
                                 return register()                                                                                                                 
                        else:
                            print("Mismatching fields")   
                                             
                    else:
                        print("Password is too short ")   
                        return   register()                                   
                else: 
                    print("") 
                    print("Invalid phone contact:")
                    return register()                                                 
            else:
                print("Invalid phone contact:")
                return register()                                                                       
        else:
            print("Name is too short: ") 
            return   register()                                               
    else:
        print("Error! ")  
        print("Id must be numeric!") 
        return   register() 
def main() :
    print("1. Login")
    print("2. Register")
    print("0. Exit")
    choice=input("Select option:")
    if choice=="1":
        login()
        while True:
            print("Acount initialised successfully.......")                              
            print("1.Add admin account")            
            print("2. Register agent")
            print("3. Register user")
            print("4. Make transactions")
            print("0.Exit")
            num=input("Enter option:")
            if num =="1":
                print("Complete the following to add admin")
                register()
            elif num =="2":
                print("Welcome to agent registration")
                return add_agent()
            elif num =="3":
                print("Welcome to user registration")
                return add_user()
            elif num =="4":
                print("Make transactions...")
                print("1. Deposite")
                print("2. Withdraw")
                print("0.Exit")
                choice=input("Select option: ")
                if choice=="1":
                    return db.admintransaction(contact)
                else:
                    print("System loading") 
                    print("System services a currently unavailable try again later")                                        
            elif num =="0":
                break
            else:
                print("Error ")
                return 0
                
    elif choice=="2":
        initialize= register()        
        while initialize==True:
            while True:
                print("Acount initialised successfully.......")                              
                print("1.Add admin account")            
                print("2. Register agent")
                print("3. Register user")
                print("4. Make transactions")
                print("0.Exit")
                num=input("Enter option:")
                if num =="1":
                    print("Complete the following to add admin")
                    register()
                elif num =="2":
                    print("Welcome to agent registration")
                    return add_agent()
                elif num =="3":
                    print("Welcome to user registration")
                    return add_user()
                elif num =="4":
                    print("Make transactions...")
                    print("1. Deposite")
                    print("2. Withdraw")
                    print("0.Exit")
                    choice=input("Select option: ")
                    if choice=="1":
                        return db.admintransaction(contact)
                    else:
                        print("System loading") 
                        print("System services a currently unavailable try again later")                                        
                elif num =="0":
                    break
                else:
                    print("Error ")                                             
    elif  choice=="0" :
        return 0            
    else:
        return main()        

main()