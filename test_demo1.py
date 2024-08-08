# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# Any code should be wrapped in method only
import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")
    print("ADDED BY USER X")
    print("EDITED BY FIRST USER")
    print("DEVELOPED FEATURES")
    print("DEVELOPED FEATURES")

@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("Good Morning")
    print("Changed by User X")
    print("DEVELOPED FEATURES")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])