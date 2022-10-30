import tkinter as tk
from tkinter import ttk, messagebox
from backend import DatabaseOperation

database = DatabaseOperation("employeeManagement.db")

window = tk.Tk()
window.title("EMPLOYEE INFORMATION SYSTEM")


appLabel = tk.Label(window, text="EMPLOYEE INFORMATION SYSTEM", fg="#06a099", width=35)
appLabel.config(font=("Sylfaen", 30))
appLabel.grid(row=0, columnspan=3, padx=(10,10), pady=(30, 0))




def DEPT_MASTERtable():
    DEPTwindow = tk.Tk()
    DEPTwindow.title('DEPARTMENT MASTER TABLE')
    deptIdLabel = tk.Label(DEPTwindow, text="Enter Dept_Id", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10,0))
    deptNameLabel = tk.Label(DEPTwindow, text="Enter Dept_name", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=2, column=0, padx=(10,0))
    
    deptIdEntry = tk.Entry(DEPTwindow, width = 30)
    deptIdEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))
    deptNameEntry = tk.Entry(DEPTwindow, width =30)
    deptNameEntry.grid(row=2, column=1, padx=(0,10))

    def deptMasterInput():
        DId = deptIdEntry.get()
        deptIdEntry.delete(0, tk.END)
        Dname = str(deptNameEntry.get())
        deptNameEntry.delete(0, tk.END)
        
        
        database.insertIntoDeptMaster(DId, Dname)
    
        messagebox.showinfo("Success", "Data Saved Successfully.")



    def DeptMasterDisplay():
        secondWindow = tk.Tk()
        secondWindow.title("Display DEPARTMENT_MASTER TABLE ")
        appLabel = tk.Label(secondWindow, text="DEPARTMENT_MASTER TABLE",fg="#06a099", width=40)
        appLabel.config(font=("Sylfaen", 30))
        appLabel.pack()

        tree = ttk.Treeview(secondWindow)
        tree["columns"] = ("one")

        tree.heading("#0", text="Dept_Id")
        tree.heading("one", text="Dept_Name")

        cursor = database.show("SELECT * FROM 'DEPARTMENT_MASTER' ;")
        i = 0
        for row in cursor:
            tree.insert('',i,text=row[0], values=(row[1]))
            i = i + 1
        tree.pack()
        secondWindow.mainloop()


    inputBtn = tk.Button(DEPTwindow, text = 'input', command=deptMasterInput)
    inputBtn.grid(row=5, column=0, pady=30)

    dispBtn = tk.Button(DEPTwindow, text ='Display', command=DeptMasterDisplay)
    dispBtn.grid(row=5, column=1, pady=30)

    quitBtn = tk.Button(DEPTwindow, text='QUIT', command=DEPTwindow.destroy)
    quitBtn.grid(row=6, column=1, pady=30)

    DEPTwindow.mainloop()





def REGION_MASTERtable():
    REGIONwindow = tk.Tk()
    REGIONwindow.title('REGION MASTER TABLE')

    regionIdLabel = tk.Label(REGIONwindow, text="Enter Region_Id", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10,0))

    regionNameLabel = tk.Label(REGIONwindow, text="Enter Region_name", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=2, column=0, padx=(10,0))

    regionStatusLabel = tk.Label(REGIONwindow, text="Enter Region_status", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=3, column=0, padx=(10,0))



    regionIdEntry = tk.Entry(REGIONwindow, width = 30)
    regionIdEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))

    regionNameEntry = tk.Entry(REGIONwindow, width =30)
    regionNameEntry.grid(row=2, column=1, padx=(0,10))

    regionStatusEntry = tk.Entry(REGIONwindow, width =30)
    regionStatusEntry.grid(row=3, column=1, padx=(0,10), pady=(30, 20))




    def regionMasterInput():
        RegionId = regionIdEntry.get()
        regionIdEntry.delete(0, tk.END)
        RegionName = regionNameEntry.get()
        regionNameEntry.delete(0, tk.END)
        RegionStatus = int(regionStatusEntry.get())
        regionStatusEntry.delete(0,tk.END)
        
        

        database.insertIntoRegionMaster(RegionId, RegionName, str(RegionStatus)) 

        messagebox.showinfo("Success", "Data Saved Successfully.")



    def regionMasterDisplay():
        secondWindow = tk.Tk()
        secondWindow.title("DISPLAY REGION_MASTER TABLE ")
        appLabel = tk.Label(secondWindow, text="REGION_MASTER TABLE",fg="#06a099", width=40)
        appLabel.config(font=("Sylfaen", 30))
        appLabel.pack()

        tree = ttk.Treeview(secondWindow)
        tree["columns"] = ("one", 'two')

        tree.heading("#0", text = "Region_Id")
        tree.heading("one", text = "Region_Name")
        tree.heading("two", text = "Region_Status")

        cursor = database.show("SELECT * FROM 'REGION_MASTER' ;")
        i = 0
        for row in cursor:
            tree.insert('',i,text=row[0], values=(row[1], row[2]))
            i = i + 1
        tree.pack()
        secondWindow.mainloop()


    inputBtn = tk.Button(REGIONwindow, text = 'Input', command=regionMasterInput)
    inputBtn.grid(row=5, column=0, pady=30)

    dispBtn = tk.Button(REGIONwindow, text ='Display', command=regionMasterDisplay)
    dispBtn.grid(row=5, column=1, pady=30)

    quitBtn = tk.Button(REGIONwindow, text='QUIT', command=REGIONwindow.destroy)
    quitBtn.grid(row=6, column=1, pady=30)

    REGIONwindow.mainloop()





