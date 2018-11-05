def output_menu(menu_data):
    for currEntryAlias in menu_data:
        curr_entry = menu_data[currEntryAlias]
        curr_entry_name = curr_entry[0]
        curr_entry_value = curr_entry[1]
        print("\t", curr_entry_name, "-", curr_entry_value)
    print("Type the characters shown in square brackets:")


def get_selection_attempt(menu_request, menu_data):
    print(menu_request)
    output_menu(menu_data)
    return input()


def get_selection(menu_request, menu_data, max_tries=3):
    selection = ""
    for i in range(max_tries):
        try:
            selection = get_selection_attempt(menu_request, menu_data)
            break
        except KeyError:
            print("You did not select a valid option")
    return menu_data[selection.lower()][1]
