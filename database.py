import sqlite3
questions=["What is your birth date?","What is you maiden name?","What is the name of you favourite pet?","What is you mothers maiden name","What is you district of birth?"]
db="project.db"
def admintable():
    conn=sqlite3.connect(db)
    cursor=conn.cursor()
    cursor.execute('''Create Table if not exists administrator(
    Id int primary key,
    email varchar(35) unique not null,
    contact varchar(10) unique not null,
    password varchar(35) not null,
    pin varchar(5) not null
    ) ''')
    conn.commit()
    conn.close()
# user table    
def users():
    conn=sqlite3.connect(db)
    cursor=conn.cursor()
    cursor.execute('''Create Table IF NOT EXISTS users(
    Id int primary key,
    name varchar(35) unique not null,
    nin varchar(20) not null,
    contact varchar(10) unique not null,
    pin varchar(5) not null,
    balance decimal(10,2) DEFAULT 500.00 ,
    data decimal(10,2) DEFAULT 100.00,
    airtime decimal(10,2) DEFAULT 500.00,
    minutes decimal(10,2) DEFAULT 30.00,
    sms int DEFAULT  100,
    recovery_qn text ,
    recovery varchar(49)     
    ) ''')
    print('table created succefully')
    
    conn.commit()
    conn.close()
users()
def add_user(Id,name,nin,contact,pin):
    try:
        conn=sqlite3.connect(db)
        cursor=conn.cursor()
        cursor.execute("INSERT INTO users(Id,name,nin,contact,pin) VALUES (?,?,?,?,?,?)",(Id,name,nin,contact,pin))
        conn.commit()
        return True
    except  sqlite3.IntegrityError:
        return False     
    finally:
        print("Agent created successfully")
        conn.close()
                           
    
    #    
 #agent section   
def agents():   
    conn=sqlite3.connect(db)
    cursor=conn.cursor()
    cursor.execute('''Create Table if not exists agents(
    Id int primary key,
    name varchar(35) unique not null,
    nin varchar(20) not null,
    contact varchar(10) unique not null,
    password varchar(35) not null,
    pin varchar(5) not null,
    balance decimal(10,4) default 0.0000 ,
    recovery_qn text ,
    recovery varchar(49)
    ) ''')
    conn.commit()
    conn.close()

def add_agent(Id,name,nin,contact,password,pin):
    conn=sqlite3.connect(db)
    cursor=conn.cursor()
    try:
        cursor.execute("INSERT INTO agents(Id,name,nin,contact,password,pin) VALUES (?,?,?,?,?,?)",(Id,name,nin,contact,password,pin))
        conn.commit() 
        return True
    except  sqlite3.IntegrityError:
        return False     
    finally:
        print("Agent created successfully")
        conn.close()
                                
                   
#admin section    
def admin():   
    conn=sqlite3.connect(db)
    cursor=conn.cursor()
    cursor.execute('''Create Table IF NOT EXISTS admins(
    Id int primary key,
    name varchar(35) unique not null,
    email varchar(35) unique not null,
    contact varchar(10) unique not null,
    password varchar(35) not null,
    pin varchar(5) not null,   
    balance decimal(10,4) DEFAULT 0.0000,
    address varchar(35) not null
    ) ''')
    conn.commit()
    conn.close()    
    
def add_admin(Id,name,email,contact,password,pin,balance,address):
    conn=sqlite3.connect(db)
    cursor=conn.cursor()
    try:
        cursor.execute("INSERT INTO admins (Id,name,email,contact,password,pin,address) VALUES (?,?,?,?,?,?,?)",(Id,name,email,contact,password,pin,address))
        conn.commit()
        return True  
       
    except sqlite3.IntegrityError:
        return False
    finally:
        print("Admin added successfully")
        conn.close()     
        
def admin_login(contact,pin):
            conn=sqlite3.connect(db)
            cursor=conn.cursor()
            cursor.execute("select contact,pin from admins where contact=? AND pin=?", (contact, pin))
            admin= cursor.fetchone()
            if admin:
                print("Account initialization successfull")
                conn.close()
                return True
            else:
                 print("Aministrator not located in system") 
                 conn.close()
                 return False           