def COUNTRY_MASTERtable():
    COUNTRYwindow = tk.Tk()
    COUNTRYwindow.title('COUNTRY MASTER TABLE')

    regionIdLabel = tk.Label(COUNTRYwindow, text="Enter Country_Id", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10,0))

    regionNameLabel = tk.Label(COUNTRYwindow, text="Enter Country_Name", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=2, column=0, padx=(10,0))


    countryIdEntry = tk.Entry(COUNTRYwindow, width = 30)
    countryIdEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))

    countryNameEntry = tk.Entry(COUNTRYwindow, width =30)
    countryNameEntry.grid(row=2, column=1, padx=(0,10))



    def countryMasterInput():
        countryId = countryIdEntry.get()
        countryIdEntry.delete(0, tk.END)
        countryName = countryNameEntry.get()
        countryNameEntry.delete(0, tk.END)
                
        
        database.insertIntoCountryMaster(countryId, countryName)  
        
        messagebox.showinfo("Success", "Data Saved Successfully.")



    def countryMasterDisplay():
        secondWindow = tk.Tk()
        secondWindow.title("COUNTRY MASTER TABLE ")
        appLabel = tk.Label(secondWindow, text="COUNTRY_MASTER TABLE",fg="#06a099", width=40)
        appLabel.config(font=("Sylfaen", 30))
        appLabel.pack()

        tree = ttk.Treeview(secondWindow)
        tree["columns"] = ("one")

        tree.heading("#0", text = "Country_Id")
        tree.heading("one", text = "Country_Name")

        cursor = database.show("SELECT * FROM 'COUNTRY_MASTER' ;")
        i = 0
        for row in cursor:
            tree.insert('',i,text=row[0], values=(row[1]))
            i = i + 1
        tree.pack()
        secondWindow.mainloop()


    inputBtn = tk.Button(COUNTRYwindow, text = 'Input', command=countryMasterInput)
    inputBtn.grid(row=5, column=0, pady=30)

    dispBtn = tk.Button(COUNTRYwindow, text ='Display', command=countryMasterDisplay)
    dispBtn.grid(row=5, column=1, pady=30)

    quitBtn = tk.Button(COUNTRYwindow, text='QUIT', command=COUNTRYwindow.destroy)
    quitBtn.grid(row=6, column=1, pady=30)

    COUNTRYwindow.mainloop()






def RELATION_MASTERtable():
    RELATIONwindow = tk.Tk()
    RELATIONwindow.title('RELATION MASTER TABLE')

    relationIdLabel = tk.Label(RELATIONwindow, text="Enter Relation_Id", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10,0))

    relationDescLabel = tk.Label(RELATIONwindow, text="Enter Relation_Desc", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=2, column=0, padx=(10,0))


    relationIdEntry = tk.Entry(RELATIONwindow, width = 30)
    relationIdEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))

    relationDescEntry = tk.Entry(RELATIONwindow, width =30)
    relationDescEntry.grid(row=2, column=1, padx=(0,10))



    def relationMasterInput():
        relationId = relationIdEntry.get()
        relationIdEntry.delete(0, tk.END)
        relationDesc = relationDescEntry.get()
        relationDescEntry.delete(0, tk.END)
                
        

        database.insertIntoRelationMaster(relationId, relationDesc)  
        
        messagebox.showinfo("Success", "Data Saved Successfully.")



    def relationMasterDisplay():
        secondWindow = tk.Tk()
        secondWindow.title("DISPLAY RELATION_MASTER TABLE ")
        appLabel = tk.Label(secondWindow, text="RELATION_MASTER TABLE",fg="#06a099", width=40)
        appLabel.config(font=("Sylfaen", 30))
        appLabel.pack()

        tree = ttk.Treeview(secondWindow)
        tree["columns"] = ("one")

        tree.heading("#0", text = "Relation_Id")
        tree.heading("one", text = "Relation_Desc")

        cursor = database.show("SELECT * FROM 'RELATION_MASTER' ;")
        i = 0
        for row in cursor:
            tree.insert('',i,text=row[0], values=(row[1]))
            i = i + 1
        tree.pack()
        secondWindow.mainloop()


    inputBtn = tk.Button(RELATIONwindow, text = 'Input', command=relationMasterInput)
    inputBtn.grid(row=5, column=0, pady=30)

    dispBtn = tk.Button(RELATIONwindow, text ='Display', command=relationMasterDisplay)
    dispBtn.grid(row=5, column=1, pady=30)

    quitBtn = tk.Button(RELATIONwindow, text='QUIT', command=RELATIONwindow.destroy)
    quitBtn.grid(row=6, column=1, pady=30)

    RELATIONwindow.mainloop()






