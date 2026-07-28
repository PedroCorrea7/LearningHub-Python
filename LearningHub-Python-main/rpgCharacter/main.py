def create_character(name, stregth, intelligence, charisma):

    full_dot = '●'
    empty_dot = '○'

    if type(name) != str:
        return('The character name should be a string')

    if name == '':
        return('The character should have a name')

    if len(name) > 10:
        return('The character name is too long')

    if ' ' in name:
        return('The character name should not contain spaces')

    if not all (isinstance(v, int) for v in (stregth, intelligence, charisma)):
        return('All stats should be integers')

    
    if any(v < 1 for v in (stregth, intelligence, charisma)):
        return('All stats should be no less than 1')
    elif any(v > 4 for v in (stregth, intelligence, charisma)):
        return('All stats should be no more than 4')

    if (stregth + intelligence + charisma) != 7:
        return('The character should start with 7 points')

    str_dots = (full_dot * stregth) + (empty_dot * (7 - stregth))
    int_dots = (full_dot * intelligence) + (empty_dot * (7 - intelligence))
    cha_dots = (full_dot * charisma) + (empty_dot * (7 - charisma))

    return (
        f'{name}\n'
        f'STR {str_dots}\n'
        f'INT {int_dots}\n'
        f'CHA {cha_dots}'
    )

print(create_character('ren', 4, 2, 1))

    