import pytest


# @pytest.fixture(params = ["a", "b"])
# def d_fixture(request):
#     print(request.param)
#
# def testLogin(d_fixture):
#     print("Login successful")

@pytest.mark.parametrize("a , b, final", [(2, 6, 8), (5, 8, 15), (5, 10, 15)])
def testadd(a, b, final):
    assert a+b == final


# def testLogoof():
#     print("Logoff successful")
#
#
# def testCalculation():
#     assert 2+2 == 4
#
