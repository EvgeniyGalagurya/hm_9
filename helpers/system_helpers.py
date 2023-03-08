import json

def get_file_data():
    file = open("database/employees.json", "r")
    data_list = json.loads(file.read())
    file.close()
    return data_list


def save_to_file(data: dict):
    data_list = get_file_data()
    data_list.append(data)
    file = open("database/employees.json", "w")
    data_in_json = json.dumps(data_list)
    file.write(data_in_json)
    file.close()


def update_to_file(data: dict, up_last_name):
    employees = get_file_data()
    up_employees = []
    for q in employees:
        if up_last_name not in q["last_name"]:
            up_employees.append(q)
    up_employees.append(data)
    file = open("database/employees.json", "w")
    data_in_json = json.dumps(up_employees)
    file.write(data_in_json)
    file.close()
