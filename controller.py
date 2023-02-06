import view


def create_member():
    name = input('Name: ')
    lastName = input('Lastname: ')
    salary = int(input('Salary: '))
    position = input('Position: ')
    return name, lastName, salary, position




def export_CSV(name, lastName, salary, position):
    with open('members.csv', 'a') as data:
         members_list_csv = data.write(f'Name: {name}\nLastname: {lastName}\nSalary: {salary}\nPosinion: {position} \n\n')





def exporn_JSON(name, lastName, salary, position):
    with open('members.json', 'a') as data:
         members_list_json = data.write(f'Name: {name}\nLastname: {lastName}\nSalary: {salary}\nPosinion: {position} \n\n')





def what_to_do():
    if view.show_menu() == 4:
        create_member()
    elif view.show_menu() == 7:
        exporn_JSON(name, lastName, salary, position)
    elif view.show_menu() == 8:
        export_CSV(name, lastName, salary, position)

what_to_do()


# как сделать программу цикличной(костыль)
# как сделать чтоб она не закрывалась


# в create_member() сразу добавлять его в файл.тхт!!!!!!!!!!!!!!!!!!!!!!!!!!