def BANK_MASTERtable():
    BANKwindow = tk.Tk()
    BANKwindow.title('BANK MASTER TABLE')

    bankIdLabel = tk.Label(BANKwindow, text="Enter Bank_Id", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10,0))

    bankNameLabel = tk.Label(BANKwindow, text="Enter Bank_Name", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=2, column=0, padx=(10,0))


    bankIdEntry = tk.Entry(BANKwindow, width = 30)
    bankIdEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))

    bankNameEntry = tk.Entry(BANKwindow, width =30)
    bankNameEntry.grid(row=2, column=1, padx=(0,10))



    def bankMasterInput():
        bankId = bankIdEntry.get()
        bankIdEntry.delete(0, tk.END)
        bankName = bankNameEntry.get()
        bankNameEntry.delete(0, tk.END)
                
        
        database.insertIntoBankMaster(bankId, bankName)  

        messagebox.showinfo("Success", "Data Saved Successfully.")



    def bankMasterDisplay():
        secondWindow = tk.Tk()
        secondWindow.title("DISPLAY BANK_MASTER TABLE ")
        appLabel = tk.Label(secondWindow, text="BANK_MASTER TABLE",fg="#06a099", width=40)
        appLabel.config(font=("Sylfaen", 30))
        appLabel.pack()

        tree = ttk.Treeview(secondWindow)
        tree["columns"] = ("one")

        tree.heading("#0", text = "Bank_Id")
        tree.heading("one", text = "Bank_Name")

        cursor = database.show("SELECT * FROM 'BANK_MASTER' ;")
        i = 0
        for row in cursor:
            tree.insert('',i,text=row[0], values=(row[1]))
            i = i + 1
        tree.pack()
        secondWindow.mainloop()


    inputBtn = tk.Button(BANKwindow, text = 'Input', command=bankMasterInput)
    inputBtn.grid(row=5, column=0, pady=30)

    dispBtn = tk.Button(BANKwindow, text ='Display', command=bankMasterDisplay)
    dispBtn.grid(row=5, column=1, pady=30)

    quitBtn = tk.Button(BANKwindow, text='QUIT', command=BANKwindow.destroy)
    quitBtn.grid(row=6, column=1, pady=30)

    BANKwindow.mainloop()





def EDUCATION_MASTERtable():
    EDUCATIONwindow = tk.Tk()
    EDUCATIONwindow.title('EDUCATION MASTER TABLE')

    educationIdLabel = tk.Label(EDUCATIONwindow, text="Enter Education_Id", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10,0))

    educationDescLabel = tk.Label(EDUCATIONwindow, text="Enter Education_Desc", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=2, column=0, padx=(10,0))


    educationIdEntry = tk.Entry(EDUCATIONwindow, width = 30)
    educationIdEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))

    educationDescEntry = tk.Entry(EDUCATIONwindow, width =30)
    educationDescEntry.grid(row=2, column=1, padx=(0,10))



    def educationMasterInput():
        educationId = educationIdEntry.get()
        educationIdEntry.delete(0, tk.END)
        educationDesc = educationDescEntry.get()
        educationDescEntry.delete(0, tk.END)
                
        
        database.insertIntoEducationMaster(educationId, educationDesc)
    
        messagebox.showinfo("Success", "Data Saved Successfully.")



    def educationMasterDisplay():
        secondWindow = tk.Tk()
        secondWindow.title("DISPLAY EDUCATION_MASTER TABLE ")
        appLabel = tk.Label(secondWindow, text="EDUCATION_MASTER TABLE",fg="#06a099", width=40)
        appLabel.config(font=("Sylfaen", 30))
        appLabel.pack()

        tree = ttk.Treeview(secondWindow)
        tree["columns"] = ("one")

        tree.heading("#0", text = "Education_Id")
        tree.heading("one", text = "Education_Desc")

        cursor = database.show("SELECT * FROM 'EDUCATION_MASTER' ;")
        i = 0
        for row in cursor:
            tree.insert('',i,text=row[0], values=(row[1]))
            i = i + 1
        tree.pack()
        secondWindow.mainloop()


    inputBtn = tk.Button(EDUCATIONwindow, text = 'Input', command=educationMasterInput)
    inputBtn.grid(row=5, column=0, pady=30)

    dispBtn = tk.Button(EDUCATIONwindow, text ='Display', command=educationMasterDisplay)
    dispBtn.grid(row=5, column=1, pady=30)

    quitBtn = tk.Button(EDUCATIONwindow, text='QUIT', command=EDUCATIONwindow.destroy)
    quitBtn.grid(row=6, column=1, pady=30)

    EDUCATIONwindow.mainloop()






def DESIGNATION_MASTERtable():
    DESIGNATIONNwindow = tk.Tk()
    DESIGNATIONNwindow.title('EDUCATION MASTER TABLE')

    designationIdLabel = tk.Label(DESIGNATIONNwindow, text="Enter Designation_Id", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10,0))

    designationDescLabel = tk.Label(DESIGNATIONNwindow, text="Enter Designation_Desc", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=2, column=0, padx=(10,0))


    designationIdEntry = tk.Entry(DESIGNATIONNwindow, width = 30)
    designationIdEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))

    designationDescEntry = tk.Entry(DESIGNATIONNwindow, width =30)
    designationDescEntry.grid(row=2, column=1, padx=(0,10))



    def designationMasterInput():
        designationId = designationIdEntry.get()
        designationIdEntry.delete(0, tk.END)
        desinationDesc = designationDescEntry.get()
        designationDescEntry.delete(0, tk.END)
                

        database.insertIntoDesignationMaster(designationId, desinationDesc)  
        
        messagebox.showinfo("Success", "Data Saved Successfully.")



    def designationMasterDisplay():
        secondWindow = tk.Tk()
        secondWindow.title("DISPLAY DESIGNATION_MASTER TABLE ")
        appLabel = tk.Label(secondWindow, text="DESIGNATION_MASTER TABLE",fg="#06a099", width=40)
        appLabel.config(font=("Sylfaen", 30))
        appLabel.pack()

        tree = ttk.Treeview(secondWindow)
        tree["columns"] = ("one")

        tree.heading("#0", text = "Designation_Id")
        tree.heading("one", text = "Designation_Desc")

        cursor = database.show("SELECT * FROM 'DESIGNATION_MASTER' ;")
        i = 0
        for row in cursor:
            tree.insert('',i,text=row[0], values=(row[1]))
            i = i + 1
        tree.pack()
        secondWindow.mainloop()


    inputBtn = tk.Button(DESIGNATIONNwindow, text = 'Input', command=designationMasterInput)
    inputBtn.grid(row=5, column=0, pady=30)

    dispBtn = tk.Button(DESIGNATIONNwindow, text ='Display', command=designationMasterDisplay)
    dispBtn.grid(row=5, column=1, pady=30)

    quitBtn = tk.Button(DESIGNATIONNwindow, text='QUIT', command=DESIGNATIONNwindow.destroy)
    quitBtn.grid(row=6, column=1, pady=30)

    DESIGNATIONNwindow.mainloop()






