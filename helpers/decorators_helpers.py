
def is_email_valid(func):
    def wrapper(email, y, a, z):
        if "@" in email:
            if "." in email.split("@")[1]:
                func(email, y, a, z)
            else:
                print("Email invalid without dot!!!!")
        else:
            print("Email invalid without @ !!!!")
    return wrapper


def is_phone_valid(func):
    def wrapper(email, y, a, phone):
        if phone[0] == '+':
            if len(phone) == 13:
                func(email, y, a, phone)
            else:
                print("Invalid len phone!!!!")
        else:
            print("Invalid format phone !!!!")
    return wrapper


'''def is_update_email_valid(func):
    def wrapper(email):
        if "@" in email:
            if "." in email.split("@")[1]:
                func(email)
            else:
                print("Email invalid without dot!!!!")
        else:
            print("Email invalid without @ !!!!")
    return wrapper


def is_update_phone_valid(func):
    def wrapper(phone):
        if phone[0] == '+':
            if len(phone) == 13:
                func(phone)
            else:
                print("Invalid len phone!!!!")
        else:
            print("Invalid format phone !!!!")
    return wrapper'''