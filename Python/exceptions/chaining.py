# Exception masking

a = {"key": "value!!"}

try:
    unvalid = a["heey"]
except KeyError as ke:
    raise Exception("I'll mask the key error!") from ke

# Python 3.7 Output
"""
Traceback (most recent call last):
  File "chaining.py", line 6, in <module>
    unvalid = a["heey"]
KeyError: 'heey'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "chaining.py", line 8, in <module>
    raise Exception("I'll mask the key error!") from ke
Exception: I'll mask the key error!
"""