#user account
def view_useraccount(contact,pin):
     conn=sqlite3.connect(db)
     cursor=conn.cursor()
     cursor.execute("SELECT balance FROM users WHERE contact=? AND pin=?", (contact, pin))
     balance = cursor.fetchone()
     if balance:
         print("You account balance is: UGX", balance[0]) 
         print("done")
         conn.close()     
     else:
         print("Incorrect pin")
         conn.close()     
def user_login(contact,pin):
            conn=sqlite3.connect(db)
            cursor=conn.cursor()
            cursor.execute("select contact,pin from users where contact=? AND pin=?", (contact, pin))
            agent = cursor.fetchone()
            
            if agent:
                print("Account initialization successfull")
                conn.close()
                return True
            else:
                 print("User not located in system please visit the nearby mobile money  centre so as to register")  
                 conn.close()
     
def user_aritme(contact):
    conn=sqlite3.connect(db)
    cursor=conn.cursor()
    cursor.execute("SELECT airtime, minutes, data, sms FROM users WHERE contact=?", (contact))
    balance = cursor.fetchone()
    print(f"You have UGX {balance[0]} Airtime  {balance[1]}minutes  {balance[2]}mbs data and {balance[3]}sms")
    print("done")
    conn.close()
        
def user_send(contact):
    print("Send money")
    number=input("Enter number to deposite:")
    conn=sqlite3.connect(db)   
    cursor=conn.cursor()  
    cursor.execite("SELECT balance, name from users WHERE contact=?",(number))
    receiver=cursor.fetchone()
    cursor.execite("SELECT balance, name from agents WHERE contact=?",(number))
    agent=cursor.fetchone()
    cursor.execite("SELECT balance, name from admins WHERE contact=?",(number))
    admin=cursor.fetchone()
    if receiver:
        amount=float(input("Enter amount: "))
        print(f"You are sending UGX {amount} to {receiver[1]}")
        print("1. Accept and complete transaction")
        print("0. Coucel process")
        choice=input("Select option: ")
        if choice=="1":
            pin=input("Enter your pin:")         
            cursor.execute("SELECT pin , balance , name from users  WHERE contact=? AND pin=?",(contact,pin))
            sender=cursor.fetchone()
            if sender:
                if sender[1]>amount*1.03:
                    newbalance=sender[1] -1.025*amount
                    increment=receiver[0]+amount
                    #admin=newbalance-amount
                    cursor.execute("UPDATE users SET balance =? where contact=? AND pin=?",(newbalance,contact,pin))
                    cursor.execute("UPDATE  users SET balance =? where contact=? ",(increment,number))
                    print(f"You have successfully sent UGX {amount} to {receiver[1]} Tax UGX {0.08*amount} transaction chareges UGX {0.017*amount}.Thank you for using our services")
                    print("Transaction completed")
                else:
                    print("You have insufficient funds") 
            else:
                print("Wrong pin entry") 
                return forgotpin()    
                                                                                     
        elif choice =="0":
           return 
        else:
            print("Invalid MMI code")
            
    elif agent:
        
        amount=float(input("Enter amount: "))
        print(f"You are sending UGX {amount} to {agent[1]}")
        print("1. Accept and complete transaction")
        print("0. Coucel process")
        choice=input("Select option: ")
        if choice=="1":
            pin=input("Enter your pin:")         
            cursor.execute("SELECT pin , balance , name from users  WHERE contact=? AND pin=?",(contact,pin))
            sender=cursor.fetchone()
            if sender:
                if sender[1]>amount*1.03:
                    newbalance=sender[1] -1.025*amount
                    increment=agent[0]+amount
                    #admin=newbalance-amount
                    cursor.execute("UPDATE users SET balance =? where contact=? AND pin=?",(newbalance,contact,pin))
                    cursor.execute("UPDATE  agents SET balance =? where contact=? ",(increment,number))
                    print(f"You have successfully sent UGX {amount} to {agent[1]} Tax UGX {0.08*amount} transaction chareges UGX {0.017*amount}.Thank you for using our services")
                    print("Transaction completed")
                else:
                    print("You have insufficient funds") 
            else:
                print("Wrong pin entry") 
                return forgotpin()    
                                                                                     
        elif choice =="0":
           return 
        else:
            print("Invalid MMI code")
        
    elif admin:
        
        amount=float(input("Enter amount: "))
        print(f"You are sending UGX {amount} to {admin[1]}")
        print("1. Accept and complete transaction")
        print("0. Coucel process")
        choice=input("Select option: ")
        if choice=="1":
            pin=input("Enter your pin:")         
            cursor.execute("SELECT pin , balance , name from users  WHERE contact=? AND pin=?",(contact,pin))
            sender=cursor.fetchone()
            if sender:
                if sender[1]>amount*1.03:
                    newbalance=sender[1] -1.025*amount
                    increment=admin[0]+amount
                    #admin=newbalance-amount
                    cursor.execute("UPDATE users SET balance =? where contact=? AND pin=?",(newbalance,contact,pin))
                    cursor.execute("UPDATE  users SET balance =? where contact=? ",(increment,number))
                    print(f"You have successfully sent UGX {amount} to {admin[1]} Tax UGX {0.08*amount} transaction chareges UGX {0.017*amount}.Thank you for using our services")
                    print("Transaction completed")
                else:
                    print("You have insufficient funds") 
            else:
                print("Wrong pin entry") 
                return forgotpin()    
                                                                                     
        elif choice =="0":
           return 
        else:
            print("Invalid MMI code")
        
    else:
        print('Incorrect contact!')                                                
