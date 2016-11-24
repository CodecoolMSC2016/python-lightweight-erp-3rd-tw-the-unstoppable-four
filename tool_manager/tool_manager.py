# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


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

CSV_NAME = "tool_manager/tools.csv"

def start_module():
    menu_point = ["Show table", "Add", "Remove", "Update", "Available tools", "Average durability time"]
    ui.print_menu("\nTool manager", menu_point, "Return to the main menu")
    choose()


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "\nTool manager")
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
        ui.print_result(get_available_tools(data_manager.get_table_from_file(
            CSV_NAME)), "Available tools")
    elif option == "6":
        ui.print_result(get_average_durability_by_manufacturers(data_manager.get_table_from_file(
            CSV_NAME)), "Average durability time")
    elif option == "0":
        pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table=data_manager.get_table_from_file("tool_manager/tools.csv")):
    title_list = ["id", "name", "manufacturer", "purchase_date", "durability"]
    return ui.print_table(table, title_list)


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    info = data_manager.get_table_from_file("tool_manager/tools.csv")
    random = common.generate_random(info)
    title_list = ["id", "name", "manufacturer", "purchase_date", "durability"]
    counter = 1
    newdata = []
    newdata.append(random)
    for i in range(1, len(info[0])):
        inp = ui.get_inputs("Enter " + title_list[counter] + ": ", "")
        newdata.append(inp[0])
        counter += 1
    info.append(newdata)
    data_manager.write_table_to_file("tool_manager/tools.csv", info)
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
# @table: list of listsremo
# @id_: string
def update(table = data_manager.get_table_from_file(CSV_NAME), id_ = None):
    counter = 0
    if id_ == None:
        id_ = ui.get_inputs("Enter id: ", "")
    title_list = ["id" ,"name", "manufacturer", "purchase_date", "durability"]
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

# the question: Which items has not yet exceeded their durability ?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_tools(table=data_manager.get_table_from_file(CSV_NAME)):
    new_list = []
    this_year = 2016
    title_list = ["id", "name", "manufacturer", "purchase_date", "durability"]
    for i in range(len(table)):
        if this_year - int(table[i][3]) < int(table[i][4]):
            new_list.append(table[i])
    return new_list


# the question: What are the average durability time for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists
def get_average_durability_by_manufacturers(table=data_manager.get_table_from_file(CSV_NAME)):

    dura_dict = {}
    company_names = []
    data_list = []
    for i in range(len(table)):
        if table[i][2] not in company_names:
            company_names.append(table[i][2])

    for j in range(len(company_names)):
        data = []
        data.append(company_names[j])
        data.append(0)
        data.append(0)
        data_list.append(data)

    for k in range(len(table)):
        if table[k][2] == data_list[0][0]:
            data_list[0][1] += int(table[k][4])
            data_list[0][2] += 1
        elif table[k][2] == data_list[1][0]:
            data_list[1][1] += int(table[k][4])
            data_list[1][2] += 1
        elif table[k][2] == data_list[2][0]:
            data_list[2][1] += int(table[k][4])
            data_list[2][2] += 1

    for m in range(len(data_list)):
        dura_dict[company_names[m]] = data_list[m][1] / data_list[m][2]

    return dura_dict
