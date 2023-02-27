
class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


email = input()
valid_domain = ['com', 'bg', 'org', 'net']

while email != 'End':
    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")
    first_part, second_part = email.split('@')
    if len(first_part) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    if '.' in second_part:
        if second_part.split('.') not in valid_domain:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
        else:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print('Email is valid')
    email = input()
