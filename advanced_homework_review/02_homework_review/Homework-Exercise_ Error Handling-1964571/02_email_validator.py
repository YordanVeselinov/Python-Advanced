from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class TooManyAtSymbols(Exception):
    pass


class AllowedSymbols(Exception):
    pass


class Digit(Exception):
    pass

command = input()
valid_domain = ("com", "bg", "net", "org")
pattern = r"[\w/-]+"

while command != "End":
    if len(command.split('@')[0]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    elif "@" not in command:
        raise MustContainAtSymbolError("Email must contain @")
    elif command.count("@") > 1:
        raise TooManyAtSymbols("Email must contain only one @")
    elif command.split(".")[-1] not in valid_domain:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    elif findall(pattern, command.split('@')[0])[0] != command.split('@')[0]:
        raise AllowedSymbols("Email contains symbol that is not allowed")
    elif command.split('@')[0].isdigit():
        for dig in command.split('@')[0]:

    print("Email is valid")

    command = input()
