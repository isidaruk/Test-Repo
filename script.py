import math
import sys
from os import rename

import requests

# print sys.version
# print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    # test = "Test"
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


# print(greet('World'))
# print(greet('Corey'))
r = requests.get("https://coreyms.com")
print(r.status_code)

# name = input("Your Name? ")
# print("Hello,", name)
