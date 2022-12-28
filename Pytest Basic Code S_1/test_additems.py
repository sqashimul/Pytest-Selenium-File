import pytest


@pytest.mark.sanity
def testLogin():
    print("Login successful")

def testLogoof():
    print("Logoff successful")

def testCalculation():
    assert 2+2 == 4