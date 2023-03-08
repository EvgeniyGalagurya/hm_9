from .system_helpers import save_to_file, get_file_data, update_to_file
from .decorators_helpers import is_email_valid, is_phone_valid
#is_update_email_valid, is_update_phone_valid


@is_phone_valid
@is_email_valid
def save(email, first_name, last_name, phone):
    new_employee = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone,
    }
    save_to_file(new_employee)


def get_all_employers():
    employees = get_file_data()
    for employee in employees:
        print("Last name: ", employee["last_name"])
        print("First name: ", employee["first_name"])
        print("Email: ", employee["email"])
        print("Telephone: ", employee["phone"])
        print("")


def get_employee_by_email(email):
    employees = get_file_data()
    for employee in employees:
        if employee["email"] == email:
            print("Last name: ", employee["last_name"])
            print("First name: ", employee["first_name"])
            print("Email: ", employee["email"])
            print("Telephone: ", employee["phone"])


def get_employee_by_last_name(last_name_find):
    employees = get_file_data()
    for employee in employees:
        if employee["last_name"] == last_name_find:
            print("Last name: ", employee["last_name"])
            print("First name: ", employee["first_name"])
            print("Email: ", employee["email"])
            print("Telephone: ", employee["phone"])


def update(up_last_name):
    employees = get_file_data()
    for employee in employees:
        if employee["last_name"] == up_last_name:
            print('Please update Employee')
            new_employee = {"first_name": input('Input first_name '),
                            "last_name": input('Input last_name '),
                            "email": input('Input email '),
                            "phone": input('Input phone ')}
            update_to_file(new_employee, up_last_name)

    #print('This Employee is not found')



