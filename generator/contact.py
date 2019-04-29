from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import sys
import getopt

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = 'data/contacts.json'

for o, a in opts:  # считывание опций -n и -f
    if o == '-n':
        n = int(a)  # количество групп
    elif o == '-f':
        f = a  # путь, по которому создавать json


def random_sting(prefix, max_len):
    symbols = string.ascii_letters + string.digits
    return prefix + (''.join([random.choice(symbols) for i in range(random.randrange(max_len))]))


testdata = [
    Contact(firstname=random_sting('firstname_', 10), lastname=random_sting('lastname_', 10),
            address=random_sting('address_', 10), homephone=random_sting('homephone_', 10),
            email3=random_sting('email3_', 10))
    for i in range(n)
]


json_file = path_to_config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)


with open(json_file, 'w') as outer_file:
    jsonpickle.set_encoder_options('json', indent=2)
    outer_file.write(jsonpickle.encode(testdata))  # преобр. в словарь и запис. в json
