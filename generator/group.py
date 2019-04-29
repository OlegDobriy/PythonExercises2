from model.group import Group
import random
import string
import os.path
import jsonpickle
import sys
import getopt

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = 'data/groups.json'

for o, a in opts:  # считывание опций -n и -f
    if o == '-n':
        n = int(a)  # количество групп
    elif o == '-f':
        f = a  # путь, по которому создавать json


def random_sting(prefix, max_len):
    symbols = string.ascii_letters + string.digits
    return prefix + (''.join([random.choice(symbols) for i in range(random.randrange(max_len))]))


testdata = [
    Group(name=random_sting('name_', 10), header=random_sting('header_', 10), footer=random_sting('footer_', 10))
    for i in range(n)
]

json_file = path_to_config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)


with open(json_file, 'w') as outer_file:
    jsonpickle.set_encoder_options('json', indent=2)
    outer_file.write(jsonpickle.encode(testdata))  # преобр. в словарь и запис. в json


'''
with open(json_file, 'w') as outer_file:
    outer_file.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))  # преобр. в словарь и запис. в json
'''