import tkinter as tk
import sqlite3

#SQL Setup
connection = sqlite3.connect("users.db")
cursor = connection.cursor()

def delete3(screen):
    screen3.destroy()
    screen.destroy()
    
def login_success(screen):
    global screen3
    screen3 = tk.Toplevel(screen)
    screen3.title("Login Success")
    screen3.geometry("150x60")
    tk.Label(screen3,text="Login Success").pack()
    tk.Button(screen3,text="OK",command=lambda:delete3(screen)).pack()

def delete4():
    screen4.destroy()    
def wrong_credentials(screen):
    global screen4
    screen4 = tk.Toplevel(screen)
    screen4.title("Login Success")
    screen4.geometry("150x60")
    tk.Label(screen4,text="Wrong Credentials").pack()
    tk.Button(screen4,text="OK",command=lambda:delete4()).pack()
    
def register_user(screen1):
    username_info = user_var.get()
    password_info = passw_var.get()
    cursor.execute("INSERT INTO users (username,password) VALUES(?,?)",(username_info,password_info))
    connection.commit()
    tk.Label(screen1,text="Registration Successful").place(x = 130, y=170)
    
def register(screen):
    screen1 = tk.Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("400x200")
    
    global user_var
    global passw_var
    
    user_var = tk.StringVar()
    passw_var = tk.StringVar()
    
    tk.Label(screen1,font=("Roboto",24) ,anchor=tk.CENTER,text="Register", foreground="white", bg="grey",width="400").pack()

    tk.Label(screen1,anchor=tk.CENTER,text = "Username").place(x = 80, y= 70)
    
    tk.Label(screen1,anchor=tk.CENTER,text = "Password").place(x = 80,y = 100)
          
    tk.Entry(screen1,textvariable = user_var ,width = 30).place(x = 140,y = 70)                             
    
    tk.Entry(screen1,textvariable = passw_var ,width = 30).place(x = 140,y = 100) 
    
    tk.Button(screen1,text="Register",anchor=tk.CENTER,width="10",height="2",command = lambda:register_user(screen1)).place(x=150,y=130)
    
def MpasswordCheck(screen):
    UID = user_va.get()
    PW = passw_va.get()
    success = 0
    userslist = cursor.execute("SELECT user_id,username,password FROM users").fetchall()
    for i in range(len(userslist)):
        if UID == userslist[i][1] and PW == userslist[i][2]:
            login_success(screen)
            success = 1
        else:
            pass
    if success == 0:    
        wrong_credentials(screen)
            
def login(screen):
    screen2 = tk.Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("400x200")
    
    global user_va
    global passw_va
    
    user_va = tk.StringVar()
    passw_va = tk.StringVar()
    
    tk.Label(screen2,font=("Roboto",24) ,anchor=tk.CENTER,text="Login", foreground="white", bg="grey",width="400").pack()
    tk.Label(screen2,anchor=tk.CENTER,text = "Username").place(x = 100, y= 70)
    
    tk.Label(screen2,anchor=tk.CENTER,text = "Password").place(x = 100,y = 100) 
            
    tk.Entry(screen2,textvariable = user_va ,width = 30).place(x = 160,y = 70)
                             
    tk.Entry(screen2,textvariable = passw_va ,width = 30).place(x = 160,y = 100)
    
    tk.Button(screen2,text = "Login",command = lambda:MpasswordCheck(screen)).place(x = 170,y = 130)
    
def main():
    screen = tk.Tk()
    screen.geometry("300x200")
    screen.title("Login Test")
    tk.Label(text = "Login Page",bg="grey",width="300",height = "2",font=("Roboto",25)).pack()
    tk.Label(text="")
    tk.Button(text="Login",height="2",width="30",command = lambda:login(screen)).pack()
    tk.Label(text="")
    tk.Button(text="Register",height="2",width="30",command = lambda:register(screen)).pack()
    
    screen.mainloop()

if __name__ == "__main__":    
    main()
