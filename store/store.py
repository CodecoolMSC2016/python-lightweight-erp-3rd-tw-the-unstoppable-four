# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollar)
# in_stock: number


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

CSV_NAME = "store/games.csv"

def start_module():
    menu_point = ["Show table", "Add", "Remove", "Update", "Games by manufacturer", "Average games in stock from manufacturer"]
    ui.print_menu("\nStore manager", menu_point, "Return to the main menu")
    choose()


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "\nStore manager")
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
        ui.print_result(get_counts_by_manufacturers(data_manager.get_table_from_file(
            CSV_NAME)), "Games by manufacturer: ")
    elif option == "6":
        manufacturer = ui.get_inputs("Enter the manufacturer: ", "")
        ui.print_result(get_average_by_manufacturer(data_manager.get_table_from_file(
            CSV_NAME), manufacturer[0]), "Average games in stock from manufacturer: ")
    elif option == "0":
        pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table=data_manager.get_table_from_file(CSV_NAME)):
    title_list = ["id", "title", "manufacturer", "price", "in_stock"]
    return ui.print_table(table, title_list)


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    info = data_manager.get_table_from_file(CSV_NAME)
    random = common.generate_random(info)
    title_list = ["id", "title", "manufacturer", "price", "in_stock"]
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
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table = data_manager.get_table_from_file(CSV_NAME), id_ = None):
    counter = 0
    if id_ == None:
        id_ = ui.get_inputs("Enter id: ", "")
    title_list = ["id", "title", "manufacturer", "price", "in_stock"]
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

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table = data_manager.get_table_from_file("store/games.csv")):

    d_list = {}

    for i in range(len(table)):
        if table[i][2] in d_list:
            d_list[table[i][2]] += 1
        else:
            d_list[table[i][2]] = 1
        
    return d_list


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):

    # your code

    pass
