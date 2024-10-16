from .module_anamaria import get_user_input


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
                break
            else:
                continue
        else:
            continue

    return input_from_user # task 2.2


if __name__ == '__main__':

    print(get_name_verified("Introdu numele "))
    print(get_cnp_verified("Introdu CNP"))