def buy_userairtime(contact):
    print("BUY AIRTIME")
    amount=float(input("Enter amount : "))
    pin=input("Enter pin to process payment: ")
    conn=sqlite3.connect(db)   
    cursor=conn.cursor()       
    cursor.execute("SELECT pin , balance , name from users  WHERE contact=? AND pin=?",(contact,pin))   
    balance=cursor.fetchone()
    if pin==balance[0]:
        if amount>=balance[1]:
            change=balance[1]-amount
            cursor.execute("UPDATE users set balance =? where contact=? ",(change,contact))
            print(f"You have successfully received a top up of UGX{amount} airtime from {contact} ,{balance[2]}")
            print(f"UGX {amount} has deducted from your account to buy airtime. Your account balance is UGX {change}")
            print("Thank you for purchasing")
            conn.commit()
            conn.close()
        else:
            print("You have insufficient funds")
    else:
        print("Invalid pin entry") 
        return forgotpin()    
def set_userrecovery(contact):
    pin=input("Enter pin to proceed: ")
    conn=sqlite3.connect(db)
    cursor=conn.cursor() 
    cursor.execute("SELECT contact pin from users where contact=? AND pin=? ",(contact,pin))  
    user=cursor.fetchone()
    if pin.isdigit()==True and len(pin)==5:
        if user:
            print("Set recovery question")
            for i in range(0,len(questions)) :
                print(f"{i+1}.{questions[i]}")
            choice=input("Select recovery question")
            if choice=="1":
                question=questions[0]
                reply=input("Enter you reply: ")
                cursor.execute("UPDATE users SET recovery=? ,recovery_qn=? where contact=? AND pin=? ",(question,reply,contact,pin))
                print(f"Your recovery question is {question} and your answer {reply} has been successfully set keep it in secret thank you")
                print("You can now use it to recover your password.......")
                conn.commit()
                conn.close()
            elif choice=="2" :
                question=questions[1]
                reply=input("Enter you reply: ")
                cursor.execute("UPDATE users SET recovery=? ,recovery_qn=? where contact=? AND pin=? ",(question,reply,contact,pin))
                conn.commit()
                conn.close()
                print(f"Your recovery question is {question} and your answer {reply} has been successfully set keep it in secret thank you")
                print("You can now use it to recover your password.......")
                              
            elif choice=="3":
                question=questions[2]
                reply=input("Enter reply: ")
                cursor.execute("UPDATE users SET recovery=? ,recovery_qn=?where contact=? AND pin=? ",(question,contact,pin))
                print(f"Your recovery question is {question} and your answer {reply} has been successfully set keep it in secret thank you")
                print("You can now use it to recover your password.......")
                conn.commit()
                conn.close()
                
                
            elif choice=="4": 
                question=questions[3]
                reply=input("Enter you reply: ")
                cursor.execute("UPDATE users SET recovery=?,recovery_qn=? where contact=? AND pin=? ",(question,reply,contact,pin))
                print(f"Your recovery question is {question} and your answer {reply} has been successfully set keep it in secret thank you")
                print("You can now use it to recover your password.......")
                conn.commit()
                conn.close()
           
            elif choice=="5":
                question=questions[4]
                reply=input("Enter you reply: ")
                cursor.execute("UPDATE users SET recovery=? , recovery_qn=? where contact=? AND pin=? ",(question,reply,contact,pin))
                print(f"Your recovery question is {question} and your answer {reply} has been successfully set keep it in secret thank you")
                print("You can now use it to recover your password.......")
                conn.commit()
                conn.close()
            else:
                print("Invalid MMI code")
                conn.commit()
                conn.close()
        else:
            print("Invalid user pin")    
            conn.commit()
            conn.close()
    else:
        print("Incorrect pin")            
