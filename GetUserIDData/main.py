from library import *

if __name__ == '__main__':
    #TODO 1.get the user's name
    var_first_name = get_name_verified("Introdu prenumele ")
    #TODO 2.get the user's name
    var_last_name = get_name_verified("Introdu numele ")
    #TODO 3.get the user's CNP
    var_cnp = get_cnp_verified("Introdu CNP")
    #TODO 4.get the user's address
    var_address = get_address_verified("Introdu adresa")
    #TODO 5.save data to files
    save_to_files(firstName=var_first_name, lastName=var_last_name, cnp=var_cnp, address=var_address)
    read_from_text_file("id_details.txt")