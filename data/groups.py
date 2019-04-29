from model.group import Group

testdata = [
    Group(name='name1', header='header1', footer='footer1'),
    Group(name='name2', header='header2', footer='footer2')
]


'''
import random
import string
def random_sting(prefix, max_len):
    symbols = string.ascii_letters + string.digits
    return prefix + (''.join([random.choice(symbols) for i in range(random.randrange(max_len))]))


testdata = [
    Group(name=random_sting('name_', 10), header=random_sting('header_', 10), footer=random_sting('footer_', 10))
    for i in range(5)
]
'''