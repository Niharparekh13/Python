# camelcase to sanke case
from functools import reduce


def change_case(str):
    a = []
    a.append(str[0].lower())
    for i in str[1:]:
        if i.isupper():
            a.append('_' + i.lower())
        else:
            a.append(i)
    return ''.join(a)

    # return reduce(lambda x, y: x + ('_' if y.isupper() else '') + y, str).lower()


str = input("enter string to convet it into snake case:")
print(change_case(str))


a = input("enter string to convert it into camel case:")
a = a.replace('_', ' ')
y = a.title()
b = y.replace(' ', '')
print(b)
