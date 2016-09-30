

def get_password_strength(password):
    # password = 'sdjfiksjdfFDSAFfdsa3424323'
    password_strength = 1
    upper = False
    lower = False
    for i in password:
        if i.islower():
            lower = True
        if i.isupper():
            upper = True

    if upper and lower:
        password_strength += 1

    return password_strength


if __name__ == '__main__':
    print(get_password_strength(input('Введите пароль: ')))
