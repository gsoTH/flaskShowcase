# Quelle der Assert Liste:https://understandingdata.com/list-of-python-assert-statements-for-unit-tests/
# Das AAA-Muster wird hier zwecks Lesbarkeit nicht eingehalten.

# zu testende Funktion
def func(x):
    return x + 1


#########################################################################
# Equal to or not equal to [value]
def test_is_equal_pass():
    assert func(3) == 4 # Success

def test_is_equal_fail():
    assert func(3) == 5 # Fail

def test_is_not_equal_pass():
    assert not func(3) == 5 # Success


#########################################################################
# type() is [value]
def test_type_is_value():
    assert type(5) is int # Success

def test_type_is_not_value():
    assert type(5) is not int # Fail


#########################################################################
# isinstance
def test_is_instance():
    assert isinstance('5', str) # Success

def test_is_not_instance_fail():
    assert not isinstance('5', str) # Fail

def test_is_not_instance_pass():
    assert not isinstance('5', int) # Success

def test_is_instance_fail():
    assert isinstance('5', int) # Fail


#########################################################################
# Boolean is [Boolean Type]
result = 5==5

def test_is_true():
    assert result is True # Success

def test_is_false():
    assert result is False # Fail
 
def test_is_true_combined():
    assert (result and 2 == 2) is True # Success


#########################################################################
# in and not in [iterable]
list_bsp=[1,3,5,6]

def test_value_in_list():
    assert 5 in list_bsp # Success
