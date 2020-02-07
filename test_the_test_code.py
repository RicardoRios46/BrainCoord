#Import the test function pytest, then import the functions to test
import pytest
from testing_code import checkFormat_referece_point
from testing_code import checkFormat_coordinate0
from testing_code import checkValues_coordinate0
from testing_code import checkExistence_file
from testing_code import checkFormat_file

def test_ref_point():
    """Function that test the function checkFormat_referece_point,
    this function is eval True"""
    assert checkFormat_referece_point("bregma") == True, "Is string"

def test_format_coord():
    """Function that test the functin checkFormat_coordinate0,
    this one is to error check"""
    with pytest.raises(TypeError) as e:
        checkFormat_coordinate0(1,2), "Missing value"

def test_val_coord():
    """Function that test checkValues_coordinate0,
    this function check when an error is notice"""
    with pytest.raises(TypeError) as e:
        checkValues_coordinate0("100mm"), "Out of range"

def test_file():
    """Function that test checkExistence_file,
    this function eval True"""
    assert checkExistence_file("datatest.csv") == True, "The db is fine"

def test_format_file():
    """Function that test checkFormat_file,
    this function eval when a wrong file is used"""
    with pytest.raises(NameError) as e:
        checkFormat_file(diagrama.png), "Format file incorrect"