def forgotpin(contact):
    conn=sqlite3.connect(db)
    cursor=conn.cursor()
    cursor.execute("SELECT  recovery , recovery_qn FROM users where contact=?",(contact))
    user=cursor.fetchone()
    if len(user[0])>0 and len(user[1])>0:
        print(f"{user[1]}")
        reply=input("Enter your reply: ")
        if reply==user[0]:
            pin=input("Enter new pin:")
            pin1=input("Confirm your pin: ")
            if pin1==pin:
                cursor.execute("UPDATE pin=? where contact =?",(pin,contact))
                conn.commit()
                conn.close()
                print("You pin has successfully been changed.")
            else:
                print("Mismatching pins")   
                conn.commit()
                conn.close()             
    else:
        print("Your recovery question was not set!")    
        print("Visit the nearby service centres to resolve your pin .")  
          
        conn.commit()
        conn.close()
                        
#agent account     
def view_agentaccount(contact,pin):
     conn=sqlite3.connect(db)
     cursor=conn.cursor()
     cursor.execute("SELECT pin, balance FROM agents WHERE contact=? AND pin=?", (contact))
     balance = cursor.fetchone()
     if pin==balance[0]:
         print("You account balance is: UGX", balance[0]) 
         print("done")
         conn.close()      
     else:
         print("Invalid user pin")
         return forgotpin()
              
def agent_login(contact,pin):
            conn=sqlite3.connect(db)
            cursor=conn.cursor()
            cursor.execute("select contact,pin from agents where contact=? AND pin=?", (contact, pin))
            agent = cursor.fetchone()
            conn.close()
            if agent:
                print("Account initialization successfull")
                conn.close()
                return True
            else:
                 print("Agent not located in system")
                 conn.close()
                 
def changeuserpin(contact):
    pin=input("Enter old pin: ")
    if pin.isdigit()==True and len(pin)==5:
        conn=sqlite3.connect(db)
        cursor=conn.cursor()
        cursor.execite("select pin from users where contact=? AND pin=?",(contact,pin))
        user=cursor.fetchone()
        for pin in user:
            newpin=input("Enter new pin: ")
            if newpin.isdigt()==True :
                if len(newpin)==5:
                    confirmpin=input("Confirm new pin: ")
                    if confirmpin==newpin:
                        cursor.execute("UPDATE user set pin =? where contact=? AND pin=?", (newpin,contact,pin))
                        conn.commit()
                        conn.close()
                        break
                    else:
                        print("Mismatching fields !")     
                        return  changeuserpin(contact,pin)
            else:
                print("PIN must only be 5 digits long")
                return changeuserpin(contact,pin)
        else:
            print("PIN must only be 5 digits long")                                            
    else:
        print("Invalid pin entry")
        return forgotpin(contact)
                
