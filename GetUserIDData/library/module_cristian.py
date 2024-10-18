from library.module_anamaria import get_user_input
from library.module_elena import birthday_from_cnp
from library.module_aidan import confirm_date

def get_name_verified(message_to_user : str):
    """
    :param message_to_user: string
    :return: the first name from user
    """
    input_from_user = ''

    while input_from_user.isalpha() == False:
        input_from_user = get_user_input(message_to_user)

    return input_from_user.upper() #task 2.4 and 2.3

def get_cnp_verified(message_to_user : str):
    """
    :param message_to_user: string
    :return: the number from user
    """
    input_from_user = ''

    while True:
        input_from_user = get_user_input(message_to_user)
        if input_from_user.isnumeric():

            if len(input_from_user) == 13:
                birthday_as_tuple = birthday_from_cnp(input_from_user)
                if confirm_date(birthday_as_tuple) is True:
                    is_birthday_in_range(input_from_user)
                    break
                else:
                    continue
            else:
                continue
        else:
            continue

    return input_from_user # task 2.2


if __name__ == '__main__':

    print(get_name_verified("Introdu numele "))
    print(get_cnp_verified("Introdu CNP"))