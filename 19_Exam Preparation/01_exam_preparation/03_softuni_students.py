def softuni_students(*args, **kwargs):

    result = ""
    invalid = []

    for id_number, username in sorted(args, key=lambda x:x[1]):
        if id_number in kwargs.keys():
            result += f"*** A student with the username {username} has successfully finished the course {kwargs[id_number]}!\n"
        else:
            invalid.append(username)

    if invalid:
        result += f"!!! Invalid course students: {', '.join(invalid)}"

    return result

print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))