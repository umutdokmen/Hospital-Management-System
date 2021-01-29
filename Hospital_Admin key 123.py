from random import randint
from datetime import datetime
import datetime
import random
def home():
    print("Welcome to hospital")
    print("Enter 1 to ADMIN LOG IN")
    print("Enter 2 to PATIENT LOG IN")
    try:
       choice = int(input("Please enter your choice:"))
    except ValueError:
        print("Invalid input.Please enter number 1 or 2")
        home()
    except:
        print("Please enter number 1 or 2")
        home()
    if choice == 1:
        key = int(input("Please enter admin key:"))
        if key == 123:
            main()
        else:
            print("invalid key")
    elif choice == 2:
        print("Press 1 to get new appoinment")
        print("Press 2 to view your appoinment")
        print("Press 3 to change your appoinment date")
        print("Press 4 to go pharmacy to get medicines")
        print("Press 5 to go home page")
        pchoice = int(input())
        if pchoice == 1:
            get_appoinment()
            chc=int(input("Press 1 to back main"))
            if chc==1:
                main()
            else:
                exit()
        elif pchoice == 2:
            view_appoinment()
            chc = int(input("Press 1 to back main"))
            if chc == 1:
                main()
            else:
                exit()
        elif pchoice==3:
            change_appoinment()
        elif pchoice==4:
            create_pharmacy()
        else:
            home()
    else:
        print("Invalid input.Please enter 1 or 2")
        main()
class Person():
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender


class Patient(Person):
    def __init__(self, name, surname, age, gender, insurance_no, protocol_no, tel_no):
        Person.__init__(self, name, surname, gender)
        self.age = age
        self.insurance_no = insurance_no
        self.protocol_no = protocol_no
        self.tel_no = tel_no

    def __str__(self):
        return "name:" + self.name + " surname: " + self.surname + "  age:" + str(self.age) + \
               " gender:" + self.gender + " insurance no:" + str(self.insurance_no) + \
               " protocol no:" + str(self.protocol_no) + " tel no:" + str(self.tel_no)

    def __repr__(self):
        return repr((self.name, self.surname, self.age, self.gender, self.insurance_no, self.protocol_no, self.tel_no))


list_patient = [Patient("Kemal", "Kabuk", 52, "male", 170435, 458, 5464783320),
                Patient("Halime", "Malik", 66, "female", 150678, 444, 5513958710),
                Patient("Hasan", "Ceylan", 30, "male", 170315, 687, 5555781324)]


def add_patient():
    a = 1
    n = int(input("how many patient do you want to add:"))
    while a < n + 1:
        print("for", a, ".employee")
        name = input("Please enter name")
        surname = input("Please enter surname")
        age = int(input("Please enter age"))
        gender = input("Please enter gender male or female ?")
        insurance_no = int(input("Please enter insurance no"))
        protocol_no = int(input("Plaese enter protocol no"))
        tel_no = int(input("Please enter tel no"))
        patient = Patient(name, surname, age, gender, insurance_no, protocol_no, tel_no)
        list_patient.append(patient)
        a += 1
    print("After adding personel list is:")
    print(list_patient[0])

    b = int(input("Press 1 to back main menu or any key to exit"))