def COMPANY_LOCATIONtable():
    LOCATIONNwindow = tk.Tk()
    LOCATIONNwindow.title('COMPANY LOCATION TABLE')

    locationIdLabel = tk.Label(LOCATIONNwindow, text="Enter Location_Id", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10,0))

    regionIdLabel = tk.Label(LOCATIONNwindow, text="Enter Region_Id", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=2, column=0, padx=(10,0))

    countryIdLabel = tk.Label(LOCATIONNwindow, text="Enter Country_Id", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=3, column=0, padx=(10,0))

    locationIdEntry = tk.Entry(LOCATIONNwindow, width = 30)
    locationIdEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))

    regionIdEntry = tk.Entry(LOCATIONNwindow, width =30)
    regionIdEntry.grid(row=2, column=1, padx=(0,10))

    countryIdEntry = tk.Entry(LOCATIONNwindow, width =30)
    countryIdEntry.grid(row=3, column=1, padx=(0,10))


    def locationMasterInput():
        locationId = locationIdEntry.get()
        locationIdEntry.delete(0, tk.END)
        regionId = regionIdEntry.get()
        regionIdEntry.delete(0, tk.END)
        countryId = countryIdEntry.get()
        countryIdEntry.delete(0, tk.END)
                
        
        database.insertIntoCompanyLocation(locationId, regionId, countryId)
        messagebox.showinfo("Success", "Data Saved Successfully.")



    def locationMasterDisplay():
        secondWindow = tk.Tk()
        secondWindow.title("DISPLAY COMPANY_LOCATION TABLE ")
        appLabel = tk.Label(secondWindow, text="COMPANY_LOCATION TABLE",fg="#06a099", width=40)
        appLabel.config(font=("Sylfaen", 30))
        appLabel.pack()

        tree = ttk.Treeview(secondWindow)
        tree["columns"] = ("one", "two")

        tree.heading("#0", text = "Location_Id")
        tree.heading("one", text = "Region_Id")
        tree.heading("two", text = "Country_Id")

        cursor = database.show("SELECT * FROM 'COMPANY_LOCATION' ;")
        i = 0
        for row in cursor:
            tree.insert('',i,text=row[0], values=(row[1], row[2]))
            i = i + 1
        tree.pack()
        secondWindow.mainloop()


    inputBtn = tk.Button(LOCATIONNwindow, text = 'Input', command=locationMasterInput)
    inputBtn.grid(row=5, column=0, pady=30)

    dispBtn = tk.Button(LOCATIONNwindow, text ='Display', command=locationMasterDisplay)
    dispBtn.grid(row=5, column=1, pady=30)

    quitBtn = tk.Button(LOCATIONNwindow, text='QUIT', command=LOCATIONNwindow.destroy)
    quitBtn.grid(row=6, column=1, pady=30)

    LOCATIONNwindow.mainloop()





