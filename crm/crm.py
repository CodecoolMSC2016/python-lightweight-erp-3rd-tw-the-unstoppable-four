# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


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

CSV_NAME = "crm/customers.csv"

def start_module():
    menu_point = ["Show table", "Add", "Remove", "Update", "Longest customer name", "Subscribed emails"]
    ui.print_menu("\nCustomer Relationship Management (CRM)", menu_point, "Return to the main menu")
    choose()


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "\nCustomer Relationship Management (CRM)")
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
        ui.print_result(get_longest_name_id(data_manager.get_table_from_file(
            CSV_NAME)), "Longest name: ")
    elif option == "6":
        ui.print_result(get_subscribed_emails(data_manager.get_table_from_file(
            CSV_NAME)), "Subscribed emails: ")
    elif option == "0":
        pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table=data_manager.get_table_from_file("crm/customers.csv")):
    title_list = ["id", "name", "email", "subscribed"]
    return ui.print_table(table, title_list)


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    info = data_manager.get_table_from_file("crm/customers.csv")
    random = common.generate_random(info)
    title_list = ["id", "name", "email", "subscribed"]
    counter = 1
    newdata = []
    newdata.append(random)
    for i in range(1, len(info[0])):
        inp = ui.get_inputs("Enter " + title_list[counter] + ": ", "")
        newdata.append(inp[0])
        counter += 1
    info.append(newdata)
    data_manager.write_table_to_file("crm/customers.csv", info)
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
    title_list = ["id", "name", "email", "subscribed"]
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


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first of descending alphabetical order
def get_longest_name_id(table= data_manager.get_table_from_file(CSV_NAME)):
    longest_names = []
    longest_name = ""
    counter = 0
    for i in table:
        if len(table[counter][1]) >= len(longest_name):
            longest_name = table[counter][1]
            longest_names.append(table[counter][1])
        counter += 1
    new_counter = 0
    lowest_unicode = 500
    lowest_index = 0
    for i in longest_names:
        if ord(longest_names[new_counter][0]) < lowest_unicode:
            lowest_unicode = ord(longest_names[new_counter][0])
            lowest_index = new_counter
        new_counter += 1
    final_index = 0
    final_counter = 0
    for i in table:
        if table[final_counter][1] == longest_names[lowest_index]:
            return table[final_counter][0]
        final_counter += 1


# the question: Which customers has subscribed to the newsletter?
# return type: list of string (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table= data_manager.get_table_from_file(CSV_NAME)):
    counter = 0
    subscribed_customer = []
    for i in table:
        if table[counter][3] == "1":
            subscribed_customer.append(table[counter][2] + ";" + table[counter][1])
        counter += 1
    return subscribed_customer
