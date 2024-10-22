from .module_elena import birthday_from_cnp
from .module_anamaria import get_user_input

#Task7: Ask the user to confirm the deduced date of birth from CNP, but have the date formated, beautified, so that
# it follow the pattern "DD.MM.YYYY". - Aidan


def confirm_date(birthday_as_tuple):
    print(f"{birthday_as_tuple[2]}.{birthday_as_tuple[1]}.{birthday_as_tuple[0]}")
    verificare = get_user_input(f" Verificati ca data de nastere va apartine. da/nu "
                                f"{birthday_as_tuple[2]}.{birthday_as_tuple[1]}.{birthday_as_tuple[0]}")
    if verificare == "da":
        #print ("e ok") #
        return True
    else:
        print ("reintroduce CNP")
        return False


if __name__ == '__main__':
    param_cnp = '2960120000000'
    birthday_as_tuple = birthday_from_cnp(param_cnp)
    confirm_date(birthday_as_tuple)