def EMPLOYEEtable():
    EMPLOYEEwindow = tk.Tk()
    EMPLOYEEwindow.title('EMPLOYEE TABLE')

    employeeIdLabel = tk.Label(EMPLOYEEwindow, text="Enter Emp_Id", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10,0))

    employeeNameLabel = tk.Label(EMPLOYEEwindow, text="Enter Emp_Name", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=2, column=0, padx=(10,0))

    employeeDeptIdLabel = tk.Label(EMPLOYEEwindow, text="Enter Emp_DEpt_id", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=3, column=0, padx=(10,0))

    employeeSexLabel = tk.Label(EMPLOYEEwindow, text="Enter Sex", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=4, column=0, padx=(10,0))

    employeeMaritialLabel = tk.Label(EMPLOYEEwindow, text="Enter Maritial_Status", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=5, column=0, padx=(10,0))

    employeeJoinDateLabel = tk.Label(EMPLOYEEwindow, text="Enter emp_join _date", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=6, column=0, padx=(10,0))

    employeeBirthDateLabel = tk.Label(EMPLOYEEwindow, text="Enter Emp_birth_date", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=7, column=0, padx=(10,0))

    employeeAgeLabel = tk.Label(EMPLOYEEwindow, text="Enter Emp_age", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=1, column=3, padx=(10,0))

    employeeEducationIDLabel = tk.Label(EMPLOYEEwindow, text="Enter Emp_Education_id", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=2, column=3, padx=(10,0))

    countryDesignationIdLabel = tk.Label(EMPLOYEEwindow, text="Enter Emp_Designation_id", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=3, column=3, padx=(10,0))

    employeeSalaryLabel = tk.Label(EMPLOYEEwindow, text="Enter Emp_Salary", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=4, column=3, padx=(10,0))

    employeeLocationIdLabel = tk.Label(EMPLOYEEwindow, text="Enter Emp_Location_id", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=5, column=3, padx=(10,0))

    employeeActiveStatusLabel = tk.Label(EMPLOYEEwindow, text="Enter Emp_Active_status", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=6, column=3, padx=(10,0))

    

    empIdEntry = tk.Entry(EMPLOYEEwindow, width = 30)
    empIdEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))

    empNameEntry = tk.Entry(EMPLOYEEwindow, width =30)
    empNameEntry.grid(row=2, column=1, padx=(0,10))

    empDeptIdEntry = tk.Entry(EMPLOYEEwindow, width =30)
    empDeptIdEntry.grid(row=3, column=1, padx=(0,10))

    empSexEntry = tk.Entry(EMPLOYEEwindow, width = 30)
    empSexEntry.grid(row=4, column=1, padx=(0,10), pady=(30, 20))

    empMaritialStatusEntry = tk.Entry(EMPLOYEEwindow, width = 30)
    empMaritialStatusEntry.grid(row=5, column=1, padx=(0,10), pady=(30, 20))

    empJoinDateEntry = tk.Entry(EMPLOYEEwindow, width = 30)
    empJoinDateEntry.grid(row=6, column=1, padx=(0,10), pady=(30, 20))

    empBirthDateEntry = tk.Entry(EMPLOYEEwindow, width = 30)
    empBirthDateEntry.grid(row=7, column=1, padx=(0,10), pady=(30, 20))

    empAgeEntry = tk.Entry(EMPLOYEEwindow, width = 30)
    empAgeEntry.grid(row=1, column=4, padx=(0,10), pady=(30, 20))

    empEducationIdEntry = tk.Entry(EMPLOYEEwindow, width = 30)
    empEducationIdEntry.grid(row=2, column=4, padx=(0,10), pady=(30, 20))

    empDesignationIdEntry = tk.Entry(EMPLOYEEwindow, width = 30)
    empDesignationIdEntry.grid(row=3, column=4, padx=(0,10), pady=(30, 20))

    empSalaryEntry = tk.Entry(EMPLOYEEwindow, width = 30)
    empSalaryEntry.grid(row=4, column=4, padx=(0,10), pady=(30, 20))

    empLocationIdEntry = tk.Entry(EMPLOYEEwindow, width = 30)
    empLocationIdEntry.grid(row=5, column=4, padx=(0,10), pady=(30, 20))

    empActiveStatusEntry = tk.Entry(EMPLOYEEwindow, width = 30)
    empActiveStatusEntry.grid(row=6, column=4, padx=(0,10), pady=(30, 20))






    def employeeMasterInput():
        empId = empIdEntry.get()
        empIdEntry.delete(0, tk.END)

        empName = empNameEntry.get()
        empNameEntry.delete(0, tk.END)

        empDeptId = empDeptIdEntry.get()
        empDeptIdEntry.delete(0,tk.END)
        
        empSex = int(empSexEntry.get())
        empSexEntry.delete(0, tk.END)

        maritialStatus = int(empMaritialStatusEntry.get())
        empMaritialStatusEntry.delete(0, tk.END)
        
        joinDate = empJoinDateEntry.get()
        empJoinDateEntry.delete(0, tk.END)
        
        birthDate = empBirthDateEntry.get()
        empBirthDateEntry.delete(0, tk.END)

        age = int(empAgeEntry.get())
        empAgeEntry.delete(0, tk.END)

        educationId = empEducationIdEntry.get()
        empEducationIdEntry.delete(0, tk.END)

        designationId = empDesignationIdEntry.get()
        empDesignationIdEntry.delete(0, tk.END)

        salary = float(empSalaryEntry.get())
        empSalaryEntry.delete(0, tk.END)

        locationId = empLocationIdEntry.get()
        empLocationIdEntry.delete(0, tk.END)
    
        activeStatus = int(empActiveStatusEntry.get())
        empActiveStatusEntry.delete(0, tk.END)


                
        
        database.insertIntoEmployee(empId, empName, empDeptId, empSex, maritialStatus, joinDate, birthDate, age, educationId, designationId, salary, locationId, activeStatus)
        
        messagebox.showinfo("Success", "Data Saved Successfully.")
        


    def employeeMasterDisplay():
        secondWindow = tk.Tk()
        secondWindow.title("DISPLAY EMPLOYEE TABLE ")
        appLabel = tk.Label(secondWindow, text="EMPLOYEE TABLE",fg="#06a099", width=40)
        appLabel.config(font=("Sylfaen", 30))
        appLabel.pack()

        tree = ttk.Treeview(secondWindow)
        tree["columns"] = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven","twelve")

        tree.heading("#0", text = "Emp_Id")
        tree.heading("one", text = "Emp_Name")
        tree.heading("two", text = "Emp_Dept_Id")
        tree.heading("three", text = "Emp_Sex")
        tree.heading("four", text = "Emp_Maritial_Status")
        tree.heading("five", text = "Emp_Join_Date")
        tree.heading("six", text = "Emp_Birth_Date")
        tree.heading("seven", text = "Emp_Age")
        tree.heading("eight", text = "Emp_Education_Id")
        tree.heading("nine", text = "Emp_Designation_Id")
        tree.heading("ten", text = "Emp_Salary")
        tree.heading("eleven", text = "Emp_Location_Id")
        tree.heading("twelve", text = "Emp_Active_Status")

        

        cursor = database.show("SELECT * FROM 'EMPLOYEE' ;")
        i = 0
        for row in cursor:
            tree.insert('',i,text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12])) 
            i = i + 1
        tree.pack()
        secondWindow.mainloop()


    inputBtn = tk.Button(EMPLOYEEwindow, text = 'Input', command=employeeMasterInput)
    inputBtn.grid(row=8, column=2, padx = 50, pady=30)

    dispBtn = tk.Button(EMPLOYEEwindow, text ='Display', command= employeeMasterDisplay)
    dispBtn.grid(row=8, column=4, padx = 50, pady=30)

    quitBtn = tk.Button(EMPLOYEEwindow, text='QUIT', command=EMPLOYEEwindow.destroy)
    quitBtn.grid(row=9, column=4, padx = 50, pady=30)

    EMPLOYEEwindow.mainloop()









