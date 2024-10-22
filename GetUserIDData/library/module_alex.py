import csv
import os

def save_to_files(firstName, lastName, birthDate="01.01.1900", address="", cnp=""):
    text_file = "id_details.txt"
    csv_file = "id_details.csv"
    with open(text_file, "a") as txt_file:  # 'a' pentru append
        txt_file.write(f"First Name: {firstName}\n")
        txt_file.write(f"Last Name: {lastName}\n")
        txt_file.write(f"Birth Date: {birthDate}\n")
        txt_file.write(f"Address: {address}\n")
        txt_file.write(f"CNP: {cnp}\n")
        txt_file.write("========================================\n")  # Separator pentru fiecare persoana


        # cauta daca exista un CSV file si daca e gol
        file_exists = os.path.isfile(csv_file)
        is_file_empty = os.stat(csv_file).st_size == 0 if file_exists else True
        # adauga detaliile la csv file si adauga header ul daca file ul e nou sau gol
    with open(csv_file, "a", newline='') as csvfile:  # 'a' pentru append
        csv_writer = csv.writer(csvfile)
        if is_file_empty:
            # Scrie header-ul daca file-ul e gol
            csv_writer.writerow(["First Name", "Last Name", "Birth Date", "Address", "CNP"])
            # Scrie detaliile
            csv_writer.writerow([firstName, lastName, birthDate, address, cnp])

    print(f"ID details saved to '{text_file}' and '{csv_file}'.")