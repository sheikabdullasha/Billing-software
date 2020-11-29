from tkinter import *

import pymysql
from tkinter import messagebox


class mainwindow:
    
    def adminlogin(self):
        self.user_id=StringVar()
        self.pass_wrd=StringVar()
        
        passframe=Frame(self.top1,bg='#f8f5ec',width='500',height='400').place(x=250,y=198)
        admin_id=Label(self.top1,text='Admin ID     :',bg='#f8f5ec').place(x=300,y=250)
        admin_pass=Label(self.top1,text='Password   :',bg='#f8f5ec').place(x=300,y=300)
        identry=Entry(self.top1,textvariable=self.user_id).place(x=400,y=250)
        pass_entry=Entry(self.top1,textvariable=self.pass_wrd).place(x=400,y=300)
        login_button=Button(self.top1,text='Login',command=self.check,bg='white',activeforeground='black',activebackground='#e8b5ce').place(x=400,y=350)
    def check(self):
        def logindes():
                    
                    self.top1.destroy()
                    mainwindow()
        self.userid=self.user_id.get()
        self.password=self.pass_wrd.get()
        
        if(self.userid=='sheik'):
            if(self.password=='abu'):
                loginframe=Frame(self.top1,bg='#f8f5ec',width='500',height='400').place(x=250,y=200)
                back2=Button(self.top1,text='Back',command=logindes,bg='white',activeforeground='black',activebackground='#e8b5ce').place(x=650,y=550)
                try:
                    mydb=pymysql.connect(host='localhost',port=3306,user='root',password='abu1110')
                    mycursor=mydb.cursor()
                    mycursor.execute('use supermarket')
                except:
                    print('database not connected')
                
                    
                    
                    
                    
                    
                mycursor.execute('select * from customer')
                data=mycursor.fetchall()
                customerlabel=Label(self.top1,text='Customer purchase Info',bg='#cf6397').place(x=410,y=199)
                adminclose=Button(self.top1,text='Back',command=logindes,bg='white',activeforeground='black',activebackground='#e8b5ce').place(x=650,y=550)
                k=0
                for i in data:
                    k=k+20
                    label1=Label(self.top1,text=i,bg='#f8f5ec').place(x=300,y=200+k)
                
            else:
                messagebox.showinfo("Warning","password Wrong")
        else:
            messagebox.showinfo("Warning","UserID mismatching")
                
                
            
        
    
    
    def billconfirmation(self):
        k=messagebox.askquestion("Bill Confirm","Are you sure?")
        if(k=='yes'):
            
            
            
            
            self.customernum=self.mobilenum.get()
            self.ricenum=self.rice_qty.get()
            self.sugarnum=self.sugar_qty.get()
            self.saltnum=self.salt_qty.get()
            
            try:
                
                
                self.item11=int(self.ricenum)* 200
                
            except:
                self.item11=0
            try:
                
                self.item2=int(self.sugarnum)*60
            except:
                self.item2=0
            try:
                
                self.item3=int(self.saltnum)*20
            except:
                self.item3=0
            
            self.amount=self.item11+self.item2+self.item3
            print('')
                
            
            if(self.item11)>0:
            
                self.item1c=f'Rice : {self.ricenum} Kg x RS {200} = RS  {self.item11}'
                    
    
            else:
                pass
            if(self.item2)>0:
                    
                self.item2c=f'Sugar: {self.sugarnum} Kg x Rs {60}  = Rs  {self.item2}'
                    
            else:
                pass
            
            if(self.item3)>0:
                    
                self.item3c=f'Salt:   {self.saltnum} Kg x Rs  {20}  = Rs {self.item3}'
                    
            else:
                pass
            if(self.amount>0):
                print('Total Amount:    ',self.amount)
            self.totalamt=f'Total Amount:      Rs: {self.amount}'
            self.paymentrecipt=Frame(self.top1,bg='#f8f5ec',width='500',height='400').place(x=250,y=200)
            l6=Label(self.top1,text='bill summary',bg='#f8f5ec',font='Ravie').place(x=400,y=200)
            l7=Label(self.top1,text=self.customernum,bg='#f8f5ec').place(x=650,y=250)
            l8=Label(self.top1,text='Mobile_no:',bg='#f8f5ec').place(x=570,y=250)
            
            
            if(int(self.item11)>0):
                self.rice1=Label(self.top1,text=self.item1c,bg='#f8f5ec').place(x=300,y=250)
                
            else:
                self.rice1=0
            if(int(self.item2)>0):
                self.sugar1=Label(self.top1,text=self.item2c,bg='#f8f5ec').place(x=300,y=300)
                
            else:
                self.sugar1=0
            if(int(self.item3)>0):
                self.salt1=Label(self.top1,text=self.item3c,bg='#f8f5ec').place(x=300,y=350)
                
            else:
                self.salt1=0
            sep=Label(self.top1,text='------------------------',bg='#f8f5ec').place(x=300,y=370)
            totallabel=Label(self.top1,text=self.totalamt,bg='#f8f5ec').place(x=300,y=400)
            
            
            def backmain():
                
                
                self.top1.destroy()
               
                self.__init__()
            back1=Button(self.top1,text='Back',command=backmain,bg='white',activeforeground='black',activebackground='#e8b5ce').place(x=650,y=550)
            rice_kg=str(self.ricenum)
            sugar_kg=str(self.sugarnum)
            salt_kg=str(self.saltnum)
            mobile_no=str(self.customernum)
            try:
                mydb=pymysql.connect(host='localhost',port=3306,user='root',password='abu1110')
                mycursor=mydb.cursor()
            except:
                print('database not connected')
            try:
                mycursor.execute('CREATE DATABASE supermarket')
                mycursor.execute('USE supermarket')
                mycursor.execute('CREATE TABLE customer(customer_id int(11) AUTO_INCREMENT,rice_kg varchar(5),sugar_kg varchar(5),salt_kg varchar(5),mobile_no int(10),PRIMARY KEY (`customer_id`))')
            except:
                print('table already exist')

            try:
                mycursor.execute('use supermarket')
                mycursor.execute("INSERT INTO customer VALUES(NULL,"+rice_kg+','+sugar_kg+','+salt_kg+','+mobile_no+")")
                mycursor.execute('SELECT * FROM customer');
                mydb.commit()
            except:
                print('Database not connected')
            
            
            
                
            
            
            
            
            
        else:
            print('product cancelled')
    def __init__(self):
        
        self.top1=Tk()
        self.top1.title('fruit stall')
        self.top1.geometry('1000x1000')
        self.top1.config(bg='#F0FFFF')
        mainframe=Frame(self.top1,bg='#cf6397',width='1050',height='150')
        mainframe.pack(side=TOP)
        mainframelabel=Label(mainframe,text='Super market',bg='#cf6397',font='Ravie').place(x=450,y=70)
        adminbutton= Button(self.top1,command=self.adminlogin,text = 'Admin login',bg='white',activeforeground = "black",activebackground = "#e8b5ce").place(x=925,y=125)
        mainwindowframe=Frame(self.top1,bg='#f8f5ec',width='500',height='400').place(x=250,y=200)
        self.rice_qty=IntVar()
        self.sugar_qty=IntVar()
        self.salt_qty=IntVar()
        self.mobilenum=StringVar()
        
        ricelabel=Label(self.top1,text='Rice   :',bg='#f8f5ec').place(x=300,y=250)
        sugarlabel=Label(self.top1,text='Sugar :',bg='#f8f5ec').place(x=300,y=300)
        saltlabel=Label(self.top1,text='salt :',bg='#f8f5ec').place(x=300,y=350)
        mobilelabel=Label(self.top1,text='Mobile no * :',bg='#f8f5ec').place(x=300,y=400)
        riceentry=Entry(self.top1,textvariable=self.rice_qty).place(x=400,y=250)
        sugarentry=Entry(self.top1,textvariable=self.sugar_qty).place(x=400,y=300)
        saltentry=Entry(self.top1,textvariable=self.salt_qty).place(x=400,y=350)
        mobileentry=Entry(self.top1,textvariable=self.mobilenum).place(x=400,y=400)
        
        
        calbutton=Button(self.top1,text='Cal total',command=self.billconfirmation,bg='white',activeforeground='black',activebackground='#e8b5ce').place(x=650,y=550)
    
    
        self.top1.mainloop()


 





mainobj=mainwindow()

