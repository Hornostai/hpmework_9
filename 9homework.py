PHONE_VOCABULAR = {'Bill': {'name': 'Bill', 'phones': ['09877777', '09933333']}}

def input_error(func):
    def wrapper(*args):
        try:
            return func(*args) 
        except KeyError:
            print("Give me name and phone please")
        except ValueError:
            print("Enter user name")
        except IndexError:
            print('Check your input and try again')
        except TypeError:
            print('TypeError')
    return wrapper


@input_error
def simple_func(args: str):
    return args.upper()
    
def add_contact(*args:str):
    name = args[0]
    phone = args[1]
    if name in PHONE_VOCABULAR.keys(): # Якщо контакт вже є в книзі контактів то додаемо номерв список номерів
        user = PHONE_VOCABULAR.get(name)
        user['phones'].append(phone)
    else:
        # перевірка якщо контакту ще нема в скнизі контактів, то створюємо його
            PHONE_VOCABULAR[name] = {'name': name, 'phones': [phone]}
            print(f'Contact {name} with phone: {phone} was created!')
    


def greeting():
    print("How can I help you?")


@input_error
def show_all(*args):
    result = f'Contact list:'
    for user in PHONE_VOCABULAR.values(): # ми ітеруємось по списку словників, кожен словник це Юзер - що має імя та телефони
        name = user.get("name")
        phones_list = user.get("phones")
        phones = ', '.join(phones_list)
        result += f'\n{name}: {phones}'
    print(result)


def exiting():
    print('Goodbye')


def unknown(*args):
    print('Command not exist.')

@input_error
def change(*args):
    name = args[0]
    old_phone = args[1]
    new_phone = args[2]
    for user in PHONE_VOCABULAR.values():  
        if name == user.get("name"):
            user["phones"].remove(old_phone)
            user['phones'].append(new_phone)
    
    print(f'Phone {old_phone} ,was changed to {new_phone}')
        


@input_error
def show_phone(*args):
    name = args[0]
    for user in PHONE_VOCABULAR.values():  
        if name == user.get("name"):
            phones_list = user.get("phones")
            phones = ', '.join(phones_list)
    print(f'{name} has phone number: {phones}')


COMMANDS = {
    greeting: ["hello"],
    add_contact: ['add', 'додай', "+"], #add + name + numer
    exiting: ['exit', 'close', '.'],
    change: ["change", 'edit'], # change + name + numer + new numer
    show_phone: ["phone" ], # phone + name
    show_all: ["show","all"]
}



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
            exiting()
            break
        command, data = command_parser(user_input)
        if data:
            command(*data)
        else:
            command()


if __name__ == '__main__':
    main()