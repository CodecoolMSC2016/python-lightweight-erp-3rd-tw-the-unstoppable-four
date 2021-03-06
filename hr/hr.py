# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader("common", current_file_path + "/../common.py").load_module()


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#

CSV_NAME = "hr/persons.csv"


def start_module():
    menu_point = ["Show table", "Add", "Remove", "Update", "Oldest person", "Closest person to average age"]
    ui.print_menu("\nHuman resources manager", menu_point, "Return to the main menu")
    choose()


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "\nHuman resources manager")
    option = inputs[0]

    if option == "1":
        show_table(table=data_manager.get_table_from_file(CSV_NAME))
    elif option == "2":
        add(data_manager.get_table_from_file(CSV_NAME))
    elif option == "3":
        my_id = ui.get_inputs("Enter the id of the line you want to delete: ", "")
        remove(data_manager.get_table_from_file(CSV_NAME), my_id)
    elif option == "4":
        my_id = ui.get_inputs("Enter the id of the line you want to update: ", "")
        update(data_manager.get_table_from_file(CSV_NAME), my_id)
    elif option == "5":
        ui.print_result(get_oldest_person(data_manager.get_table_from_file(
            CSV_NAME)), "Oldest person")
    elif option == "6":
        ui.print_result(get_persons_closest_to_average(data_manager.get_table_from_file(
            CSV_NAME)), "Name")
    elif option == "0":
        pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table=data_manager.get_table_from_file(CSV_NAME)):
    title_list = ["id", "name", "birth_date"]
    return ui.print_table(table, title_list)


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists


def add(table):
    info = data_manager.get_table_from_file(CSV_NAME)
    random = common.generate_random(info)
    title_list = ["id", "name", "birth_date"]
    counter = 1
    newdata = []
    newdata.append(random)
    for i in range(1, len(info[0])):
        inp = ui.get_inputs("Enter " + title_list[counter] + ": ", "")
        newdata.append(inp[0])
        counter += 1
    info.append(newdata)
    data_manager.write_table_to_file(CSV_NAME, info)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table=data_manager.get_table_from_file(CSV_NAME), id_=None):
    counter = 0
    if id_ == None:
        id_ = ui.get_inputs("Enter id: ", "")
    for i in table:
        if id_[0] in i:
            break
        counter += 1
    del table[counter]
    data_manager.write_table_to_file(CSV_NAME, table)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table=data_manager.get_table_from_file(CSV_NAME), id_=None):
    counter = 0
    if id_ == None:
        id_ = ui.get_inputs("Enter id: ", "")
    title_list = ["id", "name", "birth_date"]
    for i in table:
        if id_[0] in i:
            break
        counter += 1
    new_counter = 1
    for j in range(1, len(table[0])):
        inp = ui.get_inputs("Enter " + title_list[new_counter] + ": ", "")
        table[counter][new_counter] = inp[0]
        new_counter += 1
    data_manager.write_table_to_file(CSV_NAME, table)
    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table=data_manager.get_table_from_file(CSV_NAME)):
    min = 2100
    people = []
    names = []
    for year in table:
        if int(year[2]) < min:
            min = int(year[2])
    for name in table:
        if int(name[2]) == min:
            people.append(name[1])
    return people


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table=data_manager.get_table_from_file(CSV_NAME)):
    years = []
    res = []
    min = 100
    people = []
    for age in table:
        years.append(int(age[2]))
    years_sum = 0
    for i in years:
        years_sum += i
    avg = years_sum / len(years)
    avg = int(avg // 1)
    for i in years:
        res.append(abs(i - avg))
    for num in res:
        if num < min:
            min = num
    y = avg + min
    x = avg - min
    for names in table:
        if int(names[2]) == int(y) or int(names[2]) == int(x):
            people.append(names[1])
    return people
