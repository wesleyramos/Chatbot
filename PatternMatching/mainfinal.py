"""
In this example the regex recognize expressions more complex and respond accordingly with the input
"""

import re

r = r"[^a-z]*([y]o|[h']?ello|ok|hey|(good[ ])?(morn[gin']{0,3}|afternoon|even[gin']{0,3}))[\s,;:]{1,3}([a-z]{1,20})"
re_greeting = re.compile(r, flags=re.IGNORECASE)

my_names = {'rosa', 'rose', 'chatty', 'chatbot', 'bot', 'chatterbot'}
curt_names = {'hal', 'you', 'u'}
greeter_name = 'wesley'
match = re_greeting.match("Hello Rosa")  # polite
match2 = re_greeting.match("Hello hal")  # slightly rude


def my_function(match):
    if match:
        at_name = match.groups()[-1]
        if at_name in curt_names:
            print("Good one.")
        elif at_name.lower() in my_names:
            print("Hi {}, How are you?".format(greeter_name))


my_function(match)
my_function(match2)
