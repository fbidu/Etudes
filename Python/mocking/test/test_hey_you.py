import unittest
from unittest import mock

from bird import app

def test_hey_you():
    result = app.main()
    assert result == 200
