import os

path = os.getcwd() + '\\patients\\'

def patient_options():
    print("Enter one of the following actions: ")
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
    return 0

patient_options()

def create_database():
    if not os.path.isdir(path):
        os.mkdir(path)
        print("Successfully created directory " + path)
    elif os.path.isdir(path):
        return 0
    else:
        print("Unable to create patient directory at " + path)
        exit -1
    return 0

def add_patient():
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