def admintransaction(contact):
    number=input("Enter number to deposite:")
    conn=sqlite3.connect(db)
    cursor=conn.cursor() 
    cursor.execute("SELECT balance, name FROM users where contact=?",(number,))
    user=cursor.fetchone()
    cursor.execute("SELECT balance, name FROM agents where contact=?",(number,)) 
    agent=cursor.fetchone()
    cursor.execute("SELECT balance, name FROM admins where contact=?",(number,))
    adm=cursor.fetchone()
    if user:  
        amount=float(input("Enter amount: "))
        print(f"You have initiated a cash deposite of UGX {amount} to {number} {user[1]}")
        cursor.execute("SELECT name, pin, balance FROM admins where contact =?",(contact)) 
        admin=cursor.fetchone()
        pin=input("Enter pin: ")
        if admin[1]==pin:
            if admin[2]>1.02*amount:
                admin_change= admin[2]-amount
                user_balance=user[0]+amount
                cursor.execite("UPDATE users SET balance=? where contact =?",(user_balance,number))
                cursor.execute("UPDATE admins SET balance = ?where contact=?",(admin_change,contact))
                print(f"You have succeffully deposited UGX {amount} to {number} {user[1]}")
                conn.commit()
                conn.close()
            else:
                print('You have insufficient funds please recharge to continue')
                conn.commit()
                conn.close()   
        else:
            print("Wrong pin entry")
            conn.commit()
            conn.close()
            return   admintransaction(contact)         
    elif agent:
        amount=float(input("Enter amount: "))
        print(f"You have initiated a cash deposite of UGX {amount} to {number} {agent[1]}")
        cursor.execute("SELECT name, pin, balance FROM admins where contact =?",(contact,)) 
        admin=cursor.fetchone()
        pin=input("Enter pin: ")
        if admin[1]==pin:
            if admin[2]>1.02*amount:
                admin_change= admin[2]-amount
                agent_balance=agent[0]+amount
                cursor.execite("UPDATE agents SET balance=? where contact =?",(agent_balance,number))
                cursor.execute("UPDATE admins SET balance = ?where contact=?",(admin_change,contact))
                print(f"You have succeffully deposited UGX {amount} to {number} {agent[1]}")
                conn.commit()
                conn.close()
            else:
                print('You have insufficient funds please recharge to continue')
                conn.commit()
                conn.close()   
        else:
            print("Wrong pin entry")
            conn.commit()
            conn.close()
            return   admintransaction(contact)    
    elif adm:
        
        amount=float(input("Enter amount: "))
        print(f"You have initiated a cash deposite of UGX {amount} to {number} {adm[1]}")
        cursor.execute("SELECT name, pin, balance FROM admins where contact =?",(contact,)) 
        admin=cursor.fetchone()
        pin=input("Enter pin: ")
        if admin[1]==pin:
            if admin[2]>1.02*amount:
                admin_change= admin[2]-amount
                admin_balance=adm[0]+amount
                cursor.execite("UPDATE admins SET balance=? where contact =?",(admin_balance,number))
                cursor.execute("UPDATE admins SET balance = ?where contact=?",(admin_change,contact))
                print(f"You have succeffully deposited UGX {amount} to {number} {adm[1]}")
                conn.commit()
                conn.close()
            else:
                print('You have insufficient funds please recharge to continue')
                conn.commit()
                conn.close()   
        else:
            print("Wrong pin entry")
            conn.commit()
            conn.close()
            return   admintransaction(contact)
        
    else:
        print(f"User with {number} not located!")                           
def changeagentpin(contact,pin):
    pin=input("Enter old pin")
    if pin.isdigit()==True and len(pin)==5:
        conn=sqlite3.connect(db)
        cursor=conn.cursor()
        cursor.execute("select pin from agents where contact=? AND pin=?",(contact,pin))
        user=cursor.fetchone()
        for pin in user:
            newpin=input("Enter new pin: ")
            if newpin.isdigt()==True :
                if len(newpin)==5:
                    confirmpin=input("Confirm new pin: ")
                    if confirmpin==newpin:
                        cursor.execute("UPDATE agents set pin =? where contact=? AND pin=?", (newpin,contact,pin))
                        conn.commit()
                        conn.close()
                        break
                    else:
                        print("Mismatching fields !")     
                        return  changeuserpin(contact,pin)
                        conn.commit()
                        conn.close()
            else:
                print("PIN must only be 5 digits long")
                return changeuserpin(contact,pin)
        else:
            print("PIN must only be 5 digits long")                                            
    else:
        print("Invalid pin entry")
        return forgotpin(contact)       
                 
def withdraw(contact):
     
    conn=sqlite3.connect(db)
    cursor=conn.cursor()
    cursor.execute("SELECT balance , pin  from users where contact=?",(contact,))
    user=cursor.fetchone()
    if user:
        print("Withdraw funds")
        amount=float(input("Enter amount: ") )
        if user[0] > 1.02*amount and user[0]>=500:
            pin=input("Enter pin to continue:")
            if pin==user[1]:
                print(f"You have initated cash withdraw of UGX {amount} ")
                change=user[0]-1.008*amount            
                cursor.execute("UPDATE set balance=? users where contact=?",(change,contact))
                return True
                conn.commit()
                conn.close()
            else:
                print("Incorrect user PIN") 
                conn.close()
                return forgotpin(contact)                         
        else:
            print("You have insufficient funds")   
            conn.close()  
    else:
        print("User not found!")               
 
                                                                                        