def ACCOUNT_DETAILStable():
    ACCOUNTwindow = tk.Tk()
    ACCOUNTwindow.title('ACCOUNT DETAILS TABLE')

    empIdLabel = tk.Label(ACCOUNTwindow, text="Enter Emp_Id", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10,0))

    accountNOLabel = tk.Label(ACCOUNTwindow, text="Enter Account_No", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=2, column=0, padx=(10,0))

    bankIdLabel = tk.Label(ACCOUNTwindow, text="Enter Bank_Id", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=3, column=0, padx=(10,0))

    accountTypeLabel = tk.Label(ACCOUNTwindow, text="Enter Account_type ", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=4, column=0, padx=(10,0))


    empIdEntry = tk.Entry(ACCOUNTwindow, width = 30)
    empIdEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))

    accountNoEntry = tk.Entry(ACCOUNTwindow, width =30)
    accountNoEntry.grid(row=2, column=1, padx=(0,10))

    bankIdEntry = tk.Entry(ACCOUNTwindow, width = 30)
    bankIdEntry.grid(row=3, column=1, padx=(0,10), pady=(30, 20))

    accountTypeEntry = tk.Entry(ACCOUNTwindow, width = 30)
    accountTypeEntry.grid(row=4, column=1, padx=(0,10), pady=(30, 20))


    def accountMasterInput():
        empId = empIdEntry.get()
        empIdEntry.delete(0, tk.END)
        accountNo = int(accountNoEntry.get())
        accountNoEntry.delete(0, tk.END)
        bankId = bankIdEntry.get()
        bankIdEntry.delete(0, tk.END)
        accountType = int(accountTypeEntry.get())
        accountTypeEntry.delete(0, tk.END)
                
        
        database.insertIntoAccountDetails(empId, accountNo, bankId, accountType)
        
        messagebox.showinfo("Success", "Data Saved Successfully.")



    def accountMasterDisplay():
        secondWindow = tk.Tk()
        secondWindow.title("DISPLAY ACCOUNT DETAILS TABLE ")
        appLabel = tk.Label(secondWindow, text="ACCOUNT_DETAILS TABLE",fg="#06a099", width=40)
        appLabel.config(font=("Sylfaen", 30))
        appLabel.pack()

        tree = ttk.Treeview(secondWindow)
        tree["columns"] = ("one", "two", "three")

        tree.heading("#0", text = "Emp_Id")
        tree.heading("one", text = "Account_No")
        tree.heading("two", text = "Bank_Id")
        tree.heading("three", text = "Account_Type")

        cursor = database.show("SELECT * FROM 'ACCOUNT_DETAILS' ;")
        i = 0
        for row in cursor:
            tree.insert('',i,text=row[0], values=(row[1], row[2], row[3]))
            i = i + 1
        tree.pack()
        secondWindow.mainloop()


    inputBtn = tk.Button(ACCOUNTwindow, text = 'Input', command=accountMasterInput)
    inputBtn.grid(row=6, column=0, pady=30)

    dispBtn = tk.Button(ACCOUNTwindow, text ='Display', command=accountMasterDisplay)
    dispBtn.grid(row=6, column=1, pady=30)

    quitBtn = tk.Button(ACCOUNTwindow, text='QUIT', command=ACCOUNTwindow.destroy)
    quitBtn.grid(row=7, column=1, pady=30)

    ACCOUNTwindow.mainloop()






