import csv

def read():
    filename = input("Enter filename of which ou want to access the data: ")
    with open(f"{filename}.csv", "r") as f:
        reader = csv.reader(f, delimiter = ",")
        for data in enumerate(reader):
            
            # getting the data from the file

            if data[1][0] != "Employee_Id":
                sales = data[1][5]
                salary = data[1][4]
                desig = data[1][3]
                depart = data[1][2]
                name = data[1][1]
                Id = data[1][0]
                print(f"---------------------------")
                print(f"         Id : {Id}")
                print(f"       Name : {name}")
                print(f" Department : {depart}")
                print(f"Designation : {desig}")
                print(f"     Salary : ₹ {salary}")
                print(f"      Sales : {sales} sales")
                print(f"---------------------------")
