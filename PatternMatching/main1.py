"""
In this example only content starting with hi or hello or hey with 0 or more spaces and letters will be matched
"""

import re

r = "(hi|hello|hey)[ ]*([a-z]*)"
print(re.match(r, 'Hello Rosa', flags=re.IGNORECASE))
print(re.match(r, "ho ho, hi ho, it's off to work ...", flags=re.IGNORECASE))
print(re.match(r, "hey, what's up", flags=re.IGNORECASE))

r = ".*(hi|hello|hey)[ ]*([a-z]*)"
print(re.match(r, "ho ho, hi ho, it's off to work ...", flags=re.IGNORECASE))

