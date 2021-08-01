import csv
import os

def edit():
    open('aofnadsfnadojfn.csv', 'x')
    duplicate_file = open('aofnadsfnadojfn.csv', 'w')
    duplicate_writer = csv.writer(duplicate_file)

    # writing headings in the temporary file
    duplicate_writer.writerow(
        ["Employee_Id", "Employee_Name", "Employee_Department", "Employee_Designation", "Employee_Salary",
         "Employee_Sales"])
    filename = input("Enter file which you want to edit: ")
    with open(f"{filename}.csv", "r") as f:
        reader = csv.reader(f, delimiter = ",")
        for data in enumerate(reader):

            # getting the data from the file
            sales = data[1][5]
            salary = data[1][4]
            desig = data[1][3]
            depart = data[1][2]
            name = data[1][1]
            Id = data[1][0]

            # skip checking the headers
            if sales != 'Employee_Sales':

                # Check if sales are more than 500000
                if int(sales) > 500000:
                    # Giving bonus of 5%
                    salary = float(salary)
                    salary *= 105 / 100
                    # saving in duplicate file
                    duplicate_writer.writerow(
                        [
                            Id, name, depart, desig, salary, sales
                        ]
                    )

                # For the remaining amount of sales
                else:
                    # saving data without giving bonus
                    duplicate_writer.writerow(
                        [
                            Id, name, depart, desig, salary, sales
                        ]
                    )

    # Closing Duplicate file
    duplicate_file.close()

    # Delete the main file and rename the duplicate file to main file
    os.remove(f'{filename}.csv')
    os.rename('aofnadsfnadojfn.csv', f'{filename}.csv')

    print(f"Edited {filename}.csv")