import csv

def search():
    filename = input("Enter file name to search in: ")
    searchfile = open(f'{filename}.csv', 'r')
    reader = csv.reader(searchfile, delimiter = ',')
    a = input("Enter employee ID: ")
    for row in reader:
        if a in row[0] or a in row[1]:
            print()
            print()
            print(f'----------------------------')
            print(f"Employee details with ID {a}")
            print(f"         Id : {row[0]}")
            print(f'       Name : {row[1]}')
            print(f' Department : {row[2]}')
            print(f'Designation : {row[3]}')
            print(f'     Salary : {row[4]}')
            print(f'      Sales : {row[5]}')
            print(f'----------------------------')
            print()
            print()