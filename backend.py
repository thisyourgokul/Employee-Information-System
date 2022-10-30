import sqlite3

class DatabaseOperation:

    def __init__(self,db):
        self.connection = sqlite3.connect(db)
        self.cur = self.connection.cursor()
        self.cur.execute(" CREATE TABLE IF NOT EXISTS DEPARTMENT_MASTER (Dept_Id VARCHAR PRIMARY KEY, Dept_Name VARCHAR); ")

        self.cur.execute(" CREATE TABLE IF NOT EXISTS REGION_MASTER (Region_Id VARCHAR PRIMARY KEY, Region_Name TEXT, Region_Status INTEGER); ")

        self.cur.execute(" CREATE TABLE IF NOT EXISTS COUNTRY_MASTER (Country_Id VARCHAR PRIMARY KEY, Country_Name text); ")

        self.cur.execute(" CREATE TABLE IF NOT EXISTS RELATION_MASTER (Relation_Id VARCHAR PRIMARY KEY, Relation_Desc VARCHAR); ")

        self.cur.execute(" CREATE TABLE IF NOT EXISTS BANK_MASTER (Bank_Id VARCHAR PRIMARY KEY, Bank_Name TEXT); ")

        self.cur.execute(" CREATE TABLE IF NOT EXISTS EDUCATION_MASTER (Education_Id VARCHAR PRIMARY KEY, Education_Desc VARCHAR); ")

        self.cur.execute(" CREATE TABLE IF NOT EXISTS DESIGNATION_MASTER (Designation_Id VARCHAR PRIMARY KEY, Designation_Desc VARCHAR); ")

        self.cur.execute(" CREATE TABLE IF NOT EXISTS COMPANY_LOCATION (Location_Id VARCHAR PRIMARY KEY, Region_Id VARCHAR, Country_Id VARCHAR, FOREIGN KEY(Region_Id) REFERENCES REGION_MASTER(Region_Id), FOREIGN KEY(Country_Id) REFERENCES COUNTRY_MASTER(Country_Id) ); ")

        self.cur.execute(" CREATE TABLE IF NOT EXISTS EMPLOYEE (Emp_Id VARCHAR PRIMARY KEY, Emp_Name TEXT, Emp_Dept_Id VARCHAR, Emp_Sex INTEGER, Emp_Maritial_Status INTEGER, Emp_Join_Date DATE, Emp_Birth_Date DATE DATE, Emp_Age INTEGER, Emp_Education_Id VARCHAR, Emp_Designation_Id VARCHAR, Emp_Salary NUMBER(10,2), Emp_Location_Id VARCHAR, Emp_Active_Status INTEGER, FOREIGN KEY(Emp_Dept_Id) REFERENCES DEPARTMENT_MASTER(Dept_Id), FOREIGN KEY(Emp_Education_Id) REFERENCES EDUCATION_MASTER(Education_Id), FOREIGN KEY(Emp_Designation_Id) REFERENCES DESIGNATION_MASTER(Designation_Id), FOREIGN KEY(Emp_Location_ID) REFERENCES COMPANY_LOCATION(Location_Id) ); ")

        self.cur.execute(" CREATE TABLE IF NOT EXISTS ACCOUNT_DETAILS (Emp_Id VARCHAR, Account_No INTEGER(10), Bank_Id VARCHAR, Account_Type INTEGER, PRIMARY KEY(Emp_Id, Account_No),  FOREIGN KEY(Emp_ID) REFERENCES EMPLOYEE(Emp_Id), FOREIGN KEY(Bank_Id) REFERENCES BANK_MASTER(Bank_Id) ); ")

        self.cur.execute(" CREATE TABLE IF NOT EXISTS FAMILY_DETAILS (Family_Id VARCHAR, Emp_Id VARCHAR, Emp_Relation_Id VARCHAR, Relation_Name TEXT, Relation_Age INTEGER, Nominee INTEGE, PRIMARY KEY(Family_Id, Emp_Id), FOREIGN KEY(Emp_Id) REFERENCES EMPLOYEE(Emp_Id), FOREIGN KEY(Emp_Relation_Id) REFERENCES RELATION_MASTER(Relation_Id) ); ")

        self.cur.execute(" CREATE TABLE IF NOT EXISTS ADDRESS (Address_Id VARCHAR, Emp_Id VARCHAR, Address1 VARCHAR, Address2 VARCHAR, Tel_No VARCHAR, Address_Type INTEGER, PRIMARY KEY(Address_Id, Emp_Id), FOREIGN KEY(Emp_Id) REFERENCES EMPLOYEE(Emp_Id) ); ")
        self.connection.commit()

    def show(self, query):
        cursor = self.cur.execute(query)
        return cursor

    def insertIntoDeptMaster(self, DId, Dname):
        self.cur.execute("INSERT INTO DEPARTMENT_MASTER (Dept_Id, Dept_Name) VALUES ('" + DId + "','"+ Dname + "')")
        self.connection.commit()             

    def insertIntoRegionMaster(self, RegionId, RegionName, RegionStatus):
        self.cur.execute("INSERT INTO REGION_MASTER (Region_Id, Region_Name, Region_Status) VALUES ('" + RegionId +"','" + RegionName +"'," + str(RegionStatus) + ")" )
        self.connection.commit()

    def insertIntoCountryMaster(self, countryId, countryName):
        self.cur.execute("INSERT INTO COUNTRY_MASTER (Country_Id, Country_Name) VALUES ('" + countryId +"','" + countryName + "')")
        self.connection.commit()

    def insertIntoRelationMaster(self, relationId, relationDesc):
        self.cur.execute("INSERT INTO RELATION_MASTER (Relation_Id, Relation_Desc) VALUES ('" + relationId +"','" + relationDesc + "')")
        self.connection.commit()

    def insertIntoBankMaster(self, bankId, bankName):
        self.cur.execute("INSERT INTO BANK_MASTER (Bank_Id, Bank_Name) VALUES ('" + bankId +"','" + bankName + "')")
        self.connection.commit()

    def insertIntoEducationMaster(self, educationId, educationDesc):
        self.cur.execute("INSERT INTO EDUCATION_MASTER (Education_Id, Education_Desc) VALUES ('" + educationId +"','" + educationDesc + "')")
        self.connection.commit()

    def insertIntoDesignationMaster(self, designationId, desinationDesc):
        self.cur.execute("INSERT INTO DESIGNATION_MASTER (Designation_Id, Designation_Desc) VALUES ('" + designationId +"','" + desinationDesc + "')")
        self.connection.commit()

    def insertIntoCompanyLocation(self, locationId, regionId, countryId):
        self.cur.execute("INSERT INTO COMPANY_LOCATION (Location_Id, Region_Id, Country_Id) VALUES ('" + locationId +"','" + regionId + "','" + countryId + "' )")
        self.connection.commit()  

    def insertIntoEmployee(self, empId, empName, empDeptId, empSex, maritialStatus, joinDate, birthDate, age,       educationId, designationId, salary, locationId, activeStatus):
        self.cur.execute("INSERT INTO EMPLOYEE (Emp_Id, Emp_Name, Emp_Dept_Id, Emp_Sex, Emp_Maritial_status, Emp_Join_Date, Emp_Birth_Date, Emp_Age, Emp_Education_Id, Emp_Designation_Id, Emp_Salary, Emp_Location_Id, Emp_Active_Status) VALUES ('" + empId +"','" + empName + "','" + empDeptId + "'," + str(empSex) + "," + str(maritialStatus) + ",'" + joinDate + "','" + birthDate + "'," + str(age) + ",'" + educationId + "','" + designationId + "'," + str(salary) + ",'" + locationId + "'," + str(activeStatus) + " )")
        self.connection.commit()

    def insertIntoAccountDetails(self, empId, accountNo, bankId, accountType):
        self.cur.execute("INSERT INTO ACCOUNT_DETAILS (Emp_Id, Account_No, Bank_Id, Account_Type) VALUES ('" + empId + "',"+ str(accountNo) + ",'" + bankId +"'," + str(accountType) +");")
        self.connection.commit()

    def insertIntoFamily(self, familyId, empId, relaltionId, relationName, relationAge, nominee):
        self.cur.execute("INSERT INTO FAMILY_DETAILS (Family_Id, Emp_Id, Emp_Relation_Id, Relation_Name, Relation_Age, Nominee) VALUES ('" + familyId + "','"+ empId + "','" + relaltionId + "','" + relationName + "'," + str(relationAge) + "," + str(nominee) + " );")
        self.connection.commit()

    def insertIntoAddress(self, addressId, empId, address1, address2, telNo, addressType):
        self.cur.execute("INSERT INTO ADDRESS (Address_Id, Emp_Id, Address1, Address2, Tel_No, Address_Type) VALUES ('" + addressId + "','"+ empId + "','" + address1 + "','" + address2 + "','" + telNo + "'," + str(addressType) + "); ")
        self.connection.commit() 