def search_patient():
    print("Press 1 To search according to 'PROTOCOL NO'")
    print("Press 2 To search according to 'NAME'")
    print("Press 3 To search according to 'TEL NO'")
    print("Press 4 To back 'MAIN MENU'")
    c = int(input("Please enter your choice"))
    if c == 1:
        j = int(input("Please enter protocol no that you want to search"))
        list_protocol = []
        for i in range(len(list_patient)):
            if list_patient[i].protocol_no == j:
                list_protocol.append(list_patient[i])
        if len(list_protocol) == 0:
            print("Record does not exist")
            y = int(input("Please enter 1 to back main menu or 2 to try again"))
            if y == 1:
                main()
            if y == 2:
                search_patient()
        else:
            print(list_protocol[0])
    elif c == 2:
        j = input("Please enter name that you want to search")
        listnamepatient = []
        for i in range(len(list_patient)):
            if list_patient[i].name == j:
                listnamepatient.append(list_patient[i])
        for i in range(len(listnamepatient)):
            print(listnamepatient[i])
        if len(listnamepatient) == 0:
            print("Please try again as enter first letter capital other letters are lower case")
            search_patient()
    elif c == 3:
        j = int(input("Please enter 'Tel No' that you want to search"))
        listtelno = []
        for i in range(len(list_patient)):
            if list_patient[i].tel_no == j:
                listtelno.append(list_patient[i])
        if len(listtelno) == 0:
            print("Record does not exist")
        else:
            print(list_patient[i])
    elif c == 4:
        main()
    ch = int(input("Press '1' to enter 'MAIN MENU' or any key to 'EXIT' "))
    if ch == 1:
        main()


def delete_patient():
    pn = int(input("Please enter protocol no of patient you want to delete "))
    for i in list_patient:
        if i.protocol_no == pn:
            print("The patient you want to delete", i)
            list_patient.remove(i)
    print("Patient list after delete")
    for m in list_patient:
        print(m)
    x = int(input("Please press 1 to back main menu or 2 to exit"))
    if x == 1:
        main()
    else:
        exit()


def sort_patient():
    print("Enter 1 to sort by age")
    print("Enter 2 to sort by surname")
    print("Enter 3 to sort by insurance no")
    choice = int(input("Please enter sort type"))
    if choice == 1:
        print(sorted(list_patient, key=lambda Patient: Patient.age))
    elif choice == 2:
        print(sorted(list_patient, key=lambda Patient: Patient.surname))
    elif choice == 3:
        print(sorted(list_patient, key=lambda Patient: Patient.insurance_no))
    print("Enter 1 to back main menu")
    c = int(input())
    if c == 1:
        main()


class Employee(Person):
    def __init__(self, job, name, surname, gender, department, ID):
        Person.__init__(self, name, surname, gender)
        self.job = job
        self.department = department
        self.ID = ID

    def __str__(self):
        return "job:" + self.job + "  name: " + self.name + "  surname:" + self.surname + \
               " gender:" + self.gender + "  department:" + self.department + "  ID:" + str(self.ID)

    def change_ID(self, new_ID):
        self.ID = new_ID

    def __repr__(self):
        return repr((self.job, self.name, self.surname, self.gender, self.department, self.ID))


list = [Employee("doctor", "Umut", "Dökmen", "male", "cardiology", 160),
        Employee("doctor", "Ege", "Helvaci", "male", "gastro", 150),
        Employee("nurse", "Fatma", "Selvi", "female", "ear nose and throat", 220),
        Employee("doctor", "Mustafa", "Akar", "male", "oncology", 170),
        Employee("nurse", "Begum", "Su", "female", "dermatology", 210),
        Employee("doctor", "Ferit", "Yenice", "male", "general surgery", 140),
        Employee("doctor", "Cemil", "Solak", "male", "neurology", 180),
        Employee("doctor", "Ferhat", "Yaman", "male", "urology", 190),
        Employee("doctor", "Hale", "Pehlivan", "female", "psychiatry", 130),
        Employee("doctor", "Yasemin", "Denizli", "female", "dermatology", 110),
        Employee("nurse", "Canan", "Akdeniz", "female", "gastro", 250),
        Employee("nurse", "Buse", "Soylu", "female", "cardiology", 260),
        Employee("nurse", "Canan", "Ak", "female", "neurology", 280),
        Employee("doctor", "Melih", "Soyer", "male", "ear nose and throat", 120),
        Employee("nurse", "Sevim", "Bilginer", "female", "general surgery", 240),
        Employee("secretary","Cansu","Tatar","female","general personal",300),
        Employee("cleaner","Sevim","Cambaz","female","domestic",410)
        ]

