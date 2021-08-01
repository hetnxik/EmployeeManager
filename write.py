import csv

def write():
    newfile = input("Enter Name of file which you want to create: ")
    open(f'{newfile}.csv', 'x')
    file = open(f'{newfile}.csv', 'w')
    filewriter = csv.writer(file)
    filewriter.writerow(["Employee_Id", "Employee_Name", "Employee_Department", "Employee_Designation", "Employee_Salary", "Employee_Sales"])
    ids = []
    names = []
    departments = []
    designations = []
    Salary = []
    sales = []
    cont = 'y'
    while cont == 'y':
        Id = int(input("Enter employee Id: "))
        ids.append(Id)
        Name = input("Enter name of employee: ")
        names.append(Name)
        department = input("Enter department of employee: ")
        departments.append(department)
        designation = input("Enter designation of employee: ")
        designations.append(designation)
        salary = float(input("Enter salary of employee: "))
        Salary.append(salary)
        sale = int(input("Enter sales of employee: "))
        sales.append(sale)
        cont = input("Continue? (y/n): ")
        # print(ids, names, departments, designations, Salary, sales)


    if len(ids) != len(set(ids)) and len(ids) != 1:
        print("Multiple employees have same ID. Please provide every employee with a unique ID.")

    else:
        for i in range(len(ids)):

            filewriter.writerow([ids[i], names[i], departments[i], designations[i], Salary[i], sales[i]])
            print(ids, names, departments, designation, Salary, sales)
    file.close()

