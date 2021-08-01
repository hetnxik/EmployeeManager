import sys
from write import write
from update import edit
from delete import delete
from search import search
from read import read

tasks_description = ["Write", "Read", "Update", "Delete", "Search", "Exit"]
tasks = [1, 2, 3, 4, 5, 6]


def show_menu():
    print()
    print("----------------------------[Main Menu]----------------------------")
    print()
    print("This is the number of tasks the program has:")
    for key in range(len(tasks)):
        print(f"{key+1}. {tasks_description[key]}")


if __name__ == '__main__':
    print("""
        --------------------------------------------------------------------
        ███████╗███╗   ███╗██████╗ ██╗      █████╗ ██╗   ██╗███████╗███████╗
        ██╔════╝████╗ ████║██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔════╝
        █████╗  ██╔████╔██║██████╔╝██║     ██║  ██║ ╚████╔╝ █████╗  █████╗  
        ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║     ██║  ██║  ╚██╔╝  ██╔══╝  ██╔══╝  
        ███████╗██║ ╚═╝ ██║██║     ███████╗╚█████╔╝   ██║   ███████╗███████╗
        ╚══════╝╚═╝     ╚═╝╚═╝     ╚══════╝ ╚════╝    ╚═╝   ╚══════╝╚══════╝

        ███╗   ███╗ █████╗ ███╗  ██╗ █████╗  ██████╗ ███████╗██████╗
        ████╗ ████║██╔══██╗████╗ ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
        ██╔████╔██║███████║██╔██╗██║███████║██║  ██╗ █████╗  ██████╔╝
        ██║╚██╔╝██║██╔══██║██║╚████║██╔══██║██║  ╚██╗██╔══╝  ██╔══██╗
        ██║ ╚═╝ ██║██║  ██║██║ ╚███║██║  ██║╚██████╔╝███████╗██║  ██║
        ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
        --------------------------------------------------------------------
        """, "\nWelcome to Employee Manager")

    while True:
        show_menu()
        task = int(input("Pls enter the number corresponding to the task that you want to do: "))
        if task == 6:
            print()
            print('---------------')
            print("Closing Program")
            print()
            sys.exit()
        if task == 1:
            write()
        if task == 2:
            read()
        if task == 3:
            edit()
        if task == 4:
            delete()
        if task == 5:
            search()