def FAMILY_DETAILStable():
    FAMILYwindow = tk.Tk()
    FAMILYwindow.title('FAMILY DETAILS TABLE')

    familyIdLabel = tk.Label(FAMILYwindow, text="Enter Family_Id", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10,0))

    empIdLabel = tk.Label(FAMILYwindow, text="Enter Emp_id", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=2, column=0, padx=(10,0))

    relationIdLabel = tk.Label(FAMILYwindow, text="Enter Emp_Relation_Id", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=3, column=0, padx=(10,0))

    relationNameLabel = tk.Label(FAMILYwindow, text="Enter Relation Name ", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=4, column=0, padx=(10,0))

    relationAgeLabel = tk.Label(FAMILYwindow, text="Enter Relation Age ", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=5, column=0, padx=(10,0))

    nomineeLabel = tk.Label(FAMILYwindow, text="Enter Nominee", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=6, column=0, padx=(10,0))



    familyIdEntry = tk.Entry(FAMILYwindow, width = 30)
    familyIdEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))

    empIdEntry = tk.Entry(FAMILYwindow, width =30)
    empIdEntry.grid(row=2, column=1, padx=(0,10))

    relationIdEntry = tk.Entry(FAMILYwindow, width = 30)
    relationIdEntry.grid(row=3, column=1, padx=(0,10), pady=(30, 20))

    relationNameEntry = tk.Entry(FAMILYwindow, width = 30)
    relationNameEntry.grid(row=4, column=1, padx=(0,10), pady=(30, 20))

    relationAgeEntry = tk.Entry(FAMILYwindow, width = 30)
    relationAgeEntry.grid(row=5, column=1, padx=(0,10), pady=(30, 20))

    nomineeEntry = tk.Entry(FAMILYwindow, width = 30)
    nomineeEntry.grid(row=6, column=1, padx=(0,10), pady=(30, 20))


    def familyMasterInput():
        familyId = familyIdEntry.get()
        familyIdEntry.delete(0, tk.END)

        empId = empIdEntry.get()
        empIdEntry.delete(0, tk.END)

        relaltionId = relationIdEntry.get()
        relationIdEntry.delete(0, tk.END)

        relationName = relationNameEntry.get()
        relationNameEntry.delete(0, tk.END)
                
        relationAge = int(relationAgeEntry.get())
        relationAgeEntry.delete(0, tk.END)

        nominee = int(nomineeEntry.get())
        nomineeEntry.delete(0, tk.END)


        
        database.insertIntoFamily(familyId, empId, relaltionId, relationName, relationAge, nominee)   
    
        messagebox.showinfo("Success", "Data Saved Successfully.")



    def familyMasterDisplay():
        secondWindow = tk.Tk()
        secondWindow.title("DISPLAY FAMILY DETAILS TABLE ")
        appLabel = tk.Label(secondWindow, text="FAMILY_DETAILS TABLE",fg="#06a099", width=40)
        appLabel.config(font=("Sylfaen", 30))
        appLabel.pack()

        tree = ttk.Treeview(secondWindow)
        tree["columns"] = ("one", "two", "three", "four", "five")

        tree.heading("#0", text = "Family_Id")
        tree.heading("one", text = "Emp_Id")
        tree.heading("two", text = "Relation_Id")
        tree.heading("three", text = "Relation_Name")
        tree.heading("four", text = "Relation_Age")
        tree.heading("five", text = "Nominee")


        cursor = database.show("SELECT * FROM 'FAMILY_DETAILS' ;")
        i = 0
        for row in cursor:
            tree.insert('',i,text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))
            i = i + 1
        tree.pack()
        secondWindow.mainloop()


    inputBtn = tk.Button(FAMILYwindow, text = 'Input', command=familyMasterInput)
    inputBtn.grid(row=8, column=0, pady=30)

    dispBtn = tk.Button(FAMILYwindow, text ='Display', command=familyMasterDisplay)
    dispBtn.grid(row=8, column=1, pady=30)

    quitBtn = tk.Button(FAMILYwindow, text='QUIT', command=FAMILYwindow.destroy)
    quitBtn.grid(row=9, column=1, pady=30)

    FAMILYwindow.mainloop()








def ADDRESStable():
    ADDRESSwindow = tk.Tk()
    ADDRESSwindow.title('ADDRESS TABLE')

    addressIdLabel = tk.Label(ADDRESSwindow, text="Enter Address_Id", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10,0))

    empIdLabel = tk.Label(ADDRESSwindow, text="Enter Emp_id", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=2, column=0, padx=(10,0))

    address1Label = tk.Label(ADDRESSwindow, text="Enter Address1", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=3, column=0, padx=(10,0))

    address2Label = tk.Label(ADDRESSwindow, text="Enter Address2", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=4, column=0, padx=(10,0))

    telNoLabel = tk.Label(ADDRESSwindow, text="Enter Tel_No ", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=5, column=0, padx=(10,0))

    addressTypeLabel = tk.Label(ADDRESSwindow, text="Enter Address_Type", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=6, column=0, padx=(10,0))



    addressIdEntry = tk.Entry(ADDRESSwindow, width = 30)
    addressIdEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))

    empIdEntry = tk.Entry(ADDRESSwindow, width =30)
    empIdEntry.grid(row=2, column=1, padx=(0,10))

    address1Entry = tk.Entry(ADDRESSwindow, width = 30)
    address1Entry.grid(row=3, column=1, padx=(0,10), pady=(30, 20))

    address2Entry = tk.Entry(ADDRESSwindow, width = 30)
    address2Entry.grid(row=4, column=1, padx=(0,10), pady=(30, 20))

    telNoEntry = tk.Entry(ADDRESSwindow, width = 30)
    telNoEntry.grid(row=5, column=1, padx=(0,10), pady=(30, 20))

    addressTypeEntry = tk.Entry(ADDRESSwindow, width = 30)
    addressTypeEntry.grid(row=6, column=1, padx=(0,10), pady=(30, 20))


    def addressMasterInput():
        addressId = addressIdEntry.get()
        addressIdEntry.delete(0, tk.END)

        empId = empIdEntry.get()
        empIdEntry.delete(0, tk.END)

        address1 = address1Entry.get()
        address1Entry.delete(0, tk.END)

        address2 = address2Entry.get()
        address2Entry.delete(0, tk.END)
                
        telNo = telNoEntry.get()
        telNoEntry.delete(0, tk.END)

        addressType = int(addressTypeEntry.get())
        addressTypeEntry.delete(0, tk.END)


        
        database.insertIntoAddress(addressId, empId, address1, address2, telNo, addressType)
        
        messagebox.showinfo("Success", "Data Saved Successfully.")



    def addressMasterDisplay():
        secondWindow = tk.Tk()
        secondWindow.title("DISPLAY ADDRESS TABLE ")
        appLabel = tk.Label(secondWindow, text="ADDRESS TABLE",fg="#06a099", width=40)
        appLabel.config(font=("Sylfaen", 30))
        appLabel.pack()

        tree = ttk.Treeview(secondWindow)
        tree["columns"] = ("one", "two", "three", "four", "five")

        tree.heading("#0", text = "Address_Id")
        tree.heading("one", text = "Emp_Id")
        tree.heading("two", text = "Address1")
        tree.heading("three", text = "Address2")
        tree.heading("four", text = "Tel_No")
        tree.heading("five", text = "Address_Type")


        cursor = database.show("SELECT * FROM 'ADDRESS' ;")
        i = 0
        for row in cursor:
            tree.insert('',i,text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))
            i = i + 1
        tree.pack()
        secondWindow.mainloop()


    inputBtn = tk.Button(ADDRESSwindow, text = 'Input', command=addressMasterInput)
    inputBtn.grid(row=8, column=0, pady=30)

    dispBtn = tk.Button(ADDRESSwindow, text ='Display', command=addressMasterDisplay)
    dispBtn.grid(row=8, column=1, pady=30)

    quitBtn = tk.Button(ADDRESSwindow, text='QUIT', command=ADDRESSwindow.destroy)
    quitBtn.grid(row=9, column=1, pady=30)

    ADDRESSwindow.mainloop()

