def main_menu():
    """
    Task 4: Display the main menu and read the user's response.

    The following options should be displayed:

    '[1] Process Data', '[2] Visualise Data', '[3] Export Data' and '[4] Exit'

    In each of the above cases, the user's response should be read in and returned as an integer
    corresponding to the selected option.
    E.g. 1 for 'Process Data', 2 for 'Visualise Data' and so on.

    If the user enters a invalid option then a suitable error should be displayed and the user
    prompted to try again.

    :return: an integer for a valid selection
    """
    # TODO: Your code here
    while True:
        option = input("'[1] Process Data', '[2] Visualise Data', '[3] Export Data' and '[4] Exit'")
        if option == "1":
            return 1
        elif option == "2":
            return 2
        elif option == "3":
            return 3
        elif option == "4":
            return 4
            break
        else:
            print("Input was not recognized please try again")
    pass  # can remove
def progress(operation, value):
    """
    Task 3: Display a message to indicate the progress of an operation.

    The function should display a message in the following format:
    'Operation: {operation} [{status}].'

    Where {operation} is the value of the parameter passed to this function
    and
    {status} is 'initiated' if the value of the parameter 'value' is 0
    {status} is 'in progress ({value}% completed)' if the value of the parameter 'value' is between,
    but not including, 0 and 100
    {status} is 'completed' if the value of the parameter 'value' is 100

    :param operation: a string indicating the operation being started
    :param value: an integer indicating the amount of progress made
    :return: does not return anything
    """
    # TODO: Your code here
    if value == 0:
        status = "initiated"
    elif value < 100:
        status = f"in progress [{value}% completed]"
    elif value == 100:
        status = f"completed"

    print(f'Operation: {operation} [{status}].')
    pass  # can remove
def sub_menu(variant=0):
    """
    Task 5: Display a sub menu of options and read the user's response.

    If no value or a zero is supplied for the parameter 'variant' then a suitable error should be displayed
    and the value 0 should be returned.

    If the value of the parameter 'variant' is 1 then a menu with the following options should be displayed:

    '[1] Reviews for Hotel', '[2] Reviews for Dates', '[3] Reviews for Nationality,
    '[4] Reviews Summary'

    If the value of the parameter 'variant' is 2 then a menu with the following options should be displayed:

    '[1] Positive/Negative Pie Chart', '[2] Reviews Per Nationality Chart', '[3] Animated Summary'

    If the value of the parameter 'variant' is 3 then a menu with the following options should be displayed:

    '[1] All Reviews', '[2] Reviews for Specific Hotel'

    In each of the above cases, the user's response should be read in and returned as an integer
    corresponding to the selected option.
    E.g. 1 for 'Reviews for Hotel', 2 for 'Reviews for Dates' and so on.

    If the user enters a invalid option then a suitable error message should be displayed

    :return: 0 if invalid selection otherwise an integer for a valid selection
    """
    # TODO: Your code here
    if variant == "1":
        option1 = int(input(
            "'[1] Reviews for Hotel', '[2] Reviews for Dates', '[3] Reviews for Nationality,'[4] Reviews Summary'"))
        if option1 in range(1, 4):
            print(option1)
        else:
            print("0")
            print("Input was not recognized")
    elif variant == "2":
        option2 = int(
            input("'[1] Positive/Negative Pie Chart', '[2] Reviews Per Nationality Chart', '[3] Animated Summary'"))
        if option2 in range(1, 3):
            print(option2)
        else:
            print("0")
            print("Input was not recognized")
    elif variant == "3":
        option3 = int(input("'[1] All Reviews', '[2] Reviews for Specific Hotel'"))
        if option3 in range(1, 3):
            print(option3)
        else:
            print("0")
            print("Input was not recognized")
    else:
        print("0")
        print("Input was not recognized")
    pass  # can remove
def hotel_name():
    """
    Task 7: Read in and return the name of a hotel.

    The function should ask the user to enter a hotel name e.g. Hotel Arena
    The function should then read in and return the user's response as a string.

    :return: the name of a hotel
    """
    # TODO: Your code here
    hotel_n = input("What is the hotel name?")
    return hotel_n
    pass  # can remove

def review_dates():
    """
    Task 8: Read in and return a list of review dates.

    The function should ask the user to enter some review dates
    This should be entered in the format mm/dd/yyyy (same as that in the file)
    where dd is two-digit day,
    mm is two digit month and
    yyyy is a four digit year
    e.g. 01/22/2020
    The function should return a list containing the specified review dates.

    :return: a list of review dates
    """
    # TODO: Your code here
    dates = input("enter review dates in the format mm/dd/yyyy e.g. 05/20/2005")
    dates_list = dates.split()
    return dates_list
    pass  # can remove