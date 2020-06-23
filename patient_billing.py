import os
from pathlib import Path

data_folder = Path("patients/")

def patient_options():
    print("\nEnter one of the following actions: ")
    print("A - Add a new patient")
    print("R - Read a patient record")
    print("U - Update a patient's information")
    print("D - Delete a patient")
    print("T - Display total number of patients")

    user_input = input("= ")

    if user_input in ('A', 'a'):
        add_patient()
    elif user_input in ('R', 'r'):
        read_patient()
    elif user_input in ('U', 'u'):
        update_patient()
    elif user_input in ('D', 'd'):
        delete_patient()
    elif user_input in ('T', 't'):
        total_patients()
    else:
        print("\nUser entered character with no patient options\n")
        patient_options()

    print()
    continue_program = input("Would you like to do anything else? (Y or N): ")
    if continue_program in ('Y', 'y'):
        print()
        patient_options()
    else:
        exit
    return 0

def create_database():
    if not os.path.isdir(data_folder):
        os.mkdir(data_folder)
        print("Successfully created directory " + data_folder)
    elif os.path.isdir(data_folder):
        print("Directory " + data_folder + " already exists")
        return 0
    else:
        print("Unable to create patient directory at " + data_folder)
        exit
    return 0

def add_patient():
    first_name = input("\nEnter patient first name: ")
    last_name = input("Enter patient last name: ")
    billing_date = input("Enter initial billing date (MM/DD/YYYY): ")
    billing_amount = input("Enter billing amount: ")
    defib = input("Does patient use a defibrillator? (Y or N): ")
    
    file_name = first_name.lower() + last_name.lower() + ".txt"
    file_to_open = data_folder / file_name

    if os.path.isfile(file_to_open):
        print("File already exists")
        patient_options()
    elif not os.path.isfile(file_to_open):
        f = open(file_to_open, 'w')
        patient_information = [first_name.upper() + ' ' + last_name.upper() + '\n', billing_date + '\n', billing_amount + '\n', defib.upper() + '\n']
        f.writelines(patient_information)
        f.close()
    print("\nNew file has been successfully created for " + first_name.upper(), last_name.upper())
    return 0

def read_patient():
    return 0

def update_patient():
    return 0

def update_information():
    return 0

def delete_patient():
    return 0

def total_patients():
    return 0

patient_options()
