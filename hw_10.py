from collections import UserDict

class Field:
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return self.value

class Name(Field):
    pass

class Phone(Field):
    pass


class Record:
    def __init__(self, name: Name, phone: Phone = None) -> None:
        self.name = name
        self.phones = []
        if phone:
            self.add_phone(phone)

    def add_phone(self, phone):
        self.phones.append(phone)

    def change_phone(self, phone, new_phone):
        if self.del_phone(phone):
            self.add_phone(new_phone)
            return True
        return False

    def del_phone(self, phone):
        for i, p in enumerate(self.phones):
            if p.value == phone.value:
                return self.phones.pop(i)

    def __repr__(self) -> str:
        return ','.join([p.value for p in self.phones])
            

class AddressBook(UserDict):
    def add_record(self, rec: Record):
        self.data[rec.name.value] = rec


contacts = AddressBook()


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except (KeyError, ValueError, IndexError):
            return "You should enter command (space) name (space) phone"

    return wrapper


def hello(*args):
    return 'How can I help you?'


def exit(*args):
    return 'Good bye'


@input_error
def add(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    rec = Record(name, phone)
    contacts.add_record(rec)
    return f'contact {name.value} added successfully'


@input_error
def change(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    new_phone = Phone(args[2])
    rec = contacts.get(name.value)
    if rec:
        result = rec.change_phone(phone, new_phone)
        if result:
            return f'Contact {name.value} changed successfully'


def get_phone(*args):
    name = Name(args[0])
    rec = contacts.get(name.value)
    if rec:
        return rec.phones
    return "No such contact"


def show_all(*args):
    return '\n'.join([f'{k}:{v}' for k,v in contacts.items()])
    


COMMANDS = {exit: ['good bye', 'exit', 'close', '.'], add: ['add', 'додай'], change: [
    'change', 'заміни'], get_phone: ['phone', 'номер'], show_all: ['show all', 'show'], hello: ['hello', 'hi']}


def parse_command(request: str):
    for k, v in COMMANDS.items():
        for i in v:
            if request.lower().startswith(i.lower()):
                return k, request[len(i):].strip().split(' ')


def main():

    while True:
        request = input('You: ')

        result, data = parse_command(request)
        print(result(*data))

        if result is exit:
            break




if __name__ == '__main__':
    main()