def reportGenerator():
    def viewReport():
        VIEWwindow = tk.Tk()
        VIEWwindow.title('VIEW REPORT')

        query = str(queryEntry.get())
        queryEntry.delete(0, tk.END)

        
        tree = ttk.Treeview(VIEWwindow)
    
        cursor = database.show(query)  

        i = 0
        for row in cursor:
            tree.insert('',i,text = row[0], values = (row[1:]))
            i = i + 1
        tree["columns"] = (row)
        tree.pack()
        VIEWwindow.mainloop()

    REPORTwindow = tk.Tk()
    REPORTwindow.title('REPORT GENERATION')

    queryLabel = tk.Label(REPORTwindow, text="Enter the Query to generate REPORT ", width=40, anchor='w', font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10,0))

    queryEntry = tk.Entry(REPORTwindow, width = 30)
    queryEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))


    enterButton = tk.Button(REPORTwindow, text = 'ENTER', command = viewReport)
    enterButton.grid(row = 3, column = 0, padx = (10,10), pady = 30)

    quitButton = tk.Button(REPORTwindow, text='QUIT', command=REPORTwindow.destroy)
    quitButton.grid(row=3, column=2, padx = (10,10), pady=30)
    REPORTwindow.mainloop()


    



button1 = tk.Button(window, text="DEPARTMENT_MASTER", command=DEPT_MASTERtable)
button1.grid(row=1, column=0, pady=30)

button2 = tk.Button(window, text="REGION_MASTER", command=REGION_MASTERtable)
button2.grid(row=1, column=1, pady=30)

button3 = tk.Button(window, text="COUNTRY_MASTER", command=COUNTRY_MASTERtable)
button3.grid(row=1, column=2, padx=(10,10), pady=30)

button4 = tk.Button(window, text="RELATION_MASTER", command=RELATION_MASTERtable)
button4.grid(row=2, column=0, pady = 30)

button5 = tk.Button(window, text="BANK_MASTER", command=BANK_MASTERtable)
button5.grid(row=2, column=1, pady = 30)

button6 = tk.Button(window, text="EDUCATION_MASTER", command=EDUCATION_MASTERtable)
button6.grid(row=2, column=2, padx = (10,10), pady = 30)

button7 = tk.Button(window, text="DESIGNATION_MASTER", command=DESIGNATION_MASTERtable)
button7.grid(row=3, column=0, pady = 30)

button8 = tk.Button(window, text="COMPANY_LOCATION", command=COMPANY_LOCATIONtable)
button8.grid(row=3, column=1, pady = 30)

button9 = tk.Button(window, text="EMPLOYEE", command=EMPLOYEEtable)
button9.grid(row=3, column=2, padx = (10,10), pady = 30)

button10 = tk.Button(window, text="ACCOUNT_DETAILS", command=ACCOUNT_DETAILStable)
button10.grid(row=4, column=0, pady = 30)

button11 = tk.Button(window, text="FAMILY_DETAILS", command=FAMILY_DETAILStable)
button11.grid(row=4, column=1, pady = 30)

button12 = tk.Button(window, text="ADDRESS", command=ADDRESStable)
button12.grid(row=4, column=2, padx = (10,10), pady = 30)


button13 = tk.Button(window, text='QUIT', command=window.destroy)
button13.grid(row=6, column=2, padx = (10,10), pady=30)


button14 = tk.Button(window, text = 'REPORT GENERATION', command = reportGenerator)
button14.grid(row = 6, column = 0, padx = (10,10), pady = 30)


window.mainloop()