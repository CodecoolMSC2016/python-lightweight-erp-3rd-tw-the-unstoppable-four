

# This function needs to print outputs like this:
# /-----------------------------------\
# |   id   |      title     |  type   |
# |--------|----------------|---------|
# |   0    | Counter strike |    fps  |
# |--------|----------------|---------|
# |   1    |       fo       |    fps  |
# \-----------------------------------/
#
# @table: list of lists - the table to print out
# @title_list: list of strings - the head of the table
def print_table(table, title_list):
    extended_table = table
    extended_table.insert(0, title_list)
    length_list = []
    for k in range(len(title_list)):
        length_list.append(0)
    for i in range(len(extended_table[0])):
        for j in range(len(extended_table)):
            if len(extended_table[j][i]) > length_list[i]:
                length_list[i] = len(extended_table[j][i])
    new_list = []
    for t in range(len(extended_table)):
        sub_list = []
        new_list.append(sub_list)
    for s in range(len(extended_table[0])):
        for r in range(len(extended_table)):
            this_string = extended_table[r][s]
            if len(this_string) != length_list[s]:
                difference = length_list[s] - len(extended_table[r][s])
                if difference % 2 == 1:
                    this_string = " "*int(difference/2) + this_string + " "*int(difference/2 + 1)
                    new_list[r].append(this_string)
                else:
                    this_string = " "*int(difference/2) + this_string + " "*int(difference/2)
                    new_list[r].append(this_string)
            else:
                new_list[r].append(this_string)
    lenght_of_titles = len(extended_table[0]) * "| {} |"
    total = 0
    for i in length_list:
        total += i
    total += len(extended_table[0])*4
    print("/" + (total-2) * "-" + "\\")
    for i in range(len(new_list)):
        print(lenght_of_titles.format(*new_list[i]))
        if i < len(new_list)-1:
            print(total * "-")
    print("\\" + (total-2) * "-" + "/")

# This function needs to print result of the special functions
#
# @result: string or list or dictionary - result of the special function
# @label: string - label of the result
def print_result(result, label):
    print(label + ": ")
    print(result)

# This function needs to generate outputs like this:
# Main menu:
# (1) Store manager
# (2) Human resources manager
# (3) Inventory manager
# (4) Accounting manager
# (5) Selling manager
# (6) Customer relationship management (CRM)
# (0) Exit program
#
# @title: string - title of the menu
# @list_options: list of strings - the options in the menu
# @exit_message: string - the last option with (0) (example: "Back to main menu")


def print_menu(title, list_options, exit_message):
    print(title)
    num = 1
    for i in list_options:
        print("(" + str(num) + ") " + i)
        num += 1
    print("(0) " + exit_message)


# This function gets a list of inputs from the user by the terminal
#
# @list_labels: list of strings - the labels of the inputs
# @title: string - title of the "input section"
# @inputs: list of string - list of the received values from the user
def get_inputs(list_labels, title):
    inputs = []
    print(title)
    key = input((list_labels))
    for element in key:
        inputs.append(element)

    return inputs


# This function needs to print an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):
    print("A(n) " + message + "has occured!")