class Pharmacy(Person):
    def __init__(self,name,surname,gender,insurance_no,cost):
        Person.__init__(self,name,surname,gender)
        self.insurance_no=insurance_no
        self.cost=cost

    def __str__(self):
        return "name:" + self.name+" surname: " + self.surname + " gender:" + self.gender +\
               " insurance no:" + str(self.insurance_no) +" total cost:"+str(self.cost)+" TL"
    def compute_cost(self,price):
        self.cost=price+self.cost
        return self.cost
def create_pharmacy():
    name=input("Please enter patient name: ")
    surname = input("Please enter patient surname: ")
    gender = input("Please enter gender male or female: ")
    insurance_no = int(input("Please enter patient insurance no: "))
    cost=0
    x=Pharmacy(name,surname,gender,insurance_no,cost)
    determine_price(x)
dict_medicine={"danitrin fort":4.63,"digoxon":2.5,"monodur":16.2,"isordil":6.03,"lansor":14.91,
"famodin":19.16,"esopro":29.70,"talcit":19.33,"zimax":25.94,"suprax":25.94,"sancefix":19.55,
"clobesol":19.33,"corbinal":28.94,"troderm":23.59,"proctolog":6.5,"dilaprost":33.1,"flomax":16.52,
"hytrin":23.78,"depalex":37.73,"citoles":20.61,"abilify":71.21,"alyse":59.44,"uropan":20.73,"spasmex":73.43,
"volterra":65.54,"kinzy":68.80,"toltex":116.93,"prozac":25.15,"efexor":21.91,"lustral":27.92,"cipram":16.36}
def determine_price(x):
    print("---------CURRENT STOCK MEDICINE LIST----------")
    print("CARDIOLOGY:danitrin fort; digoxin ;monodur ;isordil-GASTRO:lansor; famodin; esopro; talcit")
    print("EAR-NOSE-THROAT:zimax;suprax;sancefix-DERMATOLOGY:clobesol;corbinal;troderm")
    print("GENERAL SURGERY:proctolog;dilaprost;flomax;hytrin-NEUROLOGY:depalex;citoles;abilify;alyse")
    print("UROLOGY:uropan;spasmex;volterra;kinzy;toltex-PSYCHIATRY:prozac;efexor;lustral;cipram")
    medicine_name = input("Please enter medicine name you want")
    medicine_count = int(input("How many box do you need"))
    for i in dict_medicine:
        if medicine_name == i:
            print("One",i,"'s price is:",dict_medicine[i])
            price = dict_medicine[i]*medicine_count
    x.compute_cost(price)
    print(x)
    c=int(input("Enter 1 you to get more medicine,Enter 2 to go main menu "))
    if c==1:
        determine_price(x)
    elif c==2:
        home()
    else:
        exit()
class Appointment(Person):
    def __init__(self, name, surname, protocol_no, department, doctor_name, doctor_surname, date, hour, minute):
        self.name = name
        self.surname = surname
        self.protocol_no = protocol_no
        self.date = date
        self.department = department
        self.doctor_name = doctor_name
        self.doctor_surname = doctor_surname
        self.hour = hour
        self.minute = minute

    def __str__(self):
        return "name:" + self.name + " surname:" + self.surname + \
               " department:" + self.department + "\ndoctor name:" + self.doctor_name + \
               " doctor surname:" + self.doctor_surname + " date:" + str(self.date) + "  " + str(
            self.hour) + ":" + str(self.minute)

    def get_date(self, newdate):
        return newdate


list_appoinment = []


