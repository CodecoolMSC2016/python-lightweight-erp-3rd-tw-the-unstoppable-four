# implement commonly used functions here

import string
import random

# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of list
# @generated: string - generated random string (unique in the @table)


def generate_random(table):

    spec_char = ("!", "\"", "#", "$", "%", "&", "\'", "(", ")", "*",
                 "+", ",", "-", ".", "/", ":", "<", ">", "=", "?")

    id = []

    for i in range(2):
        id.append(random.choice(string.ascii_uppercase))
        id.append(random.choice(string.ascii_lowercase))
        id.append(random.choice(string.digits))
        id.append(random.choice(spec_char))
    generated = ""

    for i in range(len(id)):
        generated += id[i]
    return generated
