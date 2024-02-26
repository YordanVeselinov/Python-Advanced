class MustContainAtSymbolError(Exception):
    pass

class NameTooShortError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

valid_domains = ["com", "bg", "org", "net"]

input_line = input()

while input_line != "End":
    email = input_line
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")
    elif len(email.split("@")[0]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    elif email.split(".")[1] not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    else:
        print("Email is valid")
    input_line = input()

