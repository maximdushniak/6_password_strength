import re


def contain_lower(password):
    return re.search(r'.*[a-z]+.*', password)


def contain_upper(password):
    return re.search(r'.*[A-Z]+.*', password)


def contain_numeric(password):
    return re.search(r'.*[0-9]+.*', password)


def contain_special(password):
    return re.search(r'.*[~!@#$%^&*()_+\-=\{\}\[\]:;\`<>\.\/\\]+.*', password)

def get_password_strength(password):
    # password = 'sdjfiksjdfFDSAFfdsa3424323'
    password_strength = 1

    if contain_lower(password):
        password_strength += 1

    if contain_upper(password):
        password_strength += 1

    if contain_numeric(password):
        password_strength += 1

    if contain_special(password):
        password_strength += 1

    return password_strength


if __name__ == '__main__':
    print(get_password_strength(input('Введите пароль: ')))
