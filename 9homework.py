PHONE_VOCABULAR = [
    {
        "Contact_name": "Bill",
        "Number": ['+380123456789', '0989008080']
    },
]
# структура така повина бути, один користувач може мати список номерів

def add_contact(*args):
    name = args[0]
    phone = args[1]
    for user in PHONE_VOCABULAR: # Якщо контакт вже є в книзі контактів то додаемо номерв список номерів
        if name == user.get("Contact_name"):
            user['Number'].append(phone)
         
        if name not in user.values(): # перевірка якщо контакту ще нема в скнизі контактів, то створюємо його
            PHONE_VOCABULAR.append({"Contact_name": name, "Number": [phone]})
            print(f'Contact {name} with phone: {phone} was created!')
    


def input_error(func):

    def wrapper(*args):
        try:
            return func(
                *args
            )  # тут треба повертати результат виконання функції та викликати в тілі try-except
        except KeyError:
            print("Give me name and phone please")
        except ValueError:
            print("Enter user name")
        except IndexError:
            print('якусь підказку для користувача')
        except TypeError:
            print('TypeError')


    return wrapper


@input_error
def simple_func(args: str):
    return args.upper()


def greeting(*args):
    print("How can I help you?")

@input_error
def all_contacts(*args):
    result = f'Contact list:'
    for user in PHONE_VOCABULAR: # ми ітеруємось по списку словників, кожен словник це Юзер - що має імя та телефони
        name = user.get("Contact_name")
        phones_list = user.get("Number")
        phones = ', '.join(phones_list)
        result += f'\n{name}: {phones}'
    print(result)


def exiting(*args):
    print('Goodbye')


def unknown(*args):
    print('Command not exist')

@input_error
def change(*args):
    name = args[0]
    old_phone = args[1]
    new_phone = args[2]
    for user in PHONE_VOCABULAR:  
        if name == user.get("Contact_name"):
            user['Number'].remove(old_phone)
            user['Number'].append(new_phone)
    print(f'Phone was changed')

@input_error
def show_number(*args):
    name = args[0]
    for user in PHONE_VOCABULAR:  
        if name == user.get("Contact_name"):
            phones_list = user.get("Number")
            phones = ', '.join(phones_list)
    print(f'{name} has phone number: {phones}')


COMMANDS = {
    greeting: ["hello"],
    add_contact: ['add', 'додай', "+"],
    exiting: ['exit', 'close', '.'],
    change: ["change", 'edit'],
    show_number: ["phone"],
    all_contacts: ["show all"]
}


@input_error
def command_parser(user_input: str):
    for command, key_words in COMMANDS.items():
        for key_word in key_words:
            if user_input.startswith(key_word):
                return command, user_input.replace(key_word, "").split()
    return unknown, None

def main():
    while True:
        user_input = input('>>> ')
        if user_input in COMMANDS[exiting]:
            break
        command, data = command_parser(user_input)
        if data:
            command(*data)
        else:
            command()


if __name__ == '__main__':
    main()