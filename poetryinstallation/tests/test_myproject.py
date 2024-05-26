from poetryinstallation import main

def test_funciton1():
    r : str = main.my_first_function()
    assert r == "Hello World!"

def test_function2():
    r : str = main.my_first_function()
    assert r != "Pakistan"      