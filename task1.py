import tkinter as tk
from tkinter import messagebox

#main window
root = tk.Tk()
root.title("Welcome to my app")

#main frame
mainframe = tk.Frame(root, padx=20, pady=20, bg="white")
mainframe.pack(pady=20, padx=20, expand=True, fill=tk.BOTH)  # Expand to fill available space

#variable for main label
text_var = tk.StringVar()
text_var.set("Registration Form")

label = tk.Label(mainframe,
                 textvariable=text_var,
                 anchor=tk.CENTER,
                 bg="lightblue",
                 height=2,
                 width=20,
                 bd=3,
                 font=("Times New Roman", 20, "bold", "italic"),
                 cursor = "hand2",
                 fg = "darkblue",
                 padx = 15,
                 pady = 15,
                 relief = tk.RAISED
                 )
label.pack()

#sub frame within main frame
sub_frame = tk.Frame(mainframe, bg="white")
sub_frame.pack(anchor=tk.CENTER)

#variables for name,email,age and gender 
name_var = tk.StringVar()
email_var = tk.StringVar()
age_var = tk.StringVar()
gen_var = tk.StringVar(root,"1")

#function called when clicked on entry field
def on_click(var,entry,placeholder):
    if var.get() == placeholder:
        var.set("")
        entry.configure(state="normal")


#function called when clicked on other entry fields
def on_focusout(var,entry,placeholder):
    if var.get() == "":
        entry.insert(0, placeholder)
        entry.configure(state="disabled")

#function to reset values after clicking submit button
def reset_values():
    name_entry.insert(0, "Enter your name")
    name_entry.configure(state="disabled")
    email_entry.insert(0, "Enter your email id (eg: abc@gmail.com)")
    email_entry.configure(state="disabled")    
    age_entry.insert(0, "Enter your age")
    age_entry.configure(state="disabled")
    gen_var.set("1")
    

#function called when submit button is clicked
def submit():
    name = name_var.get()
    email = email_var.get()
    age = age_var.get()
    gen = gen_var.get()

    if name=="" or email=="" or age=="" or gen=="":
        messagebox.showwarning("Warning","Please fill all fields!!")
    else:
        if age.isdigit():
            print("Your name : "+name)
            print("Your email : "+email)
            print("Your age : "+age)
            print("Your Gender : "+gen)
            messagebox.showinfo("Registration info", name+"\n"+email+"\n"+age+"\n"+gen+"\nRegistration Successful!")
        else:
            messagebox.showerror("Invalid Data", "Please enter a digit for age!!")

    reset_values()


#label and entry for all fields
name_label = tk.Label(sub_frame, text="Username", font=("Times New Roman", 10, "bold"), bg="white")
name_entry = tk.Entry(sub_frame, textvariable = name_var, font=('calibre',10,'normal'), bg="lightgrey", width=40)
name_placeholder = "Enter your name"
name_entry.insert(0, name_placeholder)  #initial text displayed on entry field before clicking
name_entry.configure(state="disabled")  #initial state as disabled
name_entry.bind("<Button-1>", lambda event: on_click(name_var,name_entry,name_placeholder))  #event happening on right click on entry
name_entry.bind("<FocusOut>", lambda event: on_focusout(name_var,name_entry,name_placeholder))  #event happening on focus out

email_label = tk.Label(sub_frame, text="Email Id", font=("Times New Roman", 10, "bold"), bg="white")
email_entry = tk.Entry(sub_frame, textvariable = email_var, font=('calibre',10,'normal'), bg="lightgrey", width=40)
email_placeholder= "Enter your email id (eg: abc@gmail.com)"
email_entry.insert(0, email_placeholder)
email_entry.configure(state="disabled")
email_entry.bind("<Button-1>", lambda event: on_click(email_var,email_entry,email_placeholder))
email_entry.bind("<FocusOut>", lambda event: on_focusout(email_var,email_entry,email_placeholder))


age_label = tk.Label(sub_frame, text="User Age", font=("Times New Roman", 10, "bold"), bg="white")
age_entry = tk.Entry(sub_frame, textvariable= age_var, font=('calibre',10,'normal'), bg="lightgrey", width=40)
age_placeholder = "Enter your age"
age_entry.insert(0, age_placeholder)
age_entry.configure(state="disabled")
age_entry.bind("<Button-1>", lambda event: on_click(age_var,age_entry,age_placeholder))
age_entry.bind("<FocusOut>", lambda event: on_focusout(age_var,age_entry,age_placeholder))

gen_label = tk.Label(sub_frame, text="Gender", font=("Times New Roman", 10, "bold"), bg="white")

#radio buttons for different options for gender
male_radio = tk.Radiobutton(sub_frame, text="Male", variable=gen_var, value="Male", bg="white")
female_radio = tk.Radiobutton(sub_frame, text="Female", variable=gen_var, value="Female", bg="white")
other_radio = tk.Radiobutton(sub_frame, text="Other", variable=gen_var, value="Other", bg="white")

sub_btn = tk.Button(mainframe, text="Submit", command= submit)  #submit button

#placing all widgets in window
name_label.grid(row=0,column=0,pady=10, padx=10)
name_entry.grid(row=0, column=1)

email_label.grid(row=1,column=0, pady=10)
email_entry.grid(row=1,column=1)

age_label.grid(row=2,column=0, pady=10)
age_entry.grid(row=2,column=1)

gen_label.grid(row=3,column=0, pady=10)
male_radio.grid(row=4,column=0)
female_radio.grid(row=4,column=1)
other_radio.grid(row=4,column=2)

sub_btn.pack(pady=10)

root.mainloop()
                 
