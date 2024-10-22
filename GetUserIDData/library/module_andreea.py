
#Read data from a text file
def read_from_text_file(filepath):
    with open(filepath, "r") as file:
        check_fields(file.read())


#Check if file.txt contains the required fields
def check_fields(content):
    required_fields = ["First Name", "Last Name", "CNP", "Address"]
    found_fields = []
#Check each required field
    for field in required_fields:
        if field in content:
            found_fields.append(field)
#Check each required field
    if "First Name" not in found_fields:
        print("The First Name field is missing.")
    if "Last Name" not in found_fields:
        print("The Last Name field is missing.")
    if "CNP" not in found_fields:
        print("The CNP field is missing.")
    if "Address" not in found_fields:
        print("The Adress field is missing.")
#Check if all fields are found
    if len(found_fields) == len(required_fields):
        print("All required fields are present in the file")






