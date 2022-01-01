from sys import setrecursionlimit
from tkinter import *
import qrcode
from PIL import Image, ImageTk
from resizeimage import resizeimage

class Qr_Generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Code Generator | Developed by PVP")
        self.root.resizable(False,False)

        title=Label(self.root,text=" QR Code Generator",font=("times new roman",40), bg='#053246', fg='white', anchor='w').place(x=0,y=0,relwidth=1)
        
        #=======Employee Details window==========
        #======Variables=========
        self.var_emp_id=StringVar()
        self.var_emp_name=StringVar()
        self.var_emp_department=StringVar()
        self.var_emp_designation=StringVar()

        emp_Frame=Frame(self.root, bd=2, relief=RIDGE, bg='white')
        emp_Frame.place(x=50, y=100, width=500, height=380)

        emp_title=Label(emp_Frame,text="Employee Details",font=("goudy old style",20), bg='#043256', fg='white').place(x=0,y=0,relwidth=1)

        lbl_emp_code=Label(emp_Frame,text="Employee ID",font=("times new roman",15, 'bold'), bg='white').place(x=20,y=60)
        lbl_emp_name=Label(emp_Frame,text="Name",font=("times new roman",15, 'bold'), bg='white').place(x=20,y=100)
        lbl_emp_department=Label(emp_Frame,text="Department",font=("times new roman",15, 'bold'), bg='white').place(x=20,y=140)
        lbl_emp_designation=Label(emp_Frame,text="Designation",font=("times new roman",15, 'bold'), bg='white').place(x=20,y=180)

        text_emp_code=Entry(emp_Frame,font=("times new roman",15), bg='lightyellow', textvariable=self.var_emp_id).place(x=200,y=60)
        text_emp_name=Entry(emp_Frame,font=("times new roman",15), bg='lightyellow', textvariable=self.var_emp_name).place(x=200,y=100)
        text_emp_department=Entry(emp_Frame,font=("times new roman",15), bg='lightyellow', textvariable=self.var_emp_department).place(x=200,y=140)
        text_emp_designation=Entry(emp_Frame,font=("times new roman",15), bg='lightyellow', textvariable=self.var_emp_designation).place(x=200,y=180)

        btn_generate=Button(emp_Frame, text="Generate QR Code", command=self.generate, font=('times new roman',18, 'bold'), bg='#2196f3' , fg='white').place(x=80, y=250, width=200, height=30)
        btn_clear=Button(emp_Frame, text="Clear", command=self.clear,font=('times new roman',18, 'bold'), bg='#607d8b' , fg='white').place(x=320, y=250, width=80, height=30)

        self.msg=""
        self.lbl_msg=Label(emp_Frame,text=self.msg,font=("times new roman",15), bg='white', fg='green')
        self.lbl_msg.place(x=0,y=310,relwidth=1)

        #=======Employee QR code window==========
        qr_Frame=Frame(self.root, bd=2, relief=RIDGE, bg='white')
        qr_Frame.place(x=600, y=100, width=250, height=380)

        emp_title=Label(qr_Frame,text="Employee QR Code",font=("goudy old style",20), bg='#043256', fg='white').place(x=0,y=0,relwidth=1)

        self.qr_code=Label(qr_Frame, text='QR Code \nNot available',font=('times new roman',15),bg='#3F51b5',fg='white',bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=180)

    def clear(self):
        self.var_emp_id.set('')
        self.var_emp_name.set('')
        self.var_emp_department.set('')
        self.var_emp_designation.set('')
        self.msg=''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')

    def generate(self):
        if self.var_emp_id.get()=='' or self.var_emp_name.get()=='' or self.var_emp_department.get()=='' or self.var_emp_designation.get()=='':
            self.msg="All fields are required !!!"
            self.lbl_msg.config(text=self.msg, fg='red')
        else:
            qr_data=(f"Employee ID: {self.var_emp_id.get()}\nEmployee Name: {self.var_emp_name.get()}\nDepartment: {self.var_emp_department.get()}\nDesignation: {self.var_emp_designation.get()}")
            qr_code=qrcode.make(qr_data)
            #print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("Employee_QR/Emp_"+str(self.var_emp_id.get())+'.png')
            #====== QR Code image update =====
            self.im=ImageTk.PhotoImage(qr_code)             
            self.qr_code.config(image=self.im)
            #====== notification========
            self.msg="QR code generated sucessfully !!!"
            self.lbl_msg.config(text=self.msg, fg='green')

root=Tk()
obj = Qr_Generator(root)
root.mainloop()