# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual selling price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the purchase was made


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

CSV_NAME = "selling/sellings.csv"

def start_module():
    menu_point = ["Show table", "Add", "Remove", "Update", "Lowest price", "Items sold between a period"]
    ui.print_menu("\nSelling manager", menu_point, "Return to the main menu")
    choose()


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "\nSelling manager")
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
        ui.print_result(get_lowest_price_item_id(data_manager.get_table_from_file(
            CSV_NAME)), "Lowest price item")
    elif option == "6":
        ui.print_table(get_items_sold_between(), ["id", "title", "price", "month", "day", "year"])
    elif option == "0":
        pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table=data_manager.get_table_from_file("selling/sellings.csv")):
    title_list = ["id", "title", "price", "month", "day", "year"]
    return ui.print_table(table, title_list)


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    info = data_manager.get_table_from_file("selling/sellings.csv")
    random = common.generate_random(info)
    title_list = ["id", "title", "price", "month", "day", "year"]
    counter = 1
    newdata = []
    newdata.append(random)
    for i in range(1, len(info[0])):
        inp = ui.get_inputs("Enter " + title_list[counter] + ": ", "")
        newdata.append(inp[0])
        counter += 1
    info.append(newdata)
    data_manager.write_table_to_file("selling/sellings.csv", info)
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
    title_list = ["id", "title", "price", "month", "day", "year"]
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

# the question: What is the id of the item that sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first of descending alphabetical order
def get_lowest_price_item_id(table = data_manager.get_table_from_file(CSV_NAME)):
    counter = 0
    lowest_price = 500
    for i in table:
        if int(table[counter][2]) <= lowest_price:
            lowest_price = int(table[counter][2])
        counter += 1
    new_counter = 0
    lowest_price_index = []
    for i in table:
        if lowest_price == int(table[new_counter][2]):
            lowest_price_index.append(table[new_counter][0])
        new_counter += 1
    return lowest_price_index[0]


# the question: Which items are sold between two given dates ? (from_date < birth_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table = data_manager.get_table_from_file(CSV_NAME), month_from=None, day_from=None, year_from=None, month_to=None, day_to=None, year_to=None):
    date_from = ""
    date_to = ""
    if year_from == None:
        year_from = ui.get_inputs("Enter year_from: ", "")
        date_from += year_from[0]
    if month_from == None:
        month_from = ui.get_inputs("Enter month_from: ", "")
        if len(month_from[0]) == 1:
            date_from = date_from + "0" + month_from[0]
        else:
            date_from = date_from + month_from[0]
    if day_from == None:
        day_from = ui.get_inputs("Enter day_from: ", "")
        if len(day_from[0]) == 1:
            date_from = date_from + "0" + day_from[0]
        else:
            date_from = date_from + day_from[0]
    if year_to == None:
        year_to = ui.get_inputs("Enter year_to: ", "")
        date_to += year_to[0]
    if month_to == None:
        month_to = ui.get_inputs("Enter month_to: ", "")
        if len(month_to[0]) == 1:
            date_to = date_to + "0" + month_to[0]
        else:
            date_to = date_to + month_to[0]
    if day_to == None:
        day_to = ui.get_inputs("Enter day_to: ", "")
        if len(day_to[0]) == 1:
            date_to = date_to + "0" + day_to[0]
        else:
            date_to = date_to + day_to[0]

    dates = []
    for i in range(len(table)):
        this_date = ""
        this_date += table[i][5]
        if len(table[i][3]) == 1:
            this_date += "0"
            this_date += table[i][3]
        else:
            this_date += table[i][3]
        if len(table[i][4]) == 1:
            this_date += "0"
            this_date += table[i][4]
        else:
            this_date += table[i][4]
        dates.append(this_date)

    new_table = []

    for j in range(len(table)):
        if dates[j] > date_from and dates[j] < date_to:
            new_table.append(table[j])

    return new_table
