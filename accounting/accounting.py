# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


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

CSV_NAME = "accounting/items.csv"

def start_module():
    menu_point = ["Show table", "Add", "Remove", "Update", "Highest profiting year", "Average profiting year"]
    ui.print_menu("\nAccounting manager", menu_point, "Return to the main menu")
    choose()


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "\nAccounting manager")
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
        ui.print_result(which_year_max(data_manager.get_table_from_file(CSV_NAME), "Highest profiting year: "))
    elif option == "6":
        year = ui.get_inputs("Enter the year you want to inspect: ", "")
        ui.print_result(avg_amount(data_manager.get_table_from_file(
            CSV_NAME), year[0]), "Average profit of " + str(year[0]))
    elif option == "0":
        pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table=data_manager.get_table_from_file(CSV_NAME)):
    title_list = ["id", "month", "day", "year", "type", "amount"]
    return ui.print_table(table, title_list)


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    info = data_manager.get_table_from_file(CSV_NAME)
    random = common.generate_random(info)
    title_list = ["id", "month", "day", "year", "type", "amount"]
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
def remove(table = data_manager.get_table_from_file(CSV_NAME), id_ = None):
    counter = 0
    if id_ == None:
        id_ = ui.get_inputs("Enter id: ", "")
    for i in table:
        if id_[0] in i:
            break
        counter += 1
    del table[counter]
    data_manager.write_table_to_file(CSV_NAME, table)


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table = data_manager.get_table_from_file(CSV_NAME), id_ = None):
    counter = 0
    if id_ == None:
        id_ = ui.get_inputs("Enter id: ", "")
    title_list = ["id", "month", "day", "year", "type", "amount"]
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

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table=data_manager.get_table_from_file("accounting/items.csv")):

    lista = data_manager.get_table_from_file("accounting/items.csv")

    d_lista = {}

    for i in range(len(lista)):
        if lista[i][3] in d_lista:
            if lista[i][4] == "in":
                (d_lista[lista[i][3]]) += int(lista[i][5])
            else:
                (d_lista[lista[i][3]]) -= int(lista[i][5])
        else:
            if lista[i][4] == "in":
                d_lista[lista[i][3]] = int(lista[i][5])
            else: 
                d_lista[lista[i][3]] = (int(lista[i][5])*-1)


    most_profitable = 0
    profit = 0

    for j in d_lista:
        if int(d_lista[j]) > profit:
            most_profitable = int(j)
            profit = d_lista[j]
    return (most_profitable)

print(which_year_max())


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):
    in_list = []
    out_list = []
    items = 0
    for i in table:
        if int(i[3]) == int(year):
            items += 1
            if str(i[4]) == "in":
                in_list.append(int(i[5]))
            elif str(i[4]) == "out":
                out_list.append(int(i[5]))

    income = sum(in_list) - sum(out_list)
    avg = income / items
    return avg
