# Exception masking

a = {"key": "value!!"}

try:
    unvalid = a["heey"]
except KeyError:
    raise Exception("I'll mask the key error!")

# Python 3.7 Output
"""
Traceback (most recent call last):
  File "masking.py", line 6, in <module>
    unvalid = a["heey"]
KeyError: 'heey'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "masking.py", line 8, in <module>
    raise Exception("I'll mask the key error!")
Exception: I'll mask the key error!
"""

# Python 2 Output
"""
Traceback (most recent call last):
  File "masking.py", line 8, in <module>
    raise Exception("I'll mask the key error!")
Exception: I'll mask the key error!
"""