def get_appoinment():

    name = input("Please enter patient name,'fist letter should be capital': ")
    surname = input("Please enter patient surname: 'first letter should be capital':")
    protocol_no = int(input("Please enter patient protocol no: "))
    print("cardiology-gastro-ear nose and throat-dermatology-general surgery\n-neurology"
          "-oncology-psychiatry-dermatology")
    department = input("Please enter department you want to get examined: ")

    for i in list:
        if i.department == department and i.job == "doctor":
            doctor_name = i.name
            doctor_surname = i.surname
    date = datetime.date(randint(2020, 2020), randint(5,6), randint(1, 30))
    date=datetime.datetime.strptime(str(date), "%Y-%m-%d").strftime("%d-%m-%Y")
    hour = random.randint(8, 18)
    minute = random.randrange(0,59,5)
    if minute < 9:
        minute =str(0)+str(minute)
    appointment = Appointment(name, surname, protocol_no, department, doctor_name, doctor_surname, date, hour,
                              minute)
    list_appoinment.append(appointment)
    print("APPOINMENT INFORMATIONS")
    for a in list_appoinment:
        if a.name==name:
            print(a)
    gachoice=int(input("Press 1 to get new appoinment\nPress 2 to back home page\nPress 3 to exit"))
    if gachoice==1:
        get_appoinment()
    elif gachoice==2:
        home()
    elif gachoice==3:
        exit()
def change_appoinment():
    cha=input("Please enter 'surname' of patient whose appointment you want to change,'first letter should be capital':")
    chp=int(input("Please enter 'protocol no' of patient whose appointment you want to change"))
    for i in list_appoinment:
        if i.surname==cha or i.protocol_no==chp:
            date = datetime.date(randint(2020, 2020), randint(6,7), randint(1, 30))
            date = datetime.datetime.strptime(str(date), "%Y-%m-%d").strftime("%d-%m-%Y")
            hour = random.randint(8, 18)
            minute = random.randrange(0, 59, 5)
            if minute<9:
                minute =str(0)+str(minute)
            x=Appointment(i.name,i.surname,i.protocol_no,i.department,i.doctor_name,i.doctor_surname,date,hour,minute)
            print(x)
    gachoice = int(input("Press 1 to get new appoinment\nPress 2 to back home page\nPress 3 to exit"))
    if gachoice == 1:
        get_appoinment()
    elif gachoice == 2:
        home()
    elif gachoice == 3:
        exit()

def view_appoinment():
    pn=int(input("Please enter your protocol no"))
    sn=input("Please enter surname.'Please enter first letter capital': ")
    for i in list_appoinment:
        if i.protocol_no==pn or i.surname==sn:
            print(i)
        else:
            print("record does not exist")
    if len(list_appoinment)==0:
        print("There is no any appoinment yet!")
    c=int(input("Press 1 to back main menu"))
    if c==1:
        home()
    else:
        exit()
def add_employee():
    a = 1
    n = int(input("how many employeee do you want to add:"))
    while a < n + 1:
        print("for", a, ".employee")
        job = input("Please enter job")
        name = input("Please enter name")
        surname = input("Please enter surname")
        gender = input("Please enter gender male or female ?")
        department = input("Please enter department:")
        ID = int(input("Please enter ID"))
        ob = Employee(job, name, surname, gender, department, ID)
        list.append(ob)
        a += 1
    print("After adding personel list is:")
    list_employee()

    b = int(input("Press 1 to back main menu or any key to exit"))
    if b == 1:
        home()


