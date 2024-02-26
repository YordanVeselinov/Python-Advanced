class NameTooShortError(Exception):
    pass


class TooManyAtSymbolError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class MustBeOnlyLowerCasesError(Exception):
    pass


class MustBeWithoutSpacesError(Exception):
    pass


class MustNotHaveForbiddenCharacters(Exception):
    pass


class InvalidDomainError(Exception):
    pass


DOMAINS = [".com", ".net", ".org", ".com", ".bg"]
NOT_ALLOWED_CHARS = "<>+=\\/:;*^&%$#!?'\"{}()[]|€"

while True:
    email = input()

    for char in email:
        if char.isupper():
            raise MustBeOnlyLowerCasesError("Email must contains only lower letter!")
        if char in NOT_ALLOWED_CHARS:
            raise MustNotHaveForbiddenCharacters("Email contains not allowed characters!")

    if " " in email:
        raise MustBeWithoutSpacesError("Email must be without any spaces!")

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @!")

    if email.count("@") > 1:
        raise TooManyAtSymbolError("Email has more than one @ symbol!")

    name, full_domain = email.split("@")

    if len(name) < 4:
        raise NameTooShortError("Name must be more than 4 characters!")

    domain_name, domain = full_domain.split(".")

    if "." + domain not in DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net!")

    print("Email is valid")
