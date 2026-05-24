import customtkinter as ctk
from tkinter import messagebox
import sqlite3

db="users.db"
adminkey="32501@adam"

conn=sqlite3.connect(db)
cursor=conn.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS users( id int primary key unique not null,
email varchar(35) unique not null,
contact varchar(13)  unique not null ,
password varchar(15) not null)''')
conn.commit()

def signup():
    Id=Id_entry.get()
    email=email_entry.get()
    contact=contact_entry. get()
    password=password_entry.get()
    
    if email =="" or password =="" or contact=="":
        messagebox.showwarning("Entry error", "All fields are required")
        return
    elif len(email) <3 :        
        mesagebox.showwarning("Wrong email","Emaill address is too short")
        return
    elif len(password)<3:
             messagbox.showwarning("Password error", "Password is too short")
         
         
    else  :
        cursor.execute("INSERT INTO users (id,email,contact,password) values(?,?,?,?)",(Id,email,contact,password))
        conn.commit()
        #Id_entry.delete(0,ctk.end)
        #email_entry.delete(0, ctk.end)
       # contact_entry.delete(0,ctk.end)
        #password_entry.delete(0,ctk.end)
        messagebox.showinfo("Success","Account created successfully")
        
# ui
window=ctk.CTk()
window.title("Adams Employee Systems" )

Idlabel=ctk.CTkLabel(window,text="ID",font=("Arial",20,"bold"))
Idlabel.place(x=80,y=340)
Id_entry=ctk.CTkEntry(window, font=("arial",18))
Id_entry.place(x=180, y=340)

emaillabel=ctk.CTkLabel(window,text="Email",font=("Arial",20))
emaillabel.place(x=80,y=400)
email_entry=ctk.CTkEntry(window, font=("arial",18))
email_entry.place(x=180, y=400)

contactlabel=ctk.CTkLabel(window,text="Contact",font=("Arial",20))
contactlabel.place(x=80,y=500)
contact_entry=ctk.CTkEntry(window, font=("arial",18))
contact_entry.place(x=180, y=500)

passwordlabel=ctk.CTkLabel(window,text="Password",font=("Arial",20))
passwordlabel.place(x=80,y=600)
password_entry=ctk.CTkEntry(window, font=("arial",18))
password_entry.place(x=180, y=600)
 
submit=ctk.CTkButton(window,text="Creat account", font=("arial",16), command=signup)
submit.place(x=180,y=650)
window.mainloop()
print(db)

        
    
    