def search_employee():
    print("Press 1 To search according to 'JOB'")
    print("Press 2 To search according to 'NAME'")
    print("Press 3 To search according to 'ID'")
    print("Press 4 To back 'MAIN MENU'")
    c = int(input("Please enter your choice"))
    joblist = []
    if c == 1:
        j = input("Please enter job that you want to search:'doctor,nurse,secretary or cleaner'")

        for i in range(len(list)):
            if list[i].job == j:
                joblist.append(list[i])
        if len(joblist) > 0:
            for k in range(len(joblist)):
                print(joblist[k])
            go_back_home()
        else:
            print("Invalid job name")
            print("Please enter job name all letters low case")
            print("Press 1 to try again to back top menu or press 2 to back main menu or press 3 to exit")
        choice = int(input("Please enter your choice"))
        if (choice == 1):
            search_employee()
        elif (choice == 2):
            home()
        else:
            exit()

    elif c == 2:
        j = input("Please enter name that you want to search'first letter should be capital': ")
        listname = []
        for i in range(len(list)):
            if list[i].name == j:
                listname.append(list[i])
        for i in range(len(listname)):
            print(listname[i])
        if len(listname) == 0:
            print("Please try again as enter first letter capital other letters are lower case")
            search_employee()
    elif c == 3:
        j = int(input("Please enter ID that you want to search"))
        listid = []
        for i in range(len(list)):
            if list[i].ID == j:
                listid.append(list[i])
        if len(listid) == 0:
            print("Record does not exist")
        else:
            print(listid[0])
    elif c == 4:
        main()
    go_back_home()


def change_ID():
    id = int(input("Please enter the number of the employee you want to change"))
    for i in range(len(list)):
        if list[i].ID == id:
            print("The employee's number you want to change:", list[i])
            new_id = int(input("Please enter new ID"))
            list[i].change_ID(new_id)
    print("After change,the list that")
    list_employee()
    go_back_home()
def change_name():
    x = input("Adini degistirmek istediginiz kisinin adini giriniz:")
    for i in range(len(list)):
        if list[i].name == x:
            print("ID sini degistirmek istediginiz kisi")
            new_name = input("Yeni adi giriniz")
            list[i].name = new_name
    print("after change name")
    list_employee()
    go_back_home()


def list_employee():
    for i in range(len(list)):
        print(list[i])
    go_back_home()


def delete_employee():
    id = int(input("Please enter ID of employee that you want to delete"))
    for i in range(len(list)):
        if list[i].ID == id:
            print("Silmek istediginiz kisi", list[i])
            list.remove(list[i])
            print("List after delete")
            list_employee()
    go_back_home()

def sort_employee():
    print("Enter 1 to sort by job")
    print("Enter 2 to sort by name")
    print("ENter 3 to sort by ID")
    choice = int(input("Please enter sort type"))
    if choice == 1:
        print(sorted(list, key=lambda Employee: Employee.job))
    elif choice == 2:
        print(sorted(list, key=lambda Employee: Employee.name))
    elif choice == 3:
        print(sorted(list, key=lambda Employee: Employee.ID))
    go_back_home()
def go_back_home():
    choice=int(input("Please enter 1 to back main menu or enter 2 to exit"))
    if choice==1:
        home()
    else:
        exit()

# list[0].change_ID(180)
# print(list[0])

def main():
    print("What do you want to do?")
    print("------EMPLOYEE MANAGEMENT---------")
    print("Press'1' to add employe")
    print("Press'2' to search employee")
    print("Press'3' to list employee")
    print("Press'4' to change ID")
    print("Press'5' to delete employee")
    print("Press'6' to Sort employees")
    print("------PATIENT MANAGEMENT-----------")
    print("Press'7' to add patient")
    print("Press 8 to search patient")
    print("Press 9 to delete patient")
    print("Press 10 to sort patient")
    try:
       choice = int(input("Enter your choice"))
    except ValueError:
        print("Invalid input.Please enter a number between 1-10")
        main()
    if choice == 1:
        add_employee()
    elif choice == 2:
        search_employee()
    elif choice == 3:
        list_employee()
    elif choice == 4:
        change_ID()

    elif choice == 5:
        delete_employee()
    elif choice == 6:
        sort_employee()
    elif choice == 7:
        add_patient()
    elif choice == 8:
        search_patient()
    elif choice == 9:
        delete_patient()
    elif choice == 10:
        sort_patient()
    else:
        print("Invalid input.Please enter a number between 1-10")
home()