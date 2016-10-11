import re
import os


def contain_lower(password):
    return re.search(r'[a-z]+', password)


def contain_upper(password):
    return re.search(r'[A-Z]+', password)


def contain_numeric(password):
    return re.search(r'[0-9]+', password)


def contain_special(password):
    return re.search(r'[~!@#$%^&*()_+\-=\{\}\[\]:;\`<>\.\/\\]+', password)


def contain_date(password):
    pattern_list = [
        # 20161007, 2016/10/07, 2016.10.07, 2016\10\07
        r'[12][0-9]{3}[\/\\\.]?(([0][1-9])|([1][0-2]))[\/\\\.]?(([0][1-9])|([1-2][0-9])|([3][0-1]))',
        # 07102016, 07/10/2016, 07.10.2016, 07\10\2016
        r'(([0][1-9])|([1-2][0-9])|([3][0-1]))[\/\\\.]?(([0][1-9])|([1][0-2]))[\/\\\.]?[12][0-9]{3}'
    ]
    for pattern in pattern_list:
        if re.search(pattern, password):
            return True


def check_blacklist(password, filepath='blacklist.txt'):
    if not os.path.exists(filepath):
        return True
    with open(filepath, 'r', encoding='utf-8') as blacklist:
        for badpass in blacklist:
            if badpass in password:
                return True
    return False


def get_password_strength(password):

    password_strength = 1

    if len(password) >= 8:
        password_strength += 1

    if len(password) >= 16:
        password_strength += 1

    if contain_lower(password):
        password_strength += 1

    if contain_upper(password):
        password_strength += 1

    if contain_numeric(password):
        password_strength += 1

    if contain_special(password):
        password_strength += 1

    if not contain_date(password):
        password_strength += 1

    if not check_blacklist(password):
        password_strength += 2

    return password_strength


if __name__ == '__main__':

    password = input('Введите пароль: ')
    print('Сложность Вашего пароля: ', get_password_strength(password))
